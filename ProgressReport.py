import wx
import wx.xrc

from datetime import datetime

# Reportlab Imports
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# from CreatePDF import createReportCard

from db.get_exams import getExamsInFormAndYear
from db.get_exam_results import getResultsByStudentAndExamID
from db.get_subjects import getActiveSubjectAliases

###########################################################################
# Class ProgressReport
###########################################################################


class ProgressReport(wx.Panel):

    def __init__(self, parent, student):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        self.student = student

        container = wx.BoxSizer(wx.VERTICAL)

        # self.progress_report_label = wx.StaticText(self, wx.ID_ANY, u"Progress Report", wx.DefaultPosition,
        #                                            wx.DefaultSize, wx.ALIGN_CENTRE)
        # self.progress_report_label.Wrap(-1)
        # self.progress_report_label.SetFont(wx.Font(12, 70, 90, 92, False, wx.EmptyString))
        #
        # container.Add(self.progress_report_label, 0, wx.ALL | wx.EXPAND, 10)

        title_sizer = wx.BoxSizer(wx.HORIZONTAL)

        title_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.progress_report_label = wx.StaticText(self, wx.ID_ANY, u"Progress Report", wx.DefaultPosition,
                                                   wx.DefaultSize, wx.ALIGN_CENTRE)
        self.progress_report_label.Wrap(-1)
        self.progress_report_label.SetFont(wx.Font(12, 70, 90, 92, False, wx.EmptyString))

        title_sizer.Add(self.progress_report_label, 1, wx.ALL | wx.EXPAND, 10)

        self.download_btn = wx.BitmapButton(self, wx.ID_ANY,
                                            wx.Bitmap(u"images/download_pdf.bmp", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW | wx.NO_BORDER)
        self.download_btn.SetDefault()
        title_sizer.Add(self.download_btn, 0, wx.TOP | wx.RIGHT | wx.LEFT, 15)

        container.Add(title_sizer, 0, wx.EXPAND, 5)

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.left_sizer = wx.BoxSizer(wx.VERTICAL)

        form_choices = []
        if student['form'] == 1:
            form_choices = [u"One"]
        elif student['form'] == 2:
            form_choices = [u"Two", u"One"]
        elif student['form'] == 3:
            form_choices = [u"Three", u"Two", u"One"]
        elif student['form'] == 4:
            form_choices = [u"Four", u"Three", u"Two", u"One"]

        self.select_form = SelectForm(self, form_choices)
        self.left_sizer.Add(self.select_form, 0, wx.EXPAND | wx.ALL, 5)

        self.select_exam_panel = SelectExam(self, student['form'], int(datetime.now().year))
        self.left_sizer.Add(self.select_exam_panel, 0, wx.EXPAND | wx.ALL, 5)

        self.exam_data = {
            "exam_id": 0,
            "exam_name": "",
            'term': "",
            'year': 0,
            'student_id': student['user_id'],
            "form": str(student['form']),
            'class_id': student['class_id'],
        }

        self.subjects = getActiveSubjectAliases()
        self.subjects_aliases = self.subjects['aliases']
        self.subjects_names = self.subjects['names']

        outer_sizer.Add(self.left_sizer, 0, wx.EXPAND, 5)

        right_sizer = wx.BoxSizer(wx.VERTICAL)

        self.sbSizer13 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        # Get exam to preload on the marks panel
        exam = getExamsInFormAndYear(student['form'], int(datetime.now().year))

        # If there's an exam id in the array, get results, else use dummy data
        if len(exam['ids']):

            exam_id = exam['ids'][0]
            exam_name = exam['exam_names'][0]
            exam_term = exam['terms'][0]
            exam_year = exam['years'][0]

            self.exam_data['exam_id'] = exam_id
            self.exam_data['exam_name'] = exam_name
            self.exam_data['term'] = exam_term
            self.exam_data['year'] = exam_year

            results = getResultsByStudentAndExamID(self.exam_data, self.subjects_aliases, self.subjects_names)
        else:
            results = {
                'subject': "",
                'mean': "",
                'grade': "",
                'rank': ""
            }
            results = [results]

        self.marks_panel = MarksPanel(self, results)
        self.sbSizer13.Add(self.marks_panel, 1, wx.EXPAND, 5)

        right_sizer.Add(self.sbSizer13, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        outer_sizer.Add(right_sizer, 1, wx.EXPAND, 5)

        container.Add(outer_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.download_btn.Bind(wx.EVT_BUTTON, self.downloadReportCard)

    def __del__(self):
        pass

    # --------------------------------------------
    def formSelected(self, event):
        current_form = self.student['form']
        form_selected = self.select_form.form.GetStringSelection()

        if form_selected == "One":
            form = 1
        elif form_selected == "Two":
            form = 2
        elif form_selected == "Three":
            form = 3
        elif form_selected == "Four":
            form = 4

        current_year = int(datetime.now().year)

        year = 0

        diff = current_form - form
        year = current_year - diff  # To get the year the student was in that form

        self.select_exam_panel.Hide()

        self.select_exam_panel = SelectExam(self, form, year)
        self.left_sizer.Add(self.select_exam_panel, 0, wx.EXPAND | wx.ALL, 5)

        self.Layout()

    #
    # --------------------------------------------
    def examSelected(self, event):
        examIndex = self.select_exam_panel.exam_name.GetCurrentSelection()  # get index of exam selected
        examName = self.select_exam_panel.exam_name.GetStringSelection()  # get name of exam selected
        exam_id = self.select_exam_panel.examDets['ids'][examIndex]
        exam_term = self.select_exam_panel.examDets['terms'][examIndex]
        exam_year = self.select_exam_panel.examDets['years'][examIndex]

        self.exam_data['exam_id'] = exam_id
        self.exam_data['exam_name'] = examName
        self.exam_data['term'] = exam_term
        self.exam_data['year'] = exam_year

        results = getResultsByStudentAndExamID(self.exam_data, self.subjects_aliases, self.subjects_names)

        self.marks_panel.Destroy()

        self.marks_panel = MarksPanel(self, results)
        self.sbSizer13.Add(self.marks_panel, 1, wx.EXPAND, 5)

        self.Layout()

    #
    # --------------------------------------------
    def downloadReportCard(self, event):
        results = getResultsByStudentAndExamID(self.exam_data, self.subjects_aliases, self.subjects_names)

        doc = SimpleDocTemplate("report_card.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72,
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

        #

        term = "TERM " + self.exam_data['term'].upper()
        year = str(self.exam_data['year'])
        exam_name = self.exam_data['exam_name'].upper() + " REPORT&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + term +"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +  year

        #

        adm_no = "ADM NO: " + str(self.student['reg_no'])
        student_name = self.student['first_name'].upper() + ' ' + self.student['last_name'].upper() + ' ' + self.student['surname'].upper()

        if 'Form' in self.student['class']:
            class_name = self.student['class']
        else:
            class_name = str(self.student['form']) + ' ' + self.student['class']

        kcpe = "KCPE: " + str(self.student['kcpe_marks'])

        im = Image(logo, 2 * inch, 2 * inch)  # two inches from the top and two inches from the left.
        Story.append(im)

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

        ptext = '<font name ="Helvetica-Bold" size=14>%s</font>' % school_name
        Story.append(Paragraph(ptext, style=styles['Center']))

        Story.append(Spacer(1, 10))
        ptext = '<font name ="Helvetica-Bold" size=11>%s</font>' % po_box
        Story.append(Paragraph(ptext, styles["Center"]))

        Story.append(Spacer(1, 10))
        ptext = '<font name ="Helvetica-Bold" size=11>%s</font>' % exam_name
        Story.append(Paragraph(ptext, styles["Center"]))
        Story.append(Spacer(1, 15))

        styleSheet = getSampleStyleSheet()

        data = [
            # spaces in order to span row across two columns
            [adm_no + "                 " + student_name, "", class_name + "                 " + kcpe, ""],
            ['Subject', 'Mean', 'Grade', 'Rank'],
        ]

        for result_array in results:
            # Order array in the same order as the table column titles
            result = [result_array['subject'], result_array['mean'], result_array['grade'], result_array['rank']]
            data.append(result)

        style = [
            ('LINEABOVE', (0, 0), (-1, -1), 0.75, colors.black),
            ('LINEAFTER', (0, 0), (-2, -1), 0.75, colors.black),
            ('ALIGN', (1, 0), (-1, -1), 'CENTER'),  # Center text on second Row, starting from second column
            ('SPAN', (0, 0), (1, 0)),  # Combine the adm no + name cells
            ('SPAN', (2, 0), (3, 0)),  # Combine the class name + kcpe cells
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),  # Make first column Bold, -1 reps end of row/col
            ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold')  # Make second row Bold
        ]

        table_first_row = Table(data)
        table_first_row.setStyle(TableStyle(style))

        Story.append(table_first_row)

        doc.build(Story)


class SelectForm(wx.Panel):

    def __init__(self, parent, form_choices):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        form_sizer = wx.BoxSizer(wx.VERTICAL)

        self.form_label = wx.StaticText(self, wx.ID_ANY, u"Select Form", wx.DefaultPosition, wx.DefaultSize, 0)
        self.form_label.Wrap(-1)
        form_sizer.Add(self.form_label, 0, wx.ALL, 5)

        formChoices = form_choices

        self.form = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, formChoices,
                                wx.CB_READONLY)
        self.form.SetSelection(0)
        form_sizer.Add(self.form, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(form_sizer)
        self.Layout()

        # Connect Events
        self.form.Bind(wx.EVT_COMBOBOX, self.parent.formSelected)


class SelectExam(wx.Panel):

    def __init__(self, parent, form, year):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        exam_sizer = wx.BoxSizer(wx.VERTICAL)

        self.exam_label = wx.StaticText(self, wx.ID_ANY, u"Select Exam", wx.DefaultPosition, wx.DefaultSize, 0)
        self.exam_label.Wrap(-1)
        exam_sizer.Add(self.exam_label, 0, wx.ALL, 5)

        self.examDets = getExamsInFormAndYear(form, year)

        self.exam_nameChoices = self.examDets['full_names']

        self.exam_name = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     self.exam_nameChoices, wx.CB_READONLY)
        self.exam_name.SetSelection(0)
        exam_sizer.Add(self.exam_name, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(exam_sizer)
        self.Layout()

        # Connect Events
        self.exam_name.Bind(wx.EVT_COMBOBOX, self.parent.examSelected)


class MarksPanel(wx.Panel):

    def __init__(self, parent, results):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        outer_Sizer = wx.BoxSizer(wx.HORIZONTAL)

        outer_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        content_sizer = wx.BoxSizer(wx.VERTICAL)

        titles_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.name_title = wx.StaticText(self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.name_title.Wrap(-1)
        self.name_title.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        titles_sizer.Add(self.name_title, 1, wx.ALL, 7)

        self.mean_title = wx.StaticText(self, wx.ID_ANY, u"Mean", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.mean_title.Wrap(-1)
        self.mean_title.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        titles_sizer.Add(self.mean_title, 1, wx.ALL, 7)

        self.deviation_title = wx.StaticText(self, wx.ID_ANY, u"Deviation", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ALIGN_CENTRE)
        self.deviation_title.Wrap(-1)
        self.deviation_title.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        titles_sizer.Add(self.deviation_title, 1, wx.ALL, 7)

        self.grade_title = wx.StaticText(self, wx.ID_ANY, u"Grade", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.grade_title.Wrap(-1)
        self.grade_title.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        titles_sizer.Add(self.grade_title, 1, wx.ALL, 7)

        self.rank_text = wx.StaticText(self, wx.ID_ANY, u"Rank", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.rank_text.Wrap(-1)
        self.rank_text.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        titles_sizer.Add(self.rank_text, 1, wx.ALL, 7)

        content_sizer.Add(titles_sizer, 0, wx.EXPAND, 5)

        self.under_titles_static_line = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                      wx.LI_HORIZONTAL)
        content_sizer.Add(self.under_titles_static_line, 0, wx.EXPAND | wx.TOP, 5)

        self.marks_rows = {}
        static_lines = {}
        for key, val in enumerate(results):
            self.marks_rows[str(key)] = OneMarkRow(self, val)
            content_sizer.Add(self.marks_rows[str(key)], 0, wx.EXPAND, 5)

            # Add static line below each row
            static_lines[str(key)] = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                          wx.LI_HORIZONTAL)
            content_sizer.Add(static_lines[str(key)], 0, wx.EXPAND | wx.TOP, 5)

        outer_Sizer.Add(content_sizer, 3, wx.EXPAND, 5)

        outer_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(outer_Sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

    def __del__(self):
        pass


class OneMarkRow(wx.Panel):

    def __init__(self, parent, mark):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        marks_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.subject_name = wx.StaticText(self, wx.ID_ANY, mark['subject'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.subject_name.Wrap(-1)
        self.subject_name.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        marks_sizer.Add(self.subject_name, 1, wx.ALL, 7)

        self.mean_text = wx.StaticText(self, wx.ID_ANY, str(mark['mean']), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.mean_text.Wrap(-1)
        self.mean_text.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        marks_sizer.Add(self.mean_text, 1, wx.ALL, 7)

        self.deviation_text = wx.StaticText(self, wx.ID_ANY, u"dev", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.deviation_text.Wrap(-1)
        self.deviation_text.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        marks_sizer.Add(self.deviation_text, 1, wx.ALL, 7)

        self.grade_text = wx.StaticText(self, wx.ID_ANY, str(mark['grade']), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.grade_text.Wrap(-1)
        self.grade_text.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        marks_sizer.Add(self.grade_text, 1, wx.ALL, 7)

        self.rank_text = wx.StaticText(self, wx.ID_ANY, str(mark['rank']), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.rank_text.Wrap(-1)
        self.rank_text.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        marks_sizer.Add(self.rank_text, 1, wx.ALL, 7)

        self.SetSizer(marks_sizer)
        self.Layout()

    def __del__(self):
        pass


