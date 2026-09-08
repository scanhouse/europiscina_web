#!/usr/bin/env python3
"""
Pipeline de imagenes de europiscina.es
Recorta a la proporcion de destino, genera WebP (principal) y JPEG (respaldo)
en varios anchos, y escribe un manifiesto para el generador de HTML.
"""
import pathlib, json
from PIL import Image, ImageOps

SRC = pathlib.Path("/mnt/user-data/uploads")
ZIP = pathlib.Path("/home/claude/fotos_zip")
OUT = pathlib.Path("/home/claude/web/img")
OUT.mkdir(parents=True, exist_ok=True)

# Anchos por rol. El navegador elige el que necesita.
ANCHOS = {
    "hero":   [2400, 1800, 1200, 800],
    "ancha":  [1800, 1200, 800],
    "tile":   [1200, 800, 500],
}
# Proporciones de destino
RATIO = {"hero": 16/9, "ancha": 21/9, "tile-alta": 4/5, "tile-ancha": 4/5,
         "tile-tercio": 1/1, "tile-full": 21/9}

# nombre_salida: (fichero_origen, rol, foco vertical 0=arriba .5=centro 1=abajo)
CATALOGO = {
    # Portada
    "hero-oliveres":      ("IMG_0560.jpg",                      "hero", "ancha", 0.55),
    # Mosaico de portada
    "mos-dron-cenital":   ("dji_fly_20260310_150144_0131_1773152313054_photo_beautify.JPG", "tile", "tile-alta", 0.5),
    "mos-andorra":        ("IMG_9722.jpg",                      "tile", "tile-ancha", 0.5),
    "mos-escala-pedra":   ("IMG_0673.jpg",                      "tile", "tile-tercio", 0.55),
    "mos-lamina-gris":    ("80D0E2E6-DE8B-480A-8866-C29B68781336.JPG", "tile", "tile-tercio", 0.5),
    "mos-gres-fusta":     ("9c159c2b-8476-4cde-bfe3-301d6932d7c5.JPG", "tile", "tile-tercio", 0.5),
    "mos-dron-textura":   ("dji_fly_20260310_150152_0134_1773152314621_photo_beautify.JPG", "tile", "tile-full", 0.5),
    # Cabeceras de pagina (21:9)
    "pag-obra":           ("IMG_0924.jpg",                      "ancha", "ancha", 0.55),
    "pag-lamina":         ("IMG_4636.jpg",                      "ancha", "ancha", 0.5),
    "pag-poliester":      ("IMG_9563.jpg",                      "ancha", "ancha", 0.45),
    "pag-gres":           ("IMG_1441.jpg",                      "ancha", "ancha", 0.5),
    "pag-mantenimiento":  ("IMG_20230623_113259_Original.jpg",  "ancha", "ancha", 0.5),
    "pag-fugas":          ("IMG_20230623_113421_Original.jpg",  "ancha", "ancha", 0.5),
    "pag-reformas":       ("IMG_0590.jpg",                      "ancha", "ancha", 0.45),
    "pag-empresa":        ("IMG_2302.jpg",                      "ancha", "ancha", 0.5),
    "pag-configurador":   ("IMG_0192.jpg",                      "ancha", "ancha", 0.5),
    # Obra publica
    "pub-municipal":      ("IMG_6025.JPG",                      "ancha", "ancha", 0.5),
}


def abrir(nombre):
    for base in (SRC, ZIP):
        p = base / nombre
        if p.exists():
            return ImageOps.exif_transpose(Image.open(p)).convert("RGB")
    raise FileNotFoundError(nombre)


def recortar(im, ratio, foco):
    """Recorte centrado horizontalmente y con foco ajustable en vertical."""
    w, h = im.size
    actual = w / h
    if actual > ratio:                       # sobra ancho
        nw = int(h * ratio)
        x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    nh = int(w / ratio)                      # sobra alto
    y = int((h - nh) * foco)
    return im.crop((0, y, w, y + nh))


manifiesto = {}
for salida, (origen, rol, clave_ratio, foco) in CATALOGO.items():
    im = abrir(origen)
    im = recortar(im, RATIO[clave_ratio], foco)
    anchos = [a for a in ANCHOS[rol] if a <= im.width] or [im.width]
    entradas = []
    for a in anchos:
        alto = round(a / (im.width / im.height))
        red = im.resize((a, alto), Image.LANCZOS)
        red.save(OUT / f"{salida}-{a}.webp", "WEBP", quality=82, method=6)
        entradas.append(a)
    manifiesto[salida] = {"anchos": entradas, "w": im.width, "h": im.height,
                          "origen": origen}
    print(f"  {salida:<20} {im.width}x{im.height}  {entradas}")

json.dump(manifiesto, open(OUT / "manifiesto.json", "w"), indent=1)
print(f"\n{len(manifiesto)} imagenes procesadas")
