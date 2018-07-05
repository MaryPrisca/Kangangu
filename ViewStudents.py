import wx
from ObjectListView import ObjectListView, ColumnDefn
from db.get_students import getStudents
from db.save_student import editStudent, deleteStudent
from db.get_classes import getClassNames
from datetime import datetime

# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')


class ViewStudents(wx.Panel):
    # ----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        # Create some sizers
        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"View Students", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText17, 0, wx.TOP | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 25)

        mainSizer = wx.BoxSizer(wx.HORIZONTAL)

        left_sizer = wx.BoxSizer(wx.HORIZONTAL)

        #
        #
        # Search container
        # ----------------------------------------------------------------------------------
        #

        search_container = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText53 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText53.Wrap(-1)
        search_container.Add(self.m_staticText53, 1, wx.ALL, 5)

        self.m_staticText54 = wx.StaticText(self, wx.ID_ANY, u"Search:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText54.Wrap(-1)
        search_container.Add(self.m_staticText54, 0, wx.ALL, 5)

        self.search_students = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_PROCESS_ENTER)
        search_container.Add(self.search_students, 0, wx.BOTTOM | wx.RIGHT, 8)

        self.search_students.Bind(wx.EVT_TEXT, self.searchStudents)
        self.search_students.Bind(wx.EVT_TEXT_ENTER, self.searchStudents)

        tableSizer = wx.BoxSizer(wx.VERTICAL)

        tableSizer.Add(search_container, 0, wx.EXPAND, 5)

        #
        #
        self.products = getStudents()

        self.dataOlv = ObjectListView(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.setBooks()

        # Allow the cell values to be edited when double-clicked
        # self.dataOlv.cellEditMode = ObjectListView.CELLEDIT_SINGLECLICK

        tableSizer.Add(self.dataOlv, 1, wx.ALL, 5)

        left_sizer.Add(tableSizer, 1, wx.ALL | wx.EXPAND, 5)

        # -------------------------------------------------------------------------
        # BUTTONS ON RIGHT OF TABLE
        # -------------------------------------------------------------------------

        left_btns_sizer = wx.BoxSizer(wx.VERTICAL)

        self.edit_class_btn = wx.Button(self, wx.ID_ANY, u"Edit Student", wx.DefaultPosition, wx.DefaultSize, 0)
        self.edit_class_btn.Bind(wx.EVT_BUTTON, self.getStudentInfo)
        left_btns_sizer.Add(self.edit_class_btn, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.delete_class_btn = wx.Button(self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        self.delete_class_btn.Bind(wx.EVT_BUTTON, self.deleteStudent)
        left_btns_sizer.Add(self.delete_class_btn, 0, wx.ALL | wx.EXPAND, 5)

        left_sizer.Add(left_btns_sizer, 0, wx.ALL, 5)

        # -------------------------------------------------------------------------
        # BUTTONS ON RIGHT OF TABLE
        # -------------------------------------------------------------------------




        editFormSizer = wx.BoxSizer(wx.VERTICAL)

        #
        #
        #
        #
        # EDIT FORM
        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Edit Student Form"), wx.VERTICAL)

        bSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.user_id = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.user_id.Hide()
        bSizer.Add(self.user_id, 4, wx.ALL, 5)

        sbSizer2.Add(bSizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 10)

        bSizer26 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText29 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"First Name", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)
        bSizer26.Add(self.m_staticText29, 1, wx.ALL, 8)

        self.first_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bSizer26.Add(self.first_name, 4, wx.ALL, 5)

        sbSizer2.Add(bSizer26, 1, wx.ALL | wx.EXPAND | wx.TOP, 10)

        bSizer262 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText292 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Last Name", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText292.Wrap(-1)
        bSizer262.Add(self.m_staticText292, 1, wx.ALL, 8)

        self.last_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        bSizer262.Add(self.last_name, 4, wx.ALL, 5)

        sbSizer2.Add(bSizer262, 1, wx.ALL | wx.EXPAND, 10)

        bSizer263 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText293 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Surname", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText293.Wrap(-1)
        bSizer263.Add(self.m_staticText293, 1, wx.ALL, 8)

        self.surname = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        bSizer263.Add(self.surname, 4, wx.ALL, 5)

        sbSizer2.Add(bSizer263, 1, wx.ALL | wx.EXPAND, 10)

        bSizer261 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText291 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Date of Birth", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText291.Wrap(-1)
        bSizer261.Add(self.m_staticText291, 1, wx.ALL, 8)

        self.dob = wx.DatePickerCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                     wx.DefaultSize, wx.DP_DEFAULT | wx.DP_DROPDOWN)
        bSizer261.Add(self.dob, 4, wx.ALL, 5)

        sbSizer2.Add(bSizer261, 1, wx.ALL | wx.EXPAND, 10)

        bSizer264 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText294 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Gender", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText294.Wrap(-1)
        bSizer264.Add(self.m_staticText294, 1, wx.ALL, 8)

        genderChoices = [u"Male", u"Female"]
        self.gender = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                  wx.DefaultSize, genderChoices, wx.CB_READONLY)
        bSizer264.Add(self.gender, 4, wx.ALL, 5)

        sbSizer2.Add(bSizer264, 1, wx.ALL | wx.EXPAND, 10)

        bSizer2651 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2951 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Form", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText2951.Wrap(-1)
        bSizer2651.Add(self.m_staticText2951, 1, wx.ALL, 8)

        formChoices = [u"One", u"Two", u"Three", u"Four"]
        self.form = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                formChoices, wx.CB_READONLY)
        bSizer2651.Add(self.form, 4, wx.ALL, 5)

        sbSizer2.Add(bSizer2651, 1, wx.ALL | wx.EXPAND, 10)

        bSizer265 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText295 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Class", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText295.Wrap(-1)
        bSizer265.Add(self.m_staticText295, 1, wx.ALL, 8)

        class_idChoices = getClassNames()
        self.class_id = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, class_idChoices, wx.CB_READONLY)
        bSizer265.Add(self.class_id, 4, wx.ALL, 5)

        sbSizer2.Add(bSizer265, 1, wx.ALL | wx.EXPAND, 10)

        bSizer271 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        bSizer271.Add(self.m_staticText22, 1, wx.ALL, 5)

        self.cancel_edit = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        bSizer271.Add(self.cancel_edit, 0, wx.ALL, 5)

        self.save_student = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        bSizer271.Add(self.save_student, 0, wx.ALL, 5)

        sbSizer2.Add(bSizer271, 3, wx.ALL | wx.EXPAND, 10)

        self.save_student.Bind(wx.EVT_BUTTON, self.editStudent)
        self.cancel_edit.Bind(wx.EVT_BUTTON, self.cancelEdit)

        editFormSizer.Add(sbSizer2, 1, wx.TOP | wx.EXPAND, 5)

        #
        #
        #

        mainSizer.Add(left_sizer, 1, wx.ALL | wx.EXPAND, 8)
        mainSizer.Add(editFormSizer, 1, wx.TOP | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 8)

        container.Add(mainSizer, 1, wx.ALL, 5)

        self.SetSizer(container)

    # ----------------------------------------------------------------------
    def updateControl(self, event):
        """"""
        data = getStudents()
        self.dataOlv.SetObjects(data)

    # ----------------------------------------------------------------------
    def setBooks(self, data=None):
        self.dataOlv.SetColumns([
            ColumnDefn("ID", "center", 50, "user_id"),
            ColumnDefn("Full Name", "left", 180, "full_names"),
            ColumnDefn("Form", "center", 50, "form"),
            ColumnDefn("Stream", "center", 70, "class"),
            ColumnDefn("Date of Birth", "center", 120, "dob"),
            ColumnDefn("Gender", "center", 70, "gender")
        ])

        self.dataOlv.SetObjects(self.products)

    # ----------------------------------------------------------------------
    def searchStudents(self, event):
        search = self.search_students.GetLineText(0)
        data = getStudents(search=search)
        self.dataOlv.SetObjects(data)

    # ----------------------------------------------------------------------
    def getStudentInfo(self, event):
        if not self.dataOlv.GetSelectedObject():
            dlg = wx.MessageDialog(None, "Click on a row in order to edit student.",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
        else:
            rowObj = self.dataOlv.GetSelectedObject()
            self.user_id.SetValue(str(rowObj['user_id']))
            self.first_name.SetValue(rowObj['first_name'])
            self.last_name.SetValue(rowObj['last_name'])
            self.surname.SetValue(rowObj['surname'])

            # get wxPython datetime format
            day = rowObj['dob'].day
            month = rowObj['dob'].month
            year = rowObj['dob'].year

            # -1 because the month counts from 0, whereas people count January as month #1.
            dateFormatted = wx.DateTimeFromDMY(day, month - 1, year)

            self.dob.SetValue(dateFormatted)

            if rowObj['form'] == 1:
                form = "One"
            elif rowObj['form'] == 2:
                form = "Two"
            elif rowObj['form'] == 3:
                form = "Three"
            elif rowObj['form'] == 4:
                form = "Four"
            self.class_id.SetValue(rowObj['class'])
            self.gender.SetValue(rowObj['gender'])
            self.form.SetValue(form)

    def cancelEdit(self, event):
        self.user_id.SetValue("")
        self.first_name.SetValue("")
        self.last_name.SetValue("")
        self.surname.SetValue("")

        td = datetime.today()

        # get wxPython datetime format
        day = td.day
        month = td.month
        year = td.year

        # -1 because the month counts from 0, whereas people count January as month #1.
        tdFormatted = wx.DateTimeFromDMY(day, month - 1, year)

        self.dob.SetValue(tdFormatted)

        self.class_id.SetSelection(-1)
        self.gender.SetSelection(-1)
        self.form.SetSelection(-1)

    def hasNumbers(self, inputString):  # checks for numbers in string, returns true if there is a number
        return any(char.isdigit() for char in inputString)

    def editStudent(self, event):
        user_id = self.user_id.GetLineText(0)
        first_name = self.first_name.GetLineText(0)
        last_name = self.last_name.GetLineText(0)
        surname = self.surname.GetLineText(0)
        dob = self.dob.GetValue()
        genderIndex = self.gender.GetCurrentSelection()
        classIndex = self.class_id.GetCurrentSelection()

        # Remove white spaces
        first_name = first_name.replace(" ", "")
        last_name = last_name.replace(" ", "")
        surname = surname.replace(" ", "")

        # ---------- VALIDATION ----------
        error = ""

        if user_id == "":  # Check that a student has been selected before starting validation
            dlg = wx.MessageDialog(None, "Please select a student to edit.", 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
        else:
            if first_name == "" or last_name == "" or surname == "":
                error = error + "All name fields are required.\n"

            if self.hasNumbers(first_name) or self.hasNumbers(last_name) or self.hasNumbers(surname):
                error = error + "Names cannot have numeric characters.\n"

            # check that date has been changed
            td = datetime.today()

            # get wxPython datetime format
            day = td.day
            month = td.month
            year = td.year

            # -1 because the month counts from 0, whereas people count January as month #1.
            tdFormatted = wx.DateTimeFromDMY(day, month - 1, year)
            if str(dob) == str(tdFormatted):
                error = error + "The date of birth field is required.\n"

            if genderIndex == -1:
                error = error + "The gender field is required.\n"

            if classIndex == -1:
                error = error + "The class field is required.\n"
            #
            #
            #
            if error:
                dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
                dlg.ShowModal()
                self.cancelEdit("")
            else:
                dob = str(dob)[:-9]
                dob = datetime.strptime(dob, "%d/%m/%Y").date()

                gen = self.gender.GetString(genderIndex)
                if gen == "Male":
                    gender = "M"
                else:
                    gender = "F"
                class_id = classIndex + 1

                student_data = {
                    "user_id": user_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "surname": surname,
                    "dob": dob,
                    "gender": gender,
                    "class_id": class_id
                }

                if editStudent(student_data):
                    dlg = wx.MessageDialog(None, "Student Edited Successfully.", 'Success Message.',
                                           wx.OK | wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    self.updateControl("")
                    self.cancelEdit("")
                else:
                    dlg = wx.MessageDialog(None, "Please check all fields and try again.", 'Edit Failed.',
                                           wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()

    def deleteStudent(self, event):
        if not self.dataOlv.GetSelectedObject():
            dlg = wx.MessageDialog(None, "Click on a row in order to delete student.",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
        else:
            rowObj = self.dataOlv.GetSelectedObject()

            question = "Delete " + rowObj['first_name'] + " " + rowObj['last_name'] + "?"

            dlg = wx.MessageDialog(None, question, 'Confirm Delete.', wx.YES_NO | wx.ICON_INFORMATION)
            retCode = dlg.ShowModal()

            if retCode == wx.ID_YES:
                dlg = wx.MessageDialog(None, "Are you sure? This action cannot be reversed.", 'Warning Message.', wx.YES_NO | wx.ICON_WARNING)
                retCode = dlg.ShowModal()

                if retCode == wx.ID_YES:
                    if deleteStudent(rowObj["user_id"]):
                        dlg = wx.MessageDialog(None, "Student deleted successfully.", 'Success Message.',
                                               wx.OK | wx.ICON_EXCLAMATION)
                        dlg.ShowModal()

                        self.updateControl("")

                        rowObj = ""
                else:
                    dlg.Destroy()
                    rowObj = ""
            else:
                dlg.Destroy()
                rowObj = ""





