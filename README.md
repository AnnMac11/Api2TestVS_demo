# API2Test for VS Code — Demo & Trial Pack

API2Test turns an API specification into **runnable integration tests**, generated in the language
you choose — **C#, TypeScript or Python**. Import a spec (Postman, OpenAPI/Swagger, RAML, GraphQL,
Insomnia), build up a Data Dictionary of the fields each endpoint uses, generate request classes and
test cases — from a single call to a multi-step E2E chain — then **execute** them in a built-in
sandbox or **deploy** them into your own project and CI. All inside Visual Studio Code.

This repository is a self-contained trial pack: install the extension, follow the quick start, try it
against the sample specs, and let us know how it went.

**`Api2Test.vsix` in this pack is extension version 0.2.62.** Installing starts a **60-day free trial** that
unlocks everything — there are no feature tiers.

## Start here

1. Install the extension — [`Api2Test.vsix`](Api2Test.vsix)
   (`code --install-extension Api2Test.vsix`). Full steps:
   [`InstallationGuide.pdf`](InstallationGuide.pdf).
2. On first run, **pick your language** (C#, TypeScript or Python) and map the **sandbox**. The
   requirements page then checks your toolchain, row by row — see
   [the Quick Start](QUICKSTART.md#2-first-run--pick-your-language-then-the-sandbox) for what each
   language needs.
3. Follow the [Quick Start](QUICKSTART.md) — also available as a printable
   [`QuickStartGuide.pdf`](QuickStartGuide.pdf).
4. Import a sample from [`Example Swagger Files`](Example%20Swagger%20Files)
   (try `petstore-openapi.json`), or import straight from a public URL.
5. Build a test case, press **Execute**, and read the run in the **Dashboard**.
6. Compare your output with the [`Example Generated Project`](Example%20Generated%20Project).
7. Tell us how it went — [`Feedback Questionnaire.pdf`](Feedback%20Questionnaire.pdf).

## What's in this repo

| Item | Description |
|------|-------------|
| [`Api2Test.vsix`](Api2Test.vsix) | The installable VS Code extension |
| [`InstallationGuide.pdf`](InstallationGuide.pdf) | Install steps and prerequisites |
| [`QuickStartGuide.pdf`](QuickStartGuide.pdf) / [`QUICKSTART.md`](QUICKSTART.md) | Get from install to your first executed test |
| [`Example Swagger Files`](Example%20Swagger%20Files) | Sample OpenAPI specs and Postman collections to import |
| [`Example Generated Project`](Example%20Generated%20Project) | A worked C# / MSTest output project |
| [`Feedback Questionnaire.pdf`](Feedback%20Questionnaire.pdf) | A short trial feedback form |

## Requirements at a glance

- **VS Code 1.74** or later.
- For **generating** code: nothing else. The generators are built into the extension.
- For **executing** code: the toolchain for the language you pick — the .NET SDK (C#), Node.js LTS
  (TypeScript), or Python 3 (Python). The extension's requirements page checks each one live and
  tells you how to fix anything missing.

## Regenerating the PDFs

The PDFs are built from `docs/build_pdfs.py` (the figures live in `docs/images/`):

```bash
python -m pip install reportlab svglib pillow
python docs/build_pdfs.py
```
