import wx
import wx.xrc
from ObjectListView import ObjectListView, ColumnDefn
from datetime import datetime

from db.get_exams import *
from db.save_exam import editExam, deleteExam
from db.get_subjects import getActiveSubjectAliases
from db.get_exam_results import getExamResults

# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')

###########################################################################
# Class ViewExams
###########################################################################


class ViewExams(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(669, 428),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"All Exams", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText17, 0, wx.TOP | wx.EXPAND, 25)

        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_sizer = wx.BoxSizer(wx.HORIZONTAL)
        OLV_sizer = wx.BoxSizer(wx.VERTICAL)

        #
        # Classes Object list View
        # ----------------------------------------------------------------
        # Search
        # ----------------------------------------------------------------
        search_container = wx.BoxSizer(wx.HORIZONTAL)
        self.refresh_btn = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"images/reload_16x16.bmp", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)

        self.refresh_btn.SetBitmapHover(wx.Bitmap(u"images/reload_16x16_rotated.bmp", wx.BITMAP_TYPE_ANY))
        search_container.Add(self.refresh_btn, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT, 5)

        self.m_staticText53 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText53.Wrap(-1)
        search_container.Add(self.m_staticText53, 1, wx.ALL, 5)

        self.search_exams = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            wx.TE_PROCESS_ENTER)
        self.search_exams.ShowSearchButton(True)
        self.search_exams.ShowCancelButton(False)
        search_container.Add(self.search_exams, 0, wx.BOTTOM, 8)

        self.search_exams.Bind(wx.EVT_TEXT, self.searchExams)
        self.search_exams.Bind(wx.EVT_TEXT_ENTER, self.searchExams)

        OLV_sizer.Add(search_container, 0, wx.EXPAND, 5)
        #
        #
        # ----------------------------------------------------------------
        # Table
        # ----------------------------------------------------------------
        self.exams = getAllExams()

        self.examsOLV = ObjectListView(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.setExamData()

        OLV_sizer.Add(self.examsOLV, 1, wx.EXPAND | wx.ALL, 5)

        # ----------------------------------------------------------------
        #
        #

        left_btns_sizer = wx.BoxSizer(wx.VERTICAL)

        self.view_results_btn = wx.Button(self, wx.ID_ANY, u"View Results", wx.DefaultPosition, wx.DefaultSize, 0)
        self.view_results_btn.Bind(wx.EVT_BUTTON, self.fetchExamResults)
        left_btns_sizer.Add(self.view_results_btn, 0, wx.EXPAND | wx.ALL, 5)

        self.edit_exam_btn = wx.Button(self, wx.ID_ANY, u"Edit Exam", wx.DefaultPosition, wx.DefaultSize, 0)
        self.edit_exam_btn.Bind(wx.EVT_BUTTON, self.getExamInfo)
        left_btns_sizer.Add(self.edit_exam_btn, 0, wx.ALL | wx.EXPAND, 5)

        self.delete_exam_btn = wx.Button(self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        self.delete_exam_btn.Bind(wx.EVT_BUTTON, self.deleteExam)
        left_btns_sizer.Add(self.delete_exam_btn, 0, wx.ALL | wx.EXPAND, 5)

        #
        #
        left_sizer.Add(OLV_sizer, 3, wx.EXPAND | wx.ALL, 5)
        left_sizer.Add(left_btns_sizer, 1, wx.ALL, 5)

        horizontal_sizer.Add(left_sizer, 0, wx.EXPAND, 5)

        self.right_sizer = wx.BoxSizer(wx.VERTICAL)

        self.exam_data = {
            "exam_id": 0,
            "class_id": 0,
            "form": 0,
            "subject_alias": "",
            "year": 0,
            "term": "",
            "exam_name": ""
        }

        self.edit_exam_panel = EditExam(self)
        # self.edit_exam_panel.Hide()
        #
        self.show_results = ViewResults(self, self.exam_data)
        self.show_results.Hide()

        self.show_results_panel_added = 0

        #
        #
        #
        self.right_sizer.Add(self.edit_exam_panel, 1, wx.EXPAND)
        self.right_sizer.Add(self.show_results, 1, wx.EXPAND)

        horizontal_sizer.Add(self.right_sizer, 1, wx.EXPAND, 5)

        container.Add(horizontal_sizer, 1, wx.ALL | wx.EXPAND, 10)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.refresh_btn.Bind(wx.EVT_BUTTON, self.refreshTable)

    #
    #
    # ------------------------------------------------------------------------------
    def setExamData(self, data=None):
        self.examsOLV.SetColumns([
            ColumnDefn("ID", "left", 60, "exam_id"),
            ColumnDefn("Year", "center", 70, "year"),
            ColumnDefn("Name", "center", 100, "exam_name"),
            ColumnDefn("Form", "center", 100, "form"),
            ColumnDefn("Term", "center", 70, "term"),
        ])

        self.examsOLV.SetObjects(self.exams)

    #
    # ------------------------------------------------------------------------------
    def updateExamsOLV(self, event):  # Refresh classes table
        """"""
        data = getAllExams()
        self.examsOLV.SetObjects(data)

    #
    # ------------------------------------------------------------------------------
    def refreshTable(self, event):
        self.updateExamsOLV("")

    #
    # ------------------------------------------------------------------------------
    def searchExams(self, event):
        search = self.search_exams.GetLineText(0)
        data = getAllExams(search)
        self.examsOLV.SetObjects(data)

    #
    # ------------------------------------------------------------------------------
    def fetchExamResults(self, event):
        rowObj = self.examsOLV.GetSelectedObject()

        form = getFormsInExam(rowObj['exam_id'])

        if form == "All":
            choices =[u"Form 1", u"Form 2", u"Form 3", u"Form 4"]

            formChosen = wx.GetSingleChoice(message="Select Form to View Results", caption="Exam Results.",
                                            choices=choices, parent=None)
        else:
            formChosen = form

        if formChosen == "Form 1" or formChosen == "One":
            formChosen = 1
        elif formChosen == "Form 2" or formChosen == "Two":
            formChosen = 2
        elif formChosen == "Form 3" or formChosen == "Three":
            formChosen = 3
        elif formChosen == "Form 4" or formChosen == "Four":
            formChosen = 4

        subjectChoices = getActiveSubjectAliases()
        subjectChoices = subjectChoices['aliases']
        subjectChoices.insert(0, "All Subjects")

        subjectChosen = wx.GetSingleChoice(message="Select Subject.", caption="Exam Results.",
                                        choices=subjectChoices, parent=None)

        if subjectChosen == "All Subjects":
            alias = "All"
            subjects = getActiveSubjectAliases()
            subjects = subjects['aliases']
        else:
            alias = subjectChosen
            subjects = [subjectChosen]

        self.exam_data = {
            "exam_id": rowObj['exam_id'],
            "class_id": 0,
            "form": formChosen,
            "subject_alias": alias,
            "year": rowObj['year'],
            "term": rowObj['term'],
            "exam_name": rowObj['exam_name'],
        }

        data = getExamResults(self.exam_data, subjects)
        if data:
            self.edit_exam_panel.Hide()
            # self.show_results.Hide()
            #
            # self.show_results = ViewResults(self, self.exam_data)
            # self.show_results.setExamResults()
            # self.show_results.updateResultsOLV("")
            # self.show_results.Show()
            #
            # self.Layout()

            if self.show_results_panel_added == 0:
                self.show_results = ViewResults(self, self.exam_data)
                self.right_sizer.Add(self.show_results, 1, wx.EXPAND)

                self.Layout()

                self.show_results_panel_added = 1
            else:
                self.show_results.Destroy()
                self.show_results = ViewResults(self, self.exam_data)
                self.right_sizer.Add(self.show_results, 1, wx.EXPAND)

                self.Layout()
        else:
            dlg = wx.MessageDialog(None, "No results for selected exam.",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()

            self.show_results.Hide()
            self.edit_exam_panel.Show()

            self.Layout()

    #
    # ------------------------------------------------------------------------------
    def getExamInfo(self, event):
        if not self.examsOLV.GetSelectedObject():
            dlg = wx.MessageDialog(None, "Click on a row in order to edit exam.",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            rowObj = self.examsOLV.GetSelectedObject()

            self.edit_exam_panel.exam_id.SetValue(str(rowObj['exam_id']))
            self.edit_exam_panel.exam_name.SetValue(rowObj['exam_name'])
            self.edit_exam_panel.year.SetValue(rowObj['year'])
            self.edit_exam_panel.term.SetValue(rowObj['term'])
            self.edit_exam_panel.form.SetValue(rowObj['form'])

            self.show_results.Hide()
            self.edit_exam_panel.Show()

    #
    # ------------------------------------------------------------------------------
    def deleteExam(self, event):
        if self.examsOLV.GetSelectedObject():
            rowObj = self.examsOLV.GetSelectedObject()

            dlg = wx.MessageDialog(None, "Are you sure? \nYou will lose access to all results under this exam.", 'Warning Message.', wx.YES_NO | wx.ICON_WARNING)
            retCode = dlg.ShowModal()
            dlg.Destroy()

            if retCode == wx.ID_YES:
                if deleteExam(rowObj["exam_id"]):
                    dlg = wx.MessageDialog(None, "Exam deleted successfully.", 'Success Message.',
                                           wx.OK | wx.ICON_EXCLAMATION)
                    dlg.ShowModal()
                    dlg.Destroy()

                    self.updateExamsOLV("")

            else:
                rowObj=""

        else:
            dlg = wx.MessageDialog(None, "Click on a row to delete a class.", 'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()


class EditExam(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(567, 444),
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        bSizer48 = wx.BoxSizer(wx.VERTICAL)

        bSizer73 = wx.BoxSizer(wx.HORIZONTAL)

        left_spacer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        left_spacer.Add(self.m_staticText30, 1, wx.ALL | wx.EXPAND, 5)

        bSizer73.Add(left_spacer, 1, wx.EXPAND, 5)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        form_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Edit Exam Form"), wx.VERTICAL)

        #
        # hidden class id field
        #
        exam_id_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.exam_id = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.exam_id.Hide()

        exam_id_sizer.Add(self.exam_id, 0, wx.ALL, 10)

        form_sizer.Add(exam_id_sizer, 1, wx.EXPAND, 5)
        #
        #
        #

        exam_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.statictext = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Exam Name", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.statictext.Wrap(-1)
        exam_name_sizer.Add(self.statictext, 1, wx.ALL, 10)

        self.exam_name = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        exam_name_sizer.Add(self.exam_name, 4, wx.ALL, 10)

        form_sizer.Add(exam_name_sizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 10)

        year_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.year_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.year_label.Wrap(-1)
        year_sizer.Add(self.year_label, 1, wx.ALL, 10)

        self.year = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                wx.DefaultSize, 0)
        year_sizer.Add(self.year, 4, wx.ALL, 10)

        form_sizer.Add(year_sizer, 1, wx.ALL | wx.EXPAND, 10)

        term_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.term_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Term", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.term_label.Wrap(-1)
        term_sizer.Add(self.term_label, 1, wx.ALL, 10)

        termChoices = [u"One", u"Two", u"Three"]
        self.term = wx.ComboBox(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                termChoices, wx.CB_READONLY)
        term_sizer.Add(self.term, 4, wx.ALL, 10)

        form_sizer.Add(term_sizer, 1, wx.ALL | wx.EXPAND, 10)

        form_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.form_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Form", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.form_label.Wrap(-1)
        form_name_sizer.Add(self.form_label, 1, wx.ALL, 10)

        formChoices = [u"All", u"One", u"Two", u"Three", u"Four"]
        self.form = wx.ComboBox(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                formChoices, wx.CB_READONLY)
        form_name_sizer.Add(self.form, 4, wx.ALL, 10)

        form_sizer.Add(form_name_sizer, 1, wx.ALL | wx.EXPAND, 10)

        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        buttons_sizer.Add(self.m_staticText22, 1, wx.ALL, 5)

        self.cancel_edit_btn = wx.Button(form_sizer.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        buttons_sizer.Add(self.cancel_edit_btn, 0, wx.ALL, 10)

        self.edit_exam_btn = wx.Button(form_sizer.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        buttons_sizer.Add(self.edit_exam_btn, 0, wx.ALL, 10)

        form_sizer.Add(buttons_sizer, 4, wx.ALL | wx.EXPAND, 10)

        bSizer36.Add(form_sizer, 1, 0, 50)

        bSizer73.Add(bSizer36, 1, wx.ALL | wx.EXPAND, 5)

        right_spacer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText302 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText302.Wrap(-1)
        right_spacer.Add(self.m_staticText302, 1, wx.ALL | wx.EXPAND, 5)

        bSizer73.Add(right_spacer, 1, wx.EXPAND, 5)

        bSizer48.Add(bSizer73, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer48)
        self.Layout()

        # Connect Events
        self.cancel_edit_btn.Bind(wx.EVT_BUTTON, self.cancelEditExam)
        self.edit_exam_btn.Bind(wx.EVT_BUTTON, self.editExam)

    def __del__(self):
        pass

    #
    # ------------------------------------------------------------
    def cancelEditExam(self, event):
        self.exam_id.SetValue("")
        self.exam_name.SetValue("")
        self.year.SetValue("")
        self.term.SetSelection(-1)
        self.form.SetSelection(-1)

    #
    # ------------------------------------------------------------
    def editExam(self, event):
        exam_id = self.exam_id.GetLineText(0)

        if exam_id == "":  # Check that a class has been selected before starting validation
            dlg = wx.MessageDialog(None, "Please select an exam to edit.", 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
            self.cancelEditExam("")
        else:
            exam_id = self.exam_id.GetLineText(0)
            exam_name = self.exam_name.GetLineText(0)
            year = self.year.GetLineText(0)
            termIndex = self.term.GetCurrentSelection()
            formIndex = self.form.GetCurrentSelection()

            # Remove white spaces
            exam_name = exam_name.replace(" ", "")

            #
            # ---------- VALIDATION ----------
            error = ""

            if exam_name == "":
                error = error + "The Exam Name field  is required.\n"

            if formIndex == -1:
                error = error + "The Form field is required.\n"

            if termIndex == -1:
                error = error + "The Term field is required.\n"

            if error:
                dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
                dlg.ShowModal()
                dlg.Destroy()

            else:
                form = self.form.GetString(formIndex)
                term = self.term.GetString(termIndex)

                data = {
                    "exam_id": exam_id,
                    "exam_name": exam_name,
                    "year": year,
                    "form": form,
                    "term": term
                }

                if editExam(data):
                    dlg = wx.MessageDialog(None, "Exam Edited Successfully.", 'Success Message',
                                           wx.OK | wx.ICON_INFORMATION)
                    retCode = dlg.ShowModal()
                    if retCode == wx.ID_OK:
                        """"""
                        self.parent.updateExamsOLV("")
                        self.cancelEditExam("")
                    dlg.Destroy()

                else:
                    dlg = wx.MessageDialog(None, "Exam Not Edited. Try Again.", 'Failed',
                                           wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()
                    dlg.Destroy()


class ViewResults(wx.Panel):
    # ----------------------------------------------------------------------
    def __init__(self, parent, exam_dets):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        self.parent = parent
        self.exam_dets = exam_dets

        exam_title = "FORM " + str(self.exam_dets['form']) + "              " + self.exam_dets['exam_name'] + " RESULTS"

        self.exam_title = exam_title.upper()
        self.term = "TERM " + self.exam_dets['term'].upper()
        self.year = str(self.exam_dets['year'])

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

        #
        #
        #
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

        mainSizer.Add(title_sizer, 0, wx.ALL | wx.EXPAND, 5)

        #
        #
        #

        mainSizer.Add(self.resultsOLV, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(mainSizer)

    #
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

    #
    # ----------------------------------------------------------------------
    def refreshTable(self, event):
        self.updateResultsOLV("")

    #
    # ----------------------------------------------------------------------
    def setExamResults(self, data=None):

        columns_array = [
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
                mean = ColumnDefn("MEAN", "left", 55, "student_mean")
                columns_array.append(mean)

        self.resultsOLV.SetColumns(columns_array)

        self.resultsOLV.SetObjects(self.results)