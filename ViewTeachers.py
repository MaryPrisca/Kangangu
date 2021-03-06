import wx
from ObjectListView import ObjectListView, ColumnDefn
from db.get_teachers import getTeachers
from db.save_teacher import editTeacher, deleteTeacher
from db.get_subjects import getActiveSubjectAliases
from datetime import datetime
import re
# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')


class ViewTeachers(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        # Create some sizers
        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"View Teachers", wx.DefaultPosition, wx.DefaultSize,
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

        self.refresh_btn = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"images/reload_16x16.bmp", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)

        self.refresh_btn.SetBitmapHover(wx.Bitmap(u"images/reload_16x16_rotated.bmp", wx.BITMAP_TYPE_ANY))
        search_container.Add(self.refresh_btn, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 5)

        self.m_staticText53 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText53.Wrap(-1)
        search_container.Add(self.m_staticText53, 1, wx.ALL, 5)

        self.search_teachers = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            wx.TE_PROCESS_ENTER)
        self.search_teachers.ShowSearchButton(True)
        self.search_teachers.ShowCancelButton(False)
        search_container.Add(self.search_teachers, 0, wx.BOTTOM | wx.RIGHT, 8)

        self.search_teachers.Bind(wx.EVT_TEXT, self.searchTeachers)
        self.search_teachers.Bind(wx.EVT_TEXT_ENTER, self.searchTeachers)

        tableSizer = wx.BoxSizer(wx.VERTICAL)

        tableSizer.Add(search_container, 0, wx.EXPAND, 5)

        #
        #
        self.products = getTeachers()

        self.dataOlv = ObjectListView(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.setBooks()

        tableSizer.Add(self.dataOlv, 1, wx.ALL, 5)

        left_sizer.Add(tableSizer, 1, wx.ALL | wx.EXPAND, 5)

        # -------------------------------------------------------------------------
        # BUTTONS ON RIGHT OF TABLE
        # -------------------------------------------------------------------------

        left_btns_sizer = wx.BoxSizer(wx.VERTICAL)

        self.edit_class_btn = wx.Button(self, wx.ID_ANY, u"Edit Teacher", wx.DefaultPosition, wx.DefaultSize, 0)
        self.edit_class_btn.Bind(wx.EVT_BUTTON, self.getTeacherInfo)
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
        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Edit Teacher Form"), wx.VERTICAL)

        #
        bSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.user_id = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.user_id.Hide()
        bSizer.Add(self.user_id, 4, wx.ALL, 5)
        #

        sbSizer2.Add(bSizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 10)

        fname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText29 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"First Name", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)
        fname_sizer.Add(self.m_staticText29, 1, wx.ALL, 8)

        self.first_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        fname_sizer.Add(self.first_name, 3, wx.ALL, 5)

        sbSizer2.Add(fname_sizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 7)

        lname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText292 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Last Name", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText292.Wrap(-1)
        lname_sizer.Add(self.m_staticText292, 1, wx.ALL, 8)

        self.last_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        lname_sizer.Add(self.last_name, 3, wx.ALL, 5)

        sbSizer2.Add(lname_sizer, 1, wx.ALL | wx.EXPAND, 7)

        surname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText293 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Surname", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText293.Wrap(-1)
        surname_sizer.Add(self.m_staticText293, 1, wx.ALL, 8)

        self.surname = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        surname_sizer.Add(self.surname, 3, wx.ALL, 5)

        sbSizer2.Add(surname_sizer, 1, wx.ALL | wx.EXPAND, 7)

        email_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Email Address", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.m_staticText.Wrap(-1)
        email_sizer.Add(self.m_staticText, 1, wx.ALL, 8)

        self.email = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 0)
        email_sizer.Add(self.email, 3, wx.ALL, 5)

        sbSizer2.Add(email_sizer, 1, wx.ALL | wx.EXPAND, 7)

        username_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Username", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        username_sizer.Add(self.m_staticText1, 1, wx.ALL, 8)

        self.username = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        username_sizer.Add(self.username, 3, wx.ALL, 5)

        sbSizer2.Add(username_sizer, 1, wx.ALL | wx.EXPAND, 7)

        dob_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText291 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Date of Birth", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText291.Wrap(-1)
        dob_sizer.Add(self.m_staticText291, 1, wx.ALL, 8)

        self.dob = wx.DatePickerCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                     wx.DefaultSize, wx.DP_DEFAULT | wx.DP_DROPDOWN)
        dob_sizer.Add(self.dob, 3, wx.ALL, 5)

        sbSizer2.Add(dob_sizer, 1, wx.ALL | wx.EXPAND, 7)

        gender_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText294 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Gender", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText294.Wrap(-1)
        gender_sizer.Add(self.m_staticText294, 1, wx.ALL, 8)

        genderChoices = [u"Male", u"Female"]
        self.gender = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Female", wx.DefaultPosition, wx.DefaultSize,
                                  genderChoices, wx.CB_READONLY)
        self.gender.SetSelection(-1)
        gender_sizer.Add(self.gender, 3, wx.ALL, 5)

        sbSizer2.Add(gender_sizer, 1, wx.ALL | wx.EXPAND, 7)

        #
        #
        #

        subject_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2951 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Subject 1", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText2951.Wrap(-1)
        subject_sizer.Add(self.m_staticText2951, 1, wx.ALL, 8)

        subjects = getActiveSubjectAliases()

        subjectChoices = subjects['aliases']
        self.subject = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   subjectChoices, wx.CB_READONLY)
        self.subject.SetSelection(-1)
        subject_sizer.Add(self.subject, 3, wx.ALL, 5)

        sbSizer2.Add(subject_sizer, 1, wx.ALL | wx.EXPAND, 7)

        #

        subject2_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.subject2_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Subject 2", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.subject2_label.Wrap(-1)
        subject2_sizer.Add(self.subject2_label, 1, wx.ALL, 8)

        subject2Choices = subjects['aliases']
        self.subject2 = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, subject2Choices, wx.CB_READONLY)
        self.subject2.SetSelection(-1)
        subject2_sizer.Add(self.subject2, 3, wx.ALL, 5)

        sbSizer2.Add(subject2_sizer, 1, wx.ALL | wx.EXPAND, 7)

        btns_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        btns_sizer.Add(self.m_staticText22, 1, wx.ALL, 5)

        self.cancel_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        btns_sizer.Add(self.cancel_btn, 0, wx.ALL, 5)

        self.edit_teacher = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        btns_sizer.Add(self.edit_teacher, 0, wx.ALL, 5)

        sbSizer2.Add(btns_sizer, 3, wx.ALL | wx.EXPAND, 7)

        self.edit_teacher.Bind(wx.EVT_BUTTON, self.editTeacher)
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelEdit)

        editFormSizer.Add(sbSizer2, 1, wx.TOP | wx.EXPAND, 5)

        #
        #
        #

        mainSizer.Add(left_sizer, 1, wx.ALL | wx.EXPAND, 8)
        mainSizer.Add(editFormSizer, 1, wx.TOP | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 8)

        container.Add(mainSizer, 1, wx.ALL, 5)

        self.SetSizer(container)

        self.refresh_btn.Bind(wx.EVT_BUTTON, self.refreshTable)

    # ----------------------------------------------------------------------
    def refreshTable(self, event):
        self.updateControl("")

    def updateControl(self, event):
        """"""
        data = getTeachers()
        self.dataOlv.SetObjects(data)

    # ----------------------------------------------------------------------
    def setBooks(self, data=None):
        self.dataOlv.SetColumns([
            ColumnDefn("ID", "center", 45, "user_id"),
            ColumnDefn("Full Name", "left", 140, "full_names"),
            ColumnDefn("Email", "left", 125, "email"),
            # ColumnDefn("Username", "left", 60, "username"),
            ColumnDefn("Subject1", "center", 55, "subject1"),
            ColumnDefn("Subject2", "center", 55, "subject2"),
            ColumnDefn("Date of Birth", "center", 90, "dob"),
            ColumnDefn("Gender", "left", 50, "gender")
        ])

        self.dataOlv.SetObjects(self.products)

    # ----------------------------------------------------------------------
    def searchTeachers(self, event):
        search = self.search_teachers.GetLineText(0)
        data = getTeachers(search=search)
        self.dataOlv.SetObjects(data)

    # ----------------------------------------------------------------------
    def getTeacherInfo(self, event):
        if not self.dataOlv.GetSelectedObject():
            dlg = wx.MessageDialog(None, "Click on a row in order to edit teacher.",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            rowObj = self.dataOlv.GetSelectedObject()
            self.user_id.SetValue(str(rowObj['user_id']))
            self.first_name.SetValue(rowObj['first_name'])
            self.last_name.SetValue(rowObj['last_name'])
            self.surname.SetValue(rowObj['surname'])
            self.email.SetValue(rowObj['email'])
            self.username.SetValue(rowObj['username'])

            rowObj['dob'] = datetime.strptime(str(rowObj['dob']), "%Y-%m-%d").date()

            # get wxPython datetime format
            day = rowObj['dob'].day
            month = rowObj['dob'].month
            year = rowObj['dob'].year

            # -1 because the month counts from 0, whereas people count January as month #1.
            dateFormatted = wx.DateTimeFromDMY(day, month - 1, year)

            self.dob.SetValue(dateFormatted)
            self.gender.SetValue(rowObj['gender'])

            self.subject.SetValue(rowObj['subject1'])

            if rowObj['subject2'] != "--":
                self.subject2.SetValue(rowObj['subject2'])

    def cancelEdit(self, event):
        self.user_id.SetValue("")
        self.first_name.SetValue("")
        self.last_name.SetValue("")
        self.surname.SetValue("")
        self.email.SetValue("")
        self.username.SetValue("")

        td = datetime.today()

        # get wxPython datetime format
        day = td.day
        month = td.month
        year = td.year

        # -1 because the month counts from 0, whereas people count January as month #1.
        tdFormatted = wx.DateTimeFromDMY(day, month - 1, year)

        self.dob.SetValue(tdFormatted)

        self.gender.SetSelection(-1)
        self.subject.SetSelection(-1)
        self.subject2.SetSelection(-1)

    def hasNumbers(self, inputString):  # checks for numbers in string, returns true if there is a number
        return any(char.isdigit() for char in inputString)

    def editTeacher(self, event):
        self.edit_teacher.Enable(False)

        user_id = self.user_id.GetLineText(0)
        first_name = self.first_name.GetLineText(0)
        last_name = self.last_name.GetLineText(0)
        surname = self.surname.GetLineText(0)
        email = self.email.GetLineText(0)
        username = self.username.GetLineText(0)
        dob = self.dob.GetValue()
        genderIndex = self.gender.GetCurrentSelection()
        subjectOneIndex = self.subject.GetCurrentSelection()
        subjectTwoIndex = self.subject2.GetCurrentSelection()

        # Remove white spaces
        first_name = first_name.replace(" ", "")
        last_name = last_name.replace(" ", "")
        surname = surname.replace(" ", "")
        email = email.replace(" ", "")
        username = username.replace(" ", "")

        #
        # ---------- VALIDATION ----------
        error = ""

        if user_id == "":  # Check that a teacher has been selected before starting validation
            dlg = wx.MessageDialog(None, "Please select a teacher to edit.", 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        else:
            if first_name == "" or last_name == "" or surname == "":
                error = error + "All name fields are required.\n"

            if self.hasNumbers(first_name) or self.hasNumbers(last_name) or self.hasNumbers(surname):
                error = error + "Names cannot have numeric characters.\n"

            if email == "":
                error = error + "The Email Address field is required.\n"

            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                error = error + "Enter a valid email address.\n"

            if username == "":
                error = error + "The Username field is required.\n"

            # check that date has been changed
            td = datetime.today()

            # get wxPython datetime format
            day = td.day
            month = td.month
            year = td.year

            # -1 because the month counts from 0, whereas people count January as month #1.
            tdFormatted = wx.DateTimeFromDMY(day, month - 1, year)
            if str(dob) == str(tdFormatted):
                error = error + "The Date of Birth field is required.\n"

            if genderIndex == -1:
                error = error + "The Gender field is required.\n"

            if subjectOneIndex == -1:
                error = error + "The Subject 1 field is required.\n"
            else:
                if subjectOneIndex == subjectTwoIndex:
                    error = error + "The Subject 2 field must be different from Subject 1 field .\n"

            if error:
                dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
                dlg.ShowModal()
                dlg.Destroy()

            else:
                dob = str(dob)[:-9]
                dob = datetime.strptime(dob, "%d/%m/%Y").date()

                gen = self.gender.GetString(genderIndex)

                if gen == "Male":
                    gender = "M"
                else:
                    gender = "F"

                subjects = getActiveSubjectAliases()
                subject_ids = subjects['ids']
                subjectOneid = subject_ids[subjectOneIndex]

                if subjectTwoIndex == -1:
                    subjectTwoid = None
                else:
                    subjectTwoid = subject_ids[subjectTwoIndex]

                data = {
                    "user_id": user_id,
                    "first_name": first_name.lower().capitalize(),
                    "last_name": last_name.lower().capitalize(),
                    "surname": surname.lower().capitalize(),
                    "email": email,
                    "username": username,
                    "dob": dob,
                    "gender": gender,
                    "subjectOneID": subjectOneid,
                    "subjectTwoID": subjectTwoid
                }

                if editTeacher(data):
                    dlg = wx.MessageDialog(None, "Teacher edited Successfully.", 'Success Message',
                                           wx.OK | wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    dlg.Destroy()
                    self.cancelEdit("")
                    self.updateControl("")
                else:
                    dlg = wx.MessageDialog(None, "Edit failed. Try Again.", 'Failed',
                                           wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()
                    dlg.Destroy()

        self.edit_teacher.Enable(True)

    def deleteStudent(self, event):
        if not self.dataOlv.GetSelectedObject():
            dlg = wx.MessageDialog(None, "Click on a row in order to delete student.",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            rowObj = self.dataOlv.GetSelectedObject()

            question = "Delete " + rowObj['first_name'] + " " + rowObj['last_name'] + "?"

            dlg = wx.MessageDialog(None, question, 'Confirm Delete.', wx.YES_NO | wx.ICON_INFORMATION)
            retCode = dlg.ShowModal()

            if retCode == wx.ID_YES:
                dlg = wx.MessageDialog(None, "Are you sure? This action cannot be reversed.", 'Warning Message.', wx.YES_NO | wx.ICON_WARNING)
                retCode = dlg.ShowModal()

                if retCode == wx.ID_YES:
                    if deleteTeacher(rowObj["user_id"]):
                        dlg = wx.MessageDialog(None, "Teacher deleted successfully.", 'Success Message.',
                                               wx.OK | wx.ICON_EXCLAMATION)
                        dlg.ShowModal()
                        dlg.Destroy()

                        self.updateControl("")

                        rowObj = ""
                else:
                    rowObj = ""
                dlg.Destroy()
            else:
                rowObj = ""
            dlg.Destroy()