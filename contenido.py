#!/usr/bin/env python3
"""Contenido editorial del sitio. Un diccionario por página y por idioma."""
from motor import IMG, cuerpo, ficha, faq, cinta

C = {}

# ============================================================ PISCINAS DE OBRA
C["obra"] = {
"es": dict(
 title="Piscinas de obra en Lleida | Hormigón armado a medida | Europiscina",
 desc="Construcción de piscinas de obra en hormigón armado en Lleida, Huesca y Andorra. Desbordantes, skimmer y carriles de natación. Proyecto y ejecución con equipo propio.",
 miga="Piscinas de obra", h1="Piscinas de obra: cuando el catálogo no llega.",
 entradilla="Hormigón armado proyectado o encofrado, sin límite de forma ni de medida. Es la opción cuando el terreno, el desnivel o la casa piden algo que no existe prefabricado.",
 foto=f"{IMG}/piscina-piedra-natural.jpg",
 foto_alt="Piscina de obra con coronación de piedra natural construida por Europiscina",
 cuerpo=cuerpo("Se construye una vez. Se vive treinta años.",
  """<p>Una piscina de obra no se compra, se proyecta. Estudiamos el terreno, el acceso de maquinaria, el nivel freático y el desagüe antes de dibujar nada. Ese trabajo previo evita las dos averías caras que vemos cada temporada en piscinas de otros: fisuras por asiento diferencial del terreno y vasos que flotan cuando se vacían.</p>
     <p>Después hormigonamos, impermeabilizamos y rematamos con el acabado que elijas: gres porcelánico, lámina armada o revestimiento Touch. Todo con nuestra plantilla y nuestra maquinaria.</p>""",
  """<h3>Sistemas que construimos</h3>
     <p>Skimmer, el clásico pero con el diseño SLIM, con el nivel del agua unos centímetros por debajo de la coronación. Desbordante, con el agua a ras y rebosadero perimetral hacia vaso de compensación. Y desbordante tipo infinity, con lámina cayendo hacia el paisaje.</p>
     <h3>Antes de firmar nada</h3>
     <p>Hacemos visita técnica al terreno. Miramos si entra la máquina, dónde va la depuradora, por dónde sale el desagüe y qué distancia hay al cuadro eléctrico. La mitad de los sobrecostes de una piscina salen de esas cuatro cosas, y se resuelven antes de excavar, no después.</p>""")
  + ficha("Datos de proyecto", [
     ("Estructura", "Hormigón armado o encofrado"),
     ("Acabados", "Gres porcelánico Rosa Gres, lámina armada Renolit Alkorplan"),
     ("Sistemas", "Skimmer, desbordante, infinity, carril de natación"),
     ("Depuración", "Astralpool, con opción de electrólisis salina"),
     ("Plazo orientativo", "De 8 a 14 semanas según acabado y climatología"),
     ("Zona", "Lleida, Huesca, Tarragona, Andorra y Mallorca")]),
 extra=faq("es", [
  ("¿Cuánto cuesta una piscina de obra?", "Depende de medidas, acabado, sistema y estado del terreno. El rango habitual de nuestros proyectos particulares va de los 25.000 a más de 100.000 euros. Damos precio cerrado tras la visita técnica, no antes."),
  ("¿Cuánto se tarda?", "Entre 8 y 14 semanas de obra. La climatología en invierno y los plazos de licencia municipal son las dos variables que más lo mueven."),
  ("¿Hace falta licencia?", "Sí. La mayoría de ayuntamientos de la comarca exigen licencia de obra menor o mayor según el volumen y si es piscina de hormigón. Te decimos qué necesita tu municipio y preparamos la documentación técnica."),
  ("¿Y si el terreno tiene nivel freático alto?", "Se resuelve con drenaje perimetral y válvula de fondo siempre que sea necesario.")])
  + cinta("¿Tienes el terreno y no sabes si cabe?",
          "Nos acercamos, lo miramos y te decimos qué es posible. La visita es sin compromiso.", "es")),

"ca": dict(
 title="Piscines d'obra a Lleida | Formigó armat a mida | Europiscina",
 desc="Construcció de piscines d'obra en formigó armat a Lleida, Osca i Andorra. Desbordants, skimmer i carrils de natació. Projecte i execució amb equip propi.",
 miga="Piscines d'obra", h1="Piscines d'obra: quan el catàleg no hi arriba.",
 entradilla="Formigó armat projectat o encofrat, sense límit de forma ni de mida. És l'opció quan el terreny, el desnivell o la casa demanen alguna cosa que no existeix prefabricada.",
 foto=f"{IMG}/piscina-piedra-natural.jpg",
 foto_alt="Piscina d'obra amb coronació de pedra natural construïda per Europiscina",
 cuerpo=cuerpo("Es construeix un cop. S'hi viu trenta anys.",
  """<p>Una piscina d'obra no es compra, es projecta. Estudiem el terreny, l'accés de maquinària, el nivell freàtic i el desguàs abans de dibuixar res. Aquesta feina prèvia evita les dues avaries cares que veiem cada temporada en piscines d'altres: fissures per assentament diferencial del terreny i vasos que suren quan es buiden.</p>
     <p>Després formigonem, impermeabilitzem i rematem amb l'acabat que triïs: gres porcellànic, làmina armada o revestiment Touch. Tot amb la nostra plantilla i la nostra maquinària.</p>""",
  """<h3>Sistemes que construïm</h3>
     <p>Skimmer, el clàssic però amb el disseny SLIM, amb el nivell de l'aigua uns centímetres per sota de la coronació. Desbordant, amb l'aigua arran i sobreeixidor perimetral cap a vas de compensació. I desbordant tipus infinity, amb làmina caient cap al paisatge.</p>
     <h3>Abans de signar res</h3>
     <p>Fem visita tècnica al terreny. Mirem si hi entra la màquina, on va la depuradora, per on surt el desguàs i quina distància hi ha al quadre elèctric. La meitat dels sobrecostos d'una piscina surten d'aquestes quatre coses, i es resolen abans d'excavar, no després.</p>""")
  + ficha("Dades de projecte", [
     ("Estructura", "Formigó armat o encofrat"),
     ("Acabats", "Gres porcellànic Rosa Gres, làmina armada Renolit Alkorplan"),
     ("Sistemes", "Skimmer, desbordant, infinity, carril de natació"),
     ("Depuració", "Astralpool, amb opció d'electròlisi salina"),
     ("Termini orientatiu", "De 8 a 14 setmanes segons acabat i climatologia"),
     ("Zona", "Lleida, Osca, Tarragona, Andorra i Mallorca")]),
 extra=faq("ca", [
  ("Quant costa una piscina d'obra?", "Depèn de mides, acabat, sistema i estat del terreny. El rang habitual dels nostres projectes particulars va dels 25.000 a més de 100.000 euros. Donem preu tancat després de la visita tècnica, no abans."),
  ("Quant s'hi triga?", "Entre 8 i 14 setmanes d'obra. La climatologia a l'hivern i els terminis de llicència municipal són les dues variables que més ho mouen."),
  ("Cal llicència?", "Sí. La majoria d'ajuntaments de la comarca exigeixen llicència d'obra menor o major segons el volum i si és piscina de formigó. Et diem què necessita el teu municipi i preparem la documentació tècnica."),
  ("I si el terreny té nivell freàtic alt?", "Es resol amb drenatge perimetral i vàlvula de fons sempre que sigui necessari.")])
  + cinta("Tens el terreny i no saps si hi cap?",
          "Ens hi acostem, ho mirem i et diem què és possible. La visita és sense compromís.", "ca")),
}

