#!/usr/bin/env python3
"""Portada, contacto y configurador en es/ca/en + sitemap + redirecciones."""
import pathlib, json
from motor import (BASE, IMG, WA, TEL, TEL_TXT, WA_TXT, MAIL, LANGS, FUENTES,
                   SLUGS, url, T, cabecera, pie, hreflang, imagen)

# ============================================================ PORTADA
HOME = {
"es": dict(
 title="Europiscina · Constructores de piscinas en Lleida",
 desc="Piscinas de obra, lámina armada y poliéster en Lleida, Huesca, Tarragona, Andorra y Mallorca. Construimos piscinas desde 1999 y trabajamos con agua desde 1969.",
 h1="Más de 25 años construyendo piscinas para nuestros clientes.",
 alt_hero="Piscina de obra con coronación de travertino entre olivos, construida por Europiscina", alt_publico="Piscina municipal construida por Europiscina",
 sub="Casi 60 años trabajando con el agua. GARCAM nació en 1969 con prefabricados de hormigón, riegos, tuberías e instalaciones hidráulicas. En 1999 entramos en el mundo de las piscinas.",
 
 
  cta1="Pedir presupuesto", cta2="Ver obras",
 r1="Cómo trabajamos", h2a="Nadie subcontrata tu piscina.",
 p1="""<p>Todo empezó un verano de 1999, construyendo una piscina en casa de nuestro jefe. Sin buscarlo, aquella piscina trajo otra, y luego otra. Hoy ya son más de 1.000 piscinas construidas y más de 1.000 clientes, muchos de los cuales siguen confiando en nosotros años después.</p>
        <p>Excavamos, construimos, revestimos, alicatamos y ponemos en marcha cada piscina con personal propio: albañiles, fontaneros, electricistas y técnicos de piscina. Un solo equipo, de principio a fin. No hay una empresa o gente distinta cada semana ni desaparecemos cuando acaba la obra.</p>
        <p>No solemos ser el presupuesto más barato. Y no queremos serlo. Preferimos hacer las cosas bien, con equipo propio, y seguir respondiendo años después, cuando toca cambiar una bomba, revisar una instalación o resolver un problema.</p>""",
 r2="Qué construimos", h2b="Cuatro maneras de hacer<br>la misma promesa.",
 servicios=[
  ("obra", "Piscinas de obra", "Hormigón armado, sin límite de forma ni medida. Desbordantes, skimmer y carriles de natación. La opción cuando el terreno o la casa piden algo que no existe en catálogo.", "Ver piscinas de obra"),
  ("lamina", "Lámina armada", "Impermeabilización con PVC reforzado Renolit Alkorplan, soldada in situ. La solución más rápida para reformar una piscina que pierde agua.", "Ver lámina armada"),
  ("conf", "Poliéster prefabricado", "Vaso monobloque, colocado con grúa. De la excavación al agua en cuestión de días. Calcula tu precio ahora en el configurador.", "Calcular precio"),
  ("mant", "Mantenimiento y averías", "Apertura y cierre de temporada, tratamiento del agua, electrólisis salina y búsqueda de fugas. Para particulares, comunidades y piscinas públicas.", "Ver mantenimiento")],
 r3="Obras", h2c="Todas estas están construidas por nosotros.",
 r4="Obra pública", h2d="Cuando el cliente es<br>un ayuntamiento, no hay margen.",
 pub="""<p>Buena parte de nuestro trabajo son piscinas municipales, vasos públicos y reformas para consistorios de la comarca. Se adjudican por concurso, con pliego técnico, plazo cerrado y penalización por retraso. No se elige al que cae mejor.</p>
        <p>Si un ayuntamiento nos deja abierta su piscina municipal en mayo sabiendo que tiene que estar llena en junio, tu jardín no es un problema.</p>""",
 r5="Clientes", h2e="Lo dicen mejor ellos.",
 citas=[("Era la que más subía el presupuesto, pero la calidad de los materiales y que todos los operarios fueran de su plantilla nos convenció. No nos equivocamos.", "Francesc · piscina desbordante de hormigón"),
        ("Precio un poco más caro que los otros dos presupuestos que tenía, pero me la recomendó un familiar. Gente seria y profesional.", "Josep · particular"),
        ("Nos han reformado la piscina vieja de la torre. Empresa muy seria y cumplidora.", "Lídia · reforma")],
 r6="Dónde trabajamos", h2f="Cerca es una condición<br>del servicio, no un detalle.",
 zonas=[("Lleida","Sede y almacén en Balaguer"),("Huesca","Cinca Medio y Litera"),
        ("Tarragona","Delegación en Cambrils"),("Andorra","Proyectos seleccionados"),
        ("Mallorca","Delegación en Palma")]),

"ca": dict(
 title="Europiscina · Constructors de piscines a Lleida",
 desc="Piscines d'obra, làmina armada i polièster a Lleida, Osca, Tarragona, Andorra i Mallorca. Construïm piscines des del 1999 i treballem amb aigua des del 1969.",
 h1="Més de 25 anys construint piscines per als nostres clients.",
 alt_hero="Piscina d'obra amb coronació de travertí entre oliveres, construïda per Europiscina", alt_publico="Piscina municipal construïda per Europiscina",
 sub="Gairebé 60 anys treballant amb l'aigua. GARCAM va néixer el 1969 amb prefabricats de formigó, regs, canonades i instal·lacions hidràuliques. El 1999 vam entrar al món de les piscines.",
 cta1="Demanar pressupost", cta2="Veure obres",
 r1="Com treballem", h2a="Ningú subcontracta la teva piscina.",
 p1="""<p>Tot va començar un estiu del 1999, construint una piscina a casa del nostre cap. Sense buscar-ho, aquella piscina en va portar una altra, i després una altra. Avui ja són més de 1.000 piscines construïdes i més de 1.000 clients, molts dels quals continuen confiant en nosaltres anys després.</p>
        <p>Excavem, construïm, revestim, enrajolem i posem en marxa cada piscina amb personal propi: paletes, fontaners, electricistes i tècnics de piscina. Un sol equip, de principi a fi. No hi ha una empresa o gent diferent cada setmana ni desapareixem quan s'acaba l'obra.</p>
        <p>No acostumem a ser el pressupost més barat. I no ho volem ser. Preferim fer les coses bé, amb equip propi, i continuar responent anys després, quan toca canviar una bomba, revisar una instal·lació o solucionar un problema.</p>""",
 r2="Què construïm", h2b="Quatre maneres de fer<br>la mateixa promesa.",
 servicios=[
  ("obra", "Piscines d'obra", "Formigó armat, sense límit de forma ni mida. Desbordants, skimmer i carrils de natació. L'opció quan el terreny o la casa demanen alguna cosa que no existeix al catàleg.", "Veure piscines d'obra"),
  ("lamina", "Làmina armada", "Impermeabilització amb PVC reforçat Renolit Alkorplan, soldada in situ. La solució més ràpida per reformar una piscina que perd aigua.", "Veure làmina armada"),
  ("conf", "Polièster prefabricat", "Vas monobloc, col·locat amb grua. De l'excavació a l'aigua en qüestió de dies. Calcula el teu preu ara al configurador.", "Calcular preu"),
  ("mant", "Manteniment i avaries", "Obertura i tancament de temporada, tractament de l'aigua, electròlisi salina i cerca de fuites. Per a particulars, comunitats i piscines públiques.", "Veure manteniment")],
 r3="Obres", h2c="Totes aquestes les hem construït nosaltres.",
 r4="Obra pública", h2d="Quan el client és<br>un ajuntament, no hi ha marge.",
 pub="""<p>Bona part de la nostra feina són piscines municipals, vasos públics i reformes per a consistoris de la comarca. S'adjudiquen per concurs, amb plec tècnic, termini tancat i penalització per retard. No es tria qui cau més bé.</p>
        <p>Si un ajuntament ens deixa obrir la seva piscina municipal al maig sabent que ha d'estar plena al juny, el teu jardí no és cap problema.</p>""",
 r5="Clients", h2e="Ho diuen millor ells.",
 citas=[("Era la que més pujava el pressupost, però la qualitat dels materials i que tots els operaris fossin de la seva plantilla ens va convèncer. No ens vam equivocar.", "Francesc · piscina desbordant de formigó"),
        ("Preu una mica més car que els altres dos pressupostos que tenia, però me la va recomanar un familiar. Gent seriosa i professional.", "Josep · particular"),
        ("Ens han reformat la piscina vella de la torre. Empresa molt seriosa i complidora.", "Lídia · reforma")],
 r6="On treballem", h2f="A prop és una condició<br>del servei, no un detall.",
 zonas=[("Lleida","Seu i magatzem a Balaguer"),("Osca","Cinca Mitjà i Llitera"),
        ("Tarragona","Delegació a Cambrils"),("Andorra","Projectes seleccionats"),
        ("Mallorca","Delegació a Palma")]),

"en": dict(
 title="Europiscina · Pool builders in Lleida, Catalonia",
 desc="Concrete, reinforced membrane and fibreglass pools in Lleida, Huesca, Tarragona, Andorra and Mallorca. Building pools since 1999, working with water since 1969.",
 h1="More than 25 years building pools for our clients.",
 alt_hero="Concrete pool with travertine coping among olive trees, built by Europiscina", alt_publico="Municipal swimming pool built by Europiscina",
 sub="Almost 60 years working with water. GARCAM was founded in 1969 in precast concrete, irrigation, pipework and hydraulic installations. In 1999 we moved into swimming pools.",
 cta1="Request a quote", cta2="See our work",
 r1="How we work", h2a="Nobody subcontracts your pool.",
 p1="""<p>It all started one summer in 1999, building a pool at our boss's house. Without setting out to, that pool led to another, and then another. Today there are more than 1,000 pools built and more than 1,000 clients, many of whom still come back to us years later.</p>
        <p>We excavate, build, line, tile and commission every pool with our own staff: bricklayers, plumbers, electricians and pool technicians. One team, from start to finish. There is no different company or crew each week, and we do not disappear once the job is done.</p>
        <p>We are not usually the cheapest quote. And we do not want to be. We would rather do things properly, with our own team, and still be answering years later, when a pump needs changing or an installation needs checking.</p>""",
 r2="What we build", h2b="Four ways of making<br>the same promise.",
 servicios=[
  (None, "Concrete pools", "Reinforced concrete, no limit on shape or size. Infinity edges, skimmer systems and swimming lanes. The option when the site or the house asks for something no catalogue offers.", None),
  (None, "Reinforced membrane", "Waterproofing with Renolit Alkorplan reinforced PVC, welded on site. The fastest way to bring a leaking pool back to life.", None),
  ("conf", "Fibreglass shells", "A one-piece shell craned into place. From excavation to water in a matter of days. Work out your price in the calculator.", "Calculate price"),
  ("mant", "Maintenance and repairs", "Season opening and closing, water treatment, salt chlorination and leak detection. For private owners, communities and public pools.", "See maintenance")],
 r3="Our work", h2c="Every one of these was built by us.",
 r4="Public sector", h2d="When the client is a town council,<br>there is no margin for error.",
 pub="""<p>A large part of our work is municipal pools, public basins and refurbishments for local councils. These are awarded by tender, with technical specifications, fixed deadlines and penalties for delay. Nobody is chosen because they are likeable.</p>
        <p>If a council trusts us to have its municipal pool open in May knowing it must be full by June, your garden is not a problem.</p>""",
 r5="Clients", h2e="They say it better than we do.",
 citas=[("Theirs was the highest quote, but the quality of the materials and the fact that every worker was on their own payroll convinced us. We were not wrong.", "Francesc · concrete infinity pool"),
        ("Slightly more expensive than the other two quotes I had, but a relative recommended them. Serious, professional people.", "Josep · private client"),
        ("They refurbished the old pool at our country house. A very serious and reliable company.", "Lídia · refurbishment")],
 r6="Where we work", h2f="Being close by is part of<br>the service, not a detail.",
 zonas=[("Lleida","Head office and yard in Balaguer"),("Huesca","Cinca Medio and Litera"),
        ("Tarragona","Branch in Cambrils"),("Andorra","Selected projects"),
        ("Mallorca","Branch in Palma")]),
}

