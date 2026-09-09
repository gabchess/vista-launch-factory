#!/usr/bin/env python3
"""Build the bounded public-source Vista Work demonstration package.

This script makes a local, reviewable package. It does not publish, send,
call a paid provider, or grant Barry approval. The generated motion is a
documentary concept preview because no private Vista footage was supplied.
"""
from __future__ import annotations

import csv
import hashlib
import html
import json
import shutil
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "packages" / "camp_vista_work_public_001"
FIX = REPO / "engine" / "fixtures" / "vista-work"
OLD = REPO / "packages" / "camp_vista_work_001"
FONT = "/System/Library/Fonts/SFNS.ttf"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path: Path, content: str | bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        path.write_bytes(content)
    else:
        path.write_text(content, encoding="utf-8")


def copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def markdown_html(title: str, md: str, label: str | None = None, footer: str | None = None) -> str:
    blocks = []
    for raw in md.split("\n"):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            level = min(len(line) - len(line.lstrip("#")), 3)
            blocks.append(f"<h{level}>{html.escape(line[level:].strip())}</h{level}>")
        elif line.startswith("**") and line.endswith("**"):
            blocks.append(f"<p><strong>{html.escape(line.strip('*'))}</strong></p>")
        elif line.startswith("-"):
            blocks.append(f"<li>{html.escape(line[1:].strip())}</li>")
        elif line.startswith("|"):
            continue
        else:
            blocks.append(f"<p>{html.escape(line)}</p>")
    label_html = f"<div class='label'>{html.escape(label.upper())}</div>" if label else ""
    footer_html = f"<p style='font-size:12px;color:#6c7b90'>{html.escape(footer)}</p>" if footer else ""
    return f"""<!doctype html><html lang='en'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>{html.escape(title)}</title>
<style>body{{margin:0;background:#f5f7fb;color:#12213a;font:16px/1.7 -apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif}}article{{max-width:820px;margin:32px auto;padding:42px;background:#fff;border:1px solid #dbe4f1;border-radius:18px}}.label{{color:#0052ff;font-size:12px;font-weight:700;letter-spacing:1.3px}}h1{{font-size:40px;line-height:1.12;letter-spacing:-1.5px}}h2{{font-size:26px;line-height:1.2;margin-top:34px}}p{{margin:20px 0}}li{{margin:10px 0}}a{{color:#0052ff;font-weight:700}}@media(max-width:700px){{article{{margin:0;padding:24px;border:0;border-radius:0}}h1{{font-size:31px}}}}</style></head>
<body><article>{label_html}{''.join(blocks)}
<p><a href='https://vistasocial.com/work/'>Open Vista Work →</a></p>
{footer_html}</article></body></html>"""


def email_html(subject: str, preheader: str, body: str, cta_label: str, cta_url: str) -> str:
    paragraphs = "".join(f"<p>{html.escape(p.strip())}</p>" for p in body.split("\n\n") if p.strip())
    return f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{html.escape(subject)}</title>
