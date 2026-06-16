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
                     "Import APIs · Build libraries · Generate tests — inside VS Code")
    s.append(p("API2Test imports your API definitions (Postman collections or OpenAPI/Swagger specs), "
               "organizes them into reusable libraries, and helps you generate API test classes — all "
               "inside VS Code. This guide gets you from install to your first generated test in minutes."))

    s.append(h("1. Install"))
    s.append(p("Install the bundled extension package <b>Api2Test.vsix</b>:"))
    s.append(code("code --install-extension Api2Test.vsix"))
    s.append(p("Or in VS Code: Extensions view (Ctrl+Shift+X) → “…” menu → "
               "<b>Install from VSIX…</b> → pick Api2Test.vsix. When it activates you'll see "
               "<b>“API2Test extension is ready”</b>. See InstallationGuide.pdf for full steps."))

    s.append(h("2. Open the API2Test panel"))
    s.append(p("Click the <b>flask icon</b> in the Activity Bar. The API2Test tree view opens "
               "with four entries: API Import, Data Dictionary, Test Cases and Resources."))
    s.append(figure("01-panel.svg"))
    s.append(Spacer(1, 8))
    s.append(styled_table(
        [["Entry", "What it does"],
         ["API Import", "Import a Postman collection or OpenAPI/Swagger spec"],
         ["Data Dictionary", "Define and manage field-level test data"],
         ["Test Cases", "View and generate API test cases"],
         ["Resources", "Imported APIs and the Class / Method / Data libraries"]],
        [42 * mm, 128 * mm]))

    s.append(h("3. Import an API"))
    s.append(p("Click <b>API Import</b> and choose a source. The format is detected automatically, "
               "then you pick the application the endpoints belong to."))
    s.append(bullets([
        "<b>From File</b> — a .json Postman collection or an OpenAPI/Swagger (.json / .yaml) file.",
        "<b>From URL</b> — a link to a hosted OpenAPI/Swagger spec.",
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

    s.append(h("4. Review your libraries (Resources)"))
    s.append(bullets([
        "<b>Imported APIs</b> — every endpoint you've imported, in a table view.",
        "<b>API Class Library</b> — the API client classes available for generation.",
        "<b>API Method Library</b> — individual API methods (add / edit / delete).",
        "<b>Data Library</b> — reusable data-generation methods (add / edit / delete).",
    ]))

    s.append(h("5. Set up your Data Dictionary"))
    s.append(p("Open <b>Data Dictionary</b> to define the fields your tests use — name, type, whether "
               "they're mandatory, and which data method supplies their value. Use "
               "<b>Import Data Dictionary from API Endpoints</b> to bootstrap it from imported endpoints."))
    s.append(figure("03-data-dictionary.svg"))

    s.append(h("6. Generate a test"))
    s.append(p("Open <b>Test Cases</b> and click <b>Generate Test</b>, or right-click an endpoint to "
               "<b>Generate Class</b>. The generators combine your endpoints, libraries and data "
               "dictionary into ready-to-use API test classes — see the Example Generated Project."))
    s.append(figure("04-test-cases.svg"))

    s.append(h("Where your data lives"))
    s.append(p("All API2Test data is stored as JSON at <b>~/.vscode/API2Test/data/</b> "
               "(Windows: C:\\Users\\&lt;you&gt;\\.vscode\\API2Test\\data\\). Files are created on first "
               "run and never overwritten, so your edits are safe across updates."))

    s.append(h("Troubleshooting"))
    s.append(bullets([
        "<b>Tree empty after import</b> — click Refresh at the top of the panel.",
        "<b>Import from URL fails</b> — ensure the URL returns the raw spec (JSON/YAML), not an HTML page.",
        "<b>Extension didn't activate</b> — check Output → API2Test for the activation log.",
    ]))
    s.append(Spacer(1, 6))
    s.append(HRFlowable(width="100%", color=colors.HexColor("#cdd9e5")))
    s.append(Spacer(1, 4))
    s.append(Paragraph("When you've finished trying API2Test, please complete the Feedback Questionnaire. "
                       "Thank you!", styles["Foot"]))

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
        "<b>.NET 8 SDK</b> — only needed to build/run the generated C# test projects.",
        "The bundled <b>Api2Test.vsix</b> package (in this repository).",
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

    s.append(h("Verify the installation"))
    s.append(bullets([
        "A <b>flask icon</b> appears in the Activity Bar (left edge).",
        "Clicking it opens the <b>API2Test</b> panel with API Import, Data Dictionary, Test Cases and Resources.",
        "A notification reads <b>“API2Test extension is ready”</b>.",
    ]))
    s.append(figure("01-panel.svg"))

    s.append(h("Where your data is stored"))
    s.append(p("API2Test keeps its data as JSON files under <b>~/.vscode/API2Test/data/</b>. "
               "These are created automatically on first run and are never overwritten, so upgrades "
               "preserve your applications, libraries and data dictionary."))

    s.append(h("Updating"))
    s.append(p("Install a newer Api2Test.vsix the same way — your data directory is left intact. "
               "To remove the extension, open the Extensions view, find API2Test, and click Uninstall."))

    s.append(h("Troubleshooting"))
    s.append(bullets([
        "<b>“code” not recognised</b> — in VS Code run “Shell Command: Install 'code' command in PATH”, or use Option B.",
        "<b>Extension fails to activate</b> — open Help → Toggle Developer Tools and check the Console, or Output → API2Test.",
        "<b>VSIX rejected as incompatible</b> — confirm VS Code is version 1.74 or later (Help → About).",
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