FOTOS = [("mos-dron-cenital","g-alta"),("mos-andorra","g-ancha"),
         ("mos-escala-pedra","g-tercio"),("mos-lamina-gris","g-tercio"),
         ("mos-gres-fusta","g-tercio"),("mos-dron-textura","g-full")]
PIES_FOTO = {
 "es":["Obra · Vista cenital","Andorra · Piscina interior","Detalle · Escalera de piedra",
       "Lámina armada · Gris antracita","Gres porcelánico · Efecto madera","Gres · Textura del vaso"],
 "ca":["Obra · Vista zenital","Andorra · Piscina interior","Detall · Escala de pedra",
       "Làmina armada · Gris antracita","Gres porcellànic · Efecte fusta","Gres · Textura del vas"],
 "en":["Concrete · Aerial view","Andorra · Indoor pool","Detail · Stone steps",
       "Reinforced membrane · Anthracite","Porcelain tile · Wood effect","Porcelain · Pool surface"],
}
MUNICIPIOS = ["Preixens", "Algerri", "Balaguer", "La Sentiu de Sió", "Lleida",
              "Guissona", "Tarragona", "Térmens", "Guimerà"]
MAS = {"es": "y muchos más", "ca": "i molts altres", "en": "and many more"}

FORM = {
 "es": dict(rot="Empecemos", h2="Cuéntanos qué tienes<br>y qué quieres.",
   tel="Teléfono", wa="WhatsApp", mail="Correo", dir="Almacén y tienda", hor="Horario",
   horv="Lunes a viernes, 8:00 a 18:00", nom="Nombre", telf="Teléfono", mailf="Correo",
   pob="Población", tipo="Qué necesitas", msg="Algo más que debamos saber",
   ph="Medidas aproximadas, acceso de maquinaria, plazos…", env="Enviar solicitud",
   legal="Te llamamos en 48 horas laborables. Usamos tus datos solo para preparar el presupuesto. Responsable: GARCAM Industries SLU.",
   ops=["Piscina de obra","Lámina armada","Poliéster prefabricado","Gres porcelánico",
        "Reforma de piscina existente","Fuga de agua","Mantenimiento","Todavía no lo sé"]),
 "ca": dict(rot="Comencem", h2="Explica'ns què tens<br>i què vols.",
   tel="Telèfon", wa="WhatsApp", mail="Correu", dir="Magatzem i botiga", hor="Horari",
   horv="De dilluns a divendres, 8:00 a 18:00", nom="Nom", telf="Telèfon", mailf="Correu",
   pob="Població", tipo="Què necessites", msg="Alguna cosa més que hàgim de saber",
   ph="Mides aproximades, accés de maquinària, terminis…", env="Enviar sol·licitud",
   legal="Et truquem en 48 hores laborables. Fem servir les teves dades només per preparar el pressupost. Responsable: GARCAM Industries SLU.",
   ops=["Piscina d'obra","Làmina armada","Polièster prefabricat","Gres porcellànic",
        "Reforma de piscina existent","Fuita d'aigua","Manteniment","Encara no ho sé"]),
 "en": dict(rot="Let's start", h2="Tell us what you have<br>and what you want.",
   tel="Phone", wa="WhatsApp", mail="Email", dir="Yard and shop", hor="Opening hours",
   horv="Monday to Friday, 8:00 to 18:00", nom="Name", telf="Phone", mailf="Email",
   pob="Town", tipo="What do you need", msg="Anything else we should know",
   ph="Approximate dimensions, machinery access, timing…", env="Send request",
   legal="We call back within 48 working hours. Your data is used only to prepare the quote. Data controller: GARCAM Industries SLU.",
   ops=["Concrete pool","Reinforced membrane","Fibreglass shell","Porcelain tile",
        "Refurbishment of an existing pool","Water leak","Maintenance","Not sure yet"]),
}