# ============================================================ LÁMINA ARMADA
C["lamina"] = {
"es": dict(
 title="Piscinas de lámina armada en Lleida | Renolit Alkorplan | Europiscina",
 desc="Impermeabilización de piscinas con lámina armada Renolit Alkorplan soldada in situ, somos instaladores oficiales. Obra nueva y reforma de piscinas que pierden agua. Lleida, Huesca y Andorra.",
 miga="Lámina armada", h1="Lámina armada: la piscina deja de perder agua.",
 entradilla="PVC reforzado Renolit Alkorplan, soldado in situ punto por punto. Es la solución más rápida para recuperar una piscina vieja y la más versátil en color y textura para obra nueva.",
 foto=f"{IMG}/piscina-lamina-madera.jpg",
 foto_alt="Piscina de lámina armada con tarima de madera construida por Europiscina",
 cuerpo=cuerpo("Una membrana continua, sin juntas por donde perder.",
  """<p>La lámina armada es una membrana de PVC de 1,5 mm con malla de poliéster en el interior. Se extiende sobre el vaso, se termosuelda en obra y queda una piel continua: no hay juntas de mortero, que es por donde se escapa el agua en las piscinas de gresite y baldosa cuando pasan los años.</p>
     <p>Se instala sobre vaso de hormigón nuevo o sobre uno existente, sin picar el revestimiento viejo en la mayoría de casos. Por eso es la reforma más habitual que hacemos: se entra con la piscina vacía y en dos o tres semanas está llena otra vez.</p>""",
  """<h3>Acabados</h3>
     <p>Trabajamos la gama Renolit Alkorplan completa: los lisos clásicos, los Touch con textura en relieve y los efectos piedra y arena. El color de la lámina cambia por completo el color aparente del agua, así que lo elegimos contigo con muestra física en mano, no en pantalla.</p>
     <h3>Cuidado con el mantenimiento</h3>
     <p>Un aviso que damos a todos nuestros clientes de lámina: nunca uses dosificadores flotantes de cloro. Renolit lo prohíbe expresamente porque la pastilla se apoya sobre la lámina y decolora el punto de contacto de forma irreversible. La dosificación va en el skimmer o por bomba dosificadora.</p>""")
  + ficha("Datos técnicos", [
     ("Material", "PVC armado de 1,5 a 2,0 mm con malla de poliéster"),
     ("Marca", "Renolit Alkorplan: gama lisa, Touch, Evolve y Relief"),
     ("Unión", "Termosoldadura en obra, sin juntas"),
     ("Aplicación", "Obra nueva y rehabilitación sobre vaso existente"),
     ("Plazo orientativo", "De 1 a 3 semanas en reforma"),
     ("Garantía", "Según condiciones de fabricante sobre lámina instalada")]),
 extra=faq("es", [
  ("¿Se puede poner sobre una piscina de gresite vieja?", "En la mayoría de casos sí, siempre que el vaso esté estructuralmente sano. Si hay movimiento estructural, la lámina lo tapa pero no lo arregla, y hay que resolver la estructura primero."),
  ("¿Cuánto dura?", "Con mantenimiento correcto del agua, más de 20 años. El enemigo real no es el tiempo, es el pH descontrolado y el cloro mal dosificado."),
  ("¿Se nota la soldadura?", "Se ven las líneas de solape si te fijas. En los acabados Touch con textura prácticamente desaparecen."),
  ("¿Qué pasa si se pincha?", "Se repara con un parche soldado del mismo material. Es una intervención de horas, no de días.")])
  + cinta("¿Tu piscina pierde agua?",
          "Localizamos la fuga y te decimos si compensa reparar o revestir con lámina. Sin rodeos.", "es")),

"ca": dict(
 title="Piscines de làmina armada a Lleida | Renolit Alkorplan | Europiscina",
 desc="Impermeabilització de piscines amb làmina armada Renolit Alkorplan soldada in situ, som instal·ladors oficials. Obra nova i reforma de piscines que perden aigua. Lleida, Osca i Andorra.",
 miga="Làmina armada", h1="Làmina armada: la piscina deixa de perdre aigua.",
 entradilla="PVC reforçat Renolit Alkorplan, soldat in situ punt per punt. És la solució més ràpida per recuperar una piscina vella i la més versàtil en color i textura per a obra nova.",
 foto=f"{IMG}/piscina-lamina-madera.jpg",
 foto_alt="Piscina de làmina armada amb tarima de fusta construïda per Europiscina",
 cuerpo=cuerpo("Una membrana contínua, sense juntes per on perdre.",
  """<p>La làmina armada és una membrana de PVC d'1,5 mm amb malla de polièster a l'interior. S'estén sobre el vas, es termosolda en obra i queda una pell contínua: no hi ha juntes de morter, que és per on s'escapa l'aigua a les piscines de gresite i rajola quan passen els anys.</p>
     <p>S'instal·la sobre vas de formigó nou o sobre un d'existent, sense picar el revestiment vell en la majoria de casos. Per això és la reforma més habitual que fem: s'entra amb la piscina buida i en dues o tres setmanes torna a estar plena.</p>""",
  """<h3>Acabats</h3>
     <p>Treballem la gamma Renolit Alkorplan completa: els llisos clàssics, els Touch amb textura en relleu i els efectes pedra i sorra. El color de la làmina canvia del tot el color aparent de l'aigua, així que el triem amb tu amb mostra física a la mà, no a la pantalla.</p>
     <h3>Compte amb el manteniment</h3>
     <p>Un avís que donem a tots els nostres clients de làmina: no facis servir mai dosificadors flotants de clor. Renolit ho prohibeix expressament perquè la pastilla es recolza sobre la làmina i decolora el punt de contacte de manera irreversible. La dosificació va al skimmer o per bomba dosificadora.</p>""")
  + ficha("Dades tècniques", [
     ("Material", "PVC armat d'1,5 a 2,0 mm amb malla de polièster"),
     ("Marca", "Renolit Alkorplan: gamma llisa, Touch, Evolve i Relief"),
     ("Unió", "Termosoldadura en obra, sense juntes"),
     ("Aplicació", "Obra nova i rehabilitació sobre vas existent"),
     ("Termini orientatiu", "D'1 a 3 setmanes en reforma"),
     ("Garantia", "Segons condicions de fabricant sobre làmina instal·lada")]),
 extra=faq("ca", [
  ("Es pot posar sobre una piscina de gresite vella?", "En la majoria de casos sí, sempre que el vas estigui estructuralment sa. Si hi ha moviment estructural, la làmina ho tapa però no ho arregla, i cal resoldre l'estructura primer."),
  ("Quant dura?", "Amb manteniment correcte de l'aigua, més de 20 anys. L'enemic real no és el temps, és el pH descontrolat i el clor mal dosificat."),
  ("Es nota la soldadura?", "Es veuen les línies de solapament si t'hi fixes. Als acabats Touch amb textura pràcticament desapareixen."),
  ("Què passa si es punxa?", "Es repara amb un pedaç soldat del mateix material. És una intervenció d'hores, no de dies.")])
  + cinta("La teva piscina perd aigua?",
          "Localitzem la fuita i et diem si compensa reparar o revestir amb làmina. Sense embuts.", "ca")),
}

