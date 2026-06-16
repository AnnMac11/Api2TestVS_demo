# API2Test for VS Code — Demo & Trial Pack

API2Test imports your API definitions (Postman collections or OpenAPI/Swagger specs),
organizes them into reusable libraries, and generates API test classes — all inside
Visual Studio Code.

This repository is a self-contained trial pack: install the extension, follow the
quick start, try it against the sample specs, and let us know how it went.

## Start here

1. Install the extension — [`Api2Test.vsix`](Api2Test.vsix)
   (`code --install-extension Api2Test.vsix`). Full steps: [`InstallationGuide.pdf`](InstallationGuide.pdf).
2. Follow the [Quick Start](QUICKSTART.md) — also available as a printable
   [`QuickStartGuide.pdf`](QuickStartGuide.pdf).
3. Import a sample from [`Example Swagger Files`](Example%20Swagger%20Files)
   (try `petstore-openapi.json`).
4. Compare your output with the [`Example Generated Project`](Example%20Generated%20Project).
5. Tell us how it went — [`Feedback Questionnaire.pdf`](Feedback%20Questionnaire.pdf).

## What's in this repo

| Item | Description |
|------|-------------|
| [`Api2Test.vsix`](Api2Test.vsix) | The installable VS Code extension |
| [`InstallationGuide.pdf`](InstallationGuide.pdf) | Install steps and prerequisites |
| [`QuickStartGuide.pdf`](QuickStartGuide.pdf) / [`QUICKSTART.md`](QUICKSTART.md) | Get from install to first test in minutes |
| [`Example Swagger Files`](Example%20Swagger%20Files) | Sample OpenAPI specs and Postman collections to import |
| [`Example Generated Project`](Example%20Generated%20Project) | A worked C# / MSTest output project |
| [`Feedback Questionnaire.pdf`](Feedback%20Questionnaire.pdf) | A short trial feedback form |

## Regenerating the PDFs

The PDFs are built from `docs/build_pdfs.py` (the figures live in `docs/images/`):

```bash
python -m pip install reportlab svglib pillow
python docs/build_pdfs.py
```
