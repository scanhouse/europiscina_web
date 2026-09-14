#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Páginas legales: aviso legal, privacidad y cookies, en es/ca/en.

BORRADOR TÉCNICO. Redactado sobre los requisitos del art. 10 LSSI-CE,
del RGPD (UE) 2016/679 y de la LOPDGDD 3/2018, y sobre lo que el sitio
hace realmente. NO sustituye la revisión de un abogado.
Los tramos marcados con [[ ]] los tiene que completar o validar Núria.
"""
import pathlib
from motor import (BASE, WA, TEL, TEL_TXT, WA_TXT, MAIL, LANGS, FUENTES,
                   T, cabecera, pie, url)

EMPRESA = "GARCAM Industries SLU"
CIF = "B10713675"
DIR = "Ctra. C-26, km 22, Camí d'Albesa, s/n · 25600 Balaguer (Lleida)"
REGISTRO = "[[Registro Mercantil de Lleida, tomo __, folio __, hoja __ — completar]]"

SLUG = {
 "legal":   {"es": "aviso-legal", "ca": "avis-legal",  "en": "legal-notice"},
 "priv":    {"es": "privacidad",  "ca": "privacitat",  "en": "privacy"},
 "cookies": {"es": "cookies",     "ca": "galetes",     "en": "cookies"},
}
ruta = lambda k, l: ("" if l == "es" else f"/{l}") + "/" + SLUG[k][l] + "/"

PLANTILLA = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://europiscina.es{url}">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<meta name="theme-color" content="#0B4F6C">
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
  <p class="entradilla">{sub}</p>
</section>
<section class="bloque legal">{cuerpo}</section>
</main>
{pie}
</body>
</html>"""


def escribir(clave, lang, d):
    u = ruta(clave, lang)
    dest = BASE / u.strip("/")
    dest.mkdir(parents=True, exist_ok=True)
    dest.joinpath("index.html").write_text(PLANTILLA.format(
        lang=lang, title=d["title"], desc=d["desc"], url=u, fuentes=FUENTES,
        saltar=T[lang]["saltar"], nav=cabecera(clave, lang), home=url("home", lang),
        inicio=T[lang]["inicio"], miga=d["miga"], h1=d["h1"], sub=d["sub"],
        cuerpo=d["cuerpo"], pie=pie(lang)), encoding="utf-8")
    return u


# =============================================================== CASTELLANO
IDENT_ES = f"""<h2>1. Titular del sitio web</h2>
<p>En cumplimiento del artículo 10 de la Ley 34/2002, de servicios de la sociedad de la información
y de comercio electrónico, se informa de los datos del titular de este sitio web:</p>
<ul>
 <li><strong>Denominación social:</strong> {EMPRESA}, que opera bajo la marca comercial Europiscina</li>
 <li><strong>NIF:</strong> {CIF}</li>
 <li><strong>Domicilio:</strong> {DIR}</li>
 <li><strong>Correo electrónico:</strong> <a href="mailto:{MAIL}">{MAIL}</a></li>
 <li><strong>Teléfono:</strong> {TEL_TXT}</li>
 <li><strong>Datos registrales:</strong> {REGISTRO}</li>
</ul>"""