# ============================================================ POLIÉSTER
C["polie"] = {
"es": dict(
 title="Piscinas de poliéster en Lleida | Prefabricadas e instaladas | Europiscina",
 desc="Instalación de piscinas prefabricadas de poliéster en Lleida, Huesca, Tarragona y Barcelona. Vaso monobloque colocado con grúa. Calcula tu precio en el configurador.",
 miga="Poliéster", h1="Poliéster: del camión al agua en 3 días.",
 entradilla="Vaso monobloque fabricado en taller y colocado con grúa. Cuando el plazo manda y el terreno acompaña, es la manera más rápida y previsible de tener piscina.",
 foto=f"{IMG}/piscinas-poliester.jpg",
 foto_alt="Vasos de piscina de poliéster en el almacén de Europiscina en Balaguer",
 cuerpo=cuerpo("Menos obra, menos sorpresas, menos plazo.",
  """<p>El vaso llega fabricado, con la escalera, los escalones y los alojamientos de skimmer e impulsores ya integrados. Nosotros excavamos, preparamos la solera, colocamos con grúa, nivelamos, conectamos la hidráulica y rellenamos el trasdós al mismo tiempo que se llena de agua.</p>
     <p>Todo el proceso, desde que entra la máquina hasta que puedes bañarte, se resuelve normalmente en una o dos semanas. En una piscina de obra son meses.</p>""",
  """<h3>Lo que hay que mirar antes</h3>
     <p>El poliéster tiene una condición innegociable: el acceso. El vaso llega entero sobre camión y hay que poder acercar una grúa con suficiente pluma. Si la casa está en un casco antiguo estrecho o hay tendido eléctrico sobre el jardín, hay que estudiarlo antes de vender nada.</p>
     <h3>Calcula tu precio ahora</h3>
     <p>En el configurador eliges la medida, el acabado y qué parte de la obra hacemos nosotros: excavación, gravas, solera, instalación hidráulica y coronación de piedra. El precio se calcula al momento sobre nuestra tarifa vigente.</p>
     <p><a href="/configurador/">Calcular el precio de mi piscina</a></p>""")
  + ficha("Datos de instalación", [
     ("Material", "Poliéster reforzado con fibra de vidrio y gel-coat"),
     ("Colocación", "Grúa, vaso monobloque"),
     ("Requisito clave", "Acceso para camión y grúa"),
     ("Plazo orientativo", "De 1 a 2 semanas"),
     ("Equipación", "Skimmer, impulsores, filtro, bomba y kit de limpieza"),
     ("No incluido de serie", "Excavación, solera, tapado con gravas y tuberías perimetrales")]),
 extra=faq("es", [
  ("¿Es más barata que la de obra?", "Casi siempre sí, y sobre todo es más previsible: el vaso tiene precio cerrado de catálogo y lo que varía es la obra civil de alrededor."),
  ("¿Cuánto dura el poliéster?", "Llevamos más de 25 años instalándolas, somos expertos. Dura décadas. Lo que puede degradarse con el tiempo es el color de la capa superficial, y es reparable y repintable."),
  ("¿Puedo elegir el color?", "Sí. Hay colores estándar y especiales, incluidos los acabados MINERAL. Los no estándar llevan recargo sobre tarifa."),
  ("¿Y si no entra la grúa?", "Entonces no es tu solución y te lo diremos en la visita. En ese caso vamos a lámina armada o a obra.")])
  + cinta("¿Quieres saber si tu jardín admite un vaso de poliéster?",
          "Con una foto del acceso y las medidas del jardín ya te podemos orientar por WhatsApp.", "es")),

"ca": dict(
 title="Piscines de polièster a Lleida | Prefabricades i instal·lades | Europiscina",
 desc="Instal·lació de piscines prefabricades de polièster a Lleida, Osca, Tarragona i Barcelona. Vas monobloc col·locat amb grua. Calcula el teu preu al configurador.",
 miga="Polièster", h1="Polièster: del camió a l'aigua en 3 dies.",
 entradilla="Vas monobloc fabricat al taller i col·locat amb grua. Quan el termini mana i el terreny acompanya, és la manera més ràpida i previsible de tenir piscina.",
 foto=f"{IMG}/piscinas-poliester.jpg",
 foto_alt="Vasos de piscina de polièster al magatzem d'Europiscina a Balaguer",
 cuerpo=cuerpo("Menys obra, menys sorpreses, menys termini.",
  """<p>El vas arriba fabricat, amb l'escala, els graons i els allotjaments de skimmer i impulsors ja integrats. Nosaltres excavem, preparem la solera, col·loquem amb grua, anivellem, connectem la hidràulica i omplim el trasdós al mateix temps que s'omple d'aigua.</p>
     <p>Tot el procés, des que entra la màquina fins que t'hi pots banyar, es resol normalment en una o dues setmanes. En una piscina d'obra són mesos.</p>""",
  """<h3>El que cal mirar abans</h3>
     <p>El polièster té una condició innegociable: l'accés. El vas arriba sencer sobre camió i cal poder acostar-hi una grua amb prou ploma. Si la casa és en un nucli antic estret o hi ha esteses elèctriques sobre el jardí, s'ha d'estudiar abans de vendre res.</p>
     <h3>Calcula el teu preu ara</h3>
     <p>Al configurador tries la mida, l'acabat i quina part de l'obra fem nosaltres: excavació, graves, solera, instal·lació hidràulica i coronació de pedra. El preu es calcula al moment sobre la nostra tarifa vigent.</p>
     <p><a href="/ca/configurador/">Calcular el preu de la meva piscina</a></p>""")
  + ficha("Dades d'instal·lació", [
     ("Material", "Polièster reforçat amb fibra de vidre i gel-coat"),
     ("Col·locació", "Grua, vas monobloc"),
     ("Requisit clau", "Accés per a camió i grua"),
     ("Termini orientatiu", "D'1 a 2 setmanes"),
     ("Equipació", "Skimmer, impulsors, filtre, bomba i kit de neteja"),
     ("No inclòs de sèrie", "Excavació, solera, tapat amb graves i canonades perimetrals")]),
 extra=faq("ca", [
  ("És més barata que la d'obra?", "Gairebé sempre sí, i sobretot és més previsible: el vas té preu tancat de catàleg i el que varia és l'obra civil del voltant."),
  ("Quant dura el polièster?", "Portem més de 25 anys instal·lant-ne, som experts. Dura dècades. El que es pot degradar amb el temps és el color de la capa superficial, i és reparable i repintable."),
  ("Puc triar el color?", "Sí. Hi ha colors estàndard i especials, inclosos els acabats MINERAL. Els no estàndard porten recàrrec sobre tarifa."),
  ("I si no hi entra la grua?", "Aleshores no és la teva solució i t'ho direm a la visita. En aquest cas anem a làmina armada o a obra.")])
  + cinta("Vols saber si el teu jardí admet un vas de polièster?",
          "Amb una foto de l'accés i les mides del jardí ja et podem orientar per WhatsApp.", "ca")),

"en": dict(
 title="Fibreglass pools in Lleida and Catalonia | Europiscina",
 desc="Prefabricated fibreglass pool installation in Lleida, Huesca, Tarragona, Andorra and Mallorca. One-piece shell craned into place. Calculate your price online.",
 miga="Fibreglass pools", h1="Fibreglass: from lorry to water in 3 days.",
 entradilla="A one-piece shell built in the factory and craned into place. When the timeline matters and the site allows it, this is the fastest and most predictable way to get a pool.",
 foto=f"{IMG}/piscinas-poliester.jpg",
 foto_alt="Fibreglass pool shells at the Europiscina yard in Balaguer",
 cuerpo=cuerpo("Less building work, fewer surprises, a shorter timeline.",
  """<p>The shell arrives ready-made, with steps, benches and the skimmer and inlet housings already built in. We excavate, prepare the base, lift it into place with a crane, level it, connect the hydraulics and backfill as the pool is filled with water.</p>
     <p>The whole process, from the digger arriving to your first swim, usually takes one or two weeks. A concrete pool takes months.</p>""",
  """<h3>What has to be checked first</h3>
     <p>Fibreglass has one non-negotiable condition: access. The shell arrives in one piece on a lorry and a crane with enough reach has to get close to the site. Narrow old-town streets or power lines over the garden have to be assessed before anything is sold.</p>
     <h3>Work out your price now</h3>
     <p>In the calculator you choose the size, the finish and which parts of the job we handle: excavation, gravel, base, hydraulics and the stone coping. The price is calculated instantly from our current price list.</p>
     <p><a href="/en/pool-calculator/">Calculate my pool price</a></p>""")
  + ficha("Installation details", [
     ("Material", "Glass-reinforced polyester with gel-coat"),
     ("Installation", "Craned, one-piece shell"),
     ("Key requirement", "Lorry and crane access"),
     ("Typical timeline", "One to two weeks"),
     ("Included", "Skimmer, inlets, filter, pump and cleaning kit"),
     ("Not included as standard", "Excavation, base, gravel backfill and perimeter pipework")]),
 extra=faq("en", [
  ("Is it cheaper than a concrete pool?", "Almost always, and above all it is more predictable: the shell has a fixed catalogue price and only the surrounding groundwork varies."),
  ("How long does fibreglass last?", "We have been installing them for more than 25 years. They last decades; what ages is the colour of the surface layer, and that can be repaired and refinished."),
  ("Can I choose the colour?", "Yes. There are standard and special colours, including the MINERAL finishes. Non-standard colours carry a surcharge."),
  ("What if a crane cannot reach the site?", "Then this is not your solution and we will say so at the site visit. In that case we look at a reinforced membrane or a concrete pool.")])
  + cinta("Not sure your garden can take a fibreglass shell?",
          "Send us a photo of the access and the garden dimensions and we can give you an answer on WhatsApp.", "en")),
}