<style>body{{margin:0;background:#f5f7fb;font:16px/1.7 -apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif;color:#12213a}}main{{max-width:620px;margin:30px auto;background:#fff;border-radius:16px;border:1px solid #dae4f2;overflow:hidden}}header{{background:#0052ff;color:#fff;padding:25px 30px;font-size:26px;font-weight:700}}section{{padding:30px}}h1{{font-size:27px;line-height:1.2}}a{{display:inline-block;padding:13px 19px;background:#0052ff;color:#fff;border-radius:6px;text-decoration:none;font-weight:700}}.note{{font-size:12px;color:#6c7b90}}</style></head>
<body><div style='display:none;max-height:0;overflow:hidden'>{html.escape(preheader)}</div><main><header>Vista Social</header><section><h1>{html.escape(subject)}</h1>{paragraphs}<p><a href='{html.escape(cta_url)}'>{html.escape(cta_label)} →</a></p></section></main></body></html>"""


def clean_blog(source: str) -> str:
    body = source.split("## Draft", 1)[1].split("\n---\n\n## Claim map", 1)[0].strip()
    lines = body.splitlines()
    first_heading = True
    cleaned = []
    for line in lines:
        if line.startswith("### "):
            cleaned.append(("# " if first_heading else "## ") + line[4:])
            first_heading = False
        else:
            cleaned.append(line)
    text = "\n".join(cleaned)
    text = text.replace(
        "That is different from a generic approval workflow story. Approvals (who must sign, in what order, before something goes live) can still matter as a publishing path. Vista Work’s job in this story is narrower and more practical: keep the work about the post next to the post, so the review starts with the asset, not with a scavenger hunt. Do not collapse those into one product name. Related collaboration story. Different job.",
        "Vista Work keeps the work about the post next to the post, so review starts with the asset instead of a scavenger hunt. Publishing approvals can still define who signs off and when.",
    )
    text = text.replace(
        "Humans still keep the gate. AI may help tidy or triage task admin. Approvals and strategy stay with people. Nothing in this draft claims auto-publish, and nothing claims a zero-edit pass. The bar is simpler: stop making the human pay a search tax before they can do the job they were asked to do.",
        "Humans still keep the gate. Review should begin with the post and its context in view.",
    )
    text = text.replace(
        "One workspace. One login. One source of truth for “what am I approving?” That is enough for this page.",
        "One place to look for “what am I approving?” That is enough for this page.",
    )
    text = text.replace(
        "Boards, shortcuts, and automations can live in how-tos and changelogs.",
        "Other product details can live in how-tos and changelogs.",
    )
    return text.rstrip() + "\n"


def clean_email_sections(source: str, segments: list[tuple[str, str, str]]) -> dict[str, str]:
    result = {}
    for index, (ident, _label, source_heading) in enumerate(segments):
        marker = f"## {source_heading}"
        start = source.index(marker) + len(marker)
        if index + 1 < len(segments):
            next_marker = f"## {segments[index + 1][2]}"
            end = source.index(next_marker, start)
        else:
            end = len(source)
        body = source[start:end].strip().strip("-").strip()
        body = body.split("\n## Still needs human", 1)[0].strip()
        body = body.split("\n**Claims:**", 1)[0].strip()
        if body.startswith("**Note:**"):
            body = body.split("\n\n", 1)[1].strip()
        result[ident] = body.rstrip() + "\n"
    return result


def create_motion(path: Path, duration: int, size: str, mode: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if mode == "social":
        vf = (
            "drawtext=fontfile=/System/Library/Fonts/SFNS.ttf:text='VISTA WORK':fontcolor=white:fontsize=58:x=(w-text_w)/2:y=120:enable='between(t,0,2)',"
            "drawtext=fontfile=/System/Library/Fonts/SFNS.ttf:text='Approve the next post':fontcolor=white:fontsize=58:x=(w-text_w)/2:y=280:enable='between(t,1,4)',"
            "drawtext=fontfile=/System/Library/Fonts/SFNS.ttf:text='Which one?':fontcolor=white:fontsize=72:x=(w-text_w)/2:y=410:enable='between(t,3,6)',"
            "drawtext=fontfile=/System/Library/Fonts/SFNS.ttf:text='Open the task. See the actual post.':fontcolor=white:fontsize=42:x=(w-text_w)/2:y=560:enable='between(t,5,9)',"
            "drawtext=fontfile=/System/Library/Fonts/SFNS.ttf:text='Open Vista Work':fontcolor=white:fontsize=78:x=(w-text_w)/2:y=780:enable='between(t,8,12)',"
            "drawtext=fontfile=/System/Library/Fonts/SFNS.ttf:text='CONCEPT PREVIEW · PUBLIC SOURCE':fontcolor=white@0.78:fontsize=30:x=(w-text_w)/2:y=h-90"
        )
        bg = "color=c=0x0052ff:s=1080x1920:r=30"
    else:
        vf = (
            "drawtext=fontfile=/System/Library/Fonts/SFNS.ttf:text='VISTA WORK':fontcolor=white:fontsize=68:x=(w-text_w)/2:y=240:enable='between(t,0,2)',"
            "drawtext=fontfile=/System/Library/Fonts/SFNS.ttf:text='Tasks linked to social posts':fontcolor=white:fontsize=54:x=(w-text_w)/2:y=420:enable='between(t,1,5)',"
            "drawtext=fontfile=/System/Library/Fonts/SFNS.ttf:text='A clearer place to review':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=610:enable='between(t,4,8)',"
            "drawtext=fontfile=/System/Library/Fonts/SFNS.ttf:text='CONCEPT PREVIEW':fontcolor=white@0.72:fontsize=26:x=(w-text_w)/2:y=h-90"
        )
        bg = "color=c=0x0052ff:s=1920x1080:r=30"
    cmd = ["ffmpeg", "-y", "-f", "lavfi", "-i", bg, "-t", str(duration), "-vf", vf,
           "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(path)]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    now = datetime.now(timezone.utc).isoformat()
    for directory in ("sources", "claims", "voice", "requests", "events", "jobs", "costs", "artifacts/social", "artifacts/login", "artifacts/popup", "reviews", "campaign"):
        (OUT / directory).mkdir(parents=True, exist_ok=True)

    # Source capture. The HTML is a public snapshot; fixture text preserves
    # the supplied problem statement and exact claim spans.
    copy(FIX / "sources/barry_email_transcript.txt", OUT / "sources/barry_email_transcript.txt")
    copy(FIX / "sources/vista_work_outline.md", OUT / "sources/vista_work_outline.md")
    try:
        request = urllib.request.Request("https://vistasocial.com/insights/vista-work-social-media-project-management/", headers={"User-Agent": "LaunchFactory-local-source-capture/1.0"})
        page = urllib.request.urlopen(request, timeout=30).read()
    except Exception as exc:
        page = f"Public source capture failed locally: {exc}\nUse the URL in source-manifest.json for retrieval.".encode()
    write(OUT / "sources/vista-work-insights.html", page)
    source_types = {
        "barry_email_transcript.txt": "supplied_email_source_text",
        "vista_work_outline.md": "repository_source_text",
        "vista-work-insights.html": "public_web_capture",
    }
    source_rows = []
    for source in sorted((OUT / "sources").iterdir()):
        source_rows.append({"path": str(source.relative_to(OUT)), "source_type": source_types[source.name], "sha256": digest(source), "bytes": source.stat().st_size, "retrieved_at": now})
    write(OUT / "source-manifest.json", json.dumps({"schema_version": "source-manifest/v1", "captured_at": now, "urls": [
        "https://vistasocial.com/insights/vista-work-social-media-project-management/",
        "https://support.vistasocial.com/hc/en-us/articles/54580849305243-Linking-Vista-Work-tasks-to-the-rest-of-Vista-Social",
        "https://support.vistasocial.com/hc/en-us/articles/54580761228699-Getting-started-with-Vista-Work"
    ], "files": source_rows, "retrieval_note": "The public Insights page was captured as bytes. Support URLs were retained as source URLs because their anti-bot response did not yield stable HTML in this local capture."}, indent=2) + "\n")
    claim_ledger = json.loads((FIX / "claim_ledger.json").read_text())
    claim_ledger["campaign_id"] = "camp_vista_work_public_001"
    for evidence in claim_ledger["evidence"]:
        if evidence["path"] == "sources/barry_email_transcript.txt":
            evidence["source"] = "supplied_email_source_text"
            evidence["source_label"] = "Supplied Barry email source text"
        elif evidence["path"] == "sources/vista_work_outline.md":
            evidence["source"] = "repository_source_text"
            evidence["source_label"] = "Repository source text with no captured GitHub URL"
    # The public capture supplies direct evidence for the linked-task and
    # sidebar claims. Barry's supplied text remains an expression seed and
    # keeps the narrower wording where the public article does not match it.
    public_text = page.decode("utf-8", errors="replace")
    public_evidence = [
        ("vw1", "Every task links to the post, inbox conversation, review, report, listener, or automation behind it.", "Every task links to the post, inbox conversation, review, report, listener, or automation behind it."),
        ("vw3", "Click a task, land on the source. No hunting.", "Click a task, land on the source. No hunting."),
        ("vw3", "Access it from the Work menu in your sidebar.", "Access it from the Work menu in your sidebar."),
    ]
    for claim_id, needle, quote in public_evidence:
        start = public_text.find(needle)
        if start >= 0:
            claim_ledger["evidence"].append({
                "claim_id": claim_id,
                "source": "public_web_capture",
                "source_label": "Captured Vista Social Insights page",
                "path": "sources/vista-work-insights.html",
                "span_start": start,
                "span_end": start + len(needle),
                "quote": quote,
            })
    write(OUT / "claims/claim-ledger.json", json.dumps(claim_ledger, indent=2, ensure_ascii=False) + "\n")
    write(OUT / "voice/barry-seed.md", "# Barry expression seed\n\nOne attributed email-style sample was supplied for this Vista Work package. Its use in the voice lane is limited to expression, including register and sentence rhythm. The voice projection supplies no product facts, approval or client authority.\n")
    write(OUT / "voice/public-vista-work.md", "# Public Vista Work voice context\n\nThe selected public material uses a direct product explanation, short headings and practical task language. This is a provisional public-source voice brief.\n")

    # Separate consumer copy from its provenance and review metadata.
    source_blog = (OLD / "02_blog/02_blog.md").read_text()
    blog_md = clean_blog(source_blog)
    write(OUT / "artifacts/blog.md", blog_md)
    write(OUT / "artifacts/blog.html", markdown_html("Approve the next post does not tell you which one", blog_md, "Vista Work"))
    email_text = (OLD / "03_email_segments/03_email_segments.md").read_text()
    segments = [("lead_smb", "Leads · SMB", "Leads, SMB"), ("lead_agency", "Leads · Agency", "Leads, Agency"), ("lead_reseller_affiliate", "Leads · Reseller / Affiliate", "Leads, Reseller / Affiliate"), ("customer_smb", "Customers · SMB", "Customers, SMB"), ("customer_agency", "Customers · Agency", "Customers, Agency")]
    clean_emails = clean_email_sections(email_text, segments)
    email_variants = {
        "lead_smb": ("Keep the post with the approval task", "See the social content where the decision happens.", "Your next approval should begin with the post in view.", "Learn more", "https://vistasocial.com/insights/vista-work-social-media-project-management/"),
        "lead_agency": ("Give every client approver the post in context", "Vista Work links social content to the task behind the review.", "Your team handles many client decisions. Each one needs the current post and its context.", "Learn more", "https://vistasocial.com/insights/vista-work-social-media-project-management/"),
        "lead_reseller_affiliate": ("Show the post behind each review task", "Keep social content and approval context in one workspace.", "A clear review starts when the task points to the exact social post.", "Learn more", "https://vistasocial.com/insights/vista-work-social-media-project-management/"),
        "customer_smb": ("Review your next post inside Vista Work", "Open the task and see the social content that needs a decision.", "Your Vista Work task can keep the next social review in one place.", "Open Vista Work", "https://vistasocial.com/work/"),
        "customer_agency": ("Move client reviews into Vista Work", "Give approvers the post and task context together.", "Your client review queue works better when each task carries its social post.", "Open Vista Work", "https://vistasocial.com/work/"),
    }
    email_dir = OUT / "artifacts/emails"
    email_dir.mkdir(parents=True, exist_ok=True)
    bundle = ["# Vista Work email announcements", ""]
    for ident, label, source_heading in segments:
        body = clean_emails[ident]
        subject, preheader, intro, cta_label, cta_url = email_variants[ident]
        body = intro + "\n\n" + body
        body = body.replace("\n\nOpen Vista Work →", "").replace("\nOpen Vista Work →", "")
        cta_line = f"{cta_label} →"
        write(email_dir / f"{ident}.md", f"# {subject}\n\n**Preheader:** {preheader}\n\n{body}\n\n{cta_line}\n")
        html_body = body.strip()
        write(email_dir / f"{ident}.html", email_html(subject, preheader, html_body, cta_label, cta_url))
        bundle.extend([f"## {label}", "", f"**Subject:** {subject}", f"**Preheader:** {preheader}", "", body.rstrip(), "", cta_line, ""])
    write(OUT / "artifacts/email_segments.md", "\n".join(bundle).rstrip() + "\n")

    changelog_body = """Approval queues often show a task that only says “Approve the next post.” Finding the real post and context can take longer than the decision itself.

## What’s new

- In Vista Work, the task and social posts are linked.
- Opening a Vista Work task shows the actual post content, not a card describing it.
- Approvers can see what needs a decision instead of hunting for the post first.
"""
    changelog_v1 = "# Vista Work, tasks linked to social posts\n\n" + changelog_body
    changelog_v2 = "# Vista Work: see the post behind the task\n\n" + changelog_body
    write(OUT / "artifacts/changelog.md", changelog_v1)
    write(OUT / "artifacts/changelog-v2.md", changelog_v2)
    write(OUT / "artifacts/changelog.html", markdown_html("Vista Work: see the post behind the task", changelog_v2, "Vista Work"))

    # Concept media, explicitly labelled because no private UI footage exists.
    create_motion(OUT / "artifacts/social/vista-work-social-concept.mp4", 12, "1080x1920", "social")
    create_motion(OUT / "artifacts/login/vista-work-login-concept.mp4", 8, "1920x1080", "login")
    write(OUT / "artifacts/social/storyboard.md", "# Social video storyboard\n\nA low-production, text-led documentary concept based on the public Vista Work source. It shows the approval-queue question, the linked task/post mechanism and a review CTA. No private UI or human recording was supplied.\n")
    write(OUT / "artifacts/login/README.md", "# Login animation concept\n\nA muted 8-second concept preview for the Vista login surface. It is a public-source motion study, not an observed production login recording. Add responsive placement and reduced-motion fallback before implementation.\n")

    popup_svg = """<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='720' viewBox='0 0 1200 720'><rect width='1200' height='720' rx='32' fill='#f4f7fc'/><rect x='100' y='75' width='1000' height='570' rx='24' fill='white' stroke='#d9e3f2' stroke-width='3'/><rect x='100' y='75' width='1000' height='110' rx='24' fill='#0052ff'/><text x='155' y='145' font-family='Arial' font-size='40' font-weight='700' fill='white'>Vista Work</text><text x='155' y='270' font-family='Arial' font-size='42' font-weight='700' fill='#12213a'>See the post behind the task.</text><text x='155' y='340' font-family='Arial' font-size='27' fill='#536278'>Open a task and review the linked social content</text><text x='155' y='385' font-family='Arial' font-size='27' fill='#536278'>in the same place.</text><rect x='155' y='470' width='310' height='68' rx='10' fill='#0052ff'/><text x='220' y='514' font-family='Arial' font-size='25' font-weight='700' fill='white'>Open Vista Work</text><text x='155' y='585' font-family='Arial' font-size='20' fill='#8290a5'>CONCEPT PREVIEW · BARRY REVIEW PENDING</text></svg>"""
    write(OUT / "artifacts/popup/vista-work-popup.svg", popup_svg)
    write(OUT / "artifacts/popup/copy.md", "# In-app popup\n\n**Headline:** See the post behind the task.\n\n**Body:** Open a task and review the linked social content in the same place.\n\n**CTA:** Open Vista Work\n\nConcept preview based on the public claim ledger. Receiving-app targeting, placement and Barry approval remain pending.\n")
    write(OUT / "artifacts/popup/preview.html", """<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Vista Work popup concept</title>
<style>body{margin:0;background:#f4f7fc;color:#12213a;font:16px/1.5 -apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif}main{max-width:880px;margin:42px auto;padding:32px;background:#fff;border:1px solid #d9e3f2;border-radius:18px}button{border:0;border-radius:8px;padding:12px 18px;background:#0052ff;color:#fff;font-weight:700;cursor:pointer}dialog{border:0;border-radius:18px;padding:0;max-width:min(92vw,720px);box-shadow:0 24px 70px #12213a55}dialog::backdrop{background:#12213a99}.dialog-inner{position:relative;padding:24px;background:#fff}.dialog-inner img{display:block;width:100%;height:auto}.close{position:absolute;right:10px;top:10px;background:#12213a;color:#fff;border-radius:50%;width:34px;height:34px;padding:0}.note{color:#61718a;font-size:13px}</style></head><body><main><h1>Vista Work in-app popup</h1><p>Local interaction preview using the generated popup graphic and copy.</p><button id='open' type='button'>Open popup preview</button><p class='note'>Concept preview. Host targeting, persistence and Barry approval remain pending.</p></main><dialog id='popup' aria-labelledby='popup-title'><div class='dialog-inner'><button class='close' id='close' type='button' aria-label='Close popup'>×</button><h2 id='popup-title' style='position:absolute;left:-9999px'>See the post behind the task</h2><img src='vista-work-popup.svg' alt='Vista Work popup concept: see the post behind the task'></div></dialog><script>const dialog=document.getElementById('popup');const open=document.getElementById('open');const close=document.getElementById('close');open.addEventListener('click',()=>{dialog.showModal();close.focus()});close.addEventListener('click',()=>dialog.close());dialog.addEventListener('click',e=>{if(e.target===dialog)dialog.close()});dialog.addEventListener('keydown',e=>{if(e.key==='Escape')dialog.close()});</script></body></html>""")

    social_copy = {
        "linkedin-v1": ("artifacts/social/linkedin.md", "# LinkedIn\n\nAn approval task that says “Approve the next post” leaves the reviewer searching for the post and its context. Vista Work links tasks to social posts, so the post is visible where the decision happens.\n\nOpen Vista Work →\n"),
        "x-v1": ("artifacts/social/x.md", "# X\n\nAn approval task should include the post. Vista Work links the task and social content so reviewers can decide with context in view.\n\nOpen Vista Work →\n"),
        "threads-v1": ("artifacts/social/threads.md", "# Threads\n\nWhen the approval task includes the social post, review starts with the work in view. Vista Work links tasks to social content in one place.\n\nOpen Vista Work →\n"),
        "tiktok-v1": ("artifacts/social/tiktok.md", "# TikTok caption\n\nThe task says approve the next post. Vista Work shows the post behind the task, so the reviewer can decide with context in view.\n\nOpen Vista Work →\n"),
    }
    for _asset_id, (path, content) in social_copy.items():
        write(OUT / path, content)
    asset_index = {
        "blog-v1": "artifacts/blog.html",
        "email-lead-smb-v1": "artifacts/emails/lead_smb.html",
        "email-lead-agency-v1": "artifacts/emails/lead_agency.html",
        "email-lead-reseller-affiliate-v1": "artifacts/emails/lead_reseller_affiliate.html",
        "email-customer-smb-v1": "artifacts/emails/customer_smb.html",
        "email-customer-agency-v1": "artifacts/emails/customer_agency.html",
        "changelog-v2": "artifacts/changelog.html",
        **{asset_id: path for asset_id, (path, _content) in social_copy.items()},
        "social-video-v1": "artifacts/social/vista-work-social-concept.mp4",
        "login-animation-v1": "artifacts/login/vista-work-login-concept.mp4",
        "popup-v1": "artifacts/popup/preview.html",
    }
    row_specs = [
        ["1", "blog", "all social managers", "blog-v1", "read linked-task story", "delegated_review_pending_barry"],
        ["1", "email", "lead_smb", "email-lead-smb-v1", "open Vista Work", "delegated_review_pending_barry"],
        ["1", "email", "lead_agency", "email-lead-agency-v1", "open Vista Work", "delegated_review_pending_barry"],
        ["1", "email", "lead_reseller_affiliate", "email-lead-reseller-affiliate-v1", "open Vista Work", "legal_context_pending"],
        ["2", "email", "customer_smb", "email-customer-smb-v1", "review a task", "delegated_review_pending_barry"],
        ["2", "email", "customer_agency", "email-customer-agency-v1", "review a task", "delegated_review_pending_barry"],
        ["2", "changelog", "existing users", "changelog-v2", "read what changed", "delegated_review_pending_barry"],
        ["2", "linkedin", "social directors", "linkedin-v1", "open Vista Work", "delegated_review_pending_barry"],
        ["2", "x", "social teams", "x-v1", "open Vista Work", "delegated_review_pending_barry"],
        ["2", "threads", "social teams", "threads-v1", "open Vista Work", "delegated_review_pending_barry"],
        ["2", "tiktok", "social teams", "tiktok-v1", "see review workflow", "delegated_review_pending_barry"],
        ["2", "instagram", "social teams", "social-video-v1", "see review workflow", "concept_preview_pending_barry"],
        ["2", "login", "returning users", "login-animation-v1", "open login", "concept_preview_pending_barry"],
        ["2", "in_app", "active users", "popup-v1", "open Vista Work", "concept_preview_pending_barry"],
    ]
    calendar_rows = [["week", "proposed_day", "order", "timezone", "channel", "audience", "asset_id", "asset_path", "action", "review_state"]]
    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    for order, (week, channel, audience, asset_id, action, review_state) in enumerate(row_specs, 1):
        proposed_day = f"{day_names[(order - 1) % len(day_names)]} (proposed)"
        calendar_rows.append([week, proposed_day, str(order), "America/Sao_Paulo", channel, audience, asset_id, asset_index[asset_id], action, review_state])
    with (OUT / "campaign/calendar.csv").open("w", newline="") as fh:
        csv.writer(fh).writerows(calendar_rows)
    write(OUT / "campaign/calendar.json", json.dumps({"schema_version": "campaign-calendar/v1", "campaign_id": "camp_vista_work_public_001", "weeks": 2, "timezone": "America/Sao_Paulo", "scheduled": False, "asset_index": asset_index, "rows": [dict(zip(calendar_rows[0], row)) for row in calendar_rows[1:]], "source": "one public Vista Work source pack", "tracking": "UTM values remain proposed; no channel has been scheduled."}, indent=2) + "\n")

    write(OUT / "requests/run-brief.md", "# Local run brief\n\nProduct: Vista Work. Audience: in-house social media managers and directors at mid-market brands. Problem: approval tasks lack the actual post and context. Reviewer: delegated AgentsKit marketing reviewer for this overnight demo; Barry remains the client approval seat. Mode: local-assisted.\n")
    write(OUT / "events/events.jsonl", json.dumps({"event": "local_package_built", "at": now, "paid_provider_call": False, "route": "local-script-plus-existing-source-bound-drafts"}) + "\n")
    write(OUT / "jobs/jobs.json", json.dumps({"jobs": [{"id": "local-copy-001", "state": "completed", "provider": "local-harness", "paid": False}, {"id": "local-media-001", "state": "completed", "provider": "ffmpeg-local", "paid": False}]} , indent=2) + "\n")
    write(OUT / "costs/costs.json", json.dumps({"currency": "USD", "incremental_paid_calls_this_run": 0, "observed_usd_this_run": 0, "prior_observed_usd": 0.235, "prior_provider_credit_usd_unknown": True, "ceiling_usd": 500, "note": "Existing provider receipts include unknown later charges. No new paid generation was requested in this local build."}, indent=2) + "\n")

    # One provisional review and a focused revision record. This records the
    # delegated reviewer, never a Barry approval.
    write(OUT / "reviews/delegated-marketing-review-v1.json", json.dumps({"schema_version": "delegated-review/v1", "reviewer": "AgentsKit executing-marketing-campaigns", "roleplay_subject": "Barry", "authority": "Gabe-delegated provisional demo review", "barry_approval": "pending", "verdict": "recommend_review", "findings": ["Make the changelog title more direct", "Keep all three concept previews visibly labelled", "Preserve the five segment actions"], "at": now}, indent=2) + "\n")
    write(OUT / "reviews/revision-v2.json", json.dumps({"asset": "changelog", "from": "v1", "to": "v2", "feedback": "Make the changelog title more direct", "reviewer": "AgentsKit delegated provisional reviewer", "barry_approval": "pending", "changed_file": "artifacts/changelog-v2.md", "before_sha256": digest(OUT / "artifacts/changelog.md"), "after_sha256": digest(OUT / "artifacts/changelog-v2.md"), "rendered_sha256": digest(OUT / "artifacts/changelog.html")}, indent=2) + "\n")

    write(OUT / "recording-pending.md", "# Recording checklist\n\nThe retained screen recording is pending Gabe's manual walkthrough. The package contains no fake recording receipt.\n\nRecord the local `review.html` page, open the source/run brief, review the blog, five email variants, changelog, concept media and popup, open the campaign calendar, show the delegated review and revision record, then end with Barry approval pending and publishing disabled.\n")

    review_cards = [
        ("Blog", "artifacts/blog.html"),
        ("Email · lead SMB", "artifacts/emails/lead_smb.html"),
        ("Email · lead agency", "artifacts/emails/lead_agency.html"),
        ("Email · lead reseller / affiliate", "artifacts/emails/lead_reseller_affiliate.html"),
        ("Email · customer SMB", "artifacts/emails/customer_smb.html"),
        ("Email · customer agency", "artifacts/emails/customer_agency.html"),
        ("Email source bundle", "artifacts/email_segments.md"),
        ("Changelog v2", "artifacts/changelog.html"),
        ("LinkedIn draft", "artifacts/social/linkedin.md"),
        ("X draft", "artifacts/social/x.md"),
        ("Threads draft", "artifacts/social/threads.md"),
        ("TikTok draft", "artifacts/social/tiktok.md"),
        ("Social video concept", "artifacts/social/vista-work-social-concept.mp4"),
        ("Login animation concept", "artifacts/login/vista-work-login-concept.mp4"),
        ("In-app popup concept", "artifacts/popup/preview.html"),
        ("Campaign calendar", "campaign/calendar.csv"),
        ("Revision record", "reviews/revision-v2.json"),
        ("Recording checklist", "recording-pending.md"),
    ]
    cards = "".join(f"<li><a href='{html.escape(path)}'>{html.escape(label)}</a><span> · delegated review provisional; Barry pending</span></li>" for label, path in review_cards)
    write(OUT / "review.html", f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Vista Work local review</title><style>body{{margin:0;background:#f5f7fb;color:#14233c;font:16px/1.6 -apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif}}main{{max-width:820px;margin:40px auto;padding:36px;background:#fff;border:1px solid #dae4f2;border-radius:18px}}h1{{margin-top:0;color:#0052ff}}li{{margin:14px 0}}a{{color:#0052ff;font-weight:700}}span{{color:#718098;font-size:13px}}</style></head><body><main><h1>Vista Work · local review package</h1><p>One public-source run with seven output groups and a two-week campaign. Media marked concept preview uses local documentary motion because private UI footage was not supplied.</p><p><strong>Barry approval: pending.</strong> Nothing sends, schedules or publishes.</p><ul>{cards}</ul><p><a href='RUN.md'>Run record</a> · <a href='source-manifest.json'>Source manifest</a> · <a href='export-manifest.json'>Export manifest</a></p></main></body></html>""")
    write(OUT / "README.md", "# camp_vista_work_public_001\n\nLocal review bundle for the public Vista Work source. Open `review.html` first. This package contains a blog, five email segments, a changelog, social and login concept previews, a popup concept and a two-week calendar. The media is explicitly documentary/concept work because no private Vista footage was supplied. Barry approval and publication are pending.\n")
    write(OUT / "reviews/local-verification.md", "# Local verification receipt\n\nThe package builder ran locally with no paid provider calls. `verify_public_demo.py` checks the run status, three source hashes, public claim evidence, five distinct email subjects and bodies with preheaders, both H.264 media files, the accessible popup interaction, campaign channel and planning fields, every review link, the delegated revision hashes, the cost boundary, the no-publish boundary and every export hash. A delegated AgentsKit marketing reviewer supplied provisional copy feedback. Barry approval remains pending.\n")

    records = []
    for path in sorted(p for p in OUT.rglob("*") if p.is_file() and p.name not in {"export-manifest.json"}):
        records.append({"path": str(path.relative_to(OUT)), "sha256": digest(path), "bytes": path.stat().st_size})
    write(OUT / "export-manifest.json", json.dumps({"schema_version": "export-manifest/v1", "campaign_id": "camp_vista_work_public_001", "product_id": "vista-work", "human_approval": False, "publishing_authorized": False, "delegated_review": "provisional only", "files": records}, indent=2) + "\n")
    write(OUT / "RUN.md", f"# Vista Work public-source local run\n\nRun ID: camp_vista_work_public_001\nMode: local-assisted\nStarted: {now}\n\nThe run uses the public Vista Work announcement, supplied Barry expression seed and the repository claim ledger. Blog, five email segments, changelog, LinkedIn/X/Threads/TikTok drafts, social concept, login concept, popup concept and a two-week campaign are present. The concept media is documentary motion, created locally from source-backed copy because no private UI footage was supplied.\n\nA delegated AgentsKit marketing review selected one changelog revision for the overnight demonstration. Barry approval remains pending. Nothing is scheduled, sent or published. The retained screen recording is still pending Gabe's manual walkthrough; see `recording-pending.md`.\n\nSee `source-manifest.json`, `reviews/`, `events/`, `costs/`, `campaign/` and `export-manifest.json`.\n")
    write(OUT / "run.json", json.dumps({"schema_version": "local-run/v1", "run_id": "camp_vista_work_public_001", "status": "review_ready_pending_barry", "source_revision": "public-vista-work-2026-09-09", "operator": "Gabe", "reviewer": "AgentsKit delegated provisional reviewer", "barry_approval": "pending", "paid_provider_calls": 0, "outputs": ["blog", "five_emails", "changelog", "social_video", "login_animation", "in_app_popup", "campaign"], "continuation": "Local package can resume from export-manifest and review records."}, indent=2) + "\n")
    # RUN.md and run.json are generated after the first manifest pass. Rebuild
    # the manifest once more so the retained handoff includes their hashes.
    records = []
    for path in sorted(p for p in OUT.rglob("*") if p.is_file() and p.name not in {"export-manifest.json"}):
        records.append({"path": str(path.relative_to(OUT)), "sha256": digest(path), "bytes": path.stat().st_size})
    write(OUT / "export-manifest.json", json.dumps({"schema_version": "export-manifest/v1", "campaign_id": "camp_vista_work_public_001", "product_id": "vista-work", "human_approval": False, "publishing_authorized": False, "delegated_review": "provisional only", "files": records}, indent=2) + "\n")
    print(json.dumps({"package": str(OUT), "files": len(records), "social_sha256": digest(OUT / "artifacts/social/vista-work-social-concept.mp4"), "login_sha256": digest(OUT / "artifacts/login/vista-work-login-concept.mp4"), "paid_calls": 0}, indent=2))


if __name__ == "__main__":
    main()