LEGAL_ES = dict(
 title="Aviso legal | Europiscina",
 desc="Aviso legal y condiciones de uso del sitio web de Europiscina, marca de GARCAM Industries SLU.",
 miga="Aviso legal", h1="Aviso legal",
 sub="Condiciones de uso de este sitio web y datos identificativos de su titular.",
 cuerpo=IDENT_ES + """
<h2>2. Objeto y condiciones de uso</h2>
<p>Este sitio web tiene por objeto dar a conocer los servicios de construcción, reforma y mantenimiento
de piscinas que presta la empresa, así como facilitar el contacto con clientes potenciales.</p>
<p>El acceso al sitio es gratuito y no requiere registro. Quien accede se compromete a hacer un uso
conforme a la ley y a no emplear el sitio ni los formularios para fines ilícitos, para introducir
código malicioso o para enviar comunicaciones no solicitadas.</p>

<h2>3. Carácter orientativo de los precios</h2>
<p>El configurador de piscinas y cualquier otro importe publicado en este sitio tienen carácter
<strong>meramente informativo y no vinculante</strong>. Los precios se calculan sobre la tarifa vigente
y sobre supuestos de instalación estándar, y no incluyen licencias municipales, conexión eléctrica,
pavimentación perimetral, vallado ni jardinería.</p>
<p>Circunstancias como la presencia de roca, un nivel freático alto, el acceso de maquinaria o el estado
del terreno modifican el importe. El presupuesto en firme se emite únicamente por escrito y tras
visita técnica. Ninguna cifra mostrada en el sitio constituye una oferta contractual.</p>

<h2>4. Propiedad intelectual e industrial</h2>
<p>Los textos, fotografías, diseño y código de este sitio son titularidad de la empresa o se utilizan
con autorización. Las fotografías corresponden a obras ejecutadas por la empresa. Las marcas de
terceros que aparecen citadas (Astralpool, Fluidra, Renolit Alkorplan, Rosa Gres, entre otras)
pertenecen a sus respectivos titulares y se mencionan únicamente a título informativo.</p>
<p>Queda prohibida la reproducción o distribución de los contenidos sin autorización previa
y por escrito.</p>

<h2>5. Responsabilidad</h2>
<p>La empresa procura que la información publicada sea exacta y esté actualizada, pero no puede
garantizar la ausencia de errores tipográficos o de datos desactualizados. Tampoco responde de las
interrupciones del servicio derivadas de causas ajenas a su control.</p>
<p>El sitio puede contener enlaces a webs de terceros. La empresa no controla ni responde de sus
contenidos.</p>

<h2>6. Legislación aplicable y jurisdicción</h2>
<p>Estas condiciones se rigen por la legislación española. Para cualquier controversia, y salvo que la
normativa de consumo establezca otro fuero imperativo, las partes se someten a los juzgados y
tribunales de Lleida.</p>

<h2>7. Actualización</h2>
<p>Este aviso legal puede modificarse. La versión aplicable es la publicada en cada momento
en esta página.</p>""")

PRIV_ES = dict(
 title="Política de privacidad | Europiscina",
 desc="Cómo trata Europiscina los datos personales recogidos a través de su web: finalidad, base jurídica, conservación y derechos.",
 miga="Privacidad", h1="Política de privacidad",
 sub="Qué datos recogemos, para qué, durante cuánto tiempo y qué puedes hacer con ellos.",
 cuerpo=f"""<h2>1. Responsable del tratamiento</h2>
<ul>
 <li><strong>Responsable:</strong> {EMPRESA} (marca Europiscina)</li>
 <li><strong>NIF:</strong> {CIF}</li>
 <li><strong>Domicilio:</strong> {DIR}</li>
 <li><strong>Contacto en materia de protección de datos:</strong> <a href="mailto:{MAIL}">{MAIL}</a></li>
</ul>
<p>No se ha designado delegado de protección de datos, por no concurrir ninguno de los supuestos
del artículo 37 del RGPD. [[Confirmar con asesoría]]</p>

<h2>2. Qué datos recogemos y de dónde</h2>
<p>Solo tratamos los datos que nos facilitas voluntariamente a través de dos vías:</p>
<ul>
 <li><strong>Formulario de presupuesto:</strong> nombre, teléfono, correo electrónico, población y
     la descripción que escribas en el campo libre.</li>
 <li><strong>Configurador de piscinas:</strong> nombre, correo electrónico y teléfono, junto con la
     configuración que hayas elegido (medida, acabado, elementos de obra y equipamiento, e importe
     orientativo resultante).</li>
</ul>
<p>No recogemos datos de navegación con fines analíticos ni de publicidad. No elaboramos perfiles
ni tomamos decisiones automatizadas con efectos jurídicos sobre las personas.</p>

<h2>3. Para qué los usamos y con qué base jurídica</h2>
<table class="legal-tabla">
 <tr><th>Finalidad</th><th>Base jurídica</th></tr>
 <tr><td>Responder a tu solicitud y preparar el presupuesto</td>
     <td>Aplicación de medidas precontractuales a petición del interesado (art. 6.1.b RGPD)</td></tr>
 <tr><td>Contactarte por teléfono, WhatsApp o correo sobre esa solicitud</td>
     <td>Consentimiento prestado al enviar el formulario (art. 6.1.a RGPD)</td></tr>
 <tr><td>Conservar la documentación de las operaciones realizadas</td>
     <td>Cumplimiento de obligaciones legales, mercantiles y fiscales (art. 6.1.c RGPD)</td></tr>
</table>
<p>No enviamos comunicaciones comerciales sobre productos distintos de los solicitados salvo que nos
autorices expresamente por separado.</p>

<h2>4. Cuánto tiempo los conservamos</h2>
<p>Las solicitudes que no dan lugar a contrato se conservan durante un año desde el último contacto,
y después se suprimen. Si la solicitud se convierte en un encargo, los datos se conservan durante la
relación contractual y, posteriormente, durante los plazos de prescripción legal que resulten
aplicables en materia mercantil, fiscal y de responsabilidad por la obra ejecutada.</p>

<h2>5. Quién más accede a tus datos</h2>
<p>No vendemos ni cedemos datos personales a terceros con fines comerciales. Acceden únicamente los
proveedores necesarios para prestar el servicio, en condición de encargados del tratamiento y con el
contrato exigido por el artículo 28 del RGPD:</p>
<ul>
 <li><strong>Netlify, Inc.</strong> (Estados Unidos), alojamiento del sitio web y recepción de los
     formularios. Las transferencias internacionales se amparan en las Cláusulas Contractuales Tipo
     de la Comisión Europea y en el marco de adecuación aplicable. [[Verificar y adjuntar el DPA]]</li>
 <li>Proveedores de correo electrónico y de gestión administrativa de la empresa.</li>
</ul>
<p>También pueden comunicarse datos a las administraciones públicas cuando exista obligación legal.</p>

<h2>6. Tus derechos</h2>
<p>Puedes ejercer los derechos de acceso, rectificación, supresión, oposición, limitación del
tratamiento y portabilidad, así como retirar el consentimiento en cualquier momento, escribiendo a
<a href="mailto:{MAIL}">{MAIL}</a> o a la dirección postal indicada arriba, con indicación del
derecho que ejercitas. La retirada del consentimiento no afecta a la licitud del tratamiento previo.</p>
<p>Si consideras que no hemos atendido correctamente tu solicitud, puedes presentar una reclamación
ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">www.aepd.es</a>),
C/ Jorge Juan 6, 28001 Madrid.</p>

<h2>7. Seguridad y veracidad</h2>
<p>Aplicamos medidas técnicas y organizativas razonables para proteger los datos. Te pedimos que los
datos que nos facilites sean veraces y que nos comuniques cualquier modificación.</p>

<h2>8. Menores</h2>
<p>Este sitio no está dirigido a menores de 14 años y no recogemos conscientemente sus datos.</p>""")