def bloque_form(lang, con_rotulo=True):
    f = FORM[lang]
    ops = "".join(f"<option>{o}</option>" for o in f["ops"])
    rot = f'<p class="rotulo">{f["rot"]}</p>\n  <h2>{f["h2"]}</h2>' if con_rotulo else ""
    return f"""<section class="bloque contacto" id="presupuesto">
  {rot}
  <div class="form-wrap">
    <div class="datos">
      <p><span>{f['tel']}</span><a href="tel:{TEL}">{TEL_TXT}</a></p>
      <p><span>{f['wa']}</span><a href="{WA}">{WA_TXT}</a></p>
      <p><span>{f['mail']}</span><a href="mailto:{MAIL}">{MAIL}</a></p>
      <p><span>{f['dir']}</span>Ctra. C-26, km 22<br>Camí d'Albesa, s/n<br>25600 Balaguer, Lleida</p>
      <p><span>{f['hor']}</span>{f['horv']}</p>
    </div>
    <form name="presupuesto" method="POST" data-netlify="true" netlify-honeypot="empresa">
      <input type="hidden" name="form-name" value="presupuesto">
      <input type="hidden" name="idioma" value="{lang}">
      <p style="display:none"><label>No rellenar <input name="empresa"></label></p>
      <div class="campos">
        <div class="campo"><label for="nombre">{f['nom']}</label><input id="nombre" name="nombre" required></div>
        <div class="campo"><label for="tel">{f['telf']}</label><input id="tel" name="telefono" type="tel" required></div>
        <div class="campo"><label for="mail">{f['mailf']}</label><input id="mail" name="email" type="email"></div>
        <div class="campo"><label for="pob">{f['pob']}</label><input id="pob" name="poblacion"></div>
        <div class="campo ancho"><label for="tipo">{f['tipo']}</label>
          <select id="tipo" name="tipo">{ops}</select></div>
        <div class="campo ancho"><label for="msg">{f['msg']}</label>
          <textarea id="msg" name="mensaje" placeholder="{f['ph']}"></textarea></div>
      </div>
      <button class="enviar" type="submit">{f['env']}</button>
      <p class="legal">{f['legal']}</p>
    </form>
  </div>
</section>"""


