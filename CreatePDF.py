import time
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# def createReportCard(results = None):
#     doc = SimpleDocTemplate("report_card.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72,
#                             bottomMargin=18)
#
#     # Register Helvetica bold font
#     helvetica_bold_font = r"fonts/Helvetica Bold.ttf"
#     pdfmetrics.registerFont(TTFont("Helvetica-Bold", helvetica_bold_font))
#
#     # Register Helvetica normal font
#     helvetica_normal_font = r"fonts/Helvetica-Normal.ttf"
#     pdfmetrics.registerFont(TTFont("Helvetica-Normal", helvetica_normal_font))
#
#     Story = []
#     logo = u"images\\kangangu logo-254x254.bmp"
#     school_name = "KANGANGU SECONDARY SCHOOL"
#     po_box = "P.O. BOX 183 - 01020 KENOL"
#     term = "3"
#     year = "2018"
#     exam_name = "END TERM" + " REPORT" + "     " + term + "     " + year
#     # time = time.strftime("%d/%m/%Y")
#
#     adm_no = "ADM " + "4612"
#     student_name = "MARY PRISCA WANGUI NGONJO"
#     class_name = "1J"
#     kcpe = "KCPE: " + "389"
#
#     im = Image(logo, 2 * inch, 2 * inch)  # two inches from the top and two inches from the left.
#     Story.append(im)
#
#     styles = getSampleStyleSheet()
#     styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
#
#     ptext = '<font name ="Helvetica-Bold" size=14>%s</font>' % school_name
#     Story.append(Paragraph(ptext, style=styles['Center']))
#
#     Story.append(Spacer(1, 10))
#     ptext = '<font name ="Helvetica-Bold" size=12>%s</font>' % po_box
#     Story.append(Paragraph(ptext, styles["Center"]))
#
#     Story.append(Spacer(1, 10))
#     ptext = '<font name ="Helvetica-Bold" size=12>%s</font>' % exam_name
#     Story.append(Paragraph(ptext, styles["Center"]))
#     Story.append(Spacer(1, 15))
#
#     styleSheet = getSampleStyleSheet()
#
#     data = [
#         [adm_no, student_name, class_name, kcpe],
#         ['Subject', 'Mean', 'Grade', 'Rank'],
#         ['20', '21', '22', '23'],
#         ['30', '31', '32', '33']
#     ]
#
#     # for result in results:
#     #     data.append(result)
#
#     style = [
#         ('LINEABOVE', (0, 0), (-1, -1), 0.75, colors.black),
#         ('LINEAFTER', (0, 0), (-2, -1), 0.75, colors.black),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),  # Make first column Bold, -1 reps end of row/col
#         ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold')  # Make second row Bold
#     ]
#
#     table_first_row = Table(data)
#     table_first_row.setStyle(TableStyle(style))
#
#     Story.append(table_first_row)
#
#     if doc.build(Story):
#         print "created"
#     else:
#         print "failed to create pdf"


# def createMarkSheet(results = None):
doc = SimpleDocTemplate("marksheet.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72,
                        bottomMargin=18)

# Register Helvetica bold font
helvetica_bold_font = r"fonts/Helvetica Bold.ttf"
pdfmetrics.registerFont(TTFont("Helvetica-Bold", helvetica_bold_font))

# Register Helvetica normal font
helvetica_normal_font = r"fonts/Helvetica-Normal.ttf"
pdfmetrics.registerFont(TTFont("Helvetica-Normal", helvetica_normal_font))

Story = []
logo = u"images\\kangangu logo-254x254.bmp"
school_name = "KANGANGU SECONDARY SCHOOL"
po_box = "P.O. BOX 183 - 01020 KENOL"
term = "3"
year = "2018"
exam_name = "END TERM" + " REPORT" + "     " + term + "     " + year
# time = time.strftime("%d/%m/%Y")

adm_no = "ADM " + "4612"
student_name = "MARY PRISCA WANGUI NGONJO"
class_name = "1J"
kcpe = "KCPE: " + "389"

im = Image(logo, 2 * inch, 2 * inch)  # two inches from the top and two inches from the left.
Story.append(im)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

ptext = '<font name ="Helvetica-Bold" size=14>%s</font>' % school_name
Story.append(Paragraph(ptext, style=styles['Center']))

Story.append(Spacer(1, 10))
ptext = '<font name ="Helvetica-Bold" size=12>%s</font>' % po_box
Story.append(Paragraph(ptext, styles["Center"]))

Story.append(Spacer(1, 10))
ptext = '<font name ="Helvetica-Bold" size=12>%s</font>' % exam_name
Story.append(Paragraph(ptext, styles["Center"]))
Story.append(Spacer(1, 15))

styleSheet = getSampleStyleSheet()

data = [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t = Table(data)
t.setStyle(TableStyle([('BACKGROUND', (1, 1), (-2, -2), colors.green),
                       ('TEXTCOLOR', (0, 0), (1, -1), colors.red)]))
Story.append(t)


if doc.build(Story):
    print "created"
else:
    print "failed to create pdf"