COOK_ES = dict(
 title="Política de cookies | Europiscina",
 desc="Este sitio no utiliza cookies de analítica ni publicitarias. Información sobre el almacenamiento técnico empleado.",
 miga="Cookies", h1="Política de cookies",
 sub="La versión corta: este sitio no te rastrea y no usa cookies publicitarias ni de analítica.",
 cuerpo=f"""<h2>1. Qué es una cookie</h2>
<p>Una cookie es un pequeño fichero que un sitio web guarda en tu dispositivo para recordar
información sobre tu visita. También existen otras tecnologías de almacenamiento local con efectos
equivalentes, como el almacenamiento de sesión del navegador.</p>

<h2>2. Este sitio no utiliza cookies</h2>
<p>No empleamos cookies propias ni de terceros con finalidad analítica, publicitaria o de
elaboración de perfiles. En concreto:</p>
<ul>
 <li>No utilizamos Google Analytics ni ninguna otra herramienta de medición de audiencia.</li>
 <li>No utilizamos píxeles de seguimiento de Meta, Google Ads ni de ninguna red publicitaria.</li>
 <li>Las tipografías están alojadas en nuestro propio servidor, de modo que tu navegador no realiza
     peticiones a servidores de terceros al cargar la página.</li>
</ul>
<p>Por este motivo no se muestra ningún aviso de cookies: no hay nada que consentir.</p>

<h2>3. Almacenamiento técnico en el configurador</h2>
<p>El configurador de piscinas utiliza el <em>almacenamiento de sesión</em> del navegador para recordar,
durante esa misma visita, que ya has introducido tus datos y que no hace falta volver a pedírtelos.
Es información estrictamente necesaria para el funcionamiento que has solicitado, no permite
identificarte y <strong>se borra al cerrar la pestaña</strong>. Está amparada por la excepción del
artículo 22.2 de la LSSI y no requiere consentimiento previo.</p>

<h2>4. Servicios de terceros al pulsar un enlace</h2>
<p>Si pulsas el botón de WhatsApp, tu navegador abrirá un servicio de Meta Platforms, sujeto a sus
propias políticas. Esa conexión solo se produce si tú decides pulsar.</p>

<h2>5. Registros del servidor</h2>
<p>Nuestro proveedor de alojamiento registra de forma automática datos técnicos de las conexiones
(dirección IP, fecha, hora y recurso solicitado) con la finalidad de garantizar la seguridad y el
funcionamiento del servicio. Este tratamiento se basa en el interés legítimo en mantener la
seguridad de los sistemas.</p>

<h2>6. Cómo controlar el almacenamiento</h2>
<p>Puedes borrar el almacenamiento local desde la configuración de tu navegador. Hacerlo no afecta al
funcionamiento del sitio, más allá de que el configurador vuelva a solicitarte los datos.</p>

<h2>7. Actualización</h2>
<p>Si en el futuro incorporamos herramientas de medición o de publicidad, actualizaremos esta página
e implantaremos el sistema de consentimiento previo que exija la normativa.</p>
<p>Para cualquier duda: <a href="mailto:{MAIL}">{MAIL}</a>.</p>""")

