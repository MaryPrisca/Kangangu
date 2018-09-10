import wx

from datetime import datetime
import re  # Regex
from db.save_teacher import saveTeacher
from db.get_classes import getClassNames
from db.get_subjects import getActiveSubjectAliases
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

        container.Add(self.m_staticText17, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 15)

        bSizer27 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer28 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        bSizer28.Add(self.m_staticText30, 0, wx.ALL, 5)

        bSizer27.Add(bSizer28, 1, wx.EXPAND, 5)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Add Teacher Form"), wx.VERTICAL)

        wrapper_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_controls_sizer = wx.BoxSizer(wx.VERTICAL)

        fname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.fname_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"First Name", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.fname_label.Wrap(-1)
        fname_sizer.Add(self.fname_label, 1, wx.ALL, 8)

        self.first_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        fname_sizer.Add(self.first_name, 3, wx.ALL, 5)

        left_controls_sizer.Add(fname_sizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 5)

        lname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.lname_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Last Name", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.lname_label.Wrap(-1)
        lname_sizer.Add(self.lname_label, 1, wx.ALL, 8)

        self.last_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        lname_sizer.Add(self.last_name, 3, wx.ALL, 5)

        left_controls_sizer.Add(lname_sizer, 1, wx.ALL | wx.EXPAND, 5)

        surname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.surname_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Surname", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.surname_label.Wrap(-1)
        surname_sizer.Add(self.surname_label, 1, wx.ALL, 8)

        self.surname = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        surname_sizer.Add(self.surname, 3, wx.ALL, 5)

        left_controls_sizer.Add(surname_sizer, 1, wx.ALL | wx.EXPAND, 5)

        email_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.email_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Email Address", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.email_label.Wrap(-1)
        email_sizer.Add(self.email_label, 1, wx.ALL, 8)

        self.email = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 0)
        email_sizer.Add(self.email, 3, wx.ALL, 5)

        left_controls_sizer.Add(email_sizer, 1, wx.ALL | wx.EXPAND, 5)

        phone_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.phone_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Phone Number", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.phone_label.Wrap(-1)
        phone_sizer.Add(self.phone_label, 1, wx.ALL, 8)

        self.phone = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 0)
        phone_sizer.Add(self.phone, 3, wx.ALL, 5)

        left_controls_sizer.Add(phone_sizer, 1, wx.ALL | wx.EXPAND, 5)

        address_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.address_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Postal Address", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.address_label.Wrap(-1)
        address_sizer.Add(self.address_label, 1, wx.ALL, 8)

        self.address = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 0)
        address_sizer.Add(self.address, 3, wx.ALL, 5)

        left_controls_sizer.Add(address_sizer, 1, wx.ALL | wx.EXPAND, 5)



        national_id_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.national_id_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"National ID", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.national_id_label.Wrap(-1)
        national_id_sizer.Add(self.national_id_label, 1, wx.ALL, 8)

        self.national_id = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 0)
        national_id_sizer.Add(self.national_id, 3, wx.ALL, 5)

        left_controls_sizer.Add(national_id_sizer, 1, wx.ALL | wx.EXPAND, 5)

        tsc_no_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.tsc_no_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"TSC Number", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.tsc_no_label.Wrap(-1)
        tsc_no_sizer.Add(self.tsc_no_label, 1, wx.ALL, 8)

        self.tsc_no = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 0)
        tsc_no_sizer.Add(self.tsc_no, 3, wx.ALL, 5)

        left_controls_sizer.Add(tsc_no_sizer, 1, wx.ALL | wx.EXPAND, 5)

        wrapper_sizer.Add(left_controls_sizer, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.TOP, 10)

        #
        #
        #

        right_controls_sizer = wx.BoxSizer(wx.VERTICAL)

        username_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.username_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Username", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.username_label.Wrap(-1)
        username_sizer.Add(self.username_label, 1, wx.ALL, 8)

        self.username = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        username_sizer.Add(self.username, 3, wx.ALL, 5)

        right_controls_sizer.Add(username_sizer, 1, wx.ALL | wx.EXPAND, 5)

        password_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.password_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.password_label.Wrap(-1)
        password_sizer.Add(self.password_label, 1, wx.ALL, 8)

        self.password = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, wx.TE_PASSWORD)
        password_sizer.Add(self.password, 3, wx.ALL, 5)

        right_controls_sizer.Add(password_sizer, 1, wx.ALL | wx.EXPAND, 5)

        conf_pwd_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.conf_pwd_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Confirm Password", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.conf_pwd_label.Wrap(-1)
        conf_pwd_sizer.Add(self.conf_pwd_label, 1, wx.ALL, 8)

        self.conf_password = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TE_PASSWORD)
        conf_pwd_sizer.Add(self.conf_password, 3, wx.ALL, 5)

        right_controls_sizer.Add(conf_pwd_sizer, 1, wx.ALL | wx.EXPAND, 5)

        gender_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.gender_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Gender", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.gender_label.Wrap(-1)
        gender_sizer.Add(self.gender_label, 1, wx.ALL, 8)

        genderChoices = [u"Male", u"Female"]
        self.gender = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Female", wx.DefaultPosition, wx.DefaultSize,
                                  genderChoices, wx.CB_READONLY)
        self.gender.SetSelection(-1)
        gender_sizer.Add(self.gender, 3, wx.ALL, 5)

        right_controls_sizer.Add(gender_sizer, 1, wx.ALL | wx.EXPAND, 5)

        dob_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.dob_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Date of Birth", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.dob_label.Wrap(-1)
        dob_sizer.Add(self.dob_label, 1, wx.ALL, 8)

        self.dob = wx.DatePickerCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                     wx.DefaultSize, wx.DP_DEFAULT | wx.DP_DROPDOWN)
        dob_sizer.Add(self.dob, 3, wx.ALL, 5)

        right_controls_sizer.Add(dob_sizer, 1, wx.ALL | wx.EXPAND, 5)

        subject_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.subject_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Subject 1", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.subject_label.Wrap(-1)
        subject_sizer.Add(self.subject_label, 1, wx.ALL, 8)

        subjects = getActiveSubjectAliases()
        subjectChoices = subjects['names']
        self.subject = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, subjectChoices, wx.CB_READONLY)
        self.subject.SetSelection(-1)
        subject_sizer.Add(self.subject, 3, wx.ALL, 5)

        right_controls_sizer.Add(subject_sizer, 1, wx.ALL | wx.EXPAND, 5)

        subject2_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.subject2_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Subject 2", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.subject2_label.Wrap(-1)
        subject2_sizer.Add(self.subject2_label, 1, wx.ALL, 8)

        subject2Choices = subjects['names']
        self.subject2 = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, subject2Choices, wx.CB_READONLY)
        self.subject2.SetSelection(-1)
        subject2_sizer.Add(self.subject2, 3, wx.ALL, 5)

        right_controls_sizer.Add(subject2_sizer, 1, wx.ALL | wx.EXPAND, 5)

        wrapper_sizer.Add(right_controls_sizer, 1, wx.BOTTOM | wx.EXPAND | wx.RIGHT | wx.TOP, 10)

        sbSizer2.Add(wrapper_sizer, 1, wx.EXPAND, 5)

        btns_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_spacer = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.btn_spacer.Wrap(-1)
        btns_sizer.Add(self.btn_spacer, 1, wx.ALL, 5)

        self.cancel_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        btns_sizer.Add(self.cancel_btn, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT, 15)

        self.save_teacher = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        btns_sizer.Add(self.save_teacher, 0, wx.RIGHT, 25)

        sbSizer2.Add(btns_sizer, 0, wx.BOTTOM | wx.EXPAND, 25)

        bSizer36.Add(sbSizer2, 1, wx.ALL | wx.EXPAND, 10)

        self.below_form_spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.below_form_spacer.Wrap(-1)
        bSizer36.Add(self.below_form_spacer, 0, wx.ALL, 5)

        bSizer27.Add(bSizer36, 2, wx.EXPAND, 5)

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
        self.first_name.SetValue("")
        self.last_name.SetValue("")
        self.surname.SetValue("")
        self.email.SetValue("")
        self.phone.SetValue("")
        self.address.SetValue("")
        self.national_id.SetValue("")
        self.tsc_no.SetValue("")
        self.username.SetValue("")
        self.password.SetValue("")
        self.conf_password.SetValue("")
        self.gender.SetSelection(-1)
        self.subject.SetSelection(-1)
        self.subject2.SetSelection(-1)

        td = datetime.today()

        # get wxPython datetime format
        day = td.day
        month = td.month
        year = td.year

        # -1 because the month counts from 0, whereas people count January as month #1.
        tdFormatted = wx.DateTimeFromDMY(day, month - 1, year)

        self.dob.SetValue(tdFormatted)

    def hasNumbers(self, inputString):  # checks for numbers in string, returns true if there is a number
        return any(char.isdigit() for char in inputString)

    def saveTeacher(self, event):
        self.save_teacher.Enable(False)

        first_name = self.first_name.GetLineText(0)
        last_name = self.last_name.GetLineText(0)
        surname = self.surname.GetLineText(0)
        email = self.email.GetLineText(0)
        phone = self.phone.GetLineText(0)
        address = self.address.GetLineText(0)
        national_id = self.national_id.GetLineText(0)
        tsc_no = self.tsc_no.GetLineText(0)
        username = self.username.GetLineText(0)
        password = self.password.GetLineText(0)
        conf_password = self.conf_password.GetLineText(0)
        dob = self.dob.GetValue()
        genderIndex = self.gender.GetCurrentSelection()
        subjectOneIndex = self.subject.GetCurrentSelection()
        subjectTwoIndex = self.subject2.GetCurrentSelection()

        # Remove white spaces
        first_name = first_name.replace(" ", "")
        last_name = last_name.replace(" ", "")
        surname = surname.replace(" ", "")
        email = email.replace(" ", "")
        phone = phone.replace(" ", "")
        # address = address.replace(" ", "")
        national_id = national_id.replace(" ", "")
        tsc_no = tsc_no.replace(" ", "")
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
        else:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                error = error + "Enter a valid email address.\n"

        if phone == "":
            error = error + "The Phone Number field is required.\n"
        else:
            if not phone.isdigit():
                error = error + "The Phone Number field must contain only numbers.\n"

            if len(phone) != 10:
                error = error + "The Phone Number field expects ten numbers.\n"

        if address == "":
            error = error + "The Postal Address field is required.\n"

        if national_id == "":
            error = error + "The National ID field is required.\n"

        if tsc_no == "":
            error = error + "The TSC Number field is required.\n"

        if username == "":
            error = error + "The Username field is required.\n"

        if password == "":
            error = error + "The Password field is required.\n"

        if conf_password == "":
            error = error + "The Confirm Password field is required.\n"

        if conf_password != password:
            error = error + "Passwords do not match.\n"
        else:
            if len(password) < 5:
                error = error + "The Password should have at least 5 characters.\n"

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
                "first_name": first_name.lower().capitalize(),
                "last_name": last_name.lower().capitalize(),
                "surname": surname.lower().capitalize(),
                "email": email,
                "phone": phone,
                "address": address,
                "national_id": national_id,
                "tsc_no": tsc_no,
                "username": username,
                "password": password,
                "dob": dob,
                "gender": gender,
                "subjectOneID": subjectOneid,
                "subjectTwoID": subjectTwoid
            }

            if saveTeacher(data):
                dlg = wx.MessageDialog(None, "Teacher Added Successfully.", 'Success Message',
                                       wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
                self.cancelAddTeacher("")
            else:
                dlg = wx.MessageDialog(None, "Teacher Not Saved. Try Again.", 'Failed',
                                       wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()

        self.save_teacher.Enable(True)