# ============================================================ GRES PORCELÁNICO
C["gres"] = {
"es": dict(
 title="Piscinas de gres porcelánico Rosa Gres en Lleida | Europiscina",
 desc="Construcción de piscinas con revestimiento de gres porcelánico Rosa Gres. Sistemas skimmer, desbordante y Slim. Acabados antideslizantes en playa y coronación.",
 miga="Gres porcelánico", h1="Gres porcelánico: el acabado que no se cansa.",
 entradilla="Revestimiento cerámico técnico Rosa Gres para vaso, coronación y playa. Antideslizante, estable al color y prácticamente indiferente al paso del tiempo.",
 foto=f"{IMG}/piscina-gresite-azul.jpg", foto_alt="Detalle de piscina revestida con gres porcelánico",
 cuerpo=cuerpo("La opción cuando la piscina también es la terraza.",
  """<p>El gres porcelánico resuelve algo que ningún otro acabado hace igual de bien: continuidad. La misma pieza, con acabado antideslizante, va del vaso a la coronación y de la coronación a la playa y al porche. La piscina deja de ser un objeto en el jardín y pasa a formar parte de la casa.</p>
     <p>Trabajamos los sistemas Rosa Gres skimmer, desbordante y Slim, con rejillas y piezas especiales de la propia marca.</p>""",
  """<h3>Por qué cuesta más</h3>
     <p>Porque es más lento. Cada pieza va colocada y rejuntada a mano con material específico para inmersión permanente. No es un revestimiento que se extienda: se construye. A cambio, no decolora, no se abomba y aguanta el hielo del invierno de la plana sin inmutarse.</p>
     <h3>Combinaciones</h3>
     <p>La combinación de un color cálido en playa con un tono más profundo en el vaso es la que mejor funciona en las casas de aquí, porque el agua se ve azul intensa y el entorno no reverbera con el sol de agosto.</p>""")
  + ficha("Datos técnicos", [
     ("Material", "Gres porcelánico técnico Rosa Gres"),
     ("Sistemas", "Skimmer, desbordante y Slim"),
     ("Aplicación", "Vaso, coronación, playa y entorno"),
     ("Propiedades", "Antideslizante, resistente a heladas, estable al color"),
     ("Plazo orientativo", "Suma de 2 a 4 semanas sobre la obra del vaso")]),
 extra=faq("es", [
  ("¿Se puede poner gres sobre una piscina existente?", "Sí, si el vaso está sano y las medidas permiten el despiece. Hay que valorar caso por caso."),
  ("¿Resbala?", "Las piezas de playa y coronación son antideslizantes de clase específica para exterior mojado. Es más segura que una baldosa convencional."),
  ("¿Y las juntas?", "Se rejuntan con material epoxi o cementoso técnico apto para inmersión. Es la parte que más determina la durabilidad y donde no se ahorra.")])
  + cinta("¿Quieres ver muestras físicas?",
          "Tenemos muestrario en el almacén de Balaguer. Pásate y las ves con luz de día.", "es")),

"ca": dict(
 title="Piscines de gres porcellànic Rosa Gres a Lleida | Europiscina",
 desc="Construcció de piscines amb revestiment de gres porcellànic Rosa Gres. Sistemes skimmer, desbordant i Slim. Acabats antilliscants a platja i coronació.",
 miga="Gres porcellànic", h1="Gres porcellànic: l'acabat que no es cansa.",
 entradilla="Revestiment ceràmic tècnic Rosa Gres per a vas, coronació i platja. Antilliscant, estable al color i pràcticament indiferent al pas del temps.",
 foto=f"{IMG}/piscina-gresite-azul.jpg", foto_alt="Detall de piscina revestida amb gres porcellànic",
 cuerpo=cuerpo("L'opció quan la piscina també és la terrassa.",
  """<p>El gres porcellànic resol una cosa que cap altre acabat fa igual de bé: continuïtat. La mateixa peça, amb acabat antilliscant, va del vas a la coronació i de la coronació a la platja i al porxo. La piscina deixa de ser un objecte al jardí i passa a formar part de la casa.</p>
     <p>Treballem els sistemes Rosa Gres skimmer, desbordant i Slim, amb reixes i peces especials de la mateixa marca.</p>""",
  """<h3>Per què costa més</h3>
     <p>Perquè és més lent. Cada peça va col·locada i rejuntada a mà amb material específic per a immersió permanent. No és un revestiment que s'estengui: es construeix. A canvi, no decolora, no s'abomba i aguanta la gelada de l'hivern de la plana sense immutar-se.</p>
     <h3>Combinacions</h3>
     <p>La combinació d'un color càlid a la platja amb un to més profund al vas és la que millor funciona a les cases d'aquí, perquè l'aigua es veu blava intensa i l'entorn no reverbera amb el sol d'agost.</p>""")
  + ficha("Dades tècniques", [
     ("Material", "Gres porcellànic tècnic Rosa Gres"),
     ("Sistemes", "Skimmer, desbordant i Slim"),
     ("Aplicació", "Vas, coronació, platja i entorn"),
     ("Propietats", "Antilliscant, resistent a gelades, estable al color"),
     ("Termini orientatiu", "Suma de 2 a 4 setmanes sobre l'obra del vas")]),
 extra=faq("ca", [
  ("Es pot posar gres sobre una piscina existent?", "Sí, si el vas està sa i les mides permeten el desglossament de peces. Cal valorar-ho cas per cas."),
  ("Rellisca?", "Les peces de platja i coronació són antilliscants de classe específica per a exterior mullat. És més segura que una rajola convencional."),
  ("I les juntes?", "Es rejunten amb material epoxi o cimentós tècnic apte per a immersió. És la part que més determina la durabilitat i on no s'estalvia.")])
  + cinta("Vols veure mostres físiques?",
          "Tenim mostrari al magatzem de Balaguer. Passa i les veus amb llum de dia.", "ca")),
}

