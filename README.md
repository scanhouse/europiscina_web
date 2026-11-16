# europiscina.es

Web estática de Europiscina (GARCAM Industries SLU). Se publica sola en Netlify desde la rama `main`.

## Regla de oro: no editar los `index.html` a mano

Las páginas las escriben unos scripts ("recetas"). Si se retoca un `index.html` directamente,
el siguiente que regenere la web perderá ese retoque sin darse cuenta. Para evitarlo:

- **Cada despliegue de Netlify comprueba** que el HTML coincide con las recetas
  (`python3 generar.py --comprobar`). Si no coincide, **el despliegue se bloquea** y la web
  sigue publicada como estaba. El registro de Netlify dice qué fichero y qué línea.
- **`generar.py` se niega a regenerar** si detecta un HTML tocado a mano.

## Cómo cambiar un texto

1. Edita la receta que genera esa página:
   - Textos de las páginas de servicios y empresa: `contenido.py`
   - Portada, contacto y configurador: `extras.py`
   - Aviso legal, privacidad y cookies: `legales.py`
   - Cabecera, menú y pie de todas las páginas: `motor.py`
   - Datos estructurados para Google: `schema.py`
   - Botón de WhatsApp: `snippet-whatsapp.html` (lo inyecta `whatsapp.py`)
2. Ejecuta `python3 generar.py`
3. Sube **juntos** los `.py` cambiados, los `.html` regenerados y `.generado.json`.

## Si hay una urgencia

Para publicar un retoque hecho a mano sin pasar por las recetas: en Netlify, define la variable
de entorno `PERMITIR_HTML_MANUAL=1`. La comprobación avisa pero no bloquea. Quítala en cuanto el
retoque esté pasado a su receta, o el siguiente regenerado lo borrará.

## Fuera del sistema de recetas

- `/a/` es la página de firma de albaranes: es una app aparte, no la generan las recetas.
- `img/` y `fonts/` son ficheros fijos.