# =================================================================== CATALÀ
IDENT_CA = f"""<h2>1. Titular del lloc web</h2>
<p>En compliment de l'article 10 de la Llei 34/2002, de serveis de la societat de la informació i de
comerç electrònic, s'informa de les dades del titular d'aquest lloc web:</p>
<ul>
 <li><strong>Denominació social:</strong> {EMPRESA}, que opera sota la marca comercial Europiscina</li>
 <li><strong>NIF:</strong> {CIF}</li>
 <li><strong>Domicili:</strong> {DIR}</li>
 <li><strong>Correu electrònic:</strong> <a href="mailto:{MAIL}">{MAIL}</a></li>
 <li><strong>Telèfon:</strong> {TEL_TXT}</li>
 <li><strong>Dades registrals:</strong> {REGISTRO}</li>
</ul>"""

LEGAL_CA = dict(
 title="Avís legal | Europiscina",
 desc="Avís legal i condicions d'ús del lloc web d'Europiscina, marca de GARCAM Industries SLU.",
 miga="Avís legal", h1="Avís legal",
 sub="Condicions d'ús d'aquest lloc web i dades identificatives del seu titular.",
 cuerpo=IDENT_CA + """
<h2>2. Objecte i condicions d'ús</h2>
<p>Aquest lloc web té per objecte donar a conèixer els serveis de construcció, reforma i manteniment
de piscines que presta l'empresa, i facilitar el contacte amb clients potencials.</p>
<p>L'accés és gratuït i no requereix registre. Qui hi accedeix es compromet a fer-ne un ús conforme a
la llei i a no emprar el lloc ni els formularis per a finalitats il·lícites, per introduir codi
maliciós o per enviar comunicacions no sol·licitades.</p>

<h2>3. Caràcter orientatiu dels preus</h2>
<p>El configurador de piscines i qualsevol altre import publicat en aquest lloc tenen caràcter
<strong>merament informatiu i no vinculant</strong>. Els preus es calculen sobre la tarifa vigent i
sobre supòsits d'instal·lació estàndard, i no inclouen llicències municipals, connexió elèctrica,
paviment perimetral, tanca ni jardineria.</p>
<p>Circumstàncies com la presència de roca, un nivell freàtic alt, l'accés de maquinària o l'estat del
terreny modifiquen l'import. El pressupost en ferm s'emet únicament per escrit i després de visita
tècnica. Cap xifra mostrada al lloc constitueix una oferta contractual.</p>

<h2>4. Propietat intel·lectual i industrial</h2>
<p>Els textos, fotografies, disseny i codi d'aquest lloc són titularitat de l'empresa o s'utilitzen amb
autorització. Les fotografies corresponen a obres executades per l'empresa. Les marques de tercers
que s'hi citen (Astralpool, Fluidra, Renolit Alkorplan, Rosa Gres, entre d'altres) pertanyen als seus
titulars respectius i s'esmenten únicament a títol informatiu.</p>
<p>Queda prohibida la reproducció o distribució dels continguts sense autorització prèvia i per escrit.</p>

<h2>5. Responsabilitat</h2>
<p>L'empresa procura que la informació publicada sigui exacta i actualitzada, però no pot garantir
l'absència d'errors tipogràfics o de dades desactualitzades. Tampoc no respon de les interrupcions
del servei derivades de causes alienes al seu control.</p>
<p>El lloc pot contenir enllaços a webs de tercers. L'empresa no en controla ni en respon els continguts.</p>

<h2>6. Legislació aplicable i jurisdicció</h2>
<p>Aquestes condicions es regeixen per la legislació espanyola. Per a qualsevol controvèrsia, i llevat
que la normativa de consum estableixi un altre fur imperatiu, les parts se sotmeten als jutjats i
tribunals de Lleida.</p>

<h2>7. Actualització</h2>
<p>Aquest avís legal es pot modificar. La versió aplicable és la publicada en cada moment
en aquesta pàgina.</p>""")