def escribir_home(lang):
    h, t = HOME[lang], T[lang]
    servs = ""
    for clave, tit, txt, cta in h["servicios"]:
        u = url(clave, lang) if clave else None
        enlace = f'<p class="dato"><a href="{u}">{cta}</a></p>' if u and cta else ""
        servs += f'<article class="serv"><h3>{tit}</h3><p>{txt}</p>{enlace}</article>'
    fotos = ""
    for (clave, cls), pie_f in zip(FOTOS, PIES_FOTO[lang]):
        anchura = "100vw" if cls == "g-full" else "(max-width:760px) 50vw, 33vw"
        fotos += (f'<figure class="pieza {cls}">{imagen(clave, pie_f, sizes=anchura)}'
                  f'<figcaption>{pie_f}</figcaption></figure>')
    citas = "".join(f'<blockquote class="cita">{c}<cite>{a}</cite></blockquote>' for c, a in h["citas"])
    zonas = "".join(f"<li><strong>{n}</strong><span>{d}</span></li>" for n, d in h["zonas"])
    muni = "".join(f"<li>{m}</li>" for m in MUNICIPIOS)
    muni += f'<li class="mas">{MAS[lang]}</li>'

    doc = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{h['title']}</title>
<meta name="description" content="{h['desc']}">
<link rel="canonical" href="https://europiscina.es{url('home', lang)}">
{hreflang('home')}
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/img/icon-512.png" type="image/png" sizes="512x512">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<meta name="theme-color" content="#0B4F6C">
{FUENTES}
<link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
<a class="saltar" href="#principal">{t['saltar']}</a>
{cabecera('home', lang, clara=True)}
<main id="principal">