# ============================================================ MANTENIMIENTO
C["mant"] = {
"es": dict(
 title="Mantenimiento de piscinas en Lleida | Servicio técnico Astralpool | Europiscina",
 desc="Mantenimiento de piscinas para particulares, comunidades y ayuntamientos en Lleida. Apertura y cierre de temporada, tratamiento del agua y servicio técnico Astralpool.",
 miga="Mantenimiento", h1="Mantenimiento: el agua no se cuida sola.",
 entradilla="Apertura y cierre de temporada, control del agua, electrólisis salina y servicio técnico. Para particulares, comunidades de propietarios y piscinas municipales.",
 foto=f"{IMG}/piscina-hamaca.jpg", foto_alt="Piscina en mantenimiento con el agua en condiciones",
 cuerpo=cuerpo("Casi toda avería cara empieza siendo un pH mal medido.",
  """<p>La mayoría de reparaciones que hacemos en junio se podrían haber evitado en marzo. Bombas gripadas por invernaje mal hecho, células de electrólisis calcificadas por dureza sin corregir, láminas decoloradas por dosificación incorrecta. Todo eso es mantenimiento, no mala suerte.</p>
     <p>Nuestro servicio cubre la temporada completa: puesta en marcha, visitas periódicas con analítica y ajuste, y cierre e invernaje antes del frío.</p>""",
  """<h3>Qué incluye una visita</h3>
     <p>Análisis de pH, cloro libre, estabilizante y dureza. Limpieza de cestillos y prefiltro, revisión de presión del filtro y lavado si procede, comprobación de la célula salina y del cuadro, y repaso de fondo y línea de flotación.</p>
     <h3>Comunidades y ayuntamientos</h3>
     <p>Las piscinas de uso público tienen obligaciones sanitarias distintas a las de una casa particular: registros de control, parámetros documentados y responsabilidades definidas. Lo gestionamos con el detalle que exige la normativa.</p>""")
  + ficha("Servicio", [
     ("Modalidades", "Contrato de temporada o avisos puntuales"),
     ("Cobertura", "Particulares, comunidades y piscinas municipales"),
     ("Servicio técnico", "Astralpool y equipos Fluidra"),
     ("Tratamiento", "Cloro, sal por electrólisis y corrección de parámetros"),
     ("Temporada", "Puesta en marcha en primavera, invernaje en otoño")]),
 extra=faq("es", [
  ("¿Cada cuánto hay que pasar?", "En temporada alta, semanal o quincenal según uso y volumen. Fuera de temporada, con la piscina invernada, basta con revisiones puntuales."),
  ("¿Trabajáis con piscinas que no habéis construido vosotros?", "Sí, la mayoría de nuestro mantenimiento es de piscinas construidas por otros."),
  ("¿La sal es mejor que el cloro?", "La electrólisis salina genera el cloro en el propio equipo a partir de sal. El agua resulta más suave y quita trabajo diario, pero sigue necesitando control de pH y mantenimiento de la célula."),
  ("¿Cubrís urgencias?", "Sí, con prioridad para clientes con contrato de mantenimiento.")])
  + cinta("¿Quieres presupuesto de mantenimiento para la temporada?",
          "Dinos medidas, tipo de depuración y población, y te lo pasamos.", "es")),

"ca": dict(
 title="Manteniment de piscines a Lleida | Servei tècnic Astralpool | Europiscina",
 desc="Manteniment de piscines per a particulars, comunitats i ajuntaments a Lleida. Obertura i tancament de temporada, tractament de l'aigua i servei tècnic Astralpool.",
 miga="Manteniment", h1="Manteniment: l'aigua no es cuida sola.",
 entradilla="Obertura i tancament de temporada, control de l'aigua, electròlisi salina i servei tècnic. Per a particulars, comunitats de propietaris i piscines municipals.",
 foto=f"{IMG}/piscina-hamaca.jpg", foto_alt="Piscina en manteniment amb l'aigua en condicions",
 cuerpo=cuerpo("Gairebé tota avaria cara comença sent un pH mal mesurat.",
  """<p>La majoria de reparacions que fem al juny s'haurien pogut evitar al març. Bombes gripades per hivernatge mal fet, cèl·lules d'electròlisi calcificades per duresa sense corregir, làmines decolorades per dosificació incorrecta. Tot això és manteniment, no mala sort.</p>
     <p>El nostre servei cobreix la temporada completa: posada en marxa, visites periòdiques amb analítica i ajust, i tancament i hivernatge abans del fred.</p>""",
  """<h3>Què inclou una visita</h3>
     <p>Anàlisi de pH, clor lliure, estabilitzant i duresa. Neteja de cistells i prefiltre, revisió de pressió del filtre i rentat si escau, comprovació de la cèl·lula salina i del quadre, i repàs de fons i línia de flotació.</p>
     <h3>Comunitats i ajuntaments</h3>
     <p>Les piscines d'ús públic tenen obligacions sanitàries diferents de les d'una casa particular: registres de control, paràmetres documentats i responsabilitats definides. Ho gestionem amb el detall que exigeix la normativa.</p>""")
  + ficha("Servei", [
     ("Modalitats", "Contracte de temporada o avisos puntuals"),
     ("Cobertura", "Particulars, comunitats i piscines municipals"),
     ("Servei tècnic", "Astralpool i equips Fluidra"),
     ("Tractament", "Clor, sal per electròlisi i correcció de paràmetres"),
     ("Temporada", "Posada en marxa a la primavera, hivernatge a la tardor")]),
 extra=faq("ca", [
  ("Cada quant cal passar-hi?", "En temporada alta, setmanal o quinzenal segons ús i volum. Fora de temporada, amb la piscina hivernada, n'hi ha prou amb revisions puntuals."),
  ("Treballeu amb piscines que no heu construït vosaltres?", "Sí, la majoria del nostre manteniment és de piscines construïdes per altres."),
  ("La sal és millor que el clor?", "L'electròlisi salina genera el clor al mateix equip a partir de sal. L'aigua resulta més suau i treu feina diària, però continua necessitant control de pH i manteniment de la cèl·lula."),
  ("Cobriu urgències?", "Sí, amb prioritat per a clients amb contracte de manteniment.")])
  + cinta("Vols pressupost de manteniment per a la temporada?",
          "Digues-nos mides, tipus de depuració i població, i te'l passem.", "ca")),

"en": dict(
 title="Pool maintenance in Lleida and Catalonia | Europiscina",
 desc="Pool maintenance for private owners, residents' associations and town councils in Lleida. Season opening and closing, water treatment and Astralpool service.",
 miga="Maintenance", h1="Maintenance: water does not look after itself.",
 entradilla="Season opening and closing, water control, salt chlorination and technical service. For private owners, residents' associations and municipal pools.",
 foto=f"{IMG}/piscina-hamaca.jpg", foto_alt="A well-maintained swimming pool",
 cuerpo=cuerpo("Almost every expensive breakdown starts as a badly measured pH.",
  """<p>Most of the repairs we carry out in June could have been avoided in March. Pumps seized by poor winterisation, chlorinator cells scaled up by uncorrected hardness, liners discoloured by bad dosing. That is maintenance, not bad luck.</p>
     <p>Our service covers the full season: spring start-up, regular visits with water testing and adjustment, and closing and winterisation before the cold arrives.</p>""",
  """<h3>What a visit includes</h3>
     <p>Testing of pH, free chlorine, stabiliser and hardness. Cleaning of skimmer baskets and pre-filter, filter pressure check and backwash if needed, inspection of the salt cell and control panel, and a pass over the floor and waterline.</p>
     <h3>Communities and councils</h3>
     <p>Public-use pools carry health obligations that private gardens do not: control records, documented parameters and defined responsibilities. We handle that to the standard the regulations require.</p>""")
  + ficha("Service", [
     ("Options", "Season contract or one-off call-outs"),
     ("Coverage", "Private owners, communities and municipal pools"),
     ("Technical service", "Astralpool and Fluidra equipment"),
     ("Treatment", "Chlorine, salt chlorination and parameter correction"),
     ("Season", "Spring start-up, autumn winterisation")]),
 extra=faq("en", [
  ("How often do you need to come?", "In high season, weekly or fortnightly depending on use and volume. Out of season, with the pool winterised, occasional checks are enough."),
  ("Do you maintain pools you did not build?", "Yes. Most of the pools we maintain were built by someone else."),
  ("Is salt better than chlorine?", "Salt chlorination produces chlorine in the unit itself from salt. The water feels softer and it removes daily work, but it still needs pH control and cell maintenance."),
  ("Do you cover emergencies?", "Yes, with priority for customers on a maintenance contract.")])
  + cinta("Would you like a maintenance quote for the season?",
          "Send us the dimensions, the type of filtration and your town, and we will price it.", "en")),
}