PRIV_CA = dict(
 title="Política de privacitat | Europiscina",
 desc="Com tracta Europiscina les dades personals recollides a través del web: finalitat, base jurídica, conservació i drets.",
 miga="Privacitat", h1="Política de privacitat",
 sub="Quines dades recollim, per a què, durant quant temps i què hi pots fer.",
 cuerpo=f"""<h2>1. Responsable del tractament</h2>
<ul>
 <li><strong>Responsable:</strong> {EMPRESA} (marca Europiscina)</li>
 <li><strong>NIF:</strong> {CIF}</li>
 <li><strong>Domicili:</strong> {DIR}</li>
 <li><strong>Contacte en matèria de protecció de dades:</strong> <a href="mailto:{MAIL}">{MAIL}</a></li>
</ul>
<p>No s'ha designat delegat de protecció de dades, perquè no concorre cap dels supòsits de l'article
37 del RGPD. [[Confirmar amb l'assessoria]]</p>

<h2>2. Quines dades recollim i d'on</h2>
<p>Només tractem les dades que ens facilites voluntàriament per dues vies:</p>
<ul>
 <li><strong>Formulari de pressupost:</strong> nom, telèfon, correu electrònic, població i la
     descripció que escriguis al camp lliure.</li>
 <li><strong>Configurador de piscines:</strong> nom, correu electrònic i telèfon, juntament amb la
     configuració triada (mida, acabat, elements d'obra i equipament, i import orientatiu resultant).</li>
</ul>
<p>No recollim dades de navegació amb finalitats analítiques ni publicitàries. No elaborem perfils ni
prenem decisions automatitzades amb efectes jurídics sobre les persones.</p>

<h2>3. Per a què les fem servir i amb quina base jurídica</h2>
<table class="legal-tabla">
 <tr><th>Finalitat</th><th>Base jurídica</th></tr>
 <tr><td>Respondre la teva sol·licitud i preparar el pressupost</td>
     <td>Aplicació de mesures precontractuals a petició de l'interessat (art. 6.1.b RGPD)</td></tr>
 <tr><td>Contactar-te per telèfon, WhatsApp o correu sobre aquesta sol·licitud</td>
     <td>Consentiment prestat en enviar el formulari (art. 6.1.a RGPD)</td></tr>
 <tr><td>Conservar la documentació de les operacions realitzades</td>
     <td>Compliment d'obligacions legals, mercantils i fiscals (art. 6.1.c RGPD)</td></tr>
</table>
<p>No enviem comunicacions comercials sobre productes diferents dels sol·licitats llevat que ens ho
autoritzis expressament i per separat.</p>

<h2>4. Quant de temps les conservem</h2>
<p>Les sol·licituds que no donen lloc a contracte es conserven durant un any des de l'últim contacte,
i després se suprimeixen. Si la sol·licitud es converteix en un encàrrec, les dades es conserven
durant la relació contractual i, després, durant els terminis de prescripció legal aplicables en
matèria mercantil, fiscal i de responsabilitat per l'obra executada.</p>

<h2>5. Qui més accedeix a les teves dades</h2>
<p>No venem ni cedim dades personals a tercers amb finalitats comercials. Hi accedeixen únicament els
proveïdors necessaris per prestar el servei, en condició d'encarregats del tractament i amb el
contracte que exigeix l'article 28 del RGPD:</p>
<ul>
 <li><strong>Netlify, Inc.</strong> (Estats Units), allotjament del lloc web i recepció dels
     formularis. Les transferències internacionals s'emparen en les Clàusules Contractuals Tipus de
     la Comissió Europea i en el marc d'adequació aplicable. [[Verificar i adjuntar el DPA]]</li>
 <li>Proveïdors de correu electrònic i de gestió administrativa de l'empresa.</li>
</ul>
<p>També es poden comunicar dades a les administracions públiques quan hi hagi obligació legal.</p>

<h2>6. Els teus drets</h2>
<p>Pots exercir els drets d'accés, rectificació, supressió, oposició, limitació del tractament i
portabilitat, i retirar el consentiment en qualsevol moment, escrivint a
<a href="mailto:{MAIL}">{MAIL}</a> o a l'adreça postal indicada més amunt, tot indicant quin dret
exerceixes. La retirada del consentiment no afecta la licitud del tractament previ.</p>
<p>Si consideres que no hem atès correctament la teva sol·licitud, pots presentar una reclamació
davant l'Agència Espanyola de Protecció de Dades (<a href="https://www.aepd.es" rel="noopener">www.aepd.es</a>)
o davant l'Autoritat Catalana de Protecció de Dades (<a href="https://apdcat.gencat.cat" rel="noopener">apdcat.gencat.cat</a>).</p>

<h2>7. Seguretat i veracitat</h2>
<p>Apliquem mesures tècniques i organitzatives raonables per protegir les dades. Et demanem que les
dades que ens facilitis siguin veraces i que ens comuniquis qualsevol modificació.</p>

<h2>8. Menors</h2>
<p>Aquest lloc no s'adreça a menors de 14 anys i no en recollim conscientment les dades.</p>""")

