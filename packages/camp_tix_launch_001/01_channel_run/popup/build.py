#!/usr/bin/env python3
"""Build the self-contained Tix popup draft from owned copy and font assets."""
import base64
import hashlib
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
copy = json.loads((ROOT / "copy.json").read_text())
c = copy["copy"]

def data(name):
    return base64.b64encode((ROOT / "assets" / name).read_bytes()).decode()

regular = data("Poppins-Regular.ttf")
semibold = data("Poppins-SemiBold.ttf")
inter = data("inter.woff2")
poppins_license = (ROOT / "assets/OFL.txt").read_text()
inter_license = (ROOT / "assets/Inter-OFL.txt").read_text()
mascot = (ROOT / "assets/tix-mascot-blue.svg").read_text()
mascot_inner = mascot[mascot.index(">") + 1:mascot.rindex("</svg>")]
graphic = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="470" viewBox="0 0 1000 470" role="img" aria-labelledby="graphic-title graphic-desc">
<title id="graphic-title">A secondhand buying brief with Tix</title>
<desc id="graphic-desc">''' + html.escape(copy["graphic"]["alt"]) + '''</desc>
<metadata>''' + html.escape(inter_license) + '''</metadata>
<defs>
  <style>@font-face{font-family:TixInter;src:url(data:font/woff2;base64,''' + inter + ''') format('woff2');font-weight:100 900}text{font-family:TixInter,Arial,sans-serif}</style>
  <linearGradient id="paper" x2="1" y2="1"><stop stop-color="#F7F5F2"/><stop offset="1" stop-color="#EAF0FF"/></linearGradient>
  <filter id="card-shadow" x="-20%" y="-30%" width="140%" height="170%"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#193675" flood-opacity=".10"/></filter>
