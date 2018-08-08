import wx
from ObjectListView import ObjectListView, ColumnDefn
from db.get_students import getStudents, getStudentByIDAllDetails
from db.save_student import editStudent, deleteStudent
from db.get_classes import getClassNamesWithForm
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

        self.search_students = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                             wx.TE_PROCESS_ENTER)
        self.search_students.ShowSearchButton(True)
        self.search_students.ShowCancelButton(False)
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

        #
        #
        #
        #
        # EDIT FORM
        editFormSizer = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Edit Student Form"), wx.VERTICAL)

        bSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.user_id = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.user_id.Hide()
        bSizer.Add(self.user_id, 4, wx.ALL, 5)

        sbSizer2.Add(bSizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 10)

        fname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.fname_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"First Name", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.fname_label.Wrap(-1)
        fname_sizer.Add(self.fname_label, 1, wx.ALL, 8)

        self.first_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        fname_sizer.Add(self.first_name, 2, wx.ALL, 5)

        sbSizer2.Add(fname_sizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 3)

        lname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.lname_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Last Name", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.lname_label.Wrap(-1)
        lname_sizer.Add(self.lname_label, 1, wx.ALL, 8)

        self.last_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        lname_sizer.Add(self.last_name, 2, wx.ALL, 5)

        sbSizer2.Add(lname_sizer, 1, wx.ALL | wx.EXPAND, 3)

        surname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.surname_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Surname", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.surname_label.Wrap(-1)
        surname_sizer.Add(self.surname_label, 1, wx.ALL, 8)

        self.surname = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        surname_sizer.Add(self.surname, 2, wx.ALL, 5)

        sbSizer2.Add(surname_sizer, 1, wx.ALL | wx.EXPAND, 3)

        dob_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.dob_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Date of Birth", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.dob_label.Wrap(-1)
        dob_sizer.Add(self.dob_label, 1, wx.ALL, 8)

        self.dob = wx.DatePickerCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                     wx.DefaultSize, wx.DP_DEFAULT | wx.DP_DROPDOWN)
        dob_sizer.Add(self.dob, 2, wx.ALL, 5)

        sbSizer2.Add(dob_sizer, 1, wx.ALL | wx.EXPAND, 3)

        gender_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.gender_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Gender", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.gender_label.Wrap(-1)
        gender_sizer.Add(self.gender_label, 1, wx.ALL, 8)

        genderChoices = [u"Male", u"Female"]
        self.gender = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                  wx.DefaultSize, genderChoices, wx.CB_READONLY)
        gender_sizer.Add(self.gender, 2, wx.ALL, 5)

        sbSizer2.Add(gender_sizer, 1, wx.ALL | wx.EXPAND, 3)

        class_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.class_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Class", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.class_label.Wrap(-1)
        class_sizer.Add(self.class_label, 1, wx.ALL, 8)

        self.classes = getClassNamesWithForm()

        class_idChoices = self.classes['names']

        self.class_id = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, class_idChoices, wx.CB_READONLY)
        class_sizer.Add(self.class_id, 2, wx.ALL, 5)

        sbSizer2.Add(class_sizer, 1, wx.ALL | wx.EXPAND, 3)

        kin_names_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.kin_names_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Next of Kin Names",
                                             wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.kin_names_label.Wrap(-1)
        kin_names_sizer.Add(self.kin_names_label, 1, wx.ALL, 8)

        self.kin_names = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        kin_names_sizer.Add(self.kin_names, 2, wx.ALL, 5)

        sbSizer2.Add(kin_names_sizer, 1, wx.ALL | wx.EXPAND, 3)

        kin_phone_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.kin_phone_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Next of Kin Phone",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.kin_phone_label.Wrap(-1)
        kin_phone_sizer.Add(self.kin_phone_label, 1, wx.ALL, 8)

        self.kin_phone = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        kin_phone_sizer.Add(self.kin_phone, 2, wx.ALL, 5)

        sbSizer2.Add(kin_phone_sizer, 1, wx.ALL | wx.EXPAND, 3)

        birth_cert_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.birth_cert_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Birth Certificate No",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.birth_cert_label.Wrap(-1)
        birth_cert_sizer.Add(self.birth_cert_label, 1, wx.ALL, 8)

        self.birth_cert_no = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        birth_cert_sizer.Add(self.birth_cert_no, 2, wx.ALL, 5)

        sbSizer2.Add(birth_cert_sizer, 1, wx.ALL | wx.EXPAND, 3)

        kcpe_marks_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.kcpe_marks_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"KCPE Marks", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.kcpe_marks_label.Wrap(-1)
        kcpe_marks_sizer.Add(self.kcpe_marks_label, 1, wx.ALL, 8)

        self.kcpe_marks = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        kcpe_marks_sizer.Add(self.kcpe_marks, 2, wx.ALL, 5)

        sbSizer2.Add(kcpe_marks_sizer, 1, wx.ALL | wx.EXPAND, 3)

        edit_form_btns_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.edit_btns_spacer = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.edit_btns_spacer.Wrap(-1)
        edit_form_btns_sizer.Add(self.edit_btns_spacer, 1, wx.ALL, 5)

        self.cancel_edit = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        edit_form_btns_sizer.Add(self.cancel_edit, 0, wx.ALL, 5)

        self.save_student = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        edit_form_btns_sizer.Add(self.save_student, 0, wx.ALL, 5)

        sbSizer2.Add(edit_form_btns_sizer, 3, wx.ALL | wx.EXPAND, 3)

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

            user_id = rowObj['user_id']

            studentData = getStudentByIDAllDetails(user_id)

            self.user_id.SetValue(str(studentData['user_id']))
            self.first_name.SetValue(studentData['first_name'])
            self.last_name.SetValue(studentData['last_name'])
            self.surname.SetValue(studentData['surname'])
            self.kin_names.SetValue(studentData['next_of_kin_name'])
            self.kin_phone.SetValue(studentData['next_of_kin_phone'])
            self.birth_cert_no.SetValue(studentData['birth_cert_no'])
            self.kcpe_marks.SetValue(str(studentData['kcpe_marks']))

            # get wxPython datetime format
            day = studentData['dob'].day
            month = studentData['dob'].month
            year = studentData['dob'].year

            # -1 because the month counts from 0, whereas people count January as month #1.
            dateFormatted = wx.DateTimeFromDMY(day, month - 1, year)

            self.dob.SetValue(dateFormatted)

            self.class_id.SetValue(str(studentData['form']) + " " + studentData['class'])
            self.gender.SetValue(studentData['gender'])

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
        self.gender.SetSelection(-1)
        self.class_id.SetSelection(-1)

        self.kin_names.SetValue("")
        self.kin_phone.SetValue("")
        self.birth_cert_no.SetValue("")
        self.kcpe_marks.SetValue("")

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
        kin_names = self.kin_names.GetLineText(0)
        kin_phone = self.kin_phone.GetLineText(0)
        birth_cert_no = self.birth_cert_no.GetLineText(0)
        kcpe_marks = self.kcpe_marks.GetLineText(0)

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

            if kin_names == "":
                error = error + "The Next of Kin Names field is required.\n"
            else:
                if self.hasNumbers(kin_names):
                    error = error + "The Next of Kin Names field cannot contain numeric characters. \n"

            if kin_phone == "":
                error = error + "The Next of Kin Phone field is required.\n"
            else:
                if not kin_phone.isdigit():
                    error = error + "The Next of kin phone no field expects only numbers. \n"

            if birth_cert_no == "":
                error = error + "The Birth Certificate No field is required.\n"

            if kcpe_marks == "":
                error = error + "The KCPE Marks field is required.\n"
            else:
                if not kcpe_marks.isdigit():
                    error = error + "The KCPE Marks field expects only numbers. \n"
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

                # use class Index to match with class ID's list
                class_id = self.classes['ids'][classIndex]

                student_data = {
                    "user_id": user_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "surname": surname,
                    "dob": dob,
                    "gender": gender,
                    "class_id": class_id,
                    "kin_names": kin_names,
                    "kin_phone": kin_phone,
                    "birth_cert_no": birth_cert_no,
                    "kcpe_marks": kcpe_marks
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





