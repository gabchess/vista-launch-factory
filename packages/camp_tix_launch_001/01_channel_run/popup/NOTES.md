# Popup production notes

Artifact `tix-in-app-popup`, version 1. Draft for Gabe in the combined channel review.

Open [popup.html](popup.html) for the finished preview. It contains its fonts, graphic, styles and interaction code. [graphic.svg](graphic.svg) is the standalone vector artwork. The editable inputs are [copy.json](copy.json), [build.py](build.py) and `assets/`. Run `python3 build.py` from this folder to rebuild the HTML, SVG, Markdown and hashes. It uses only the Python standard library and local assets.

## Role and source binding

The operator performed the `popup_designer` role inline after reading the generated LF popup skill, shared contract, popup bank, AgentsKit popup-CRO skill and the operator’s request/route. This was not a native `lf_popup_designer` agent invocation. The source revision is `27826b0332fd1582108ac0081165a7dd360e7aa6`. The route context digest is in `copy.json`.

The current user instruction authorizes drafts of all missing outputs before one review. No human decision was written into the older baseline or routing records. The source packet’s pending Claims Lock remains visible in review metadata.

The headline and body use `TIX-C01` and `TIX-C02`. The canonical CTA destination uses `TIX-C08`. The graphic uses the accepted buyer brief: a used Sony camera in Brooklyn for less than $950. It shows the request only. The number establishes no product cap, listing price, saving or market value. Product positioning uses building-language in the visible body.

## Design and expression

The selected channel reference is `../voice/popup.md`, derived from an externally observed login page and its public brand-assets page. That login’s Poppins, restrained hierarchy and blue-purple primary action informed the modal. The Tix character, blue and buying conversation give the artwork its product identity. Tixmancer is the publisher.

No feature-announcement popup from the reference source was visually verified. A public article contains a task-dialog image, but only its article and alt text were accessed. The 560px modal, 24px radius, graphic placement and mobile sheet are original design decisions.

The actual CTA uses `#0063E3` to `#884DF5`. This slightly darker purple preserves readable small white text at the gradient endpoint, measured at 4.74:1. The reference site's published palette still records `#8C52FF`. No logo or promotional video from the reference source was copied into the creative.

## Placement and behavior

At desktop, the modal has a 560px maximum width. Artwork is 1000 × 470 SVG, displayed at the available width. Copy padding is 32px; the headline is 34px and body is 15px. The close target is 44 × 44px, with a 52px primary action. Mobile uses 16px outer spacing, 24px copy padding, a 28px heading and 14px body. The content can scroll inside the card while the close control remains visible.

Opening this file is an intentional preview. Standalone it opens a native modal with background dimming. Close, the quiet dismissal and Escape close it; focus returns to the opener. Tab and Shift+Tab remain inside the modal. A backdrop click also dismisses it.

Inside an iframe, the same file displays the card inline without a backdrop. Initial opening sets the dialog's `open` attribute; it avoids the native `show()` autofocus that moved the parent review during root's first browser check. The card is nonmodal, so it does not trap keyboard navigation. Dismissal exposes the opener within the frame. A later live integration can bind opening to a deliberate user action. This draft implements no audience targeting, persistence, analytics or lead submission.

The CTA opens the canonical Tix domain in a new tab with `noopener noreferrer`. Verify its intended waitlist collection path before publication. The consumer surface keeps that implementation check out of its copy.

## Verification

`qa/checks.json` records source hashes, exact claim spans, text-to-graphic matching, SVG parse, JavaScript syntax, embedded-resource checks, color contrast and text advance widths. All static checks pass. The original purple endpoint failure is retained in `qa/checks-initial.json` with the correction recorded in the current receipt.

Root's first in-app-browser inspection found the graphic and copy legible, but the embedded native `show()` call stole focus and moved the outer page. The narrow correction uses the `open` attribute for the inline frame and preserves standalone `showModal()`. Root will retest iframe focus. The research Chrome surface reported an extension UI block, so browser evidence comes from root's existing in-app browser. Screen reader speech and the destination collection flow are untested.

## Asset rights

The Tix mascot is an unchanged authored vector from the accepted Tix film source. Poppins came from the official Google Fonts repository under SIL OFL 1.1; Inter came from the existing accepted local source with its OFL license. Original font files, licenses and SHA-256 receipts are in `assets/` and `asset-provenance.json`. The HTML embeds license text; the SVG includes Inter’s license metadata. No paid generation ran.
