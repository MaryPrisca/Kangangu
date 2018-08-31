import wx
import wx.xrc
from ObjectListView import ObjectListView, ColumnDefn

from db.get_exam_results import *
from db.get_classes import getFormClasses
from db.get_subjects import getActiveSubjectAliases
from db.get_exams import getPreviousExam
from db.exam_statistics import getGradePlusMark, calculateDeviation
from db.get_students import getStudentByID
# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')


###########################################################################
# Class ExamResults
###########################################################################

class ExamResults(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(546, 435),
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText98 = wx.StaticText(self, wx.ID_ANY, u"Exam Results", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText98.Wrap(-1)
        self.m_staticText98.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText98, 0, wx.EXPAND | wx.TOP, 25)

        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_container = wx.BoxSizer(wx.VERTICAL)

        self.sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Please fill in order to get mark sheet."), wx.VERTICAL)

        #
        #
        #
        reset_btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.reset_btn = wx.Button(self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0)
        reset_btn_sizer.Add(self.reset_btn, 2, wx.ALL, 5)

        self.sbSizer2.Add(reset_btn_sizer, 0, wx.EXPAND | wx.ALL, 5)

        #
        #
        #
        self.year_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        year_sizer = wx.BoxSizer(wx.VERTICAL)

        self.year_label = wx.StaticText(self.year_panel, wx.ID_ANY, u"Select Year", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.year_label.Wrap(-1)
        year_sizer.Add(self.year_label, 0, wx.ALL, 5)

        yearChoices = getPresentYears()
        self.year = wx.ComboBox(self.year_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                yearChoices, wx.CB_READONLY)
        year_sizer.Add(self.year, 0, wx.ALL | wx.EXPAND, 5)

        self.year_panel.SetSizer(year_sizer)
        self.year_panel.Layout()
        year_sizer.Fit(self.year_panel)
        self.sbSizer2.Add(self.year_panel, 0, wx.EXPAND | wx.ALL, 5)

        #
        #
        #
        self.term_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        term_sizer = wx.BoxSizer(wx.VERTICAL)

        self.term_label = wx.StaticText(self.term_panel, wx.ID_ANY, u"Select Term", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.term_label.Wrap(-1)
        term_sizer.Add(self.term_label, 0, wx.ALL, 5)

        termChoices = [u"One", u"Two", u"Three"]
        self.term = wx.ComboBox(self.term_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                termChoices, wx.CB_READONLY)
        term_sizer.Add(self.term, 0, wx.ALL | wx.EXPAND, 5)

        self.term_panel.SetSizer(term_sizer)
        self.term_panel.Layout()
        term_sizer.Fit(self.term_panel)
        self.sbSizer2.Add(self.term_panel, 0, wx.EXPAND | wx.ALL, 5)
        self.term_panel.Hide()

        #
        #
        #
        self.exam_panel_created = 0  # To check if panel has already been added to view

        #
        #
        #
        self.form_panel_created = 0  # To check if panel has already been added to view

        #
        #
        #
        self.class_panel_created = 0

        #
        #
        #
        self.subjects_panel_created = 0

        #
        #
        #
        self.buttons_panel_created = 0

        self.exam_data = {
            "year":     0,
            "term":     "",
            "exam_id":  0,
            "exam_name":  "",
            "form":     "",
            "class_id": 0,
            "class_name": "",
            "subject_alias": ""
        }

        sample_most_improved_data = {
            'student_id': [],
            'mark': 0,
            'nature': ""
        }

        #
        #
        #
        left_container.Add(self.sbSizer2, 1, wx.ALL | wx.EXPAND, 15)

        horizontal_sizer.Add(left_container, 0, wx.EXPAND, 5)

        #
        #  ==================================================================================
        #                               RIGHT SIDE
        #  ==================================================================================
        #

        self.right_container = wx.BoxSizer(wx.VERTICAL)

        self.show_results = ViewResults(self, "", self.exam_data, "", sample_most_improved_data)
        self.show_results.Hide()
        self.right_container.Add(self.show_results, 1, wx.ALL | wx.EXPAND, 15)

        self.results_panel_created = 0

        horizontal_sizer.Add(self.right_container, 5, wx.EXPAND, 5)

        container.Add(horizontal_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.reset_btn.Bind(wx.EVT_BUTTON, self.resetForm)
        self.year.Bind(wx.EVT_COMBOBOX, self.yearSelected)
        self.term.Bind(wx.EVT_COMBOBOX, self.termSelected)

    def __del__(self):
        pass

    #
    # ---------------------------------------------------------
    def yearSelected(self, event):
        year = self.year.GetStringSelection()
        self.exam_data['year'] = year

        self.term_panel.Show()
        self.Layout()

    #
    # ---------------------------------------------------------
    def termSelected(self, event):
        year = self.year.GetStringSelection()
        term = self.term.GetStringSelection()

        self.exam_data['term'] = term

        # Check if there are exams in selected year and term

        exams = getExamsinTerm(term, year)

        if exams['ids']:
            if not self.exam_panel_created:
                self.select_exam = SelectExam(self, term=term, year=year)
                self.sbSizer2.Add(self.select_exam, 0, wx.EXPAND | wx.ALL, 5)
                self.Layout()

                self.exam_panel_created = 1  # change to 1 so it's not created again

                # Disable changing year and term to avoid inconsistency
                self.year.Enable(False)
                self.term.Enable(False)
        else:
            dlg = wx.MessageDialog(None, "No exams found in " + year + " Term " + term + ".",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            ret = dlg.ShowModal()
            if ret == wx.ID_OK:
                self.year.SetSelection(-1)
                self.term.SetSelection(-1)

                self.year.Enable(True)
                self.term.Enable(True)

                self.term_panel.Hide()

                self.exam_data['year'] = 0
                self.exam_data['term'] = ""
            dlg.Destroy()

    #
    # ---------------------------------------------------------
    def examSelected(self, event):
        exam = self.select_exam.exam_name.GetCurrentSelection()  # get index of exam selected
        exam_id = self.select_exam.examDets['ids'][exam]
        form = self.select_exam.examDets['forms'][exam]

        exam_name = self.select_exam.exam_name.GetStringSelection()

        self.exam_data['exam_id'] = exam_id
        self.exam_data['exam_name'] = exam_name
        self.exam_data['form'] = form

        # Add Form and class panels concurrently because form will be disabled.
        if not self.form_panel_created:
            self.select_form = SelectForm(self, form)
            self.sbSizer2.Add(self.select_form, 0, wx.EXPAND | wx.ALL, 5)
            self.Layout()

            self.form_panel_created = 1  # change to 1 so it's not created again

        if not self.class_panel_created:
            self.select_class = SelectClass(self, int(form))
            self.sbSizer2.Add(self.select_class, 0, wx.EXPAND | wx.ALL, 5)
            self.Layout()

            self.class_panel_created = 1  # change to 1 so it's not created again

            #  Disable changing exam and form to avoid inconsistency
            self.select_exam.exam_name.Enable(False)
            self.select_form.form.Enable(False)

    #
    # ---------------------------------------------------------
    def formSelected(self, event):
        """"""
        # form = self.select_form.form.GetCurrentSelection() + 1
        #
        # self.exam_data['form'] = form
        #
        # if not self.class_panel_created:
        #     self.select_class = SelectClass(self, form)
        #     self.sbSizer2.Add(self.select_class, 0, wx.EXPAND | wx.ALL, 5)
        #     self.Layout()
        #
        #     self.class_panel_created = 1  # change to 1 so it's not created again
        #
        #     #  Disable changing exam and form to avoid inconsistency
        #     self.select_exam.exam_name.Enable(False)
        #     self.select_form.form.Enable(False)

    #
    # ---------------------------------------------------------
    def classSelected(self, event):

        if not self.subjects_panel_created:
            self.select_subject = SelectSubject(self)
            self.sbSizer2.Add(self.select_subject, 0, wx.EXPAND | wx.ALL, 5)
            self.Layout()
            self.subjects_panel_created = 1  # change to 1 so it's not created again

        # get index of class selected in order to match with ID's list
        classIndex = self.select_class.class_name.GetCurrentSelection()

        # Index starts at zero, if ind+ 1 is greater than length of classes picked from DB then option selected is "All"
        if classIndex + 1 > len(self.select_class.classes['ids']):
            class_id = 0  # To signify all classes
        else:
            class_id = self.select_class.classes['ids'][classIndex]

        class_name = self.select_class.class_name.GetStringSelection()

        self.exam_data['class_id'] = class_id
        self.exam_data['class_name'] = class_name

    #
    # ---------------------------------------------------------
    def subjectSelected(self, event):
        if not self.buttons_panel_created:
            self.buttons_panel = ButtonsPanel(self)
            self.sbSizer2.Add(self.buttons_panel, 0, wx.EXPAND | wx.ALL, 5)
            self.Layout()
            self.buttons_panel_created = 1  # change to 1 so it's not created again

        subjectIndex = self.select_subject.subject_name.GetCurrentSelection()

        # Index starts at zero, if ind+ 1 is greater than length of classes picked from DB then option selected is "All"
        if subjectIndex + 1 > len(self.select_subject.subjects['aliases']):
            alias = "All"
        else:
            alias = self.select_subject.subjects['aliases'][subjectIndex]

        self.exam_data['subject_alias'] = alias

    #
    # ---------------------------------------------------------
    def resetForm(self, event):
        self.year.SetSelection(-1)
        self.term.SetSelection(-1)

        self.year.Enable(True)
        self.term.Enable(True)

        self.term_panel.Hide()

        if self.exam_panel_created:
            self.select_exam.exam_name.SetSelection(-1)

            self.select_exam.exam_name.Enable(True)

            self.select_exam.Hide()

            self.exam_panel_created = 0

        if self.form_panel_created:
            self.select_form.form.SetSelection(-1)
            self.select_form.form.Enable(True)

            self.select_form.Hide()

            self.form_panel_created = 0

        if self.class_panel_created:
            self.select_class.class_name.SetSelection(-1)

            self.select_class.Hide()

            self.class_panel_created = 0

        if self.subjects_panel_created:
            self.select_subject.subject_name.SetSelection(-1)
            self.select_subject.Hide()

            self.subjects_panel_created = 0

        if self.buttons_panel_created:
            self.buttons_panel.Hide()

        self.exam_data = {
            "year":     0,
            "term":     "",
            "exam_id":  0,
            "exam_name":  "",
            "form":     "",
            "class_id": 0,
            "class_name": "",
            "subject_alias": ""
        }

        # Clear table
        self.show_results.updateResultsOLV("")
        self.show_results.setExamResults()
        self.show_results.Hide()

    #
    # ---------------------------------------------------------
    def getResults(self, event):
        # To get mean of most previous exam
        # 1. Get previous exam's exam_id
        prev_exam_dets = getPreviousExam(self.exam_data)

        # If
        if prev_exam_dets:
            # Switch exam id
            prev_exam_data = {
                "year": prev_exam_dets['year'],
                "term": prev_exam_dets['term'],
                "exam_id": prev_exam_dets['exam_id'],
                "exam_name": prev_exam_dets['exam_name'],
                "form": prev_exam_dets['form'],
                "class_id": self.exam_data['class_id'],
                "class_name": self.exam_data['class_name'],
                "subject_alias": self.exam_data['subject_alias'],
            }

        # check if there are results
        if self.exam_data["subject_alias"] == "All":
            subjects = getActiveSubjectAliases()
            subjects = subjects['aliases']

            mean = getClassMean(self.exam_data, subjects)

            if prev_exam_dets:
                prev_mean = getClassMean(prev_exam_data, subjects)

                # get deviation before concatenating grade to mean
                deviation = calculateDeviation(prev_mean, mean)
            else:
                deviation = ""

            mean = getGradePlusMark(mean)

        else:
            subjects = [self.exam_data["subject_alias"]]

            mean = getSubjectMean(self.exam_data)

            if prev_exam_dets:
                prev_mean = getSubjectMean(prev_exam_data)

                # get deviation before concatenating grade to mean
                deviation = calculateDeviation(prev_mean, mean)
            else:
                deviation = ""

            mean = getGradePlusMark(mean)

        exam_data = getExamResults(self.exam_data, subjects)

        if prev_exam_dets:
            mostImproved = getMostImproved(prev_exam_data, self.exam_data, subjects)
        else:
            mostImproved = ""

        if exam_data:
            if self.results_panel_created == 0:
                self.show_results = ViewResults(self, mean, self.exam_data, deviation, mostImproved)
                self.right_container.Add(self.show_results, 1, wx.ALL | wx.EXPAND, 15)

                self.Layout()

                self.results_panel_created = 1
            else:
                self.show_results.Destroy()
                self.show_results = ViewResults(self, mean, self.exam_data, deviation, mostImproved)
                self.right_container.Add(self.show_results, 1, wx.ALL | wx.EXPAND, 15)

                self.Layout()

            self.show_results.setExamResults()
            self.show_results.updateResultsOLV("")
        else:
            dlg = wx.MessageDialog(None, "No results found. Try a different class.", 'Error Message.', wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            self.select_class.class_name.SetSelection(-1)


class SelectExam(wx.Panel):

    def __init__(self, parent, term, year):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        exam_sizer = wx.BoxSizer(wx.VERTICAL)

        self.exam_label = wx.StaticText(self, wx.ID_ANY, u"Select Exam", wx.DefaultPosition, wx.DefaultSize, 0)
        self.exam_label.Wrap(-1)
        exam_sizer.Add(self.exam_label, 0, wx.ALL, 5)

        self.data = {
            "term": term,
            "year": year
        }

        self.examDets = getExamsinTerm(self.data['term'], self.data['year'])

        self.exam_nameChoices = self.examDets['names_n_form']

        self.exam_name = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     self.exam_nameChoices, wx.CB_READONLY)
        exam_sizer.Add(self.exam_name, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(exam_sizer)
        self.Layout()

        # Connect Events
        self.exam_name.Bind(wx.EVT_COMBOBOX, self.parent.examSelected)


class SelectForm(wx.Panel):

    def __init__(self, parent, form):

        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        form_sizer = wx.BoxSizer(wx.VERTICAL)

        self.form_label = wx.StaticText(self, wx.ID_ANY, u"Select Form", wx.DefaultPosition, wx.DefaultSize, 0)
        self.form_label.Wrap(-1)
        form_sizer.Add(self.form_label, 0, wx.ALL, 5)

        formChoices = [u"1", u"2", u"3", u"4"]
        self.form = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, formChoices,
                                wx.CB_READONLY)
        self.form.SetStringSelection(form)
        self.form.Enable(False)
        form_sizer.Add(self.form, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(form_sizer)
        self.Layout()

        # Connect Events
        self.form.Bind(wx.EVT_COMBOBOX, self.parent.formSelected)


class SelectClass(wx.Panel):

    def __init__(self, parent, form):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        class_sizer = wx.BoxSizer(wx.VERTICAL)

        self.class_label = wx.StaticText(self, wx.ID_ANY, u"Select Class", wx.DefaultPosition, wx.DefaultSize, 0)
        self.class_label.Wrap(-1)
        class_sizer.Add(self.class_label, 0, wx.ALL, 5)

        self.classes = getFormClasses(form)

        class_nameChoices = self.classes['names']
        class_nameChoices.append("All Classes")

        self.class_name = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      class_nameChoices, wx.CB_READONLY)
        class_sizer.Add(self.class_name, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(class_sizer)
        self.Layout()

        # Connect Events
        self.class_name.Bind(wx.EVT_COMBOBOX, self.parent.classSelected)


class SelectSubject(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        subject_sizer = wx.BoxSizer(wx.VERTICAL)

        self.subject_label = wx.StaticText(self, wx.ID_ANY, u"Select Subject", wx.DefaultPosition, wx.DefaultSize, 0)
        self.subject_label.Wrap(-1)
        subject_sizer.Add(self.subject_label, 0, wx.ALL, 5)

        self.subjects = getActiveSubjectAliases()

        subject_choices = self.subjects['names']
        subject_choices.append("All Subjects")

        self.subject_name = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      subject_choices, wx.CB_READONLY)
        subject_sizer.Add(self.subject_name, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(subject_sizer)
        self.Layout()

        # Connect Events
        self.subject_name.Bind(wx.EVT_COMBOBOX, self.parent.subjectSelected)


class ButtonsPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        wrapper_sizer = wx.BoxSizer(wx.VERTICAL)

        btns_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # self.reset_btn = wx.Button(self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0)
        # btns_sizer.Add(self.reset_btn, 1, wx.ALL, 5)


        self.spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.spacer.Wrap(-1)
        btns_sizer.Add(self.spacer, 1, wx.ALL, 5)
        self.save_btn = wx.Button(self, wx.ID_ANY, u"Get Results", wx.DefaultPosition, wx.DefaultSize, 0)
        btns_sizer.Add(self.save_btn, 1, wx.ALL, 5)

        wrapper_sizer.Add(btns_sizer, 1, wx.EXPAND | wx.TOP, 15)

        self.SetSizer(wrapper_sizer)
        self.Layout()

        # Connect Events
        # self.reset_btn.Bind(wx.EVT_BUTTON, self.parent.resetForm)
        self.save_btn.Bind(wx.EVT_BUTTON, self.parent.getResults)


class ViewResults(wx.Panel):
    # ----------------------------------------------------------------------
    def __init__(self, parent, mean, exam_data, deviation, mostImprovedData):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        self.parent = parent
        self.mean = mean
        self.exam_data = exam_data
        self.deviation = deviation

        if mostImprovedData:
            mostImprovedLabel = ""
            if mostImprovedData['nature'] == "Decline":
                mostImprovedLabel = "Least Drop: (All Dropped)"
            elif mostImprovedData['nature'] == "Improve":
                mostImprovedLabel = "Most Improved:"

            mostImprovedStud = ""

            for item in mostImprovedData['student_id']:
                student = getStudentByID(item)
                student_name = student['full_names'] + ", " + str(student['form']) + " " + student['class'] + "\n"
                mostImprovedStud = mostImprovedStud + student_name

            mostImprvdPts = str(mostImprovedData['mark']) + " Points"

        if 'Form' in self.exam_data['class_name']:
            exam_title = "              " + self.exam_data['exam_name'] + " RESULTS"
        else:
            exam_title = str(self.exam_data['form']) + " " + self.exam_data['class_name'] + "              " + self.exam_data['exam_name'] + " RESULTS"

        self.exam_title = exam_title.upper()
        self.term = "TERM " + self.exam_data['term'].upper()
        self.year = str(self.exam_data['year'])

        self.class_id = ""

        if self.parent.exam_data['subject_alias'] == "":
            self.subjects = []
        elif self.parent.exam_data['subject_alias'] == "All":
            subjects = getActiveSubjectAliases()
            self.subjects = subjects['aliases']
        else:
            self.subjects = [self.parent.exam_data['subject_alias']]

        self.results = getExamResults(self.parent.exam_data, self.subjects)

        self.resultsOLV = ObjectListView(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.setExamResults()

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        # Sizer that contains titles at the top
        title_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # space before title starts
        self.spacer_title = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.spacer_title.Wrap(-1)
        self.spacer_title.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        title_sizer.Add(self.spacer_title, 1, wx.ALL, 5)

        # Exam name
        self.exam_title_text = wx.StaticText(self, wx.ID_ANY, self.exam_title, wx.DefaultPosition, wx.DefaultSize, 0)
        self.exam_title_text.Wrap(-1)
        self.exam_title_text.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        title_sizer.Add(self.exam_title_text, 3, wx.ALL, 5)

        # space before term, after exam name
        self.before_term_spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.before_term_spacer.Wrap(-1)
        self.before_term_spacer.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        title_sizer.Add(self.before_term_spacer, 1, wx.ALL, 5)

        # Term exam was taken
        self.term_title = wx.StaticText(self, wx.ID_ANY, self.term, wx.DefaultPosition, wx.DefaultSize, 0)
        self.term_title.Wrap(-1)
        self.term_title.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        title_sizer.Add(self.term_title, 1, wx.ALL, 5)

        # space after term, before year
        self.before_yr_spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.before_yr_spacer.Wrap(-1)
        self.before_yr_spacer.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        title_sizer.Add(self.before_yr_spacer, 1, wx.ALL, 5)

        # Year exam was taken
        self.year_title = wx.StaticText(self, wx.ID_ANY, self.year, wx.DefaultPosition, wx.DefaultSize, 0)
        self.year_title.Wrap(-1)
        self.year_title.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        title_sizer.Add(self.year_title, 0, wx.ALL, 5)

        mainSizer.Add(title_sizer, 0, wx.EXPAND, 5)

        #
        #
        mainSizer.Add(self.resultsOLV, 2, wx.ALL | wx.EXPAND, 5)

        examStatsSizer = wx.BoxSizer(wx.VERTICAL)

        #
        # MEAN SIZER
        mean_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.mean_label = wx.StaticText(self, wx.ID_ANY, u"Class Mean:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.mean_label.Wrap(-1)
        self.mean_label.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        mean_sizer.Add(self.mean_label, 1, wx.ALL, 5)

        self.mean_text = wx.StaticText(self, wx.ID_ANY, self.mean, wx.DefaultPosition, wx.DefaultSize, 0)
        self.mean_text.Wrap(-1)
        self.mean_text.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))

        mean_sizer.Add(self.mean_text, 4, wx.ALL, 5)

        examStatsSizer.Add(mean_sizer, 0, wx.EXPAND, 5)

        #
        # DEVIATION
        if deviation:
            deviation_sizer = wx.BoxSizer(wx.HORIZONTAL)

            self.dev_label = wx.StaticText(self, wx.ID_ANY, u"Deviation:", wx.DefaultPosition, wx.DefaultSize, 0)
            self.dev_label.Wrap(-1)
            self.dev_label.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

            deviation_sizer.Add(self.dev_label, 1, wx.ALL, 5)

            self.dev_text = wx.StaticText(self, wx.ID_ANY, str(self.deviation), wx.DefaultPosition, wx.DefaultSize, 0)
            self.dev_text.Wrap(-1)
            self.dev_text.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))

            deviation_sizer.Add(self.dev_text, 4, wx.ALL, 5)

            examStatsSizer.Add(deviation_sizer, 0, wx.EXPAND, 5)

        # Show only if there are points in mostImprovedData['mark']
        if mostImprovedData and mostImprovedData['mark'] != "--":
            #
            # MOST IMPROVED STUDENT
            most_improved_sizer = wx.BoxSizer(wx.HORIZONTAL)

            self.most_improved_label = wx.StaticText(self, wx.ID_ANY, mostImprovedLabel, wx.DefaultPosition, wx.DefaultSize, 0)
            self.most_improved_label.Wrap(-1)
            self.most_improved_label.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

            most_improved_sizer.Add(self.most_improved_label, 1, wx.ALL, 5)

            self.most_improved_text = wx.StaticText(self, wx.ID_ANY, mostImprovedStud, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
            self.most_improved_text.Wrap(-1)
            self.most_improved_text.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))

            most_improved_sizer.Add(self.most_improved_text, 1, wx.ALL, 5)

            self.most_improved_points = wx.StaticText(self, wx.ID_ANY, mostImprvdPts, wx.DefaultPosition, wx.DefaultSize, 0)
            self.most_improved_points.Wrap(-1)
            self.most_improved_points.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

            most_improved_sizer.Add(self.most_improved_points, 3, wx.ALL, 5)

            examStatsSizer.Add(most_improved_sizer, 0, wx.EXPAND, 5)

        mainSizer.Add(examStatsSizer, 1, wx.EXPAND, 5)

        self.SetSizer(mainSizer)

    # ----------------------------------------------------------------------
    def updateResultsOLV(self, event):
        subjects = []
        if self.parent.exam_data['subject_alias'] != "":
            if self.parent.exam_data['subject_alias'] == "All":
                subjects = getActiveSubjectAliases()
                subjects = subjects['aliases']
            else:
                subjects = [self.parent.exam_data['subject_alias']]

        data = getExamResults(self.parent.exam_data, subjects)
        self.resultsOLV.SetObjects(data)

    # ----------------------------------------------------------------------
    def setExamResults(self, data=None):

        columns_array = [
            ColumnDefn("POS", "center", 50, "number"),
            ColumnDefn("ID", "center", 50, "student_id"),
            ColumnDefn("STUDENT", "left", 100, "names"),
            ColumnDefn("CLASS", "left", 50, "class_name"),
        ]

        if self.parent.exam_data['subject_alias'] != "":
            if self.parent.exam_data['subject_alias'] == "All":
                subjects = getActiveSubjectAliases()
                subjects = subjects['aliases']
            else:
                subjects = [self.parent.exam_data['subject_alias']]

            for i, val in enumerate(subjects):  # adding columns dynamically
                col = ColumnDefn(subjects[i].upper(), "left", 55, subjects[i])
                columns_array.append(col)

            if self.parent.exam_data['subject_alias'] == "All":
                mean = ColumnDefn("MEAN", "left", 55, "student_mean")
                columns_array.append(mean)

        self.resultsOLV.SetColumns(columns_array)

        self.resultsOLV.SetObjects(self.results)