COOK_CA = dict(
 title="Política de galetes | Europiscina",
 desc="Aquest lloc no utilitza galetes d'analítica ni publicitàries. Informació sobre l'emmagatzematge tècnic emprat.",
 miga="Galetes", h1="Política de galetes",
 sub="La versió curta: aquest lloc no et rastreja i no fa servir galetes publicitàries ni d'analítica.",
 cuerpo=f"""<h2>1. Què és una galeta</h2>
<p>Una galeta és un fitxer petit que un lloc web desa al teu dispositiu per recordar informació sobre
la visita. També hi ha altres tecnologies d'emmagatzematge local amb efectes equivalents, com
l'emmagatzematge de sessió del navegador.</p>

<h2>2. Aquest lloc no utilitza galetes</h2>
<p>No fem servir galetes pròpies ni de tercers amb finalitat analítica, publicitària o d'elaboració de
perfils. En concret:</p>
<ul>
 <li>No utilitzem Google Analytics ni cap altra eina de mesura d'audiència.</li>
 <li>No utilitzem píxels de seguiment de Meta, Google Ads ni de cap xarxa publicitària.</li>
 <li>Les tipografies estan allotjades al nostre propi servidor, de manera que el teu navegador no fa
     peticions a servidors de tercers en carregar la pàgina.</li>
</ul>
<p>Per aquest motiu no es mostra cap avís de galetes: no hi ha res a consentir.</p>

<h2>3. Emmagatzematge tècnic al configurador</h2>
<p>El configurador de piscines utilitza l'<em>emmagatzematge de sessió</em> del navegador per recordar,
durant aquesta mateixa visita, que ja has introduït les teves dades i que no cal tornar-te-les a
demanar. És informació estrictament necessària per al funcionament que has sol·licitat, no permet
identificar-te i <strong>s'esborra en tancar la pestanya</strong>. Està emparada per l'excepció de
l'article 22.2 de la LSSI i no requereix consentiment previ.</p>

<h2>4. Serveis de tercers en prémer un enllaç</h2>
<p>Si prems el botó de WhatsApp, el navegador obrirà un servei de Meta Platforms, subjecte a les seves
pròpies polítiques. Aquesta connexió només es produeix si tu decideixes prémer-lo.</p>

<h2>5. Registres del servidor</h2>
<p>El nostre proveïdor d'allotjament registra automàticament dades tècniques de les connexions
(adreça IP, data, hora i recurs sol·licitat) amb la finalitat de garantir la seguretat i el
funcionament del servei, sobre la base de l'interès legítim en la seguretat dels sistemes.</p>

<h2>6. Com controlar l'emmagatzematge</h2>
<p>Pots esborrar l'emmagatzematge local des de la configuració del navegador. Fer-ho no afecta el
funcionament del lloc, més enllà que el configurador et tornarà a demanar les dades.</p>

<h2>7. Actualització</h2>
<p>Si en el futur incorporem eines de mesura o de publicitat, actualitzarem aquesta pàgina i
implantarem el sistema de consentiment previ que exigeixi la normativa.</p>
<p>Per a qualsevol dubte: <a href="mailto:{MAIL}">{MAIL}</a>.</p>""")

