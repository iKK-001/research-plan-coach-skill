# Toolkit

Use this when files need to be read before coaching.

## Runtime Rule

Prefer the Codex bundled Python runtime when available because the system Python may not include document libraries.

Known bundled path on this machine:

`/Users/ikaken/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`

If that path is unavailable, try `python3`. If imports fail, explain that the extraction script needs `pypdf` for PDF and `python-docx` for DOCX.

## Scripts

### `scripts/extract_source_notes.py`

Use for:

- `.pdf`
- `.docx`
- `.pptx`
- `.txt`
- `.md`

Default behavior:

- Extracts text into `/tmp/research-plan-coach-extracted`
- Writes one `.notes.txt` file per source
- Adds likely research-relevant section headings
- Keeps raw text unless `--sections-only` is used

Recommended command:

```bash
/Users/ikaken/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/extract_source_notes.py SOURCE.pdf
```

For large files:

```bash
/Users/ikaken/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/extract_source_notes.py --max-pages 30 SOURCE.pdf
```

For quick section scan:

```bash
/Users/ikaken/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/extract_source_notes.py --sections-only SOURCE.pdf
```

For keyword-focused extraction:

```bash
/Users/ikaken/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/extract_source_notes.py --keywords "limitations,future research,method" SOURCE.pdf
```

## Extraction Workflow

1. Extract notes with the script.
2. Read the likely sections first.
3. Apply `literature_extraction_template.md`.
4. Do not treat extracted text as final interpretation.
5. If the file is a scanned PDF and text is empty, tell the user OCR is needed.

