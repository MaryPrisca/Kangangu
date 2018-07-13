import wx
import wx.xrc
from ObjectListView import ObjectListView, ColumnDefn
from datetime import datetime

from db.get_exams import getAllExams
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

        self.m_staticText54 = wx.StaticText(self, wx.ID_ANY, u"Search:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText54.Wrap(-1)
        search_container.Add(self.m_staticText54, 0, wx.ALL, 5)

        self.search_exams = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_PROCESS_ENTER)
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
        self.view_results_btn.Bind(wx.EVT_BUTTON, self.getExamResults)
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

        horizontal_sizer.Add(left_sizer, 1, wx.EXPAND, 5)

        right_sizer = wx.BoxSizer(wx.VERTICAL)


        self.edit_exam_panel = EditExam(self)
        #
        # self.show_students = ViewClassStudents(self)

        #
        #
        #
        right_sizer.Add(self.edit_exam_panel, 1, wx.EXPAND)
        # right_sizer.Add(self.show_students, 1, wx.EXPAND)
        # self.show_students.Hide()

        horizontal_sizer.Add(right_sizer, 1, wx.EXPAND, 5)

        container.Add(horizontal_sizer, 1, wx.ALL | wx.EXPAND, 10)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.refresh_btn.Bind(wx.EVT_BUTTON, self.refreshTable)

    def setExamData(self, data=None):
        self.examsOLV.SetColumns([
            ColumnDefn("ID", "left", 80, "exam_id"),
            ColumnDefn("Year", "center", 100, "year"),
            ColumnDefn("Term", "center", 100, "term"),
            ColumnDefn("Name", "center", 80, "exam_name"),
            # ColumnDefn("Form", "center", 100, "form"),
        ])

        self.examsOLV.SetObjects(self.exams)

    def updateExamsOLV(self, event):  # Refresh classes table
        """"""
        data = getAllExams()
        self.examsOLV.SetObjects(data)

    def refreshTable(self, event):
        self.updateExamsOLV("")

    def searchExams(self, event):
        search = self.search_exams.GetLineText(0)
        data = getAllExams(search)
        self.examsOLV.SetObjects(data)

    def getExamResults(self, event):
        """"""

    def getExamInfo(self, event):
        if not self.examsOLV.GetSelectedObject():
            dlg = wx.MessageDialog(None, "Click on a row in order to edit exam.",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
        else:
            rowObj = self.examsOLV.GetSelectedObject()

            self.edit_exam_panel.exam_id.SetValue(str(rowObj['exam_id']))
            self.edit_exam_panel.exam_name.SetValue(rowObj['exam_name'])
            self.edit_exam_panel.year.SetValue(rowObj['year'])
            self.edit_exam_panel.term.SetValue(rowObj['term'])
            self.edit_exam_panel.form.SetValue(rowObj['form'])

            # self.show_students.Hide()
            self.edit_exam_panel.Show()

    def deleteExam(self, event):
        if self.examsOLV.GetSelectedObject():
            rowObj = self.examsOLV.GetSelectedObject()

            dlg = wx.MessageDialog(None, "Are you sure? \nYou will lose access to all results under this exam.", 'Warning Message.', wx.YES_NO | wx.ICON_WARNING)
            retCode = dlg.ShowModal()

            if retCode == wx.ID_YES:
                if deleteExam(rowObj["exam_id"]):
                    dlg = wx.MessageDialog(None, "Exam deleted successfully.", 'Success Message.',
                                           wx.OK | wx.ICON_EXCLAMATION)
                    dlg.ShowModal()

                    self.updateExamsOLV("")

            else:
                dlg.Destroy()
                rowObj=""


        else:
            dlg = wx.MessageDialog(None, "Click on a row to delete a class.", 'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()


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

    # Virtual event handlers, overide them in your derived class
    def cancelEditExam(self, event):
        self.exam_id.SetValue("")
        self.exam_name.SetValue("")
        self.year.SetValue("")
        self.term.SetSelection(-1)
        self.form.SetSelection(-1)

    def editExam(self, event):
        exam_id = self.exam_id.GetLineText(0)

        if exam_id == "":  # Check that a class has been selected before starting validation
            dlg = wx.MessageDialog(None, "Please select an exam to edit.", 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
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

                else:
                    dlg = wx.MessageDialog(None, "Exam Not Edited. Try Again.", 'Failed',
                                           wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()


class ViewResults(wx.Panel):
    # ----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        self.parent = parent

        self.class_id = ""
        subjects = getActiveSubjectAliases()
        self.subjects = subjects['aliases']

        self.results = getExamResults(self.parent.exam_data, self.subjects)

        self.resultsOLV = ObjectListView(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.setExamResults()

        # Create some sizers
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)

        mainSizer.Add(self.resultsOLV, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(mainSizer)

    # ----------------------------------------------------------------------
    def updateResultsOLV(self, event):
        """"""
        data = getExamResults(self.parent.exam_data, self.subjects)
        self.resultsOLV.SetObjects(data)

    # ----------------------------------------------------------------------
    def refreshTable(self, event):
        self.updateResultsOLV("")

    # ----------------------------------------------------------------------
    def setExamResults(self, data=None):

        columns_array = [
            ColumnDefn("ID", "center", 100, "exam_result_id"),
            ColumnDefn("Student", "left", 135, "names"),
            ColumnDefn("Class", "left", 65, "form"),
        ]

        if self.parent.exam_data['subject_alias'] != "":
            if self.parent.exam_data['subject_alias'] == "All":
                subjects = getActiveSubjectAliases()
                subjects = subjects['aliases']
            else:
                subjects = [self.parent.exam_data['subject_alias']]

            for i, val in enumerate(subjects):  # adding columns dynamically
                col = ColumnDefn(subjects[i].upper(), "left", 65, subjects[i])
                columns_array.append(col)

        self.resultsOLV.SetColumns(columns_array)

        self.resultsOLV.SetObjects(self.results)