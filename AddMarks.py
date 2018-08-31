import wx
import wx.xrc

from MarksForm import MarksForm

from db.get_exam_results import *
from db.get_classes import getFormClasses
from db.get_subjects import getActiveSubjectAliases, getSubjectsByTeacher
from db.save_marks import *
# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')


###########################################################################
# Class AddMarks
###########################################################################

class AddMarks(wx.Panel):

    def __init__(self, parent, userdata):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(546, 435),
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent
        self.userdata = userdata

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText98 = wx.StaticText(self, wx.ID_ANY, u"Enter Marks", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText98.Wrap(-1)
        self.m_staticText98.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText98, 0, wx.EXPAND | wx.TOP, 25)

        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_container = wx.BoxSizer(wx.HORIZONTAL)

        self.sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Please fill in order to get student list"), wx.VERTICAL)

        #
        #
        #


        # self.year_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        # year_sizer = wx.BoxSizer(wx.VERTICAL)
        #
        # self.year_label = wx.StaticText(self.year_panel, wx.ID_ANY, u"Select Year", wx.DefaultPosition, wx.DefaultSize,
        #                                 0)
        # self.year_label.Wrap(-1)
        # year_sizer.Add(self.year_label, 0, wx.ALL, 5)
        #
        # current_year = int(datetime.now().year)
        # self.year = wx.TextCtrl(self.year_panel, wx.ID_ANY, str(current_year), wx.DefaultPosition,
        #                         wx.DefaultSize,
        #                         wx.TE_READONLY)
        # year_sizer.Add(self.year, 0, wx.ALL | wx.EXPAND, 5)
        #
        # self.year_panel.SetSizer(year_sizer)
        # self.year_panel.Layout()
        # year_sizer.Fit(self.year_panel)
        # self.sbSizer2.Add(self.year_panel, 0, wx.EXPAND | wx.ALL, 5)

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

        self.select_subject = SelectSubject(self)
        self.sbSizer2.Add(self.select_subject, 0, wx.EXPAND | wx.ALL, 5)

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
        self.term_panel.Hide()
        self.sbSizer2.Add(self.term_panel, 0, wx.EXPAND | wx.ALL, 5)

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
        self.buttons_panel_created = 0

        self.exam_data = {
            "year":     0,
            "term":     "",
            "exam_id":  0,
            "form":     "",
            "class_id": 0,
            "class": "",
            "subject_alias": ""
        }

        #
        #
        #

        left_container.Add(self.sbSizer2, 0, wx.ALL | wx.EXPAND, 15)

        horizontal_sizer.Add(left_container, 2, wx.EXPAND, 5)

        #
        #  ==================================================================================
        #                               RIGHT SIDE
        #  ==================================================================================
        #

        self.right_container = wx.BoxSizer(wx.VERTICAL)

        self.marks_panel_created = 0

        exam_dets = {
            'exam_id': 0,
            'exam_name': "",
            'form': 0,
            'term': "",
            'year': 0,
            'form_name': "",
            'subject': "",
            'class': ""
        }

        self.show_student_list = MarksForm(self, [], exam_dets)
        self.show_student_list.Hide()
        self.right_container.Add(self.show_student_list, 1, wx.ALL | wx.EXPAND, 15)

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

    def subjectSelected(self, event):
        self.term_panel.Show()
        self.Layout()

        alias = self.select_subject.subject_name.GetStringSelection()

        self.exam_data['subject_alias'] = alias

    def termSelected(self, event):
        year = self.exam_data['year']
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

                # Disable changing term to avoid inconsistency
                self.term.Enable(False)
        else:
            dlg = wx.MessageDialog(None, "No exams found in " + str(year) + " Term " + term + ".",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            ret = dlg.ShowModal()
            if ret == wx.ID_OK:
                self.term.SetSelection(-1)

                self.term.Enable(True)

                self.exam_data['term'] = ""
            dlg.Destroy()

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

        if not self.buttons_panel_created:
            self.buttons_panel = ButtonsPanel(self)
            self.sbSizer2.Add(self.buttons_panel, 0, wx.EXPAND | wx.ALL, 5)
            self.Layout()
            self.buttons_panel_created = 1  # change to 1 so it's not created again

        # get index of class selected in order to match with ID's list
        classIndex = self.select_class.class_name.GetCurrentSelection()
        class_name = self.select_class.class_name.GetStringSelection()

        class_id = self.select_class.classes['ids'][classIndex]

        self.exam_data['class_id'] = class_id
        self.exam_data['class'] = class_name

    def resetForm(self, event):
        self.year.SetSelection(-1)
        self.term.SetSelection(-1)
        self.select_exam.exam_name.SetSelection(-1)
        self.select_form.form.SetSelection(-1)
        self.select_class.class_name.SetSelection(-1)
        self.select_subject.subject_name.SetSelection(-1)

        self.term.Enable(True)
        self.select_exam.exam_name.Enable(True)
        self.select_form.form.Enable(True)

        self.term_panel.Hide()
        self.select_exam.Hide()
        self.select_form.Hide()
        self.select_class.Hide()
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
            "class": "",
            "subject_alias": ""
        }

        if self.marks_panel_created == 1:
            self.show_student_list.HideWithEffect(wx.SHOW_EFFECT_SLIDE_TO_LEFT, 1000)

    def getStudentList(self, event):
        marksExist = checkIfMarksAlreadyEntered(self.exam_data, [self.exam_data['subject_alias']])

        students = getStudentList(self.exam_data)
        exam_details = getExamDetails(self.exam_data)

        if not self.marks_panel_created:
            self.show_student_list = MarksForm(self, students, exam_details[0])
            self.right_container.Add(self.show_student_list, 1, wx.ALL | wx.EXPAND, 15)

            self.Layout()

            self.marks_panel_created = 1
        else:
            self.show_student_list.HideWithEffect(wx.SHOW_EFFECT_ROLL_TO_RIGHT, 1000)
            self.show_student_list = MarksForm(self, students, exam_details[0])
            self.right_container.Add(self.show_student_list, 1, wx.ALL | wx.EXPAND, 15)

            self.Layout()


