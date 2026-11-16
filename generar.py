#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regenera la web de forma segura y protege los cambios hechos a mano.

La web tiene dos capas:
  - Recetas: motor.py, contenido.py, extras.py, legales.py, schema.py, whatsapp.py
  - Resultado: los index.html que ve el visitante

Si alguien retoca un index.html a mano y después se regenera, ese retoque
se perdería sin avisar. Este script lo impide: guarda en .generado.json la
huella (SHA-256) de cada fichero tal como lo dejaron las recetas. Si un
fichero publicado ya no coincide con su huella, es que alguien lo tocó a mano.

USO
  python3 generar.py              Regenera. Se NIEGA si detecta HTML tocado a mano.
  python3 generar.py --comprobar  Solo comprueba; sale con error si algo no cuadra.
                                  Lo ejecuta Netlify en cada despliegue (netlify.toml):
                                  si falla, NO se publica y la web sigue como estaba.
  python3 generar.py --forzar     Regenera aunque se pierdan los retoques a mano.
                                  Úsalo solo después de pasar esos retoques a los .py.

FLUJO CORRECTO PARA CAMBIAR UN TEXTO
  1. Cambia el texto en el .py que lo genera (normalmente contenido.py o extras.py).
  2. python3 generar.py
  3. Sube a GitHub los .py, los .html y .generado.json juntos.

ESCAPE DE EMERGENCIA
  Si hay que publicar un retoque a mano urgente, en Netlify define la variable
  de entorno PERMITIR_HTML_MANUAL=1: la comprobación avisa pero no bloquea.
  Quítala en cuanto el retoque esté pasado a los .py.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import difflib
import pathlib

BASE = pathlib.Path(__file__).resolve().parent
PASOS = ["motor.py", "extras.py", "legales.py", "schema.py", "whatsapp.py"]
MANIFIESTO = BASE / ".generado.json"
IGNORAR = {".git", ".netlify", "__pycache__", "node_modules"}


def huella(ruta: pathlib.Path) -> str:
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def simular():
    """Ejecuta las recetas sobre una copia y devuelve {ruta_relativa: bytes} de lo que generan."""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="europiscina-gen-"))
    try:
        destino = tmp / "web"
        shutil.copytree(BASE, destino, ignore=shutil.ignore_patterns(*IGNORAR))
        antes = {p: p.stat().st_mtime_ns for p in destino.rglob("*") if p.is_file()}
        for paso in PASOS:
            r = subprocess.run([sys.executable, paso], cwd=destino,
                               capture_output=True, text=True,
                               env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
            if r.returncode != 0:
                raise SystemExit(f"ERROR ejecutando {paso}:\n{r.stderr[-2000:]}")
        generados = {}
        for p in destino.rglob("*"):
            if (not p.is_file() or p.suffix in (".py", ".pyc")
                    or "__pycache__" in p.parts or p.name == MANIFIESTO.name):
                continue
            if p not in antes or p.stat().st_mtime_ns != antes[p]:
                generados[p.relative_to(destino).as_posix()] = p.read_bytes()
        return generados
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def leer_manifiesto():
    if not MANIFIESTO.exists():
        return None
    return json.loads(MANIFIESTO.read_text(encoding="utf-8"))


def tocados_a_mano(manifiesto):
    """Ficheros cuyo contenido actual no coincide con la huella que dejaron las recetas."""
    malos = []
    for rel, h in sorted(manifiesto["ficheros"].items()):
        p = BASE / rel
        if not p.exists():
            malos.append((rel, "borrado a mano"))
        elif huella(p) != h:
            malos.append((rel, "modificado a mano"))
    return malos


def muestra_diff(rel, nuevo: bytes, lineas=12):
    actual = (BASE / rel).read_text(encoding="utf-8", errors="replace").splitlines()
    receta = nuevo.decode("utf-8", errors="replace").splitlines()
    d = list(difflib.unified_diff(receta, actual, "segun las recetas", "publicado", lineterm="", n=0))
    d = [l[:180] for l in d if not l.startswith(("---", "+++", "@@"))]
    return d[:lineas]


def escribir(generados):
    for rel, contenido in generados.items():
        p = BASE / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(contenido)
    datos = {
        "aviso": "No editar. Huellas de los ficheros generados por generar.py.",
        "ficheros": {rel: hashlib.sha256(c).hexdigest() for rel, c in sorted(generados.items())},
    }
    MANIFIESTO.write_text(json.dumps(datos, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def informar_tocados(malos, generados):
    print("\nHTML TOCADO A MANO. Estos ficheros no coinciden con lo que generan las recetas:\n")
    for rel, motivo in malos:
        print(f"  {rel}  ({motivo})")
        if rel in generados and (BASE / rel).exists():
            for l in muestra_diff(rel, generados[rel]):
                print("      " + l)
    print("\nSi se regenerara ahora, esos cambios SE PERDERÍAN.")
    print("Pasa los cambios al .py que genera esa página (contenido.py, extras.py o legales.py),")
    print("ejecuta  python3 generar.py  y sube los .py, los .html y .generado.json juntos.")


def main():
    modo = (sys.argv[1] if len(sys.argv) > 1 else "").lstrip("-")
    if modo not in ("", "comprobar", "forzar"):
        raise SystemExit(__doc__)

    manifiesto = leer_manifiesto()
    generados = simular()
    malos = tocados_a_mano(manifiesto) if manifiesto else []

    if modo == "comprobar":
        if manifiesto is None:
            print("ERROR: falta .generado.json. Ejecuta  python3 generar.py  y súbelo.")
            sys.exit(1)
        # recetas cambiadas pero HTML sin regenerar
        desfasados = [rel for rel, c in generados.items()
                      if rel not in dict(malos) and (not (BASE / rel).exists()
                                                     or (BASE / rel).read_bytes() != c)]
        if not malos and not desfasados:
            print(f"OK: {len(generados)} ficheros coinciden con las recetas.")
            return
        if malos:
            informar_tocados(malos, generados)
        if desfasados:
            print("\nRECETAS SIN APLICAR. Se cambió algún .py pero no se regeneró el HTML:\n")
            for rel in desfasados:
                print("  " + rel)
            print("\nEjecuta  python3 generar.py  y sube el resultado.")
        if os.environ.get("PERMITIR_HTML_MANUAL") == "1":
            print("\nAVISO: PERMITIR_HTML_MANUAL=1 activo. Se publica igualmente.")
            return
        print("\nDespliegue BLOQUEADO para no publicar una web incoherente. La web sigue como estaba.")
        sys.exit(1)

    if malos and modo != "forzar":
        informar_tocados(malos, generados)
        print("\nNo he tocado nada. Si ya pasaste los cambios a los .py:  python3 generar.py --forzar")
        sys.exit(1)

    if malos and modo == "forzar":
        print(f"--forzar: se sobrescriben {len(malos)} ficheros tocados a mano.")
    escribir(generados)
    print(f"Regeneradas {len(generados)} páginas y ficheros. Huellas guardadas en {MANIFIESTO.name}.")


if __name__ == "__main__":
    main()