<section class="hero">
  <div class="hero-img">{imagen("hero-oliveres", h["alt_hero"], sizes="100vw", eager=True)}</div>
  <h1>{h['h1']}</h1>
  <div class="waterline"></div>
  <div class="hero-pie">
    <p>{h['sub']}</p>
    <div class="acciones">
      <a class="btn btn-solid" href="{url('cont', lang)}">{h['cta1']}</a>
      <a class="btn btn-ghost" href="#obras">{h['cta2']}</a>
    </div>
  </div>
</section>

<section class="bloque manifiesto">
  <div><p class="rotulo">{h['r1']}</p><h2>{h['h2a']}</h2></div>
  <div class="col-txt">{h['p1']}</div>
</section>

<section class="bloque servicios">
  <p class="rotulo">{h['r2']}</p><h2>{h['h2b']}</h2>
  <div class="rejilla">{servs}</div>
</section>

<section class="bloque" id="obras">
  <p class="rotulo">{h['r3']}</p><h2>{h['h2c']}</h2>
  <div class="mosaico">{fotos}</div>
</section>

<section class="bloque publico">
  <p class="rotulo">{h['r4']}</p><h2>{h['h2d']}</h2>
  <div class="publico-txt">{h['pub']}</div>
  <ul class="municipios">{muni}</ul>
  <div class="foto-publico">{imagen("pub-municipal", h["alt_publico"], sizes="100vw")}</div>
