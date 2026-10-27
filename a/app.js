// Pàgina de signatura d'albarans (Europiscina / GARCAM / Hidrocenter).
// Tot el text que ve del servidor s'insereix amb textContent: res d'innerHTML amb dades.
(function () {
  "use strict";
  var API = "https://gwyjwmedllseirtxprlp.supabase.co/functions/v1/alb-public";
  var TOKEN = (location.pathname.split("/").filter(Boolean).pop() || "").trim();
  var $ = function (id) { return document.getElementById(id); };

  var TXT = {
    es: {
      client: "CLIENTE", data: "FECHA", tecnics: "TÉCNICOS", treballs: "Trabajos realizados", detall: "DETALLE",
      fotos: "Fotos del técnico", import: "Importe", base: "Base imponible", total: "Total",
      nota_factura: "Una vez firmado, en los próximos días recibirá la factura de este servicio.",
      conformitat: "Su conformidad", firma_ajuda: "Firme con el dedo dentro del recuadro", esborrar: "Borrar firma",
      nom: "Nombre y apellidos", dni: "DNI o NIE",
      ref: "Referencia de la obra o del trabajo", ref_et: "REFERENCIA OBRA", ref_fila: "Referencia de obra",
      ref_ajuda: "Dónde se ha hecho el trabajo, para que no haya confusiones. Ej.: Hidrante 14, Comunidad de Regantes de Térmens.",
      accepto: "He revisado los trabajos, las fotos y el importe, y estoy conforme con el servicio realizado.",
      signar: "Firmar conforme", no_conforme: "No estoy conforme, indicar qué falla",
      que_falla: "¿Qué no está bien?", explica: "Explíquenos el problema", foto_opcional: "Añadir foto (opcional)",
      enviar_reparo: "Enviar", tornar: "Volver a la firma",
      signat_tit: "Albarán firmado", signat_text: "Gracias. Le hemos enviado una copia en PDF por WhatsApp. En los próximos días recibirá la factura de este servicio.",
      signat_per: "Firmado por", data_hora: "Fecha y hora", verificacio: "Código de verificación", descarregar: "Descargar PDF",
      reparo_ok_tit: "Hemos recibido su comentario", reparo_ok_text: "Le llamaremos para resolverlo. No se emitirá ninguna factura de este servicio hasta que esté solucionado.",
      mai_banc: "Nunca le pediremos datos bancarios ni de tarjeta en esta página.",
      rgpd: "Responsable: GARCAM Industries SLU (CIF B10713675). Usamos sus datos únicamente para gestionar este servicio.",
      no_valid_tit: "Este enlace no es válido o ha caducado", no_valid_text: "Si necesita el albarán, llámenos al 973 446 445 y se lo volvemos a enviar.",
      titol: "Revise el trabajo y firme", albara: "Albarán",
      e_firma: "Firme dentro del recuadro.", e_nom: "Escriba su nombre y apellidos.", e_dni: "Escriba un DNI o NIE válido (con la letra).", e_ref: "Indique la referencia de la obra o dónde se ha hecho el trabajo.",
      e_accepta: "Marque la casilla de conformidad.", e_text: "Explíquenos brevemente qué no está bien.", e_foto: "La foto no se ha podido preparar. Pruebe con otra.",
      e_gen: "No se ha podido enviar. Revise la conexión y vuelva a intentarlo.", e_resolt: "Este albarán ya se ha firmado o tiene un comentario pendiente.",
      enviant: "Enviando…", signant: "Firmando…", vist_ok: "Firmado", reparo_estat: "Comentario recibido"
    },
    ca: {
      client: "CLIENT", data: "DATA", tecnics: "TÈCNICS", treballs: "Treballs realitzats", detall: "DETALL",
      fotos: "Fotos del tècnic", import: "Import", base: "Base imposable", total: "Total",
      nota_factura: "Un cop signat, en els propers dies rebrà la factura d'aquest servei.",
      conformitat: "La seva conformitat", firma_ajuda: "Signi amb el dit dins del requadre", esborrar: "Esborrar signatura",
      nom: "Nom i cognoms", dni: "DNI o NIE",
      ref: "Referència de l'obra o del treball", ref_et: "REFERÈNCIA OBRA", ref_fila: "Referència d'obra",
      ref_ajuda: "On s'ha fet el treball, perquè no hi hagi confusions. Ex.: Hidrant 14, Comunitat de Regants de Térmens.",
      accepto: "He revisat els treballs, les fotos i l'import, i estic conforme amb el servei realitzat.",
      signar: "Signar conforme", no_conforme: "No hi estic conforme, indicar què falla",
      que_falla: "Què no està bé?", explica: "Expliqui'ns el problema", foto_opcional: "Afegir foto (opcional)",
      enviar_reparo: "Enviar", tornar: "Tornar a la signatura",
      signat_tit: "Albarà signat", signat_text: "Gràcies. Li hem enviat una còpia en PDF per WhatsApp. En els propers dies rebrà la factura d'aquest servei.",
      signat_per: "Signat per", data_hora: "Data i hora", verificacio: "Codi de verificació", descarregar: "Descarregar PDF",
      reparo_ok_tit: "Hem rebut el seu comentari", reparo_ok_text: "El trucarem per resoldre-ho. No s'emetrà cap factura d'aquest servei fins que estigui solucionat.",
      mai_banc: "Mai li demanarem dades bancàries ni de targeta en aquesta pàgina.",
      rgpd: "Responsable: GARCAM Industries SLU (CIF B10713675). Fem servir les seves dades només per gestionar aquest servei.",
      no_valid_tit: "Aquest enllaç no és vàlid o ha caducat", no_valid_text: "Si necessita l'albarà, truqui'ns al 973 446 445 i l'hi tornarem a enviar.",
      titol: "Revisi el treball i signi", albara: "Albarà",
      e_firma: "Signi dins del requadre.", e_nom: "Escrigui el seu nom i cognoms.", e_dni: "Escrigui un DNI o NIE vàlid (amb la lletra).", e_ref: "Indiqui la referència de l'obra o on s'ha fet el treball.",
      e_accepta: "Marqui la casella de conformitat.", e_text: "Expliqui'ns breument què no està bé.", e_foto: "No s'ha pogut preparar la foto. Provi'n una altra.",
      e_gen: "No s'ha pogut enviar. Revisi la connexió i torni-ho a provar.", e_resolt: "Aquest albarà ja s'ha signat o té un comentari pendent.",
      enviant: "Enviant…", signant: "Signant…", vist_ok: "Signat", reparo_estat: "Comentari rebut"
    }
  };
  var L = TXT.es;

  function api(accio, extra) {
    var body = Object.assign({ accio: accio, t: TOKEN }, extra || {});
    return fetch(API, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body), referrerPolicy: "no-referrer", credentials: "omit" })
      .then(function (r) { return r.json().catch(function () { return { ok: false }; }).then(function (j) { j._status = r.status; return j; }); });
  }
  var eur = function (n) { return new Intl.NumberFormat("es-ES", { minimumFractionDigits: 2, maximumFractionDigits: 2, useGrouping: "always" }).format(n) + " €"; };
  function traduir() {
    document.querySelectorAll("[data-t]").forEach(function (el) { var k = el.getAttribute("data-t"); if (L[k]) el.textContent = L[k]; });
  }
  // DNI (8 xifres + lletra) o NIE (X/Y/Z + 7 xifres + lletra), amb la lletra de control.
  function dniValid(v) {
    var m = /^([0-9XYZ])([0-9]{7})([A-Z])$/.exec(v || "");
    if (!m) return false;
    var n = Number(("XYZ".indexOf(m[1]) >= 0 ? String("XYZ".indexOf(m[1])) : m[1]) + m[2]);
    return "TRWAGMYFPDXBNJZSQVHLCKE".charAt(n % 23) === m[3];
  }
  function mostra(id, on) { $(id).hidden = !on; }
  function err(id, msg) { var e = $(id); e.textContent = msg || ""; e.hidden = !msg; }
  function noValid() {
    traduir(); $("titol").textContent = L.no_valid_tit; $("subtitol").textContent = "";
    mostra("main", false); mostra("no-valid", true);
  }

  function pinta(a, fotos) {
    L = TXT[a.idioma] || TXT.es;
    document.documentElement.lang = a.idioma;
    traduir();
    document.title = L.albara + " " + a.codi + " · " + a.marca_nom;
    $("marca").textContent = String(a.marca_nom || "").toUpperCase();
    $("titol").textContent = L.titol;
    $("subtitol").textContent = L.albara + " " + a.codi + " · " + a.data_servei;
    $("client").textContent = a.client_nom;
    $("adreca").textContent = a.adreca || "";
    $("data").textContent = a.data_servei;
    $("operaris").textContent = (a.operaris || []).join(" · ") || "-";
    $("treballs").textContent = a.treballs;
    $("ref-val").textContent = a.referencia || "";
    mostra("ref-box", Boolean(a.referencia));
    if (a.referencia && !$("ref").value) $("ref").value = a.referencia;
    var li = $("linies"); li.textContent = "";
    (a.linies || []).forEach(function (l) {
      var row = document.createElement("div"); row.className = "linia";
      var d = document.createElement("span"); d.textContent = l.desc + " ";
      var q = document.createElement("span"); q.className = "q"; q.textContent = "× " + String(l.qty).replace(".", ",");
      d.appendChild(q);
      var i = document.createElement("span"); i.className = "imp"; i.textContent = eur(l.imp);
      row.appendChild(d); row.appendChild(i); li.appendChild(row);
    });
    var fo = $("fotos"); fo.textContent = "";
    (fotos || []).forEach(function (f) {
      var fig = document.createElement("figure");
      var lnk = document.createElement("a"); lnk.href = f.url; lnk.target = "_blank"; lnk.rel = "noopener noreferrer";
      var img = document.createElement("img"); img.src = f.url; img.alt = f.etiqueta || L.fotos; img.loading = "lazy"; img.referrerPolicy = "no-referrer";
      lnk.appendChild(img); fig.appendChild(lnk);
      var cap = document.createElement("figcaption");
      var hora = f.presa ? new Date(f.presa).toLocaleTimeString("es-ES", { timeZone: "Europe/Madrid", hour: "2-digit", minute: "2-digit" }) : "";
      cap.textContent = [f.etiqueta, hora].filter(Boolean).join(" · ");
      fig.appendChild(cap); fo.appendChild(fig);
    });
    mostra("sec-fotos", (fotos || []).length > 0);
    $("base").textContent = eur(a.base);
    $("iva-et").textContent = "IVA " + String(a.iva_pct).replace(".", ",") + " %";
    $("iva").textContent = eur(a.iva);
    $("total").textContent = eur(a.total);

    var signat = a.estat === "signat" || a.estat === "conforme_tacit";
    var reparo = a.estat === "reparo";
    mostra("sec-signar", !signat && !reparo);
    mostra("sec-reparo", false);
    mostra("sec-signat", signat);
    mostra("sec-reparo-ok", reparo);
    if (signat) {
      $("titol").textContent = L.signat_tit;
      $("s-nom").textContent = a.signant_nom || "-";
      $("s-data").textContent = a.signat_el ? new Date(a.signat_el).toLocaleString("es-ES", { timeZone: "Europe/Madrid", day: "2-digit", month: "2-digit", year: "numeric", hour: "2-digit", minute: "2-digit" }) : "-";
      $("s-verif").textContent = a.verificacio || "-";
      $("s-ref").textContent = a.signant_ref || a.referencia || "-";
    }
    if (reparo) $("titol").textContent = L.reparo_estat;
    mostra("main", true);
  }

  // ---------- pad de signatura ----------
  var pad = $("pad"), ctx = pad.getContext("2d"), traços = 0, dibuixant = false, ultim = null;
  function midaPad() {
    var r = pad.getBoundingClientRect(), dpr = Math.min(window.devicePixelRatio || 1, 2);
    pad.width = Math.round(r.width * dpr); pad.height = Math.round(r.height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.lineWidth = 2.6; ctx.lineCap = "round"; ctx.lineJoin = "round"; ctx.strokeStyle = "#0F1B24";
    traços = 0;
  }
  function pos(e) { var r = pad.getBoundingClientRect(); return { x: e.clientX - r.left, y: e.clientY - r.top }; }
  pad.addEventListener("pointerdown", function (e) { e.preventDefault(); pad.setPointerCapture(e.pointerId); dibuixant = true; ultim = pos(e); });
  pad.addEventListener("pointermove", function (e) {
    if (!dibuixant) return; e.preventDefault();
    var p = pos(e); ctx.beginPath(); ctx.moveTo(ultim.x, ultim.y); ctx.lineTo(p.x, p.y); ctx.stroke(); ultim = p; traços++;
  });
  ["pointerup", "pointercancel", "pointerleave"].forEach(function (ev) { pad.addEventListener(ev, function () { dibuixant = false; }); });
  $("esborrar").addEventListener("click", function () { ctx.clearRect(0, 0, pad.width, pad.height); traços = 0; });

  // ---------- accions ----------
  $("btn-signar").addEventListener("click", function () {
    err("err-signar", "");
    var nom = $("nom").value.replace(/\s+/g, " ").trim();
    var dni = $("dni").value.replace(/[\s.-]/g, "").toUpperCase();
    var ref = $("ref").value.replace(/\s+/g, " ").trim();
    if (traços < 8) return err("err-signar", L.e_firma);
    if (nom.length < 3) return err("err-signar", L.e_nom);
    if (!dniValid(dni)) return err("err-signar", L.e_dni);
    if (ref.length < 3) return err("err-signar", L.e_ref);
    if (!$("accepta").checked) return err("err-signar", L.e_accepta);
    var b = $("btn-signar"); b.disabled = true; b.textContent = L.signant;
    api("signar", { nom: nom, dni: dni, referencia: ref, accepta: true, firma: pad.toDataURL("image/png") }).then(function (r) {
      b.disabled = false; b.textContent = L.signar;
      if (r.ok && r.albara) { pinta(r.albara, null); mostra("sec-fotos", false); window.scrollTo(0, 0); return; }
      if (r.error === "ja_resolt") return err("err-signar", L.e_resolt);
      if (r.error === "dni_no_valid") return err("err-signar", L.e_dni);
      if (r.error === "ref_no_valida") return err("err-signar", L.e_ref);
      if (r.error === "nom_no_valid") return err("err-signar", L.e_nom);
      if (r._status === 404) return noValid();
      err("err-signar", L.e_gen);
    }).catch(function () { b.disabled = false; b.textContent = L.signar; err("err-signar", L.e_gen); });
  });

  $("btn-obre-reparo").addEventListener("click", function () { mostra("sec-signar", false); mostra("sec-reparo", true); $("reparo-text").focus(); });
  $("btn-tanca-reparo").addEventListener("click", function () { mostra("sec-reparo", false); mostra("sec-signar", true); });

  function comprimeix(file) {
    return new Promise(function (ok, ko) {
      if (!file) return ok(null);
      var img = new Image(), url = URL.createObjectURL(file);
      img.onload = function () {
        var m = 1600, s = Math.min(1, m / Math.max(img.width, img.height));
        var c = document.createElement("canvas"); c.width = Math.round(img.width * s); c.height = Math.round(img.height * s);
        c.getContext("2d").drawImage(img, 0, 0, c.width, c.height); URL.revokeObjectURL(url);
        ok(c.toDataURL("image/jpeg", 0.8));
      };
      img.onerror = function () { URL.revokeObjectURL(url); ko(); };
      img.src = url;
    });
  }
  $("btn-reparo").addEventListener("click", function () {
    err("err-reparo", "");
    var text = $("reparo-text").value.replace(/\s+/g, " ").trim();
    if (text.length < 5) return err("err-reparo", L.e_text);
    var b = $("btn-reparo"); b.disabled = true; b.textContent = L.enviant;
    comprimeix($("reparo-foto").files[0]).then(function (foto) {
      return api("reparo", { text: text, foto: foto || undefined });
    }, function () { throw new Error("foto"); }).then(function (r) {
      b.disabled = false; b.textContent = L.enviar_reparo;
      if (r.ok) { mostra("sec-reparo", false); mostra("sec-reparo-ok", true); $("titol").textContent = L.reparo_estat; window.scrollTo(0, 0); return; }
      if (r.error === "ja_resolt") return err("err-reparo", L.e_resolt);
      if (r._status === 404) return noValid();
      err("err-reparo", L.e_gen);
    }).catch(function (e) { b.disabled = false; b.textContent = L.enviar_reparo; err("err-reparo", e && e.message === "foto" ? L.e_foto : L.e_gen); });
  });

  $("btn-pdf").addEventListener("click", function () {
    api("pdf").then(function (r) { if (r.ok && r.url) location.href = r.url; else err("err-signar", L.e_gen); });
  });

  // ---------- inici ----------
  if (!/^[A-Za-z0-9_-]{43}$/.test(TOKEN)) return noValid();
  api("veure").then(function (r) {
    if (!r.ok) return noValid();
    pinta(r.albara, r.fotos);
    requestAnimationFrame(midaPad);
    api("obert"); // només quan la pàgina s'ha carregat de debò en un navegador
  }).catch(noValid);
  window.addEventListener("resize", function () { if (traços === 0) midaPad(); });
})();
