"""Regenerate the downloadable resume from confirmed portfolio facts.

Uses ReportLab and Windows Arial fonts to preserve Slovak name accents.
Review this content alongside src/pages/resume.astro whenever facts change.
"""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader

root = Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold', 'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='ArialBold', italic='Arial', boldItalic='ArialBold')
output = root / 'public' / 'jakub-bartosovic-resume.pdf'
ink = HexColor('#172034')
accent = HexColor('#59418a')
styles = {
    'name': ParagraphStyle('name', fontName='ArialBold', fontSize=23, leading=28, textColor=ink, spaceAfter=5),
    'role': ParagraphStyle('role', fontName='Arial', fontSize=11, leading=15, textColor=accent, spaceAfter=7),
    'body': ParagraphStyle('body', fontName='Arial', fontSize=9.5, leading=13, textColor=ink, spaceAfter=5),
    'contact': ParagraphStyle('contact', fontName='Arial', fontSize=9, leading=12, textColor=ink, spaceAfter=3),
    'section': ParagraphStyle('section', fontName='ArialBold', fontSize=11, leading=15, textColor=accent, spaceBefore=10, spaceAfter=5, keepWithNext=True),
    'item': ParagraphStyle('item', fontName='ArialBold', fontSize=9.5, leading=13, textColor=ink, spaceBefore=4, spaceAfter=3, keepWithNext=True),
    'bullet': ParagraphStyle('bullet', fontName='Arial', fontSize=9.5, leading=13, textColor=ink, leftIndent=10, firstLineIndent=-7, spaceAfter=3),
}
story = []
def add(text, kind='body'):
    story.append(Paragraph(text, styles[kind]))

add('Jakub Bartošovič', 'name')
add('Entry-level IT candidate | Aspiring software developer', 'role')
add('Bratislava, Slovakia | <link href="mailto:jakubbartosovic@gmail.com">jakubbartosovic@gmail.com</link>', 'contact')
add('<link href="https://github.com/Interacti0n">github.com/Interacti0n</link> | <link href="https://www.linkedin.com/in/jakub-bartosovic/">linkedin.com/in/jakub-bartosovic</link>', 'contact')
add('Profile', 'section')
add('Seeking an entry-level IT opportunity, with previous junior Oracle DBA experience and a background in automotive operations. In personal projects, I guide AI-generated implementation through instructions and feedback, manually try the applications, and report visual issues while learning from the code.')
add('Experience', 'section')
add('Logistics / operations - Automotive industry | Current role', 'item')
add('- Coordinate material transport from warehouse to production line, organize people, and prioritize delayed or urgent deliveries.', 'bullet')
add('- Respond to material shortages by checking parts availability and order history, checking operational software, and handling phone coordination.', 'bullet')
add('Junior database administrator | 2022', 'item')
add('- Basic Oracle Database user and access administration.', 'bullet')
add('- Simple SQL diagnostics; work with logs, monitoring, and Linux.', 'bullet')
add('Projects', 'section')
add('NumForge | C17, CMake', 'item')
add('A mathematics project with a C17 core and tools for precise calculations, graphs, equations, and matrices. <link href="https://github.com/Interacti0n/NumForge" color="#59418a">Source: github.com/Interacti0n/NumForge</link>')
add('TwinStar Progress | React, TypeScript, SQLite', 'item')
add('A live guild rankings website with searchable raid progress, speedkills, and scheduled data updates. <link href="https://twinstar-progress.pages.dev/" color="#59418a">Live: twinstar-progress.pages.dev</link>')
add('ARC - Advanced Raid Check | Lua, WoW API', 'item')
add('A World of Warcraft addon helping raid leaders check group readiness, equipment, and raid-session activity. <link href="https://github.com/Interacti0n/ARC-Advanced-Raid-Check" color="#59418a">Source: github.com/Interacti0n/ARC-Advanced-Raid-Check</link>')
add('Education', 'section')
add('FIIT STU | 2018-2021', 'item')
add('Three years of studies at the Faculty of Informatics and Information Technologies, Slovak University of Technology.')
add('Skills &amp; interests', 'section')
add('<b>Technologies in my AI-assisted projects:</b> C17, CMake, Lua, React, TypeScript, SQLite, Cloudflare Pages.<br/><b>Professional experience:</b> Oracle Database, basic SQL diagnostics, access administration, logs, monitoring, Linux.<br/><b>Interests:</b> C, C#, .NET, backend development, databases, DevOps.<br/><b>Workplace strengths:</b> communication, prioritization, practical problem solving, operational awareness.')
add('Languages', 'section')
add('Slovak - native | English - B2')
doc = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=42, leftMargin=42, topMargin=36, bottomMargin=36, title='Jakub Bartošovič - Resume', author='Jakub Bartošovič')
doc.build(story)
reader = PdfReader(output)
assert len(reader.pages) == 1, f'Expected one page, found {len(reader.pages)}'
assert 'Jakub Bartošovič' in reader.pages[0].extract_text()
print(f'Resume generated: {len(reader.pages)} page')
