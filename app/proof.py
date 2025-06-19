from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib import colors
from datetime import datetime
from langdetect import detect
from googletrans import Translator
import os

def get_font_for_lang(lang_code):
    if lang_code in ['hi', 'mr', 'ne']: 
        return "NotoHindi", os.path.join("fonts", "NotoSansDevanagari-Regular.ttf")
    else:
        return "NotoEng", os.path.join("fonts", "NotoSansDevanagari-Regular.ttf")

def generate_proof(excuse_text: str, scenario: str) -> str:
    os.makedirs("proofs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"proof_{timestamp}.pdf"
    output_path = os.path.join("proofs", filename)

    lang_code = detect(excuse_text)

    font_name, font_path = get_font_for_lang(lang_code)
    pdfmetrics.registerFont(TTFont(font_name, font_path))

    translator = Translator()
    def tr(text):
        return translator.translate(text, dest=lang_code).text

    q1 = tr("Why were you absent yesterday?")
    a1 = tr("I see. Please make sure to inform me next time.")
    a2 = tr("Sure, I’ll keep that in mind. Thank you!")

    doc = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=40)

    chat_user = ParagraphStyle(
        name="User",
        fontName=font_name,
        fontSize=13,
        leading=18,
        textColor=colors.white,
        backColor=colors.darkblue,
        alignment=TA_RIGHT,
        borderPadding=5,
        leftIndent=120,
        rightIndent=0,
    )

    chat_other = ParagraphStyle(
        name="Other",
        fontName=font_name,
        fontSize=13,
        leading=18,
        textColor=colors.black,
        backColor=colors.whitesmoke,
        alignment=TA_LEFT,
        borderPadding=5,
        leftIndent=0,
        rightIndent=120,
    )

    msg1 = Paragraph(q1, chat_other)
    msg2 = Paragraph(excuse_text, chat_user)
    msg3 = Paragraph(a1, chat_other)
    msg4 = Paragraph(a2, chat_user)

    story = [Spacer(1, 12), msg1, Spacer(1, 8), msg2, Spacer(1, 8), msg3, Spacer(1, 8), msg4]

    doc.build(story)

    return output_path
