import wx
import wx.xrc
from ObjectListView import ObjectListView, ColumnDefn

from db.get_exam_results import *
from db.get_classes import getFormClasses
from db.get_subjects import getActiveSubjectAliases
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
            "form":     "",
            "class_id": 0,
            "subject_alias": ""
        }

        #
        #
        #
        left_container.Add(self.sbSizer2, 1, wx.ALL | wx.EXPAND, 15)
        # left_container.Add(self.sbSizer, 1, wx.ALL | wx.EXPAND, 15)

        horizontal_sizer.Add(left_container, 0, wx.EXPAND, 5)

        #
        #  ==================================================================================
        #                               RIGHT SIDE
        #  ==================================================================================
        #

        self.right_container = wx.BoxSizer(wx.VERTICAL)

        self.show_results = ViewResults(self, "")
        self.show_results.Hide()
        self.right_container.Add(self.show_results, 1, wx.ALL | wx.EXPAND, 15)

        self.results_panel_created = 0

        horizontal_sizer.Add(self.right_container, 5, wx.EXPAND, 5)

        container.Add(horizontal_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.year.Bind(wx.EVT_COMBOBOX, self.yearSelected)
        self.term.Bind(wx.EVT_COMBOBOX, self.termSelected)

    def __del__(self):
        pass

    def yearSelected(self, event):
        year = self.year.GetStringSelection()
        self.exam_data['year'] = year

        self.term_panel.Show()
        self.Layout()

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

    def examSelected(self, event):

        if not self.form_panel_created:
            self.select_form = SelectForm(self)
            self.sbSizer2.Add(self.select_form, 0, wx.EXPAND | wx.ALL, 5)
            self.Layout()

            self.form_panel_created = 1  # change to 1 so it's not created again

        exam = self.select_exam.exam_name.GetCurrentSelection()  # get index of exam selected
        exam_id = self.select_exam.examDets['ids'][exam]

        self.exam_data['exam_id'] = exam_id

    def formSelected(self, event):
        form = self.select_form.form.GetCurrentSelection() + 1

        self.exam_data['form'] = form

        if not self.class_panel_created:
            self.select_class = SelectClass(self, form)
            self.sbSizer2.Add(self.select_class, 0, wx.EXPAND | wx.ALL, 5)
            self.Layout()

            self.class_panel_created = 1  # change to 1 so it's not created again

            #  Disable changing exam and form to avoid inconsistency
            self.select_exam.exam_name.Enable(False)
            self.select_form.form.Enable(False)

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

        self.exam_data['class_id'] = class_id

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

    def resetForm(self, event):
        self.year.SetSelection(-1)
        self.term.SetSelection(-1)
        self.select_exam.exam_name.SetSelection(-1)
        self.select_form.form.SetSelection(-1)
        self.select_class.class_name.SetSelection(-1)
        self.select_subject.subject_name.SetSelection(-1)

        self.year.Enable(True)
        self.term.Enable(True)
        self.select_exam.exam_name.Enable(True)
        self.select_form.form.Enable(True)

        self.term_panel.Hide()
        self.select_exam.Hide()
        self.select_form.Hide()
        self.select_class.Hide()
        self.select_subject.Hide()
        self.buttons_panel.Hide()

        self.exam_panel_created = 0
        self.form_panel_created = 0
        self.class_panel_created = 0
        self.subjects_panel_created = 0
        self.buttons_panel_created = 0

        self.exam_data = {
            "year":     0,
            "term":     "",
            "exam_id":  0,
            "form":     "",
            "class_id": 0,
            "subject_alias": ""
        }

        # Clear table
        self.show_results.updateResultsOLV("")
        self.show_results.setExamResults()

    def getResults(self, event):
        # check if there are results

        if self.exam_data["subject_alias"] == "All":
            subjects = getActiveSubjectAliases()
            subjects = subjects['aliases']
            mean = getClassMean(self.exam_data, subjects)
        else:
            subjects = [self.exam_data["subject_alias"]]
            mean = getSubjectMean(self.exam_data)

        exam_data = getExamResults(self.exam_data, subjects)

        if exam_data:
            if self.results_panel_created == 0:
                self.show_results = ViewResults(self, mean)
                # self.show_results.Hide()
                self.right_container.Add(self.show_results, 1, wx.ALL | wx.EXPAND, 15)

                self.Layout()

                self.results_panel_created = 1
            else:
                self.show_results.Destroy()
                self.show_results = ViewResults(self, mean)
                self.right_container.Add(self.show_results, 1, wx.ALL | wx.EXPAND, 15)

                self.Layout()

            self.show_results.setExamResults()
            self.show_results.updateResultsOLV("")
        else:
            dlg = wx.MessageDialog(None, "No results found. Try a different class.", 'Error Message.', wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
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

        self.exam_nameChoices = self.examDets['names']

        self.exam_name = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     self.exam_nameChoices, wx.CB_READONLY)
        exam_sizer.Add(self.exam_name, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(exam_sizer)
        self.Layout()

        # Connect Events
        self.exam_name.Bind(wx.EVT_COMBOBOX, self.parent.examSelected)


class SelectForm(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        form_sizer = wx.BoxSizer(wx.VERTICAL)

        self.form_label = wx.StaticText(self, wx.ID_ANY, u"Select Form", wx.DefaultPosition, wx.DefaultSize, 0)
        self.form_label.Wrap(-1)
        form_sizer.Add(self.form_label, 0, wx.ALL, 5)

        formChoices = [u"One", u"Two", u"Three", u"Four"]
        self.form = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, formChoices,
                                wx.CB_READONLY)
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

        self.spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.spacer.Wrap(-1)
        btns_sizer.Add(self.spacer, 1, wx.ALL, 5)

        self.reset_btn = wx.Button(self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0)
        btns_sizer.Add(self.reset_btn, 0, wx.ALL, 5)

        self.save_btn = wx.Button(self, wx.ID_ANY, u"Get Results", wx.DefaultPosition, wx.DefaultSize, 0)
        btns_sizer.Add(self.save_btn, 0, wx.ALL, 5)

        wrapper_sizer.Add(btns_sizer, 1, wx.EXPAND | wx.TOP, 15)

        self.SetSizer(wrapper_sizer)
        self.Layout()

        # Connect Events
        self.reset_btn.Bind(wx.EVT_BUTTON, self.parent.resetForm)
        self.save_btn.Bind(wx.EVT_BUTTON, self.parent.getResults)


class ViewResults(wx.Panel):
    # ----------------------------------------------------------------------
    def __init__(self, parent, mean):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        self.parent = parent
        self.mean = mean

        self.class_id = ""
        # subjects = getActiveSubjectAliases()
        # self.subjects = subjects['aliases']

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

        # Create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        mean_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.mean_label = wx.StaticText(self, wx.ID_ANY, u"Class Mean:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.mean_label.Wrap(-1)
        self.mean_label.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        mean_sizer.Add(self.mean_label, 1, wx.ALL, 5)

        self.mean_text = wx.StaticText(self, wx.ID_ANY, self.mean, wx.DefaultPosition, wx.DefaultSize, 0)
        self.mean_text.Wrap(-1)
        self.mean_text.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))

        mean_sizer.Add(self.mean_text, 2, wx.ALL, 5)

        mainSizer.Add(mean_sizer, 0, wx.EXPAND, 5)

        mainSizer.Add(self.resultsOLV, 1, wx.ALL | wx.EXPAND, 5)

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
            ColumnDefn("Pos", "center", 50, "number"),
            ColumnDefn("ID", "center", 50, "exam_result_id"),
            ColumnDefn("Student", "left", 100, "names"),
            ColumnDefn("Class", "left", 50, "form"),
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
                mean = ColumnDefn("Mean", "left", 55, "student_mean")
                columns_array.append(mean)

        self.resultsOLV.SetColumns(columns_array)

        self.resultsOLV.SetObjects(self.results)


