#!/usr/bin/env python3
"""
Motor del sitio multiidioma de europiscina.es
  es -> raíz    ca -> /ca/    en -> /en/ (5 páginas clave)
El contenido vive en contenido.py. Este módulo solo renderiza.
"""
import pathlib

BASE = pathlib.Path(__file__).parent
IMG = "https://resonant-sunshine-1d0aa4.netlify.app/images"
WA = "https://wa.me/34680335438"
TEL, TEL_TXT, WA_TXT = "+34973446445", "973 446 445", "680 335 438"
MAIL = "comercial@europiscina.es"

LANGS = ["es", "ca", "en"]
PREFIJO = {"es": "", "ca": "/ca", "en": "/en"}

FUENTES = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
           '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
           '<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@400;500;600'
           '&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&display=swap" rel="stylesheet">')

# clave -> slug por idioma. None = la página no existe en ese idioma.
SLUGS = {
 "home":   {"es": "",                       "ca": "",                       "en": ""},
 "obra":   {"es": "piscinas-de-obra",       "ca": "piscines-obra",          "en": None},
 "lamina": {"es": "piscinas-lamina-armada", "ca": "piscines-lamina-armada", "en": None},
 "polie":  {"es": "piscinas-poliester",     "ca": "piscines-poliester",     "en": "fibreglass-pools"},
 "gres":   {"es": "gres-porcelanico",       "ca": "gres-porcellanic",       "en": None},
 "mant":   {"es": "mantenimiento",          "ca": "manteniment",            "en": "pool-maintenance"},
 "fugas":  {"es": "fugas-de-agua",          "ca": "fuites-aigua",           "en": None},
 "ref":    {"es": "reformas",               "ca": "reformes",               "en": None},
 "emp":    {"es": "empresa",                "ca": "empresa",                "en": None},
 "conf":   {"es": "configurador",           "ca": "configurador",           "en": "pool-calculator"},
 "cont":   {"es": "contacto",               "ca": "contacte",               "en": "contact"},
}


def url(clave, lang):
    s = SLUGS[clave][lang]
    if s is None:
        return None
    if s == "":
        return (PREFIJO[lang] + "/") if PREFIJO[lang] else "/"
    return PREFIJO[lang] + "/" + s + "/"




# ---------------------------------------------------------------- imagenes
import json as _json
_MAN = _json.load(open(BASE / "img" / "manifiesto.json"))

# Cabecera de cada pagina de servicio
FOTO_PAGINA = {
 "obra": "pag-obra", "lamina": "pag-lamina", "polie": "pag-poliester",
 "gres": "pag-gres", "mant": "pag-mantenimiento", "fugas": "pag-fugas",
 "ref": "pag-reformas", "emp": "pag-empresa", "conf": "pag-configurador",
}


def imagen(clave, alt, sizes="100vw", eager=False, clase=""):
    """Devuelve un <picture> con WebP y respaldo JPEG, srcset completo."""
    d = _MAN[clave]
    webp = ", ".join(f"/img/{clave}-{a}.webp {a}w" for a in d["anchos"])
    grande = max(d["anchos"])
    carga = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    cls = f' class="{clase}"' if clase else ""
    return (f'<img{cls} src="/img/{clave}-{grande}.webp" srcset="{webp}" sizes="{sizes}" '
            f'alt="{alt}" width="{d["w"]}" height="{d["h"]}" {carga}>')

NAV = {
 "es": [("obra", "Piscinas de obra"), ("lamina", "Lámina armada"), ("polie", "Poliéster"),
        ("conf", "Configurador"), ("mant", "Mantenimiento"), ("cont", "Contacto")],
 "ca": [("obra", "Piscines d'obra"), ("lamina", "Làmina armada"), ("polie", "Polièster"),
        ("conf", "Configurador"), ("mant", "Manteniment"), ("cont", "Contacte")],
 "en": [("polie", "Fibreglass pools"), ("conf", "Price calculator"),
        ("mant", "Maintenance"), ("cont", "Contact")],
}

