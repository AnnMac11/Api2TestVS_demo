# API2Test for VS Code — Quick Start

API2Test imports your API definitions (Postman collections or OpenAPI/Swagger specs),
organizes them into reusable libraries, and helps you generate API test classes — all
inside VS Code.

This guide gets you from install to your first generated test in a few minutes.

---

## 1. Install

**From a `.vsix` package**

```bash
code --install-extension api2test-vscode-0.0.19.vsix
```

Or in VS Code: open the Extensions view (`Ctrl+Shift+X`) → `…` menu →
**Install from VSIX…** → pick the file.

**For development (from source)**

```bash
npm install
npm run compile
# then press F5 in VS Code to launch the Extension Development Host
```

When the extension activates you'll see the message **"API2Test extension is ready"**.

---

## 2. Open the API2Test panel

Click the **flask icon** (🧪) in the Activity Bar on the left edge of VS Code.
The **API2Test** tree view opens with four entries:

| Entry | What it does |
|-------|--------------|
| **API Import** | Import a Postman collection or OpenAPI/Swagger spec |
| **Data Dictionary** | Define and manage field-level test data |
| **Test Cases** | View and generate API test cases |
| **Resources** | Imported APIs, API Class Library, API Method Library, Data Library |

> Tip: use the **Refresh** button (top of the panel) any time the tree looks stale.

---

## 3. Import an API

Click **API Import**. The import dialog opens with two options:

- **From File** — choose a `.json` Postman collection or an OpenAPI/Swagger
  (`.json` / `.yaml`) file.
- **From URL** — paste a link to a hosted OpenAPI/Swagger spec.

The format is detected automatically. You'll be prompted to pick (or name) the
**application** the endpoints belong to, then the endpoints are imported into your
library.

Verify the result under **Resources → Imported APIs**, which shows every imported
endpoint in a table.

---

## 4. Review your libraries (Resources)

Expand **Resources** to find:

- **Imported APIs** — every endpoint you've imported, in a table view.
- **API Class Library** — the API client classes available for generation.
- **API Method Library** — individual API methods (add / edit / delete).
- **Data Library** — reusable data-generation methods (add / edit / delete).

These are the building blocks the generators draw on.

---

## 5. Set up your Data Dictionary (optional but recommended)

Click **Data Dictionary** to open its table page. Here you define the fields your
tests use — name, type, whether they're mandatory, and which **data method**
supplies their value.

To bootstrap it quickly, use **Import Data Dictionary from API Endpoints** (the
download icon on the Data Dictionary section) to derive fields directly from the
endpoints you imported.

---

## 6. Generate a test

Click **Test Cases** to open the Test Cases page, then use the toolbar to
**Generate Test**. You can also right-click an endpoint to **Generate Class** for
that specific API method.

The generators combine your imported endpoints, class/method libraries, and data
dictionary into ready-to-use API test classes.

---

## Where your data lives

All API2Test data is stored as JSON on your machine at:

```
~/.vscode/API2Test/data/
```

(on Windows: `C:\Users\<you>\.vscode\API2Test\data\`)

Files include `applications.json`, `api-methods.json`, `api-method-library.json`,
`api-class-library.json`, `data-dictionary.json`, `data-library.json`,
`generated-classes.json`, and `api-tests.json`. They're created automatically on
first run and never overwritten, so your edits are safe across updates.

---

## Typical workflow at a glance

```
API Import  →  Resources (review)  →  Data Dictionary  →  Test Cases (generate)
```

1. **Import** your Postman collection or OpenAPI spec.
2. **Review** the endpoints and libraries under Resources.
3. **Define** test data in the Data Dictionary.
4. **Generate** test classes from the Test Cases page.

---

## Troubleshooting

- **Tree is empty after import** — click **Refresh** at the top of the panel.
- **Import from URL fails** — make sure the URL returns the raw spec (JSON/YAML),
  not an HTML page; API2Test rejects responses that start with `<html>`.
- **Extension didn't activate** — check **Output → API2Test** (or the Developer
  Console, `Help → Toggle Developer Tools`) for the activation log.
</content>
</invoke>
