# B1: portable article verification

IF-ARTICLE-VERIFIER-CONTEXT is a CORE data interface. The canonical router provides a fresh `specialist-route/v1` projection to the article verifier through an in-process Python call and local UTF-8 files.

Preconditions: the full repository and Python dependencies exist; the immutable request, source spans, claim ledger and article artifacts match their recorded bindings. The workspace root may differ from the builder's root. Required fields include request identity, source hashes and spans, expected context digest and selected role. Absolute paths are local routing output.

Postcondition: a zero exit code means the current request passed the canonical workspace validator, reached `ready_for_protocol`, selected `blog_editor`, and matched the provenance context digest. All remaining article checks must pass. Default verification writes no files. `--write-report` explicitly refreshes the local check report; it grants no approval. The recorded route byte hash remains historical production evidence.

Invariants: no provider calls; no approval authority; no acceptance of changed source bytes or changed semantic context. Every invocation recomputes the route. Repetition is safe. No network timeout exists at this local seam; orchestration tests use a bounded subprocess timeout. Missing or corrupt input exits nonzero and reports the failing input. Oversized campaigns retain the existing router limits; this audit adds no new ingestion API.

The misleading-success case is a forged route JSON that repeats the expected digest. Recompute directly from source bytes so that file cannot establish truth. Hold on digest mismatch or router refusal. Restoring the correct input restores the verified state.

Acceptance: a relocated package with no routing receipt passes; altered source bytes fail even when an old route remains; changed article bytes fail. Run default verification twice and confirm the saved report stays unchanged. Shared coupling is the router schema and context-digest algorithm; an intentional change requires a new provenance review. Failure blocks article acceptance and the final package, without changing other assets.
