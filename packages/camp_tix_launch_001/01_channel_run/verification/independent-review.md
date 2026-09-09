# Independent review: channel preparation and campaign review

Date: 8 September 2026. Scope: current `automation/n8n/channel-production/`, plus `01_channel_run/review.html` and `serve_review.py`. Production files were read only during this review. Root separately authorized the narrow popup iframe-focus correction recorded below.

All six code findings from this bounded review are fixed. Focused retests pass against the corrected production files. Root also confirmed the popup iframe-focus correction and desktop/mobile legibility in the in-app browser. No code blocker remains from this pass.

## Findings and disposition

| ID | Priority | Finding | Disposition |
| --- | --- | --- | --- |
| E01 | P2 | The Code node accepted `constructor`, `toString` and `__proto__` as extra request fields. An inherited property lookup bypassed `additionalProperties:false`. Each malformed packet returned `ready_for_operator`. | **Fixed by the verifier; retest passed.** `prepare.js` now uses own-property checks for required and allowed keys. Each exact probe returns `needs_inputs` with the matching unknown-field error. |
| E02 | P2 | An existing article marked in `changed_ids` could retain `stage:draft` with no revision record. Preparation returned all four work packets, bypassing feedback counting and scoped revision. | **Fixed by the verifier; retest passed.** A changed existing artifact forces revision handling. The malformed packet now returns `blog:revision_target_requires_counted_feedback`. |
| E03 | P2 | The review note key omitted `context_digest`. A changed fact or voice context could reuse an old Ready/Changes note when the artifact ID, version and bytes stayed the same. | **Fixed by root; focused script test passed.** The current key changes with the context digest, and the old note is absent from the new subject. |
| E04 | P2 | Save note replaced an existing Changes or Ready intent with the nonblocking Note state. Adding detail could silently remove a change request from the exported record. | **Fixed by root; focused script test passed.** Saving feedback preserves the current decision status. A Changes intent retained its state and received the updated text. Authentication and applied-approval fields remained false. |
| E05 | P2 | The server accepted any `--film` or `--animation` file while the page showed the approved row and expected hash. A wrong attachment could be displayed under another asset's approval. | **Fixed by root; retest passed.** Startup compares the supplied bytes with the approved row. The first fix used an API absent from default Apple Python 3.9; root replaced it with a chunked SHA-256 read. On Python 3.9.6 the actual CLI now exits with code 2 and the expected mismatch message. Socket creation was disabled during the test. |
| E06 | P2 | Mobile preview styled only the existing iframe. Switching assets replaced that iframe at full width while the button still indicated mobile mode. | **Fixed by root; focused script test passed.** Navigation creates a new iframe and applies the active 390px mode. The toggle state stays consistent. |

## Probe evidence

The tests used the actual embedded Code node from `workflow.json`, with the supplied fictional request example as the control. No provider or workflow execution service was called.

| Probe | Before | After |
| --- | --- | --- |
| Unknown property `constructor` | `ready_for_operator` | `needs_inputs`; `requests[0]:unknown_field_constructor` |
| Unknown property `toString` | `ready_for_operator` | `needs_inputs`; `requests[0]:unknown_field_toString` |
| Unknown property `__proto__` | `ready_for_operator` | `needs_inputs`; `requests[0]:unknown_field___proto__` |
| Changed existing article, draft stage, no revision | Four selected lanes | `needs_inputs`; counted-feedback issue |
| Valid 4000-artifact acyclic graph, 692590-character envelope | Completed without an exception | No performance guarantee inferred for an n8n host |

Retested embedded Code SHA-256: `0af08274e7edcbdeb4f1b6673049f468915e430e360691efdc7aac9aebe4ba85`.

The review-page probes executed its actual script with small DOM/storage stand-ins and no network. They checked context invalidation, preservation of Changes intent while saving feedback, width mode after navigation and the final export filter. A deliberately mismatched context record was omitted from the exported intent. These are function-level checks; browser layout and screen-reader output require their own inspection.

## Checks with no remaining preparation finding

Claim spans use Unicode characters and hashes use UTF-8 bytes. Fact claims require fact sources; voice references require voice sources. Mixed campaign/product/revision/reviewer input is refused. Exact artifact version and hash are required for counted revision feedback. Affected dependencies are expanded, and an unrouted affected artifact is held. The loader uses the canonical workspace validator before preparation. Semantic claim truth still needs an editor.

The workflow is inactive. Its nodes prepare data only. The returned execution, publishing, approval and authentication flags stay false. Durable attempt counts, human identity, actual model/provider calls and recipient-host n8n execution remain outside this implementation. The documented crypto requirement is explicit. Local tests do not establish a hosted integration.

The server binds to `127.0.0.1` and supplies GET content without a publishing or account API. No current critical remote-action path was found in this bounded inspection. The page stores local intent; it does not apply an approval event.

## Related browser finding from root

The reviewer observed that the popup's embedded `dialog.show()` moved focus to its close control and scrolled the outer review page. The operator made the authorized narrow correction: iframe mode sets the `open` attribute; standalone mode retains `showModal()`. Copy and graphic hashes stayed unchanged. Script syntax passed. Root then reloaded and selected the popup in the in-app browser: focus remained in the outer web area and no forced scroll occurred. Root also reported legible desktop/mobile artwork and copy. This browser result is attributed to root, not an independent full-browser pass by the operator.

Corrected popup HTML SHA-256: `c2254ad3a876e051c6309b90b682ae714e00f164f62eec8394eb4ae26903b397`.

The popup's three original working-asset references were changed from author-local absolute paths to historical relative labels. The bundled `assets/` paths remain the load paths, and source hashes were retained. Provenance SHA-256: `42e507ef462ee624b163ce2d36092ed89b40cfb03b985759fee5b95122daa3bc`.

Media playback, screen-reader output and the waitlist collection path were not tested in this independent code pass. Root owns the remaining actual browser/media checks. No paid calls, publication, commit or product-repository changes occurred here.

## Retested source files

| File | SHA-256 |
| --- | --- |
| `automation/n8n/channel-production/prepare.js` | `aa0d60fa25af2e317d792be02b310cd247b5c2644a7ddaaee673255da82d3c98` |
| `automation/n8n/channel-production/workflow.json` | `5e56ebe9ad68e46febe887e4e9f800b1781967e7ed058f7a9c96f5358d91040c` |
| `packages/camp_tix_launch_001/01_channel_run/review.html` | `470b74c4edb41b83078fe8286c46cc90a9f81a448adb8d028a211b08cf95cf5d` |
| `packages/camp_tix_launch_001/01_channel_run/serve_review.py` | `9674f1be7222c548665987f5b578ce70ffae320f01edf9270ac88fe271f9e707` |
