#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inyecta el botón flotante de WhatsApp con burbuja de bienvenida
en todas las páginas comerciales ya generadas.

Se ejecuta DESPUÉS de motor.py, extras.py, legales.py y schema.py:

    python3 motor.py && python3 extras.py && python3 legales.py
    python3 schema.py && python3 whatsapp.py

El componente vive en snippet-whatsapp.html, es autocontenido y no
depende de assets/styles.css: así sobrevive a una caché desfasada
del CSS, que es lo que ya nos falló dos veces.

Excluye /a/ (página de firma de albarán, noindex): ahí el botón
comercial no pinta nada.
"""
import pathlib
import re

BASE = pathlib.Path(__file__).parent
SNIPPET = BASE / "snippet-whatsapp.html"
EXCLUIR = {"a"}                      # carpetas que no llevan botón
MARCA_INI = "<!-- ============================================================\n     Botón flotante de WhatsApp"
MARCA_FIN = "<!-- ======================= fin WhatsApp ======================= -->"


def paginas():
    for p in sorted(BASE.rglob("index.html")):
        rel = p.relative_to(BASE)
        if rel.parts and rel.parts[0] in EXCLUIR:
            continue
        if ".git" in rel.parts:
            continue
        yield p


def limpiar(html: str) -> str:
    """Quita el botón anterior y cualquier inyección previa de este script."""
    # inyecciones anteriores de este mismo script
    html = re.sub(
        re.escape(MARCA_INI).replace(r"\\n", r"\n") + r".*?" + re.escape(MARCA_FIN),
        "", html, flags=re.S)
    html = re.sub(r"<!-- =+\s*\n\s*Bot[oó]n flotante de WhatsApp.*?fin WhatsApp\s*=+ -->",
                  "", html, flags=re.S)
    # botón antiguo <a class="wa">...</a>
    html = re.sub(r'<a class="wa".*?</a>\s*', "", html, flags=re.S)
    return html


def main():
    if not SNIPPET.exists():
        raise SystemExit("Falta snippet-whatsapp.html")
    bloque = SNIPPET.read_text(encoding="utf-8").strip()

    n = 0
    for p in paginas():
        s = p.read_text(encoding="utf-8")
        s = limpiar(s)
        if "</body>" not in s:
            print("  SIN </body>, omitida:", p)
            continue
        # colapsar el espacio previo a </body>: repetir no acumula líneas en blanco
        s = re.sub(r"\s*</body>", lambda _m: "\n" + bloque + "\n</body>", s, count=1)
        p.write_text(s, encoding="utf-8")
        n += 1
    print(f"{n} páginas con botón de WhatsApp")

    saltadas = [d for d in EXCLUIR if (BASE / d).exists()]
    if saltadas:
        print("excluidas:", ", ".join("/" + d + "/" for d in saltadas))


if __name__ == "__main__":
    main()
