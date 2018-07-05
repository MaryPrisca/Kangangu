import wx

from datetime import datetime
import re  # Regex
from db.save_teacher import saveTeacher
from db.get_classes import getClassNames
# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')


class AddTeacher(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(665, 855),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"Add New Teacher", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText17, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 25)

        bSizer27 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer28 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        bSizer28.Add(self.m_staticText30, 0, wx.ALL, 5)

        bSizer27.Add(bSizer28, 1, wx.EXPAND, 5)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Add Teacher Form"), wx.VERTICAL)

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

        password_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        password_sizer.Add(self.m_staticText2, 1, wx.ALL, 8)

        self.password = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize,  wx.TE_PASSWORD )
        password_sizer.Add(self.password, 3, wx.ALL, 5)

        sbSizer2.Add(password_sizer, 1, wx.ALL | wx.EXPAND, 7)

        conf_pwd_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText21 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Confirm Password", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        conf_pwd_sizer.Add(self.m_staticText21, 1, wx.ALL, 8)

        self.conf_password = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize,  wx.TE_PASSWORD )
        conf_pwd_sizer.Add(self.conf_password, 3, wx.ALL, 5)

        sbSizer2.Add(conf_pwd_sizer, 1, wx.ALL | wx.EXPAND, 7)

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
        self.gender.SetSelection(1)
        gender_sizer.Add(self.gender, 3, wx.ALL, 5)

        sbSizer2.Add(gender_sizer, 1, wx.ALL | wx.EXPAND, 7)

        # class_id_sizer = wx.BoxSizer(wx.HORIZONTAL)
        #
        # self.m_staticText295 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Class", wx.DefaultPosition,
        #                                      wx.DefaultSize, 0)
        # self.m_staticText295.Wrap(-1)
        # class_id_sizer.Add(self.m_staticText295, 1, wx.ALL, 8)
        #
        # class_idChoices = []
        # self.class_id = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
        #                             wx.DefaultSize, class_idChoices, wx.CB_READONLY)
        # self.class_id.SetSelection(0)
        # class_id_sizer.Add(self.class_id, 3, wx.ALL, 5)
        #
        # sbSizer2.Add(class_id_sizer, 1, wx.ALL | wx.EXPAND, 7)
        #
        # subject_sizer = wx.BoxSizer(wx.HORIZONTAL)
        #
        # self.m_staticText2951 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Subjects", wx.DefaultPosition,
        #                                       wx.DefaultSize, 0)
        # self.m_staticText2951.Wrap(-1)
        # subject_sizer.Add(self.m_staticText2951, 1, wx.ALL, 8)
        #
        # subjectChoices = [u"English", u"Kiswahili"]
        # self.subject = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, u"English", wx.DefaultPosition, wx.DefaultSize,
        #                            subjectChoices, wx.CB_READONLY)
        # self.subject.SetSelection(0)
        # subject_sizer.Add(self.subject, 3, wx.ALL, 5)
        #
        # sbSizer2.Add(subject_sizer, 1, wx.ALL | wx.EXPAND, 7)

        btns_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        btns_sizer.Add(self.m_staticText22, 1, wx.ALL, 5)

        self.cancel_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        btns_sizer.Add(self.cancel_btn, 0, wx.ALL, 5)

        self.save_teacher = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        btns_sizer.Add(self.save_teacher, 0, wx.ALL, 5)

        sbSizer2.Add(btns_sizer, 3, wx.ALL | wx.EXPAND, 7)

        bSizer36.Add(sbSizer2, 1, wx.EXPAND, 5)

        self.m_staticText301 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText301.Wrap(-1)
        self.m_staticText301.SetFont(wx.Font(30, 70, 90, 90, False, wx.EmptyString))

        bSizer36.Add(self.m_staticText301, 0, wx.ALL | wx.EXPAND, 5)

        bSizer27.Add(bSizer36, 3, wx.EXPAND, 5)

        bSizer281 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        bSizer281.Add(self.m_staticText31, 0, wx.ALL, 5)

        bSizer27.Add(bSizer281, 1, wx.EXPAND, 5)

        container.Add(bSizer27, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelAddTeacher)
        self.save_teacher.Bind(wx.EVT_BUTTON, self.saveTeacher)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancelAddTeacher(self, event):
        event.Skip()

    def hasNumbers(self, inputString):  # checks for numbers in string, returns true if there is a number
        return any(char.isdigit() for char in inputString)

    def saveTeacher(self, event):
        first_name = self.first_name.GetLineText(0)
        last_name = self.last_name.GetLineText(0)
        surname = self.surname.GetLineText(0)
        email = self.email.GetLineText(0)
        username = self.username.GetLineText(0)
        password = self.password.GetLineText(0)
        conf_password = self.conf_password.GetLineText(0)
        dob = self.dob.GetValue()
        genderIndex = self.gender.GetCurrentSelection()
        # classIndex = self.class_id.GetCurrentSelection()

        # Remove white spaces
        first_name = first_name.replace(" ", "")
        last_name = last_name.replace(" ", "")
        surname = surname.replace(" ", "")
        email = email.replace(" ", "")
        username = username.replace(" ", "")
        password = password.replace(" ", "")
        conf_password = conf_password.replace(" ", "")

        #
        # ---------- VALIDATION ----------
        error = ""

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

        if password == "":
            error = error + "The Password field is required.\n"

        if conf_password == "":
            error = error + "The Confirm Password field is required.\n"

        if conf_password != password:
            error = error + "Passwords do not match.\n"

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

        # if classIndex == -1:
        #     error = error + "The Class field is required.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            retCode = dlg.ShowModal()
            if retCode == wx.ID_OK:
                ''''''
                # print "yes"
                # dlg.Destroy()

        else:
            gen = self.gender.GetString(genderIndex)

            if gen == "Male":
                gender = "M"
            else:
                gender = "F"

            # class_id = classIndex + 1

            data = {
                "first_name": first_name,
                "last_name": last_name,
                "surname": surname,
                "email": email,
                "username": username,
                "password": password,
                "dob": dob,
                "gender": gender,
                # "class_id": class_id
            }

            if saveTeacher(data):
                dlg = wx.MessageDialog(None, "Teacher Added Successfully.", 'Success Message',
                                       wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                self.cancelAddTeacher("")
            else:
                dlg = wx.MessageDialog(None, "Teacher Not Saved. Try Again.", 'Failed',
                                       wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()