# ============================================================ FUGAS DE AGUA
C["fugas"] = {
"es": dict(
 title="Fugas de agua en piscinas en Lleida | Localización y reparación | Europiscina",
 desc="Localización y reparación de fugas de agua en piscinas en Lleida y Huesca. Detección en vaso, hidráulica y skimmers sin destrozar la obra.",
 miga="Fugas de agua", h1="La piscina pierde agua. Vamos a saber por dónde.",
 entradilla="Antes de picar nada, hay que localizar. Diagnosticamos si la pérdida está en el vaso, en la hidráulica enterrada o en los pasamuros, y damos dos presupuestos: el parche y la solución.",
 foto=f"{IMG}/piscina-borde.jpg", foto_alt="Detalle del borde de una piscina",
 cuerpo=cuerpo("Perder agua no siempre significa romper el suelo.",
  """<p>Una piscina que baja más de lo que evapora tiene fuga en uno de tres sitios: el vaso, la instalación hidráulica enterrada o las piezas de paso: skimmers, focos, impulsores y sumideros. Cada uno se localiza de una manera distinta y cada uno tiene un coste de reparación muy distinto.</p>
     <p>Empezamos siempre por descartar lo barato: test de evaporación, prueba con el equipo parado y en marcha, y revisión de pasamuros y juntas. Solo si hace falta pasamos a presurizar circuitos.</p>""",
  """<h3>Lo que te vamos a decir</h3>
     <p>Después del diagnóstico te damos dos números: cuánto cuesta reparar el punto concreto y cuánto costaría revestir con lámina armada y olvidarte. En piscinas de gresite con más de veinte años, muchas veces el segundo número tiene más sentido, y te lo diremos aunque sea el trabajo más grande.</p>
     <h3>Cuándo llamar</h3>
     <p>Si estás rellenando más de dos o tres centímetros por semana en pleno verano, o si notas el terreno de alrededor blando o hundido, no esperes. Una fuga enterrada que lava el terreno bajo el vaso acaba siendo un problema estructural.</p>"""),
 extra=faq("es", [
  ("¿Cuánto se pierde por evaporación y es normal?", "En verano, en la plana de Lleida, entre 3 y 5 mm al día es evaporación normal. Bastante más que eso ya es fuga."),
  ("¿Hay que vaciar la piscina para buscarla?", "En la mayoría de casos no. Vaciar una piscina sin control es además arriesgado si el nivel freático es alto."),
  ("¿Cuánto cuesta el diagnóstico?", "Se cobra la visita de diagnóstico y se descuenta del importe de la reparación si nos la encargas.")])
  + cinta("Llevas semanas rellenando.",
          "Cuanto antes se localiza, más barata sale. Escríbenos y concretamos visita.", "es")),

"ca": dict(
 title="Fuites d'aigua en piscines a Lleida | Localització i reparació | Europiscina",
 desc="Localització i reparació de fuites d'aigua en piscines a Lleida i Osca. Detecció al vas, a la hidràulica i als skimmers sense destrossar l'obra.",
 miga="Fuites d'aigua", h1="La piscina perd aigua. Sabrem per on.",
 entradilla="Abans de picar res, cal localitzar. Diagnostiquem si la pèrdua és al vas, a la hidràulica enterrada o als passamurs, i donem dos pressupostos: el pedaç i la solució.",
 foto=f"{IMG}/piscina-borde.jpg", foto_alt="Detall de la vora d'una piscina",
 cuerpo=cuerpo("Perdre aigua no sempre vol dir trencar el terra.",
  """<p>Una piscina que baixa més del que evapora té fuita en un de tres llocs: el vas, la instal·lació hidràulica enterrada o les peces de pas: skimmers, focus, impulsors i embornals. Cadascun es localitza d'una manera diferent i cadascun té un cost de reparació molt diferent.</p>
     <p>Comencem sempre per descartar el barat: test d'evaporació, prova amb l'equip aturat i en marxa, i revisió de passamurs i juntes. Només si cal passem a pressuritzar circuits.</p>""",
  """<h3>El que et direm</h3>
     <p>Després del diagnòstic et donem dos números: quant costa reparar el punt concret i quant costaria revestir amb làmina armada i oblidar-te'n. En piscines de gresite amb més de vint anys, sovint el segon número té més sentit, i t'ho direm encara que sigui la feina més gran.</p>
     <h3>Quan trucar</h3>
     <p>Si estàs omplint més de dos o tres centímetres per setmana en ple estiu, o si notes el terreny del voltant tou o enfonsat, no esperis. Una fuita enterrada que renta el terreny sota el vas acaba sent un problema estructural.</p>"""),
 extra=faq("ca", [
  ("Quant es perd per evaporació i és normal?", "A l'estiu, a la plana de Lleida, entre 3 i 5 mm al dia és evaporació normal. Bastant més que això ja és fuita."),
  ("Cal buidar la piscina per buscar-la?", "En la majoria de casos no. Buidar una piscina sense control és a més arriscat si el nivell freàtic és alt."),
  ("Quant costa el diagnòstic?", "Es cobra la visita de diagnòstic i es descompta de l'import de la reparació si ens l'encarregues.")])
  + cinta("Fa setmanes que omples.",
          "Com abans es localitza, més barata surt. Escriu-nos i concretem visita.", "ca")),
}