</defs>
<rect width="1000" height="470" fill="url(#paper)"/>
<circle cx="930" cy="22" r="230" fill="#0052FF" opacity=".025"/>
<circle cx="66" cy="450" r="210" fill="#8C52FF" opacity=".025"/>
<g filter="url(#card-shadow)"><rect x="50" y="36" width="900" height="392" rx="30" fill="#FFFFFF" stroke="#DAE3F2" stroke-width="2"/></g>
<g transform="translate(82 66) scale(2.4)" shape-rendering="crispEdges">''' + mascot_inner + '''</g>
<text x="148" y="103" fill="#0052FF" font-size="46" font-weight="750" letter-spacing="-1.7">Tix</text>
<circle cx="887" cy="84" r="5" fill="#0052FF" opacity=".25"/>
<circle cx="906" cy="84" r="5" fill="#0052FF" opacity=".25"/>
<text x="82" y="166" fill="#1A2C44" font-size="38" font-weight="550" letter-spacing="-.6">What are you looking for?</text>
<path d="M124 199H883Q914 199 914 230V340Q914 371 883 371H151L125 389V371H124Q94 371 94 340V230Q94 199 124 199Z" fill="#0052FF"/>
<text x="130" y="260" fill="#FFFFFF" font-size="40" font-weight="500" letter-spacing="-.7">A used Sony camera in Brooklyn.</text>
<text x="130" y="321" fill="#FFFFFF" font-size="40" font-weight="650" letter-spacing="-.7">Less than $950.</text>
</svg>
'''
(ROOT / "graphic.svg").write_text(graphic)

template = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="referrer" content="no-referrer">
<title>Tix announcement</title>
<script type="text/plain" id="poppins-license">__POPPINS_LICENSE__</script>
<script type="text/plain" id="inter-license">__INTER_LICENSE__</script>
<!-- Poppins is embedded under SIL OFL 1.1. Full license: assets/OFL.txt.
Inter is embedded under SIL OFL 1.1. Full license: assets/Inter-OFL.txt.
Product: Tixmancer. Vista Social supplies a design reference only.
Review and availability notes are in copy.json; this file contains the consumer draft. -->
<style>
@font-face{font-family:PopupPoppins;src:url(data:font/ttf;base64,__REGULAR__) format('truetype');font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:PopupPoppins;src:url(data:font/ttf;base64,__SEMIBOLD__) format('truetype');font-weight:600;font-style:normal;font-display:swap}
*{box-sizing:border-box}
:root{font-family:PopupPoppins,Arial,sans-serif;color:#101010;background:#F5F8FD;font-synthesis:none}
body{margin:0;min-height:100dvh;background:radial-gradient(ellipse at 10% 10%,#EDF2FF,transparent 55%),#F5F8FD}
button,a{-webkit-tap-highlight-color:transparent}
button{font:inherit;cursor:pointer}
button:focus-visible,a:focus-visible{outline:3px solid #0052FF;outline-offset:4px}
.stage{max-width:650px;margin:0 auto;padding:100px 28px;text-align:center}
.wordmark{color:#0052FF;font-weight:600;font-size:26px;letter-spacing:-1px}
.stage h1{font-size:clamp(28px,5vw,42px);line-height:1.25;letter-spacing:-1.5px;font-weight:600;margin:28px 0}
.opener{min-height:48px;padding:0 24px;border:1px solid #CBD6EE;background:#FFFFFF;border-radius:10px;color:#0052FF;font-weight:600}
.announcement{position:fixed;width:min(560px,calc(100vw - 32px));max-width:none;max-height:calc(100dvh - 40px);padding:0;border:1px solid #E5EAF2;border-radius:24px;background:#FFFFFF;color:#101010;box-shadow:0 32px 100px #1A2C442B;overflow:hidden}
.announcement::backdrop{background:#15284155;backdrop-filter:blur(5px)}
.popup-scroll{max-height:calc(100dvh - 42px);overflow:auto;overscroll-behavior:contain;scrollbar-width:thin}
.close{position:absolute;z-index:2;right:12px;top:12px;display:grid;place-items:center;width:44px;height:44px;border:1px solid #DCE3EE;border-radius:50%;background:#FFFFFF;color:#1A2C44;box-shadow:0 3px 12px #18325D0D}
.close svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.8}
.graphic{margin:0;line-height:0;border-bottom:1px solid #EDF0F5}
.graphic>svg{display:block;width:100%;height:auto}
.content{padding:25px 32px 20px}
.eyebrow{margin:0;color:#0063E3;font-size:11px;font-weight:600;line-height:1.5;letter-spacing:1.6px}
h2{margin:10px 0 14px;font-size:34px;font-weight:600;line-height:1.2;letter-spacing:-1.15px;max-width:460px;overflow-wrap:normal}
h2:focus{outline:none}
.body-copy{margin:0;color:#536278;font-size:15px;line-height:1.75}
.actions{margin-top:23px;display:grid;gap:5px}
.cta{display:flex;align-items:center;justify-content:center;gap:13px;min-height:52px;padding:12px 20px;border-radius:8px;background:linear-gradient(90deg,#0063E3,#884DF5);color:#FFFFFF;text-decoration:none;font-size:15px;font-weight:600;line-height:1.5;box-shadow:0 6px 18px #0063E326}
.cta svg{width:19px;height:19px;stroke:currentColor;stroke-width:1.8;fill:none;flex-shrink:0}
.cta:hover{background:linear-gradient(90deg,#0054C1,#7541E0)}
.dismiss{justify-self:center;min-width:120px;min-height:44px;border:0;border-radius:8px;padding:8px 18px;color:#526078;background:transparent;font-size:13px}
.dismiss:hover{background:#F5F8FD;color:#1A2C44}
body.embedded{min-height:0;background:transparent}
.embedded .stage{padding:24px}
.embedded.is-open .stage{display:none}
.embedded .announcement{position:relative;margin:16px auto;box-shadow:0 8px 34px #1A2C4412;max-height:calc(100dvh - 32px)}
.embedded .popup-scroll{max-height:calc(100dvh - 34px)}
@media(max-width:520px){
 .announcement{margin:auto 16px 16px;width:calc(100vw - 32px);max-height:calc(100dvh - 32px);border-radius:22px}
 .popup-scroll{max-height:calc(100dvh - 34px)}
 .content{padding:22px 24px 14px}
 h2{font-size:28px;line-height:1.22;letter-spacing:-.9px;margin-bottom:12px}
 .body-copy{font-size:14px;line-height:1.7}
 .actions{margin-top:20px}
 .cta{font-size:14px;min-height:50px}
 .close{top:10px;right:10px;width:44px;height:44px}
 .close svg{width:18px;height:18px}
 .embedded .announcement{margin:16px auto}
}
@media(prefers-reduced-motion:no-preference){.announcement[open]{animation:enter .18s ease-out}@keyframes enter{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}}
</style>
</head>
<body>
<main class="stage">
 <div class="wordmark">Tix</div>
 <h1>Your next secondhand find.</h1>
 <button id="open-announcement" class="opener" type="button" aria-haspopup="dialog" aria-controls="tix-announcement">Meet Tix</button>
</main>
<dialog id="tix-announcement" class="announcement" aria-labelledby="popup-heading" aria-describedby="popup-body">
 <button id="close-announcement" class="close" type="button" aria-label="__CLOSE_LABEL__"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg></button>
 <div class="popup-scroll">
  <figure class="graphic">__GRAPHIC__</figure>
  <div class="content">
   <p class="eyebrow">__EYEBROW__</p>
   <h2 id="popup-heading" tabindex="-1">__HEADLINE__</h2>
   <p id="popup-body" class="body-copy">__BODY__</p>
   <div class="actions">
    <a class="cta" href="__CTA_URL__" target="_blank" rel="noopener noreferrer"><span>__CTA__</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6"/></svg></a>
    <button id="dismiss-announcement" class="dismiss" type="button">__DISMISSAL__</button>
   </div>
  </div>
 </div>
</dialog>
<script>
(() => {
  const popup = document.querySelector('#tix-announcement');
  const opener = document.querySelector('#open-announcement');
  const heading = document.querySelector('#popup-heading');
  const embedded = window.self !== window.top;
  let returnFocus = opener;
  document.body.classList.toggle('embedded', embedded);

  function openAnnouncement(moveFocus = true) {
    if (popup.open) return;
    const active = document.activeElement;
    returnFocus = active instanceof HTMLElement && active !== document.body ? active : opener;
    popup.setAttribute('aria-modal', String(!embedded));
    // Native show() autofocuses even when moveFocus is false. An inline frame
    // uses the open attribute so opening the review cannot move parent focus.
    if (embedded) popup.setAttribute('open', ''); else popup.showModal();
    document.body.classList.add('is-open');
    popup.querySelector('.popup-scroll').scrollTop = 0;
    if (moveFocus) heading.focus({preventScroll:true});
  }

  function closeAnnouncement() {
    if (popup.open) popup.close();
  }

  opener.addEventListener('click', () => openAnnouncement());
  document.querySelector('#close-announcement').addEventListener('click', closeAnnouncement);
  document.querySelector('#dismiss-announcement').addEventListener('click', closeAnnouncement);
  popup.addEventListener('close', () => {
    document.body.classList.remove('is-open');
    if (returnFocus.isConnected) returnFocus.focus({preventScroll:true});
  });
  popup.addEventListener('cancel', event => { event.preventDefault(); closeAnnouncement(); });
  popup.addEventListener('click', event => {
    if (embedded || event.target !== popup) return;
    const rect = popup.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) closeAnnouncement();
  });
  document.addEventListener('keydown', event => {
    if (!popup.open) return;
    if (event.key === 'Escape') { event.preventDefault(); closeAnnouncement(); return; }
    if (embedded || event.key !== 'Tab') return;
    const controls = [...popup.querySelectorAll('button:not([disabled]),a[href]')];
    const first = controls[0], last = controls[controls.length - 1];
    if (event.shiftKey && (document.activeElement === first || document.activeElement === heading)) {
      event.preventDefault(); last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault(); first.focus();
    }
  });
  // Opening this file is an explicit preview. Embedded previews remain inline
  // and do not take focus from the parent review page.
  openAnnouncement(!embedded);
})();
</script>
</body>
</html>
'''