</section>

<section class="bloque voces">
  <p class="rotulo">{h['r5']}</p><h2>{h['h2e']}</h2>
  <div class="voces-grid">{citas}</div>
</section>

<section class="bloque zonas">
  <p class="rotulo">{h['r6']}</p><h2>{h['h2f']}</h2>
  <ul>{zonas}</ul>
</section>

{bloque_form(lang)}
</main>
{pie(lang)}
</body>
</html>"""
    d = BASE / url("home", lang).strip("/")
    d.mkdir(parents=True, exist_ok=True)
    d.joinpath("index.html").write_text(doc, encoding="utf-8")
    return url("home", lang)


# ============================================================ CONTACTO
CONT = {
 "es": dict(title="Contacto y presupuesto | Europiscina, Balaguer (Lleida)",
   desc=f"Pide presupuesto de piscina en Lleida. Teléfono {TEL_TXT}, WhatsApp {WA_TXT}. Almacén y tienda en Ctra. C-26 km 22, Balaguer.",
   miga="Contacto", h1="Cuéntanos qué tienes y qué quieres.",
   sub="Respondemos en 48 horas laborables. Si prefieres hablar antes de escribir, el WhatsApp es el camino más rápido."),
 "ca": dict(title="Contacte i pressupost | Europiscina, Balaguer (Lleida)",
   desc=f"Demana pressupost de piscina a Lleida. Telèfon {TEL_TXT}, WhatsApp {WA_TXT}. Magatzem i botiga a Ctra. C-26 km 22, Balaguer.",
   miga="Contacte", h1="Explica'ns què tens i què vols.",
   sub="Responem en 48 hores laborables. Si prefereixes parlar abans d'escriure, el WhatsApp és el camí més ràpid."),
 "en": dict(title="Contact and quotes | Europiscina, Balaguer (Lleida)",
   desc=f"Request a pool quote in Lleida. Phone {TEL_TXT}, WhatsApp {WA_TXT}. Yard and shop at Ctra. C-26 km 22, Balaguer.",
   miga="Contact", h1="Tell us what you have and what you want.",
   sub="We reply within 48 working hours. If you would rather talk than write, WhatsApp is the fastest route."),
}


def escribir_contacto(lang):
    c, t = CONT[lang], T[lang]
    doc = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c['title']}</title>
<meta name="description" content="{c['desc']}">
<link rel="canonical" href="https://europiscina.es{url('cont', lang)}">
{hreflang('cont')}
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/img/icon-512.png" type="image/png" sizes="512x512">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<meta name="theme-color" content="#0B4F6C">
{FUENTES}
<link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
<a class="saltar" href="#principal">{t['saltar']}</a>
{cabecera('cont', lang)}
<main id="principal">
<section class="cabecera">
  <p class="miga"><a href="{url('home', lang)}">{t['inicio']}</a> · {c['miga']}</p>
  <h1>{c['h1']}</h1>
  <p class="entradilla">{c['sub']}</p>
</section>
{bloque_form(lang, con_rotulo=False)}
</main>
{pie(lang)}
</body>
</html>"""
    d = BASE / url("cont", lang).strip("/")
    d.mkdir(parents=True, exist_ok=True)
    d.joinpath("index.html").write_text(doc, encoding="utf-8")
    return url("cont", lang)


if __name__ == "__main__":
    for l in LANGS:
        print(" home    ", escribir_home(l))
        print(" contacto", escribir_contacto(l))