# ============================================================ REFORMAS
C["ref"] = {
"es": dict(
 title="Reforma y rehabilitación de piscinas en Lleida | Europiscina",
 desc="Reforma integral de piscinas en Lleida: cambio de revestimiento, renovación de depuración, climatización, cubiertas y adaptación a normativa.",
 miga="Reformas", h1="Tu piscina no está acabada. Está anticuada.",
 entradilla="Cambio de revestimiento, renovación de la sala de máquinas, electrólisis salina, iluminación LED, cubiertas y climatización. Casi siempre sale mejor que hacerla nueva.",
 foto=f"{IMG}/piscina-rustica.jpg", foto_alt="Piscina reformada e integrada en su entorno",
 cuerpo=cuerpo("El vaso suele estar bien. Lo que sobra son treinta años.",
  """<p>Una piscina de los años noventa normalmente tiene el vaso perfectamente sano y todo lo demás obsoleto: gresite que se cae, filtro sobredimensionado y ruidoso, bomba de consumo alto, cloración manual y ni un punto de luz decente.</p>
     <p>La reforma ataca esas capas por separado. Puedes hacerlas todas de golpe o repartirlas en dos temporadas según presupuesto, y te decimos cuál es el orden que más se nota.</p>""",
  """<h3>Lo que más cambia la piscina</h3>
     <p>Por orden de impacto real: revestimiento nuevo, bomba de velocidad variable, electrólisis salina y luz LED. Las dos primeras se notan cada día; las dos segundas se notan cada factura.</p>
     <h3>Adaptación a normativa</h3>
     <p>En comunidades y piscinas de uso público, la reforma suele ser también el momento de resolver cumplimientos pendientes: sumideros de seguridad, barreras y registros. Lo revisamos en la visita.</p>"""),
 extra=faq("es", [
  ("¿Sale a cuenta reformar o hacerla nueva?", "Si el vaso está estructuralmente sano, reformar cuesta una fracción y se hace en semanas en vez de meses. Si hay movimiento estructural, la respuesta cambia y te lo diremos claro."),
  ("¿Se puede hacer en invierno?", "Es el mejor momento. Llegas a la temporada con la piscina lista y sin competir por agenda con el resto de trabajos de junio."),
  ("¿Podéis climatizarla?", "Sí, con bomba de calor y, si interesa, cubierta para conservar temperatura. La cubierta es lo que hace que el gasto energético tenga sentido.")])
  + cinta("¿Reformamos este invierno?",
          "La agenda de invierno se cierra en otoño. Cuanto antes lo miramos, mejor fecha coges.", "es")),

"ca": dict(
 title="Reforma i rehabilitació de piscines a Lleida | Europiscina",
 desc="Reforma integral de piscines a Lleida: canvi de revestiment, renovació de depuració, climatització, cobertes i adaptació a normativa.",
 miga="Reformes", h1="La teva piscina no està acabada. Està antiquada.",
 entradilla="Canvi de revestiment, renovació de la sala de màquines, electròlisi salina, il·luminació LED, cobertes i climatització. Gairebé sempre surt millor que fer-la nova.",
 foto=f"{IMG}/piscina-rustica.jpg", foto_alt="Piscina reformada i integrada al seu entorn",
 cuerpo=cuerpo("El vas sol estar bé. El que sobra són trenta anys.",
  """<p>Una piscina dels anys noranta normalment té el vas perfectament sa i tota la resta obsoleta: gresite que cau, filtre sobredimensionat i sorollós, bomba de consum alt, cloració manual i cap punt de llum decent.</p>
     <p>La reforma ataca aquestes capes per separat. Pots fer-les totes de cop o repartir-les en dues temporades segons pressupost, i et diem quin és l'ordre que més es nota.</p>""",
  """<h3>El que més canvia la piscina</h3>
     <p>Per ordre d'impacte real: revestiment nou, bomba de velocitat variable, electròlisi salina i llum LED. Les dues primeres es noten cada dia; les dues segones es noten cada factura.</p>
     <h3>Adaptació a normativa</h3>
     <p>En comunitats i piscines d'ús públic, la reforma sol ser també el moment de resoldre compliments pendents: embornals de seguretat, barreres i registres. Ho revisem a la visita.</p>"""),
 extra=faq("ca", [
  ("Surt a compte reformar o fer-la nova?", "Si el vas està estructuralment sa, reformar costa una fracció i es fa en setmanes en lloc de mesos. Si hi ha moviment estructural, la resposta canvia i t'ho direm clar."),
  ("Es pot fer a l'hivern?", "És el millor moment. Arribes a la temporada amb la piscina llesta i sense competir per agenda amb la resta de feines de juny."),
  ("Podeu climatitzar-la?", "Sí, amb bomba de calor i, si interessa, coberta per conservar temperatura. La coberta és el que fa que la despesa energètica tingui sentit.")])
  + cinta("Reformem aquest hivern?",
          "L'agenda d'hivern es tanca a la tardor. Com abans ho mirem, millor data agafes.", "ca")),
}

