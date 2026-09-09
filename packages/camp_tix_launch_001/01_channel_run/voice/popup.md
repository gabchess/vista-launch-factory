# Design reference

Observed 8 September 2026. An externally observed login page and its published brand-assets page supply layout and expression references. Tix claims come from the frozen Tix campaign source.

## Live login page

Source: an externally observed login page. Screenshot: private login-desktop.png. Exact DOM measurements: private login-observed-dom.json.

At 1710 x 952, the page divides evenly. The white form column contains a centered 420px form. Poppins is the computed font. The welcome line is 20px/30px, weight 600; supporting text is 18px/27px. Inputs are 54px high with a 6px radius and 16px vertical gap. The primary button is 52px high, with white text and a blue-to-purple gradient. Field text uses dark navy; secondary links use muted blue.

The right side is a full-height video, not separate live promotional controls. It combines a short feature badge, a large product heading, a brief benefit statement and a painted CTA above enlarged task cards. Two observed frames show a task card moving across a board. This was a still-based inspection, not a full watch.

The media reports 11.066s, 1600 x 1890, autoplay, muted, loop and no controls. CSS covers an 855 x 952 panel, so crop safety matters. WebM is selected, with MP4 fallback. The promo's baked-in font cannot be identified from the surrounding DOM. A painted CTA needs a separate HTML link in a usable implementation.

## Official brand source

The same source's public brand-assets page lists primary blue `#0063E3`, purple `#8C52FF` and pink `#FF66C4`. Background colors are `#91BCF3`, `#E2D4FF`, `#FFD9F0`; body text is `#101010`. Accent colors are `#3081E8`, `#B894FF`, `#FFA0DA`. The page prefers the horizontal logo and instructs users to preserve logo artwork. No logo from that source is needed in Tix campaign artwork.

These are published brand colors. Poppins and the spacing above are measurements of one login surface, not a complete official design system.

## Public popup evidence and limits

A public article from the same source includes a task-dialog image. Its alt text identifies a trend-to-post dialog with angle and tone choices.

That is evidence of a task dialog, not a feature-announcement modal. Its pixels were not inspected: web image access failed safe-URL validation and Chrome reported an extension UI blocking further automation. No image was downloaded to bypass that failure. An authenticated announcement popup was not accessed.

## Proposed popup treatment

**Design inference:** use a white modal with a 560px desktop maximum, 24px radius, 32px copy padding and a contained product graphic above its heading. Mobile gets a compact bottom sheet with a visible close button and at least 16px outer space. Use one benefit-led headline, a short explanatory paragraph and one primary action. A quiet dismissal keeps the choice easy.

Adapt the login's restrained form hierarchy and blue-purple action treatment. Keep Tix's `#0052FF`, paper background and character identity within the graphic. Depict a buyer composing a brief; avoid implying external results. Use Tix's approved waitlist CTA. Availability checks belong in review metadata.

The preview should be manually opened, support Escape and focus return, and expose a useful graphic description. Trigger timing and frequency remain integration decisions; no live targeting system is claimed.

## Capture limits

Saved one desktop screenshot plus computed DOM and video metadata. The brand page was read through its public HTML extraction; no brand-page screenshot was captured. Chrome navigation timed out once, then the login loaded and was inspected. A later new-tab action met an extension UI block. No forms were submitted, accounts opened or media generated during this research.
