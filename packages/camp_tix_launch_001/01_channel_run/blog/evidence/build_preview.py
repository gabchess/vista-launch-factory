#!/usr/bin/env python3
"""Render this article's small Markdown subset without external dependencies."""
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
metadata = json.loads((ROOT / "metadata.json").read_text())
blocks = (ROOT / "article.md").read_text().strip().split("\n\n")


def inline(value):
    value = html.escape(value)
    value = re.sub(r"\[([^\]]+)\]\((https://[^ )]+)\)", r'<a href="\2">\1</a>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    return re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", value)


body = []
for index, block in enumerate(blocks):
    if block.startswith("# "):
        body.append("<h1>" + inline(block[2:]) + "</h1>")
    elif block.startswith("## "):
        title = block[3:]
        anchor = re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")
        body.append(f'<h2 id="{anchor}">{inline(title)}</h2>')
    elif block.startswith("!["):
        match = re.fullmatch(r"!\[([^\]]+)\]\((assets/[a-z0-9-]+\.png)\)", block)
        if match is None:
            raise ValueError("Image outside the expected local article assets")
        alt, path = match.groups()
        if not (ROOT / path).is_file():
            raise FileNotFoundError(path)
        image_class = "hero" if path == metadata["hero"]["path"] else "product-view"
        body.append(f'<figure class="{image_class}"><img src="{path}" alt="{html.escape(alt, quote=True)}"></figure>')
    elif block.startswith("> "):
        body.append("<blockquote><p>" + inline(block[2:]) + "</p></blockquote>")
    elif block.startswith("*") and block.endswith("*") and not block.startswith("**"):
        body.append('<p class="caption">' + inline(block) + "</p>")
    else:
        class_name = ' class="dek"' if index == 1 else ""
        if index == len(blocks) - 1:
            class_name = ' class="cta"'
        body.append(f"<p{class_name}>" + inline(block) + "</p>")

toc = "".join(f'<a href="#{item["anchor"]}">{html.escape(item["title"])}</a>' for item in metadata["table_of_contents"])
page = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title><meta name="description" content="__DESCRIPTION__">
<style>
:root{color-scheme:light;--blue:#0052ff;--ink:#17222b;--paper:#f7f5f2}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#fff;color:var(--ink);font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.top{border-bottom:1px solid #e7eaed;padding:22px 7%;display:flex;justify-content:space-between;align-items:center;gap:20px}.brand{font-weight:850;letter-spacing:-1px;font-size:25px;color:var(--blue);text-decoration:none}.top span{font-size:13px;color:#64727f}.layout{max-width:1190px;margin:0 auto;display:grid;grid-template-columns:minmax(0,790px) 225px;gap:64px;padding:52px 32px 92px}article{min-width:0}.eyebrow{font-size:12px;text-transform:uppercase;letter-spacing:.12em;font-weight:700;color:var(--blue);margin:0 0 22px}h1{font-size:clamp(32px,4.2vw,52px);line-height:1.09;letter-spacing:-.035em;font-weight:780;margin:0 0 24px}.dek{font-size:21px;line-height:1.5;color:#53626e;margin:0 0 32px}p{font-size:17px;line-height:1.78;margin:0 0 24px}h2{font-size:29px;line-height:1.23;letter-spacing:-.025em;margin:49px 0 19px;scroll-margin-top:26px}figure{margin:32px 0}.hero{background:var(--blue);display:flex;justify-content:center;border-radius:14px;overflow:hidden}.hero img{display:block;width:min(100%,460px);height:auto}.product-view img{display:block;width:100%;height:auto;border:1px solid #e6e8e4;border-radius:10px}.caption{font-size:13px;line-height:1.6;color:#66717a;margin-top:-18px}blockquote{margin:28px 0;padding:21px 27px;border-left:4px solid var(--blue);background:#f1f5ff;border-radius:0 8px 8px 0}blockquote p{font-size:19px;line-height:1.6;margin:0}a{color:var(--blue);text-underline-offset:4px}.cta{padding:26px;background:var(--paper);border-radius:10px;font-size:17px}.cta a{font-weight:750}.cta strong{font-family:ui-monospace,SFMono-Regular,monospace;font-size:15px}aside{padding-top:8px}.sticky{position:sticky;top:24px;border-left:1px solid #e4e8ec;padding-left:24px}.sticky p{font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#71808c;margin-bottom:19px}.sticky a{display:block;color:#52616c;text-decoration:none;font-size:14px;line-height:1.5;margin:0 0 17px}.sticky a:hover{color:var(--blue)}footer{border-top:1px solid #e7eaed;padding:25px 7%;font-size:13px;color:#71808c}@media(max-width:950px){.layout{grid-template-columns:minmax(0,790px);max-width:850px;gap:0;padding:38px 24px 70px}aside{display:none}.top{padding:20px 24px}}@media(max-width:520px){.top span{display:none}.layout{padding:31px 20px 56px}.dek{font-size:19px}p{font-size:16px}h2{font-size:25px}.hero img{width:100%}.cta{padding:19px}.cta strong{display:block;margin-top:10px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}@media print{.top,aside,footer{display:none}.layout{display:block;padding:0;max-width:none}.hero img{max-width:300px}h2{break-after:avoid}figure,blockquote{break-inside:avoid}}
</style></head><body><header class="top"><a class="brand" href="https://tixmancer.xyz/">Tixmancer</a><span>Secondhand finds, in conversation</span></header>
<main class="layout"><article><div class="eyebrow">Product preview · Tixmancer team · __READING__ min read</div>__BODY__</article><aside aria-label="Article contents"><nav class="sticky"><p>On this page</p>__TOC__</nav></aside></main>
<footer>Tixmancer · <a href="https://tixmancer.xyz/">tixmancer.xyz</a></footer></body></html>
"""
page = page.replace("__TITLE__", html.escape(metadata["seo_title"]))
page = page.replace("__DESCRIPTION__", html.escape(metadata["meta_description"], quote=True))
page = page.replace("__READING__", str(metadata["estimated_reading_minutes"]))
page = page.replace("__BODY__", "\n".join(body)).replace("__TOC__", toc)
(ROOT / "article.html").write_text(page)
print(json.dumps({"output": "article.html", "rendered_blocks": len(blocks), "external_scripts": 0, "external_fonts": 0}))