replacements = {
    "__REGULAR__": regular, "__SEMIBOLD__": semibold, "__GRAPHIC__": graphic,
    "__POPPINS_LICENSE__": poppins_license, "__INTER_LICENSE__": inter_license,
    "__CLOSE_LABEL__": html.escape(c["close_label"], quote=True),
    "__EYEBROW__": html.escape(c["eyebrow"]), "__HEADLINE__": html.escape(c["headline"]),
    "__BODY__": html.escape(c["body"]), "__CTA_URL__": html.escape(c["cta_url"], quote=True),
    "__CTA__": html.escape(c["cta"]), "__DISMISSAL__": html.escape(c["dismissal"]),
}
for key, value in replacements.items():
    template = template.replace(key, value)
(ROOT / "popup.html").write_text(template)

(ROOT / "copy.md").write_text(
    "# Tix in-app popup\n\nVersion 1. Draft for Gabe’s review. Publisher: Tixmancer.\n\n"
    f"**{c['eyebrow']}**\n\n## {c['headline']}\n\n{c['body']}\n\n"
    f"[{c['cta']}]({c['cta_url']})\n\n{c['dismissal']}\n\n"
    "---\n\nGraphic: [graphic.svg](graphic.svg). Preview: [popup.html](popup.html).\n\n"
    f"Alt text: {copy['graphic']['alt']}\n\n"
    "Claims: TIX-C01 and TIX-C02 support the conversation positioning. TIX-C08 supports the canonical domain. The buyer’s Sony/Brooklyn/$950 brief comes from the accepted campaign scenario.\n\n"
    "Vista supplies the selected design/expression reference. Product facts and publisher identity belong to Tixmancer. Review metadata, source qualifiers and the destination check are recorded in copy.json.\n"
)

outputs = ["copy.json", "copy.md", "graphic.svg", "popup.html"]
manifest = {name: {"sha256": hashlib.sha256((ROOT/name).read_bytes()).hexdigest(), "bytes": (ROOT/name).stat().st_size} for name in outputs}
(ROOT / "artifact-hashes.json").write_text(json.dumps({"artifact_id":copy["artifact_id"],"version":copy["version"],"files":manifest},indent=2)+"\n")
print(json.dumps(manifest,indent=2))
