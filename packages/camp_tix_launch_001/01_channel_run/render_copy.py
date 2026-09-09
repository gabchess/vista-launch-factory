"""Render the batch's authored JSON into copy files and reviewable HTML.

Run locally with Python 3. No model, ESP or publishing request is made.
"""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent


def e(value):
    return escape(value, quote=True)


def email_html(data, variant):
    paragraphs = ''.join(f'<p style="margin:0 0 20px">{e(p["text"])}</p>' for p in variant['paragraphs'])
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(variant['subject'])}</title></head>
<body style="margin:0;background:#f3f5fa;color:#101010;font-family:Arial,Helvetica,sans-serif">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all">{e(variant['preheader'])}</div>
<table role="presentation" style="width:100%;border-spacing:0"><tr><td style="padding:24px 12px">
<table role="presentation" style="width:100%;max-width:600px;margin:auto;border-spacing:0;background:white;border:1px solid #e1e7ee;border-radius:16px;overflow:hidden">
<tr><td style="padding:28px 32px 22px;background:#0052ff;color:white;font-size:25px;font-weight:bold">Tix<span style="display:block;margin-top:8px;font-weight:normal;font-size:12px;letter-spacing:1px">PRODUCT NOTES</span></td></tr>
<tr><td style="padding:30px 32px;font-size:16px;line-height:1.7"><h1 style="font-size:25px;line-height:1.25;margin:0 0 24px;letter-spacing:-.6px">{e(variant['subject'])}</h1>
<p style="margin:0 0 20px">{e(data['greeting'])}</p>{paragraphs}
<table role="presentation" style="border-spacing:0;margin:26px 0"><tr><td style="border-radius:6px;background:#0063e3"><a href="{e(variant['cta']['url'])}" style="display:inline-block;padding:15px 24px;color:#fff;font-weight:bold;text-decoration:none">{e(variant['cta']['label'])}</a></td></tr></table>
<p style="margin:28px 0 0">{e(data['signoff'])}</p></td></tr></table></td></tr></table>
<!-- ESP sender identity, postal address and unsubscribe footer are configured before a real send. This is a review artifact. -->
</body></html>'''


def main():
    data = json.loads((ROOT/'email/emails.json').read_text())
    for v in data['variants']:
        segment = {key: data[key] for key in ['schema_version', 'product_id', 'campaign_id', 'source_revision', 'version', 'state', 'voice_profile', 'sender_name', 'greeting', 'signoff']}
        segment['version'] = v.get('version', data['version'])
        segment['variant'] = v
        (ROOT/'email'/f"{v['id']}.json").write_text(json.dumps(segment, indent=2, ensure_ascii=False)+'\n')
        md = f"# {v['subject']}\n\nPreheader: {v['preheader']}\n\n{data['greeting']}\n\n"
        md += '\n\n'.join(p['text'] for p in v['paragraphs'])
        md += f"\n\n[{v['cta']['label']}]({v['cta']['url']})\n\n{data['signoff']}\n"
        (ROOT/'email'/f"{v['id']}.md").write_text(md)
        (ROOT/'email'/f"{v['id']}.html").write_text(email_html(data, v))
    d = json.loads((ROOT/'changelog/entry.json').read_text())
    md = f"# {d['title']}\n\n"+'\n\n'.join(p['text'] for p in d['paragraphs'])
    md += f"\n\n[{d['cta']['label']}]({d['cta']['url']})\n"
    (ROOT/'changelog/entry.md').write_text(md)
    body = ''.join(f'<p>{e(p["text"])}</p>' for p in d['paragraphs'])
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(d['title'])}</title>
<style>@font-face{{font-family:Poppins;src:url('../popup/assets/Poppins-Regular.ttf')}}@font-face{{font-family:Poppins;src:url('../popup/assets/Poppins-SemiBold.ttf');font-weight:600}}*{{box-sizing:border-box}}body{{margin:0;background:#f4f6fb;color:#101010;font:16px/1.7 Poppins,Arial,sans-serif}}article{{max-width:780px;margin:24px auto;background:white;padding:42px;border:1px solid #dfe5ef;border-radius:18px}}.label{{color:#0063e3;font-size:12px;font-weight:600;letter-spacing:.8px}}h1{{font-size:32px;line-height:1.25;letter-spacing:-.7px;margin:18px 0 24px}}img{{width:100%;height:auto;border-radius:12px;border:1px solid #edf0f5}}a{{color:#0051b9;font-weight:600}}p{{margin:22px 0}}@media(max-width:600px){{article{{margin:0;padding:24px;border:0;border-radius:0}}h1{{font-size:27px}}}}</style></head>
<body><article><div class="label">TIX / {e(d['category']).upper()}</div><h1>{e(d['title'])}</h1>
<img src="../blog/assets/tix-camera-brief.png" alt="A frame from the approved Tix walkthrough showing a buyer's used-camera brief.">{body}<a href="{e(d['cta']['url'])}">{e(d['cta']['label'])} →</a></article></body></html>'''
    (ROOT/'changelog/entry.html').write_text(html)
    print('Rendered five Markdown/HTML emails and the changelog.')


if __name__ == '__main__':
    main()
