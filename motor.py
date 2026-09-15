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

FUENTES = ('<link rel="preload" href="/fonts/libre-franklin-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>'
           '<link rel="preload" href="/fonts/newsreader-latin-300-normal.woff2" as="font" type="font/woff2" crossorigin>')

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
 "emp":    {"es": "empresa",                "ca": "empresa",                "en": "about-us"},
 "conf":   {"es": "configurador",           "ca": "configurador",           "en": "pool-calculator"},
 "cont":   {"es": "contacto",               "ca": "contacte",               "en": "contact"},
}


SLUG_LEGAL = {
 "legal":   {"es": "aviso-legal", "ca": "avis-legal", "en": "legal-notice"},
 "priv":    {"es": "privacidad",  "ca": "privacitat", "en": "privacy"},
 "cookies": {"es": "cookies",     "ca": "galetes",    "en": "cookies"},
}


def url_legal(clave, lang):
    return ("" if lang == "es" else f"/{lang}") + "/" + SLUG_LEGAL[clave][lang] + "/"


def url(clave, lang):
    if clave in SLUG_LEGAL:
        return url_legal(clave, lang)
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
        ("conf", "Configurador"), ("mant", "Mantenimiento"),
        ("emp", "Empresa"), ("cont", "Contacto")],
 "ca": [("obra", "Piscines d'obra"), ("lamina", "Làmina armada"), ("polie", "Polièster"),
        ("conf", "Configurador"), ("mant", "Manteniment"),
        ("emp", "Qui som"), ("cont", "Contacte")],
 "en": [("polie", "Fibreglass pools"), ("conf", "Price calculator"),
        ("mant", "Maintenance"), ("emp", "About us"), ("cont", "Contact")],
}

T = {
 "es": {"con": "Construcción", "ser": "Servicio", "saltar": "Ir al contenido", "inicio": "Inicio",
        "tag": "Agua desde 1969, piscinas desde 1999. Official Partner de Astralpool Fluidra y miembros de ASOFAP.",
        "legal_avis": "Aviso legal", "legal_priv": "Privacidad", "legal_cook": "Cookies", "wa": "Escríbenos por WhatsApp",
        "cta1": "Pedir presupuesto", "faq": "Preguntas frecuentes"},
 "ca": {"con": "Construcció", "ser": "Servei", "saltar": "Vés al contingut", "inicio": "Inici",
        "tag": "Aigua des del 1969, piscines des del 1999. Official Partner d'Astralpool Fluidra i membres d'ASOFAP.",
        "legal_avis": "Avís legal", "legal_priv": "Privacitat", "legal_cook": "Galetes", "wa": "Escriu-nos per WhatsApp",
        "cta1": "Demanar pressupost", "faq": "Preguntes freqüents"},
 "en": {"con": "Construction", "ser": "Service", "saltar": "Skip to content", "inicio": "Home",
        "tag": "Water since 1969, pools since 1999. Astralpool Fluidra Official Partner and ASOFAP members.",
        "legal_avis": "Legal notice", "legal_priv": "Privacy", "legal_cook": "Cookies", "wa": "Message us on WhatsApp",
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
    etiq = {"es": "Menú", "ca": "Menú", "en": "Menu"}[lang]
    # <details> nativo: hamburguesa sin JavaScript, funciona siempre
    return (f'<header class="{clase}">'
            f'<a class="marca" href="{url("home", lang)}" aria-label="Europiscina">{marca}</a>'
            f'<nav class="menu">{items}</nav>'
            f'{selector(clave, lang)}'
            f'<details class="hamb"><summary aria-label="{etiq}">'
            f'<span class="hamb-icono"><i></i><i></i><i></i></span></summary>'
            f'<div class="hamb-panel"><nav>{items}</nav>'
            f'<a class="hamb-wa" href="{WA}">WhatsApp {WA_TXT}</a>'
            f'<a class="hamb-tel" href="tel:{TEL}">{TEL_TXT}</a>'
            f'</div></details>'
            f'</header>')


def enlaces_legales(lang):
    t = T[lang]
    return " · ".join(
        f'<a href="{url_legal(k, lang)}">{t[e]}</a>'
        for k, e in (("legal", "legal_avis"), ("priv", "legal_priv"), ("cookies", "legal_cook")))


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
    <span class="pie-legales">{enlaces_legales(lang)}</span>
  </div>
</footer>
<a class="wa" href="{WA}" aria-label="WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.64-2.05-.17-.3-.02-.46.13-.6.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.6-.92-2.2-.24-.58-.49-.5-.67-.5h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.480 1.46 1.07 2.88 1.22 3.08.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.28.17-1.41-.07-.13-.27-.2-.57-.35z"/><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21 5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2zm0 18.15c-1.53 0-3.03-.41-4.34-1.19l-.31-.18-3.23.85.86-3.15-.2-.32a8.2 8.2 0 0 1-1.26-4.37c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.83 2.41a8.18 8.18 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24z"/></svg><span>{t['wa']}</span></a>"""


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