# ================================================================== ENGLISH
LEGAL_EN = dict(
 title="Legal notice | Europiscina",
 desc="Legal notice and terms of use for the Europiscina website, a trading name of GARCAM Industries SLU.",
 miga="Legal notice", h1="Legal notice",
 sub="Terms of use of this website and identification details of its owner.",
 cuerpo=f"""<h2>1. Website owner</h2>
<p>In accordance with article 10 of Spanish Law 34/2002 on information society services and electronic
commerce, the details of the owner of this website are:</p>
<ul>
 <li><strong>Company name:</strong> {EMPRESA}, trading as Europiscina</li>
 <li><strong>Tax ID (NIF):</strong> {CIF}</li>
 <li><strong>Registered address:</strong> {DIR}, Spain</li>
 <li><strong>Email:</strong> <a href="mailto:{MAIL}">{MAIL}</a></li>
 <li><strong>Telephone:</strong> +34 {TEL_TXT}</li>
 <li><strong>Company register:</strong> {REGISTRO}</li>
</ul>

<h2>2. Purpose and terms of use</h2>
<p>This website presents the pool construction, refurbishment and maintenance services provided by the
company, and allows prospective clients to get in touch. Access is free and requires no registration.
Users undertake to use the site lawfully and not to use it or its forms for unlawful purposes, to
introduce malicious code or to send unsolicited communications.</p>

<h2>3. Prices are indicative</h2>
<p>The pool calculator and any other figure published on this site are <strong>for information only and
are not binding</strong>. Prices are calculated from our current price list and assume standard
installation conditions. They do not include municipal licences, electrical connection, surrounding
paving, fencing or landscaping.</p>
<p>Rock, a high water table, machinery access or ground conditions all change the final figure. A firm
quotation is issued only in writing and after a site visit. No figure shown on this site constitutes
a contractual offer.</p>

<h2>4. Intellectual property</h2>
<p>The texts, photographs, design and code of this site are owned by the company or used with
permission. The photographs show projects built by the company. Third-party trade marks mentioned
(Astralpool, Fluidra, Renolit Alkorplan, Rosa Gres, among others) belong to their respective owners
and are cited for information purposes only. Reproduction or distribution without prior written
authorisation is prohibited.</p>

<h2>5. Liability</h2>
<p>The company aims to keep published information accurate and up to date but cannot guarantee the
absence of typographical errors or outdated data, nor is it liable for service interruptions caused
by circumstances beyond its control. The site may link to third-party websites, whose content the
company neither controls nor is responsible for.</p>

<h2>6. Governing law and jurisdiction</h2>
<p>These terms are governed by Spanish law. Save where consumer legislation provides otherwise, the
parties submit to the courts of Lleida, Spain.</p>""")