T = {
 "es": {"con": "Construcción", "ser": "Servicio", "saltar": "Ir al contenido", "inicio": "Inicio",
        "tag": "Agua desde 1969, piscinas desde 1999. Official Partner de Astralpool Fluidra y miembros de ASOFAP.",
        "legal": "Aviso legal · Privacidad · Cookies", "wa": "Escríbenos por WhatsApp",
        "cta1": "Pedir presupuesto", "faq": "Preguntas frecuentes"},
 "ca": {"con": "Construcció", "ser": "Servei", "saltar": "Vés al contingut", "inicio": "Inici",
        "tag": "Aigua des del 1969, piscines des del 1999. Official Partner d'Astralpool Fluidra i membres d'ASOFAP.",
        "legal": "Avís legal · Privacitat · Galetes", "wa": "Escriu-nos per WhatsApp",
        "cta1": "Demanar pressupost", "faq": "Preguntes freqüents"},
 "en": {"con": "Construction", "ser": "Service", "saltar": "Skip to content", "inicio": "Home",
        "tag": "Water since 1969, pools since 1999. Astralpool Fluidra Official Partner and ASOFAP members.",
        "legal": "Legal notice · Privacy · Cookies", "wa": "Message us on WhatsApp",
        "cta1": "Request a quote", "faq": "Frequently asked questions"},
}

PIE_LINKS = {
 "es": [("con", [("obra", "Piscinas de obra"), ("lamina", "Lámina armada"),
                 ("gres", "Gres porcelánico"), ("polie", "Poliéster")]),
        ("ser", [("mant", "Mantenimiento"), ("ref", "Reformas"),
                 ("fugas", "Fugas de agua"), ("cont", "Contacto")])],
 "ca": [("con", [("obra", "Piscines d'obra"), ("lamina", "Làmina armada"),
                 ("gres", "Gres porcellànic"), ("polie", "Polièster")]),
        ("ser", [("mant", "Manteniment"), ("ref", "Reformes"),
                 ("fugas", "Fuites d'aigua"), ("cont", "Contacte")])],
 "en": [("con", [("polie", "Fibreglass pools"), ("conf", "Price calculator")]),
        ("ser", [("mant", "Maintenance"), ("cont", "Contact")])],
}



def logo(variant="color", clase="marca"):
    """variant: 'color' (fons clar) o 'blanc' (fons fosc)."""
    base = "logo" if variant == "color" else "logo-blanc"
    return (f'<img src="/img/{base}-400.webp" '
            f'srcset="/img/{base}-260.webp 260w, /img/{base}-400.webp 400w, /img/{base}-600.webp 600w" '
            f'sizes="180px" alt="Europiscina" width="2092" height="657" class="{clase}-img">')


def hreflang(clave):
    out = []
    for l in LANGS:
        u = url(clave, l)
        if u:
            out.append(f'<link rel="alternate" hreflang="{l}" href="https://europiscina.es{u}">')
    u_es = url(clave, "es")
    if u_es:
        out.append(f'<link rel="alternate" hreflang="x-default" href="https://europiscina.es{u_es}">')
    return "".join(out)


def selector(clave, lang):
    items = ""
    for l in LANGS:
        u = url(clave, l) or url("home", l)
        act = ' class="act"' if l == lang else ""
        items += f'<a href="{u}"{act} hreflang="{l}">{l.upper()}</a>'
    return f'<span class="idiomas">{items}</span>'


def cabecera(clave, lang, clara=False):
    items = ""
    for k, t in NAV[lang]:
        u = url(k, lang)
        if not u:
            continue
        cur = ' aria-current="page"' if k == clave else ""
        items += f'<a href="{u}"{cur}>{t}</a>'
    clase = "top top-clara" if clara else "top top-solida"
    marca = logo("blanc" if clara else "color")
    return (f'<header class="{clase}">'
            f'<a class="marca" href="{url("home", lang)}" aria-label="Europiscina, inici">{marca}</a>'
            f'<nav class="menu">{items}</nav>{selector(clave, lang)}</header>')