class SelectSubject(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        subject_sizer = wx.BoxSizer(wx.VERTICAL)

        self.subject_label = wx.StaticText(self, wx.ID_ANY, u"Select Subject", wx.DefaultPosition, wx.DefaultSize, 0)
        self.subject_label.Wrap(-1)
        subject_sizer.Add(self.subject_label, 0, wx.ALL, 5)

        # self.subjects = getActiveSubjectAliases()
        #
        # subject_choices = self.subjects['names']

        subject_choices = []

        # populate combo box with subjects the teacher logged in teachers
        teacher_subject_data = getSubjectsByTeacher(self.parent.userdata['user_id'])

        subject_choices.append(teacher_subject_data['subject_alias1'])

        if teacher_subject_data['subject_alias2'] is not None:
            subject_choices.append(teacher_subject_data['subject_alias2'])

        self.subject_name = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      subject_choices, wx.CB_READONLY)
        subject_sizer.Add(self.subject_name, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(subject_sizer)
        self.Layout()

        # Connect Events
        self.subject_name.Bind(wx.EVT_COMBOBOX, self.parent.subjectSelected)


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

        self.class_name = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      class_nameChoices, wx.CB_READONLY)
        class_sizer.Add(self.class_name, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(class_sizer)
        self.Layout()

        # Connect Events
        self.class_name.Bind(wx.EVT_COMBOBOX, self.parent.classSelected)


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

        self.save_btn = wx.Button(self, wx.ID_ANY, u"Enter Marks", wx.DefaultPosition, wx.DefaultSize, 0)
        btns_sizer.Add(self.save_btn, 0, wx.ALL, 5)

        wrapper_sizer.Add(btns_sizer, 1, wx.EXPAND | wx.TOP, 15)

        self.SetSizer(wrapper_sizer)
        self.Layout()

        # Connect Events
        self.reset_btn.Bind(wx.EVT_BUTTON, self.parent.resetForm)
        self.save_btn.Bind(wx.EVT_BUTTON, self.parent.getStudentList)