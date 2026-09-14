#!/usr/bin/env python3
"""
Inyecta datos estructurados (JSON-LD) en todas las páginas ya generadas.

Tres esquemas por página:
  1. Organization / LocalBusiness  -> quién eres, dónde, qué servicios
  2. BreadcrumbList                -> jerarquía de navegación
  3. FAQPage                       -> se extrae de los <details> de cada página

El bloque 3 es el que más pesa en las respuestas de los asistentes de IA:
son preguntas y respuestas literales, listas para ser citadas.
"""
import json, pathlib, re, html

BASE = pathlib.Path(__file__).parent
SITIO = "https://europiscina.es"

IDIOMA_DE_RUTA = lambda u: "ca" if u.startswith("/ca/") else ("en" if u.startswith("/en/") else "es")

# ------------------------------------------------------------------ 1. NEGOCIO
ORGANIZACION = {
 "@type": ["HomeAndConstructionBusiness", "LocalBusiness"],
 "@id": f"{SITIO}/#organization",
 "name": "Europiscina",
 "alternateName": "Europiscina Balaguer",
 "legalName": "GARCAM Industries SLU",
 "url": f"{SITIO}/",
 "logo": f"{SITIO}/img/logo.png",
 "image": f"{SITIO}/img/og-europiscina.jpg",
 "email": "comercial@europiscina.es",
 "telephone": "+34973446445",
 "taxID": "B10713675",
 "vatID": "ESB10713675",
 "foundingDate": "1969",
 "priceRange": "€€€",
 "slogan": "Aigua des del 1969, piscines des del 1999",
 "description": ("Construcción, reforma y mantenimiento de piscinas de obra, lámina armada, "
                 "gres porcelánico y poliéster. Equipo y maquinaria propios. "
                 "Official Partner de Astralpool Fluidra y miembros de ASOFAP."),
 "address": {
   "@type": "PostalAddress",
   "streetAddress": "Ctra. C-26, Km 22, Camí d'Albesa, s/n",
   "addressLocality": "Balaguer",
   "addressRegion": "Lleida",
   "postalCode": "25600",
   "addressCountry": "ES"},
 "geo": {"@type": "GeoCoordinates", "latitude": 41.7905, "longitude": 0.8062},
 "contactPoint": [
   {"@type": "ContactPoint", "telephone": "+34973446445",
    "contactType": "customer service", "contactOption": "TollFree",
    "areaServed": "ES", "availableLanguage": ["ca", "es", "en"]},
   {"@type": "ContactPoint", "telephone": "+34680335438",
    "contactType": "sales", "areaServed": "ES",
    "availableLanguage": ["ca", "es", "en"]}],
 "openingHoursSpecification": [{
   "@type": "OpeningHoursSpecification",
   "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
   "opens": "08:00", "closes": "18:00"}],
 "areaServed": [{"@type": "AdministrativeArea", "name": n} for n in
   ["Provincia de Lleida", "Provincia de Tarragona", "Provincia de Huesca",
    "Provincia de Barcelona", "Illes Balears", "Andorra"]],
 "knowsAbout": [
   "Construcción de piscinas de hormigón armado encofrado", "Lámina armada Renolit Alkorplan",
   "Gres porcelánico Rosa Gres", "Piscinas prefabricadas de poliéster",
   "Cloración salina", "Detección de fugas de agua en piscinas",
   "Mantenimiento de piscinas de uso público"],
 "hasOfferCatalog": {
   "@type": "OfferCatalog",
   "name": "Servicios de construcción, reforma y mantenimiento de piscinas",
   "itemListElement": [
     {"@type": "Offer", "itemOffered": {"@type": "Service",
      "name": "Construcción de piscinas de obra en hormigón armado",
      "description": "Diseño y construcción integral de piscinas de obra en hormigón armado encofrado, en sistema skimmer, desbordante o infinity, para particulares, comunidades y ayuntamientos. No trabajamos con hormigón proyectado: el encofrado da espesor constante y mayor durabilidad.",
      "url": f"{SITIO}/piscinas-de-obra/"}},
     {"@type": "Offer", "itemOffered": {"@type": "Service",
      "name": "Impermeabilización con lámina armada Renolit Alkorplan",
      "description": "Revestimiento estanco con PVC armado de 1,5 a 2,0 mm termosoldado in situ, en obra nueva y en rehabilitación de piscinas que pierden agua. Instaladores oficiales.",
      "url": f"{SITIO}/piscinas-lamina-armada/"}},
     {"@type": "Offer", "itemOffered": {"@type": "Service",
      "name": "Instalación de piscinas prefabricadas de poliéster",
      "description": "Venta, excavación, colocación con grúa e instalación hidráulica de vasos monobloque de poliéster reforzado con fibra de vidrio.",
      "url": f"{SITIO}/piscinas-poliester/"}},
     {"@type": "Offer", "itemOffered": {"@type": "Service",
      "name": "Revestimiento de piscinas con gres porcelánico Rosa Gres",
      "description": "Revestimiento cerámico técnico antideslizante para vaso, coronación y playa, en sistemas skimmer, desbordante y Slim.",
      "url": f"{SITIO}/gres-porcelanico/"}},
     {"@type": "Offer", "itemOffered": {"@type": "Service",
      "name": "Localización y reparación de fugas de agua en piscinas",
      "description": "Diagnóstico de pérdidas en vaso, hidráulica enterrada y piezas de paso, y reparación sin destrozar la obra.",
      "url": f"{SITIO}/fugas-de-agua/"}},
     {"@type": "Offer", "itemOffered": {"@type": "Service",
      "name": "Mantenimiento de piscinas y servicio técnico Astralpool",
      "description": "Apertura y cierre de temporada, control del agua, electrólisis salina y servicio técnico para particulares, comunidades y piscinas municipales.",
      "url": f"{SITIO}/mantenimiento/"}},
     {"@type": "Offer", "itemOffered": {"@type": "Service",
      "name": "Reforma y rehabilitación de piscinas",
      "description": "Cambio de revestimiento, renovación de sala de máquinas, bomba de velocidad variable, iluminación LED, climatización y adaptación a normativa.",
      "url": f"{SITIO}/reformas/"}}]}}

