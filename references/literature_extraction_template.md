# Literature Extraction Template

Use when the user provides PDFs, DOCX, PPTX, citations, abstracts, or paper text.

## Goal

Extract what the source can do for the student's proposal. Do not merely summarize.

## Per-Paper Extraction

For each paper, extract:

- Full citation if available
- Research question
- Research object and context
- Theory/framework
- Key constructs
- Independent variable(s)
- Dependent variable(s)
- Mediator(s)
- Moderator(s)
- Method and sample
- Main findings
- Limitations
- Future research suggestions
- How this paper helps the student's proposal
- What cannot be directly borrowed
- Possible research gap or new angle

## Synthesis Across Papers

After extracting multiple papers, group them by:

- Shared dependent variable
- Shared theoretical logic
- Shared method
- Similar or conflicting findings
- Missing mechanism
- Missing boundary condition
- Missing context
- Measurement inconsistency

## Literature Function Labels

Assign each paper one or more roles:

- Definition source
- Theory source
- Variable source
- Method source
- Scale/source of measurement
- Evidence for practical importance
- Evidence for academic gap
- Contrasting or conflicting result
- Boundary-condition clue

## Common Student Mistakes

- Treating market reports as prior research
- Listing papers one by one without synthesis
- Using a paper to support a claim it did not study
- Copying a variable name without its definition or measurement
- Ignoring the paper's own limitations/future research section

## Extraction Tools

Use `scripts/extract_source_notes.py` to extract raw text and likely sections from PDF/DOCX/PPTX/TXT/MD files. See `toolkit.md` for commands and fallback behavior.