def pie(lang):
    t = T[lang]
    cols = ""
    for cab, links in PIE_LINKS[lang]:
        li = "".join(f'<li><a href="{url(k, lang)}">{n}</a></li>'
                     for k, n in links if url(k, lang))
        cols += f'<div><h4>{t[cab]}</h4><ul>{li}</ul></div>'
    return f"""<footer>
  <div class="pie-grid">
    <div><a class="marca-pie" href="{url('home', lang)}" aria-label="Europiscina">{logo('blanc', 'marca-pie')}</a><p>{t['tag']}</p></div>
    {cols}
  </div>
  <div class="pie-legal">
    <span>© 2026 Europiscina · GARCAM Industries SLU · Ctra. C-26 km 22, 25600 Balaguer (Lleida)</span>
    <span>{t['legal']}</span>
  </div>
</footer>
<a class="wa" href="{WA}">{t['wa']}</a>"""


def ficha(titulo, filas):
    dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in filas)
    return (f'<section class="bloque" style="padding-top:0">'
            f'<div class="ficha"><h3>{titulo}</h3><dl>{dl}</dl></div></section>')


def faq(lang, pares):
    it = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in pares)
    return (f'<section class="bloque faq"><h2>{T[lang]["faq"]}</h2>'
            f'<div style="margin-top:32px">{it}</div></section>')


def cinta(h, p, lang):
    return (f'<section class="bloque cinta"><h2>{h}</h2><p>{p}</p>'
            f'<div class="acciones">'
            f'<a class="btn btn-solid" href="{url("cont", lang)}">{T[lang]["cta1"]}</a>'
            f'<a class="btn btn-ghost" href="{WA}">WhatsApp</a></div></section>')


def cuerpo(h2, izq, der):
    return (f'<section class="bloque cuerpo"><div><h2>{h2}</h2>{izq}</div>'
            f'<div class="col-txt">{der}</div></section>')


PLANTILLA = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://europiscina.es{url}">
{alt}
<link rel="icon" href="/favicon.ico" sizes="32x32"><link rel="icon" href="/img/icon-512.png" type="image/png" sizes="512x512"><link rel="apple-touch-icon" href="/img/apple-touch-icon.png"><meta name="theme-color" content="#0B4F6C">
{fuentes}
<link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
<a class="saltar" href="#principal">{saltar}</a>
{nav}
<main id="principal">
<section class="cabecera">
  <p class="miga"><a href="{home}">{inicio}</a> · {miga}</p>
  <h1>{h1}</h1>
  <p class="entradilla">{entradilla}</p>
</section>
<div class="foto-ancha">{foto}</div>
{cuerpo}
{extra}
</main>
{pie}
</body>
</html>"""


def escribir(clave, lang, p):
    u = url(clave, lang)
    dest = BASE / u.strip("/")
    dest.mkdir(parents=True, exist_ok=True)
    t = T[lang]
    dest.joinpath("index.html").write_text(PLANTILLA.format(
        lang=lang, title=p["title"], desc=p["desc"], url=u, alt=hreflang(clave),
        fuentes=FUENTES, saltar=t["saltar"], nav=cabecera(clave, lang),
        home=url("home", lang), inicio=t["inicio"], miga=p["miga"], h1=p["h1"],
        entradilla=p["entradilla"],
        foto=imagen(FOTO_PAGINA[clave], p["foto_alt"], sizes="100vw"),
        cuerpo=p["cuerpo"], extra=p.get("extra", ""), pie=pie(lang)), encoding="utf-8")
    return u


if __name__ == "__main__":
    import contenido
    n = 0
    for clave, porlang in contenido.C.items():
        for lang, p in porlang.items():
            print(" ", lang, escribir(clave, lang, p))
            n += 1
    print(f"\n{n} páginas de servicio")