DELEGACION = {
 "@type": ["HomeAndConstructionBusiness", "LocalBusiness"],
 "@id": f"{SITIO}/#delegacion-tarragona",
 "name": "Europiscina Tarragona",
 "legalName": "GARCAM Industries SLU",
 "url": f"{SITIO}/contacto/",
 "telephone": "+34973446445",
 "image": f"{SITIO}/img/og-europiscina.jpg",
 "parentOrganization": {"@id": f"{SITIO}/#organization"},
 "address": {
   "@type": "PostalAddress",
   "streetAddress": "Carrer del Doctor Alexandre Fleming, 3",
   "addressLocality": "Cambrils",
   "addressRegion": "Tarragona",
   "postalCode": "43850",
   "addressCountry": "ES"},
 "areaServed": [{"@type": "AdministrativeArea", "name": n}
                for n in ["Provincia de Tarragona", "Costa Daurada"]]}


def extraer(ruta):
    """Saca de la página el título, la descripción y las FAQ ya publicadas."""
    p = BASE / (ruta.strip("/") + "/index.html" if ruta != "/" else "index.html")
    s = p.read_text(encoding="utf-8")
    lim = lambda t: html.unescape(re.sub(r"<[^>]+>", "", t)).strip()
    tit = re.search(r"<title>(.*?)</title>", s, re.S)
    des = re.search(r'name="description" content="(.*?)"', s, re.S)
    faqs = [(lim(q), lim(a)) for q, a in
            re.findall(r"<summary>(.*?)</summary><p>(.*?)</p>", s, re.S)]
    miga = re.search(r'<p class="miga">.*?·\s*([^<]+)</p>', s, re.S)
    return p, s, (lim(tit.group(1)) if tit else ""), (lim(des.group(1)) if des else ""), faqs, \
           (lim(miga.group(1)) if miga else "")


def bloque(ruta, lang, titulo, desc, faqs, miga):
    grafo = [ORGANIZACION, DELEGACION, {
        "@type": "WebSite",
        "@id": f"{SITIO}/#website",
        "url": f"{SITIO}/",
        "name": "Europiscina",
        "publisher": {"@id": f"{SITIO}/#organization"},
        "inLanguage": ["ca-ES", "es-ES", "en"]}]

    grafo.append({
        "@type": "WebPage",
        "@id": f"{SITIO}{ruta}#webpage",
        "url": f"{SITIO}{ruta}",
        "name": titulo,
        "description": desc,
        "inLanguage": lang,
        "isPartOf": {"@id": f"{SITIO}/#website"},
        "about": {"@id": f"{SITIO}/#organization"},
        "primaryImageOfPage": f"{SITIO}/img/og-europiscina.jpg"})

    if miga:
        grafo.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Inicio",
               "item": f"{SITIO}/" if lang == "es" else f"{SITIO}/{lang}/"},
              {"@type": "ListItem", "position": 2, "name": miga,
               "item": f"{SITIO}{ruta}"}]})

    if faqs:
        grafo.append({
            "@type": "FAQPage",
            "@id": f"{SITIO}{ruta}#faq",
            "inLanguage": lang,
            "mainEntity": [{
              "@type": "Question", "name": q,
              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]})

    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": grafo},
                         ensure_ascii=False, separators=(",", ":"))
            + "</script>")


if __name__ == "__main__":
    rutas = []
    for p in sorted(BASE.rglob("index.html")):
        d = str(p.parent.relative_to(BASE)).strip(".")
        rutas.append("/" + d.strip("/") + "/" if d else "/")

    n_faq = 0
    for ruta in rutas:
        p, s, tit, des, faqs, miga = extraer(ruta)
        lang = IDIOMA_DE_RUTA(ruta)
        s = re.sub(r'<script type="application/ld\+json">.*?</script>', "", s, flags=re.S)
        # Open Graph y Twitter, para que el enlace se vea bien al compartirlo
        og = (f'<meta property="og:type" content="website">'
              f'<meta property="og:site_name" content="Europiscina">'
              f'<meta property="og:locale" content="{lang}_ES">'
              f'<meta property="og:title" content="{html.escape(tit)}">'
              f'<meta property="og:description" content="{html.escape(des)}">'
              f'<meta property="og:url" content="{SITIO}{ruta}">'
              f'<meta property="og:image" content="{SITIO}/img/og-europiscina.jpg">'
              f'<meta name="twitter:card" content="summary_large_image">')
        s = re.sub(r'(<meta property="og:[^>]*>|<meta name="twitter:[^>]*>)', "", s)
        s = s.replace("</head>", og + bloque(ruta, lang, tit, des, faqs, miga) + "\n</head>")
        p.write_text(s, encoding="utf-8")
        n_faq += len(faqs)
        print(f"  {ruta:<32} {len(faqs)} FAQ")
    print(f"\n{len(rutas)} páginas, {n_faq} preguntas indexables")