# ============================================================ EMPRESA
C["emp"] = {
"es": dict(
 title="Quiénes somos | Europiscina, constructores de piscinas desde 1999",
 desc="Europiscina, marca de GARCAM Industries SLU. Agua desde 1969, piscinas desde 1999. Equipo y maquinaria propios en Balaguer, Lleida.",
 miga="Empresa", h1="Empezamos con tuberías. Acabamos haciendo piscinas.",
 entradilla="En 1969 abrimos con canalizaciones, bombas y riego en la plana de Lleida. En 1999 aplicamos ese oficio a construir piscinas. Seguimos en el mismo sitio, en Balaguer.",
 foto=f"{IMG}/piscina-deportiva.jpg", foto_alt="Piscina de gran formato construida por Europiscina",
 cuerpo=cuerpo("Nadie subcontrata tu piscina.",
  """<p>Excavamos, armamos, impermeabilizamos y ponemos en marcha con gente de nuestra plantilla y maquinaria propia. No hay una cuadrilla distinta cada semana ni un teléfono que deja de responder cuando acaba la obra.</p>
     <p>Eso tiene un precio, y no lo escondemos: rara vez somos el presupuesto más barato de los tres que pides. Somos el que sigue respondiendo el teléfono siete años después, cuando toca cambiar la bomba.</p>""",
  """<h3>Por qué la hidráulica es nuestra ventaja</h3>
     <p>Las averías caras de una piscina casi nunca son estéticas. Son drenajes mal resueltos, freáticos no previstos, retornos mal dimensionados y salas de máquinas mal calculadas. Es exactamente lo que llevamos haciendo desde antes de dedicarnos a las piscinas.</p>
     <h3>Marcas con las que trabajamos</h3>
     <p>Official Partner de Astralpool Fluidra y miembros de ASOFAP. Lámina armada Renolit Alkorplan, gres porcelánico Rosa Gres, poliéster de Europa Piscinas.</p>"""),
 extra=cinta("¿Hablamos de tu proyecto?",
             "Visita al terreno sin compromiso en Lleida, Huesca, Tarragona, Andorra y Mallorca.", "es")),

"ca": dict(
 title="Qui som | Europiscina, constructors de piscines des del 1999",
 desc="Europiscina, marca de GARCAM Industries SLU. Aigua des del 1969, piscines des del 1999. Equip i maquinària propis a Balaguer, Lleida.",
 miga="Empresa", h1="Vam començar amb canonades. Vam acabar fent piscines.",
 entradilla="El 1969 vam obrir amb canalitzacions, bombes i reg a la plana de Lleida. El 1999 vam aplicar aquest ofici a construir piscines. Continuem al mateix lloc, a Balaguer.",
 foto=f"{IMG}/piscina-deportiva.jpg", foto_alt="Piscina de gran format construïda per Europiscina",
 cuerpo=cuerpo("Ningú subcontracta la teva piscina.",
  """<p>Excavem, armem, impermeabilitzem i posem en marxa amb gent de la nostra plantilla i maquinària pròpia. No hi ha una colla diferent cada setmana ni un telèfon que deixa de respondre quan s'acaba l'obra.</p>
     <p>Això té un preu, i no l'amaguem: poques vegades som el pressupost més barat dels tres que demanes. Som el que continua responent el telèfon set anys després, quan toca canviar la bomba.</p>""",
  """<h3>Per què la hidràulica és el nostre avantatge</h3>
     <p>Les avaries cares d'una piscina gairebé mai són estètiques. Són drenatges mal resolts, freàtics no previstos, retorns mal dimensionats i sales de màquines mal calculades. És exactament el que fem des d'abans de dedicar-nos a les piscines.</p>
     <h3>Marques amb què treballem</h3>
     <p>Official Partner d'Astralpool Fluidra i membres d'ASOFAP. Làmina armada Renolit Alkorplan, gres porcellànic Rosa Gres, polièster d'Europa Piscinas.</p>"""),
 extra=cinta("Parlem del teu projecte?",
             "Visita al terreny sense compromís a Lleida, Osca, Tarragona, Andorra i Mallorca.", "ca")),
}
