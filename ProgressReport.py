import wx
import wx.xrc

from datetime import datetime

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

        self.progress_report_label = wx.StaticText(self, wx.ID_ANY, u"Progress Report", wx.DefaultPosition,
                                                   wx.DefaultSize, wx.ALIGN_CENTRE)
        self.progress_report_label.Wrap(-1)
        self.progress_report_label.SetFont(wx.Font(12, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.progress_report_label, 0, wx.ALL | wx.EXPAND, 10)

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
            "form": 0,
            "exam_name": "",
            "exam_id": 0
        }

        outer_sizer.Add(self.left_sizer, 0, wx.EXPAND, 5)

        right_sizer = wx.BoxSizer(wx.VERTICAL)

        sbSizer13 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        # Get exam to preload on the marks panel
        exam = getExamsInFormAndYear(student['form'], int(datetime.now().year))
        exam_id = exam['ids'][0]

        subjects = getActiveSubjectAliases()
        subjects_aliases = subjects['aliases']
        subjects_names = subjects['names']

        data = {
            'exam_id': exam_id,
            'student_id':student['user_id'],
            'form': str(student['form']),
            'class_id': student['class_id']
        }

        results = getResultsByStudentAndExamID(data, subjects_aliases, subjects_names)

        self.marks_panel = MarksPanel(self, results)
        sbSizer13.Add(self.marks_panel, 1, wx.EXPAND, 5)

        right_sizer.Add(sbSizer13, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        outer_sizer.Add(right_sizer, 1, wx.EXPAND, 5)

        container.Add(outer_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

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

    # --------------------------------------------
    def examSelected(self, event):
        exam = self.select_exam_panel.exam_name.GetCurrentSelection()  # get index of exam selected
        exam_id = self.select_exam_panel.examDets['ids'][exam]

        print exam_id


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


