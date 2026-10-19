"""Generate the API2Test demo PDFs: Quick Start, Installation Guide, Feedback Questionnaire."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable,
    ListItem, HRFlowable, KeepTogether,
)
from svglib.svglib import svg2rlg

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
IMG = os.path.join(HERE, "images")

BRAND = colors.HexColor("#0e70c0")
DARK = colors.HexColor("#222222")
GREY = colors.HexColor("#555555")
LIGHT = colors.HexColor("#f2f6fa")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("Brand", parent=styles["Title"], textColor=BRAND, fontSize=26, spaceAfter=12))
styles.add(ParagraphStyle("Sub", parent=styles["Normal"], textColor=GREY, fontSize=11, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle("H", parent=styles["Heading2"], textColor=BRAND, fontSize=15, spaceBefore=14, spaceAfter=6))
styles.add(ParagraphStyle("Body", parent=styles["Normal"], fontSize=10.5, leading=15, textColor=DARK, spaceAfter=6))
styles.add(ParagraphStyle("Mono", parent=styles["Code"], fontSize=9.5, leading=13, backColor=LIGHT,
                          borderPadding=6, textColor=colors.HexColor("#0b3d62"), spaceAfter=8))
styles.add(ParagraphStyle("Bul", parent=styles["Normal"], fontSize=10.5, leading=15, textColor=DARK))
styles.add(ParagraphStyle("Foot", parent=styles["Normal"], fontSize=8.5, textColor=GREY, alignment=TA_CENTER))


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BRAND)
    canvas.rect(0, A4[1] - 8, A4[0], 8, fill=1, stroke=0)
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(20 * mm, 12 * mm, "API2Test for VS Code")
    canvas.drawRightString(A4[0] - 20 * mm, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


def figure(name, max_w=170 * mm):
    drawing = svg2rlg(os.path.join(IMG, name))
    scale = max_w / drawing.width
    drawing.width *= scale
    drawing.height *= scale
    drawing.scale(scale, scale)
    drawing.hAlign = "CENTER"
    return drawing


def title_block(title, subtitle):
    return [Paragraph(title, styles["Brand"]),
            Paragraph(subtitle, styles["Sub"]),
            HRFlowable(width="100%", color=BRAND, thickness=1.2, spaceAfter=10)]


def h(t): return Paragraph(t, styles["H"])
def p(t): return Paragraph(t, styles["Body"])
def code(t): return Paragraph(t.replace(" ", "&nbsp;").replace("\n", "<br/>"), styles["Mono"])
def bullets(items): return ListFlowable([ListItem(Paragraph(i, styles["Bul"]), leftIndent=10) for i in items],
                                        bulletType="bullet", start="•", leftIndent=12, spaceAfter=8)


def styled_table(data, col_widths):
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BRAND),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 9.5),
        ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
        ("TEXTCOLOR", (0, 1), (-1, -1), DARK),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cdd9e5")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def doc(path):
    return SimpleDocTemplate(path, pagesize=A4, topMargin=20 * mm, bottomMargin=18 * mm,
                             leftMargin=20 * mm, rightMargin=20 * mm,
                             title=os.path.basename(path).replace(".pdf", ""), author="API2Test")


# ─────────────────────────── Quick Start Guide ───────────────────────────
def build_quickstart():
    s = []
    s += title_block("API2Test — Quick Start Guide",
                     "Import · Generate · Execute · Deploy — inside VS Code")
    s.append(p("API2Test turns an API specification into <b>runnable integration tests</b>, generated "
               "in the language you choose — <b>C#, TypeScript or Python</b>. Import a spec, build up "
               "a Data Dictionary of the fields each endpoint uses, generate request classes and test "
               "cases (a single call or a multi-step chain), then <b>execute</b> them in a built-in "
               "sandbox or <b>deploy</b> them into your own project and CI. This guide takes you from "
               "install to your first executed test."))

    s.append(h("1. Install"))
    s.append(p("Install the bundled extension package <b>Api2Test.vsix</b> (this pack ships extension version 0.2.62):"))
    s.append(code("code --install-extension Api2Test.vsix"))
    s.append(p("Or in VS Code: Extensions view (Ctrl+Shift+X) → the “…” menu → "
               "<b>Install from VSIX…</b> → pick the .vsix file. Installing starts a <b>60-day free "
               "trial</b> that unlocks everything — there are no feature tiers — and the status bar "
               "shows the countdown, for example <b>API2Test: 54d left</b>. After the trial a licence "
               "key is needed (Command Palette → <b>API2Test: Enter License Key</b>); keys are "
               "verified offline and one key covers VS Code and the Desktop app. Full install steps "
               "are in InstallationGuide.pdf."))

    s.append(h("2. First run — pick your language, then the sandbox"))
    s.append(p("On first activation API2Test asks <b>which language to generate in</b>. The choice is "
               "locked for the workspace, so pick the language your team tests in (C# is the default "
               "if you dismiss the prompt). It then maps a <b>sandbox</b> folder — the default offered "
               "is %APPDATA%\\Api2Test\\sandbox — where <b>Execute</b> builds and runs your tests, "
               "deliberately apart from your own source."))
    s.append(p("<b>Generating code needs nothing installed</b> — the generators are built in. "
               "<b>Executing it</b> needs the toolchain for the language you picked:"))
    s.append(styled_table(
        [["Language", "Toolchain (machine-wide)", "VS Code extension", "Test framework + libraries"],
         ["C#", ".NET SDK (puts dotnet on PATH)", "C# Dev Kit", "MSTest + Bogus, already in the scaffolded ApiTests.csproj and restored on the first build"],
         ["TypeScript", "Node.js LTS + npm", "Vitest", "npm install once in the sandbox typescript folder (vitest, typescript, @faker-js/faker)"],
         ["Python", "Python 3 + pip (tick Add python.exe to PATH)", "Python", "pip install -r requirements.txt once in the sandbox python folder (pytest, requests, Faker)"]],
        [24 * mm, 42 * mm, 26 * mm, 78 * mm]))
    s.append(Spacer(1, 4))
    s.append(p("A <b>requirements page</b> then checks your machine row by row and reopens at every "
               "launch until everything is ✓. Each failing row says what to install and where. Only "
               "when all of them pass does the extension report that API2Test is ready."))

    s.append(h("3. Open the API2Test panel"))
    s.append(p("Click the <b>flask icon</b> in the Activity Bar. The API2Test tree view opens with six "
               "entries, in the order you work through them:"))
    s.append(figure("01-panel.svg"))
    s.append(Spacer(1, 8))
    s.append(styled_table(
        [["Entry", "What it does"],
         ["API Import", "Import a spec — Postman, OpenAPI/Swagger, RAML, GraphQL or Insomnia"],
         ["Data Dictionary", "The fields each endpoint uses, and the data method that fills each one"],
         ["Test Cases", "Build, generate, execute and deploy test cases"],
         ["Dashboard", "The result of every run, with a drill-down report"],
         ["Resources", "Imported APIs and the Class / Method / Data libraries"],
         ["Admin", "Language, sandbox, deploy paths, requirements and licence"]],
        [42 * mm, 128 * mm]))

    s.append(h("4. Import an API"))
    s.append(p("Click <b>API Import</b> and choose a source. The format is detected automatically, "
               "then you pick the <b>application</b> the endpoints belong to — that name keeps each "
               "API separate all the way through to the generated folders and namespaces."))
    s.append(bullets([
        "<b>From File</b> — a Postman collection, an OpenAPI/Swagger .json / .yaml, or a RAML, GraphQL or Insomnia export.",
        "<b>From URL</b> — a link to a hosted spec.",
    ]))
    s.append(figure("02-import.svg"))
    s.append(p("Try it with the samples in the <b>Example Swagger Files</b> folder, or pick "
               "<b>From URL</b> and paste one of these live, free specs (no API key needed):"))
    s.append(styled_table(
        [["Public API", "Spec URL (Import from URL)"],
         ["Swagger PetStore (OpenAPI 3.0)", "https://petstore3.swagger.io/api/v3/openapi.json"],
         ["Swagger PetStore (Swagger 2.0)", "https://petstore.swagger.io/v2/swagger.json"],
         ["APIs.guru Directory (OpenAPI 3.0)", "https://api.apis.guru/v2/specs/apis.guru/2.2.0/openapi.json"]],
        [58 * mm, 112 * mm]))
    s.append(Spacer(1, 4))
    s.append(p("Then verify the result under <b>Resources → Imported APIs</b>."))

    s.append(h("5. Generate request classes"))
    s.append(p("Under <b>Resources → API Class Library</b>, tick the endpoints you want and press "
               "<b>Generate Class</b> — one or a hundred in one go. Each class is named from the "
               "application, the verb and the path (POST /pet becomes PetStorePostPet), carries the "
               "spec field names as its JSON keys, and gets a ToJson() for use as a request body. The "
               "header keeps a running tally of generated, pending and failed. Change a field later "
               "and <b>Update &amp; Generate</b> brings the class back into line."))

    s.append(h("6. Review the Data Dictionary"))
    s.append(p("Open <b>Data Dictionary</b> to see every field the imported endpoints use — its type, "
               "its <b>location</b> (path, query or body), whether it is mandatory, and the <b>data "
               "method</b> that supplies its value. The method list is narrowed to the methods that "
               "suit the type, and arguments are enabled only for methods that take them, so DateStr "
               "becomes DateStr(-3) for three days ago. A field left as <b>Not Assigned</b> is "
               "generated without a default value."))
    s.append(figure("03-data-dictionary.svg"))

    s.append(h("7. Build a test case — one call or a chain"))
    s.append(p("Open <b>Test Cases</b> and press <b>Create Test</b>. Give the test a name, pick the "
               "application and the framework (MSTest for C#, Vitest for TypeScript, pytest for "
               "Python), then choose a <b>base path method</b> for the base URL and a <b>token "
               "method</b> for authentication. Now add steps with <b>Add class…</b> and <b>Add "
               "method…</b>, in the order they should run:"))
    s.append(bullets([
        "<b>A method step</b> is one call from the API Method Library — PostJsonAsync, GetAsync, a Validate… check, an Extract… capture.",
        "<b>A class step</b> is the request body for that call, with any field pinned to a fixed value or to a value captured earlier.",
        "<b>IN</b> shows what a step needs (path parameters, body fields); <b>OUT</b> shows what it produces, where “store as” names a value for later steps.",
    ]))
    s.append(p("A three-step PetStore chain reads: create a pet, validate the 200/201, capture the id "
               "it came back with, then fetch that pet by the captured id. Press <b>Generate &amp; "
               "Save</b> and the test joins the list with its step count and status."))
    s.append(figure("04-test-cases.svg"))

    s.append(h("8. Execute it"))
    s.append(p("Press <b>Execute</b> (the ▶ on the row). API2Test copies the test, its classes and the "
               "libraries into the sandbox, builds, runs, and brings the result back — the row turns "
               "green or red, and <b>Dashboard</b> records the run with a report you can drill into, "
               "step by step. The same thing runs by hand in the sandbox folder with "
               "<b>dotnet test</b>, <b>npx vitest run</b> or <b>python -m pytest</b>."))

    s.append(h("9. Deploy into your own project"))
    s.append(p("When a test earns its place in your repo, set the destinations once in <b>Admin → "
               "Deploy Paths</b>, then tick rows in Test Cases and press <b>Deploy</b>. API2Test "
               "writes a complete, compiling unit — the libraries, the request classes and the tests "
               "— into folders that mirror their namespaces:"))
    s.append(code("Libraries/        -&gt; Api2Test.Generated.Libraries\n"
                  "Classes/&lt;App&gt;/    -&gt; Api2Test.Generated.Classes.&lt;App&gt;\n"
                  "Tests/&lt;App&gt;/      -&gt; Api2Test.Generated.Tests.&lt;App&gt;"))
    s.append(p("The <b>Example Generated Project</b> folder in this repository is exactly that "
               "output, for the PetStore API, and it builds with dotnet build."))

    s.append(h("Where your data lives"))
    s.append(p("All API2Test data is stored as JSON at <b>~/.vscode/API2Test/data/</b> "
               "(Windows: C:\\Users\\&lt;you&gt;\\.vscode\\API2Test\\data\\). Files are created on first "
               "run and never overwritten, so your edits are safe across updates."))

    s.append(h("Troubleshooting"))
    s.append(bullets([
        "<b>The requirements page keeps reopening</b> — a row is still red. It reopens at every launch until all of them pass, and each row says what to install.",
        "<b>Tree empty after import</b> — click Refresh at the top of the panel.",
        "<b>Import from URL fails</b> — make sure the URL returns the raw spec (JSON/YAML), not an HTML page.",
        "<b>Execute fails on the first run</b> — for TypeScript run npm install once in the sandbox typescript folder; for Python run pip install -r requirements.txt in the sandbox python folder.",
        "<b>A generated step carries a placeholder comment</b> — an argument was not supplied; reopen the test case and fill in the IN value.",
        "<b>Trial expired</b> — enter a key with API2Test: Enter License Key, or check Admin → Licence.",
    ]))
    s.append(Spacer(1, 6))
    s.append(HRFlowable(width="100%", color=colors.HexColor("#cdd9e5")))
    s.append(Spacer(1, 4))
    s.append(Paragraph("When you have finished trying API2Test, please complete the Feedback "
                       "Questionnaire. Thank you!", styles["Foot"]))

    d = doc(os.path.join(ROOT, "QuickStartGuide.pdf"))
    d.build(s, onFirstPage=header_footer, onLaterPages=header_footer)


# ─────────────────────────── Installation Guide ───────────────────────────
def build_installation():
    s = []
    s += title_block("API2Test — Installation Guide",
                     "Installing the API2Test extension for Visual Studio Code")

    s.append(h("Prerequisites"))
    s.append(bullets([
        "<b>Visual Studio Code 1.74</b> or later.",
        "The bundled <b>Api2Test.vsix</b> package (in this repository — extension version 0.2.62).",
        "<b>Nothing else is needed to import or generate.</b> To <b>execute</b> the generated tests "
        "you also need the toolchain for the language you pick — see “First run” below.",
    ]))

    s.append(h("Option A — Install from the command line"))
    s.append(p("With the VS Code <b>code</b> command on your PATH, run:"))
    s.append(code("code --install-extension Api2Test.vsix"))
    s.append(p("Restart VS Code if prompted."))

    s.append(h("Option B — Install from the VS Code UI"))
    s.append(styled_table(
        [["Step", "Action"],
         ["1", "Open the Extensions view (Ctrl+Shift+X)."],
         ["2", "Click the “…” (More Actions) menu at the top of the view."],
         ["3", "Choose “Install from VSIX…”."],
         ["4", "Select Api2Test.vsix from this repository."],
         ["5", "Reload VS Code when prompted."]],
        [18 * mm, 152 * mm]))
    s.append(p("<b>Upgrading from an earlier build?</b> Uninstall the installed API2Test first, then "
               "install the new .vsix and reload. Your data directory is left untouched."))

    s.append(h("Verify the installation"))
    s.append(bullets([
        "A <b>flask icon</b> appears in the Activity Bar (left edge).",
        "Clicking it opens the <b>API2Test</b> panel with API Import, Data Dictionary, Test Cases, Dashboard, Resources and Admin.",
        "The status bar (bottom-right) shows the trial countdown, for example <b>API2Test: 54d left</b>.",
    ]))
    s.append(figure("01-panel.svg"))

    s.append(h("First run — language, sandbox and requirements"))
    s.append(p("The first activation asks <b>which language to generate in</b> — C#, TypeScript or "
               "Python. The choice is locked for the workspace. It then maps a <b>sandbox</b> folder "
               "(the default offered is %APPDATA%\\Api2Test\\sandbox), where Execute builds and runs "
               "tests apart from your own source."))
    s.append(p("A <b>requirements page</b> then checks your machine row by row, and reopens at every "
               "launch until every row is ✓. Install only the row for the language you picked:"))
    s.append(styled_table(
        [["Language", "Toolchain (machine-wide)", "VS Code extension", "One-off setup in the sandbox"],
         ["C#", ".NET SDK, with dotnet on PATH", "C# Dev Kit", "None — MSTest and Bogus restore on the first build"],
         ["TypeScript", "Node.js LTS + npm", "Vitest", "npm install in the typescript folder"],
         ["Python", "Python 3 + pip, with python.exe on PATH", "Python", "pip install -r requirements.txt in the python folder"]],
        [24 * mm, 48 * mm, 26 * mm, 72 * mm]))

    s.append(h("Trial and licence"))
    s.append(p("Installing starts a <b>60-day free trial</b> with every feature unlocked. The status "
               "bar counts down, and <b>Admin → Licence</b> reads it in full (“Trial — 54 days left”, "
               "or “Licensed — 192 days left”), turning amber in the last week. When the trial ends "
               "the panel asks for a key."))
    s.append(bullets([
        "<b>API2Test: Enter License Key</b> — paste your key. It is verified <b>offline</b> and stored in VS Code secret storage.",
        "<b>API2Test: Show License Status</b> — licensed (with expiry), trial (days left), or expired.",
        "<b>API2Test: Remove License</b> — drops the stored key; access falls back to the trial clock.",
    ]))
    s.append(p("One licence covers both editions — the VS Code extension and the API2Test Desktop app."))

    s.append(h("Where your data is stored"))
    s.append(p("API2Test keeps its data as JSON files under <b>~/.vscode/API2Test/data/</b>. "
               "These are created automatically on first run and are never overwritten, so upgrades "
               "preserve your applications, libraries, data dictionary and test cases."))

    s.append(h("Troubleshooting"))
    s.append(bullets([
        "<b>“code” not recognised</b> — in VS Code run “Shell Command: Install code command in PATH”, or use Option B.",
        "<b>The requirements page keeps reopening</b> — a row is still red. It reopens at every launch until all of them pass.",
        "<b>Extension fails to activate</b> — open Help → Toggle Developer Tools and check the Console, or Output → API2Test.",
        "<b>VSIX rejected as incompatible</b> — confirm VS Code is version 1.74 or later (Help → About).",
        "<b>A newly installed VSIX seems to change nothing</b> — uninstall the old API2Test, then install the new one and reload.",
    ]))

    d = doc(os.path.join(ROOT, "InstallationGuide.pdf"))
    d.build(s, onFirstPage=header_footer, onLaterPages=header_footer)


# ─────────────────────────── Feedback Questionnaire ───────────────────────────
def build_feedback():
    s = []
    s += title_block("API2Test — Feedback Questionnaire",
                     "Your feedback shapes the next release. It takes about 5 minutes.")
    s.append(p("Thanks for trying API2Test. Please answer the questions below and return this form to "
               "the team. Tick the box that best matches your view, and add comments where helpful."))

    def scale_row(q):
        return [q, "[ ] 1", "[ ] 2", "[ ] 3", "[ ] 4", "[ ] 5"]

    s.append(h("About you"))
    s.append(styled_table(
        [["Question", "Your answer"],
         ["Name (optional)", ""],
         ["Role", ""],
         ["Team / Organisation", ""],
         ["Date", ""]],
        [55 * mm, 115 * mm]))

    s.append(h("Rate your experience"))
    s.append(p("1 = Strongly disagree &nbsp;·&nbsp; 5 = Strongly agree"))
    rating_rows = [["Statement", "1", "2", "3", "4", "5"]]
    for q in [
        "Installing the extension was straightforward.",
        "Importing my API (Postman / OpenAPI) worked as expected.",
        "The Data Dictionary was easy to understand and use.",
        "The generated test classes were useful and accurate.",
        "The panel and workflow were intuitive.",
        "Overall, API2Test saved me time.",
    ]:
        rating_rows.append([q, "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"])
    t = styled_table(rating_rows, [110 * mm] + [12 * mm] * 5)
    s.append(t)

    s.append(h("Tell us more"))
    for q in [
        "What worked well?",
        "What was confusing or frustrating?",
        "Which feature would you most like added or improved?",
        "Would you recommend API2Test to a colleague? Why / why not?",
    ]:
        s.append(p("<b>" + q + "</b>"))
        s.append(Table([[""]], colWidths=[170 * mm], rowHeights=[20 * mm],
                       style=TableStyle([("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#cdd9e5")),
                                         ("BACKGROUND", (0, 0), (-1, -1), colors.white)])))
        s.append(Spacer(1, 6))

    s.append(h("How likely are you to keep using API2Test?"))
    s.append(styled_table([scale_row("0 = Not at all, 5 = Definitely")],
                          [70 * mm] + [20 * mm] * 5))
    s.append(Spacer(1, 10))
    s.append(Paragraph("Please return this completed form to the API2Test team. Thank you!", styles["Foot"]))

    d = doc(os.path.join(ROOT, "Feedback Questionnaire.pdf"))
    d.build(s, onFirstPage=header_footer, onLaterPages=header_footer)


if __name__ == "__main__":
    build_quickstart()
    build_installation()
    build_feedback()
    print("PDFs built:", os.listdir(ROOT))