PRIV_EN = dict(
 title="Privacy policy | Europiscina",
 desc="How Europiscina processes personal data collected through its website: purpose, legal basis, retention and your rights.",
 miga="Privacy", h1="Privacy policy",
 sub="What we collect, what for, how long we keep it and what you can do about it.",
 cuerpo=f"""<h2>1. Data controller</h2>
<ul>
 <li><strong>Controller:</strong> {EMPRESA} (trading as Europiscina)</li>
 <li><strong>Tax ID (NIF):</strong> {CIF}</li>
 <li><strong>Address:</strong> {DIR}, Spain</li>
 <li><strong>Data protection contact:</strong> <a href="mailto:{MAIL}">{MAIL}</a></li>
</ul>

<h2>2. What we collect</h2>
<p>We only process data you provide voluntarily, through two channels:</p>
<ul>
 <li><strong>Quote form:</strong> name, telephone, email, town and whatever you write in the free text field.</li>
 <li><strong>Pool calculator:</strong> name, email and telephone, together with the configuration you
     selected (size, finish, groundwork and equipment, and the resulting indicative price).</li>
</ul>
<p>We do not collect browsing data for analytics or advertising, we do not build profiles and we do not
carry out automated decision-making producing legal effects.</p>

<h2>3. Purposes and legal basis</h2>
<table class="legal-tabla">
 <tr><th>Purpose</th><th>Legal basis</th></tr>
 <tr><td>Answering your enquiry and preparing a quotation</td>
     <td>Pre-contractual measures at your request (Art. 6(1)(b) GDPR)</td></tr>
 <tr><td>Contacting you by phone, WhatsApp or email about that enquiry</td>
     <td>Consent given when submitting the form (Art. 6(1)(a) GDPR)</td></tr>
 <tr><td>Keeping records of completed transactions</td>
     <td>Compliance with legal, commercial and tax obligations (Art. 6(1)(c) GDPR)</td></tr>
</table>

<h2>4. Retention</h2>
<p>Enquiries that do not lead to a contract are kept for one year from the last contact and then
deleted. If the enquiry becomes an order, data is kept for the duration of the contract and
thereafter for the applicable statutory limitation periods.</p>

<h2>5. Recipients</h2>
<p>We do not sell or transfer personal data to third parties for commercial purposes. Access is limited
to processors necessary to provide the service, bound by an Art. 28 GDPR agreement:</p>
<ul>
 <li><strong>Netlify, Inc.</strong> (United States), website hosting and form handling. International
     transfers rely on the European Commission's Standard Contractual Clauses and the applicable
     adequacy framework. [[Verify and attach the DPA]]</li>
 <li>Email and administrative service providers.</li>
</ul>

<h2>6. Your rights</h2>
<p>You may exercise your rights of access, rectification, erasure, objection, restriction and
portability, and withdraw consent at any time, by writing to <a href="mailto:{MAIL}">{MAIL}</a> or to
the postal address above. Withdrawing consent does not affect the lawfulness of prior processing.</p>
<p>You may also lodge a complaint with the Spanish Data Protection Agency
(<a href="https://www.aepd.es" rel="noopener">www.aepd.es</a>).</p>

<h2>7. Minors</h2>
<p>This site is not aimed at children under 14 and we do not knowingly collect their data.</p>""")

COOK_EN = dict(
 title="Cookie policy | Europiscina",
 desc="This website uses no analytics or advertising cookies. Information about the technical storage used.",
 miga="Cookies", h1="Cookie policy",
 sub="The short version: this site does not track you and uses no advertising or analytics cookies.",
 cuerpo=f"""<h2>1. This site uses no cookies</h2>
<p>We use no first-party or third-party cookies for analytics, advertising or profiling. Specifically:</p>
<ul>
 <li>No Google Analytics or any other audience measurement tool.</li>
 <li>No Meta, Google Ads or other advertising network tracking pixels.</li>
 <li>Fonts are hosted on our own server, so your browser makes no requests to third-party servers
     when loading the page.</li>
</ul>
<p>That is why no cookie banner is shown: there is nothing to consent to.</p>

<h2>2. Technical storage in the pool calculator</h2>
<p>The calculator uses the browser's <em>session storage</em> to remember, within that same visit, that
you have already entered your details. This is strictly necessary for the functionality you
requested, does not identify you and <strong>is deleted when you close the tab</strong>.</p>

<h2>3. Third-party services when you click a link</h2>
<p>If you tap the WhatsApp button, your browser will open a Meta Platforms service subject to its own
policies. That connection only happens if you choose to tap it.</p>

<h2>4. Server logs</h2>
<p>Our hosting provider automatically records technical connection data (IP address, date, time and
requested resource) to ensure the security and operation of the service, on the basis of legitimate
interest.</p>

<h2>5. Updates</h2>
<p>If we add measurement or advertising tools in future, we will update this page and implement the
prior consent mechanism required by law.</p>
<p>Any questions: <a href="mailto:{MAIL}">{MAIL}</a>.</p>""")

CONTENIDO = {
 "legal":   {"es": LEGAL_ES, "ca": LEGAL_CA, "en": LEGAL_EN},
 "priv":    {"es": PRIV_ES,  "ca": PRIV_CA,  "en": PRIV_EN},
 "cookies": {"es": COOK_ES,  "ca": COOK_CA,  "en": COOK_EN},
}

if __name__ == "__main__":
    for clave, porlang in CONTENIDO.items():
        for lang, d in porlang.items():
            print(" ", escribir(clave, lang, d))
    print(f"\n{sum(len(v) for v in CONTENIDO.values())} páginas legales")
