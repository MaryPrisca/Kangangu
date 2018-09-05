import wx
import wx.xrc

from db.edit_profile import editProfile
from datetime import datetime
import re  # Regex

# import sys
# sys.path.insert(0, r'../Kngangu')
###########################################################################
# Class MyProfile
###########################################################################


class MyProfile(wx.Panel):

    def __init__(self, parent, userdata):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(597, 764),
                          style=wx.TAB_TRAVERSAL)

        self.userdata = userdata

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"My Profile", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText17, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 30)

        bSizer27 = wx.BoxSizer(wx.HORIZONTAL)

        left_spacer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        left_spacer.Add(self.m_staticText30, 0, wx.ALL, 5)

        bSizer27.Add(left_spacer, 1, wx.EXPAND, 5)

        form_sizer = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"My Details"), wx.VERTICAL)

        user_id_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.user_id = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.user_id.Hide()

        user_id_sizer.Add(self.user_id, 3, wx.ALL, 5)

        sbSizer2.Add(user_id_sizer, 1, wx.EXPAND, 5)

        fname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText29 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"First Name", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)
        self.m_staticText29.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        fname_sizer.Add(self.m_staticText29, 1, wx.ALL, 10)

        self.first_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        fname_sizer.Add(self.first_name, 3, wx.ALL, 5)

        sbSizer2.Add(fname_sizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 10)

        lname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText292 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Last Name", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText292.Wrap(-1)
        self.m_staticText292.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        lname_sizer.Add(self.m_staticText292, 1, wx.ALL, 10)

        self.last_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        lname_sizer.Add(self.last_name, 3, wx.ALL, 5)

        sbSizer2.Add(lname_sizer, 1, wx.ALL | wx.EXPAND, 10)

        surname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText293 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Surname", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText293.Wrap(-1)
        self.m_staticText293.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        surname_sizer.Add(self.m_staticText293, 1, wx.ALL, 10)

        self.surname = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        surname_sizer.Add(self.surname, 3, wx.ALL, 5)

        sbSizer2.Add(surname_sizer, 1, wx.ALL | wx.EXPAND, 10)

        email_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Email Address", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.m_staticText.Wrap(-1)
        self.m_staticText.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        email_sizer.Add(self.m_staticText, 1, wx.ALL, 10)

        self.email = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 0)
        email_sizer.Add(self.email, 3, wx.ALL, 5)

        sbSizer2.Add(email_sizer, 1, wx.ALL | wx.EXPAND, 10)

        dob_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText291 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Date of Birth", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText291.Wrap(-1)
        self.m_staticText291.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        dob_sizer.Add(self.m_staticText291, 1, wx.ALL, 10)

        self.dob = wx.DatePickerCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                     wx.DefaultSize, wx.DP_DEFAULT | wx.DP_DROPDOWN)
        dob_sizer.Add(self.dob, 3, wx.ALL, 5)

        sbSizer2.Add(dob_sizer, 1, wx.ALL | wx.EXPAND, 10)

        gender_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText294 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Gender", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText294.Wrap(-1)
        self.m_staticText294.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        gender_sizer.Add(self.m_staticText294, 1, wx.ALL, 10)

        genderChoices = [u"Male", u"Female"]
        self.gender = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Male", wx.DefaultPosition, wx.DefaultSize,
                                  genderChoices, wx.CB_READONLY)
        self.gender.SetSelection(0)
        gender_sizer.Add(self.gender, 3, wx.ALL, 5)

        sbSizer2.Add(gender_sizer, 1, wx.ALL | wx.EXPAND, 10)

        username_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Username", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        username_sizer.Add(self.m_staticText1, 1, wx.ALL, 10)

        self.username = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        username_sizer.Add(self.username, 3, wx.ALL, 5)

        sbSizer2.Add(username_sizer, 1, wx.ALL | wx.EXPAND, 10)

        btns_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        btns_sizer.Add(self.m_staticText22, 1, wx.ALL, 5)

        self.cancel_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.cancel_btn.Hide()
        btns_sizer.Add(self.cancel_btn, 0, wx.ALL, 5)

        self.edit_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0)
        btns_sizer.Add(self.edit_btn, 0, wx.ALL, 5)

        self.save_edit = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
        self.save_edit.Hide()
        btns_sizer.Add(self.save_edit, 0, wx.ALL, 5)

        sbSizer2.Add(btns_sizer, 3, wx.ALL | wx.EXPAND, 10)

        form_sizer.Add(sbSizer2, 1, wx.EXPAND, 5)

        self.m_staticText301 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText301.Wrap(-1)
        self.m_staticText301.SetFont(wx.Font(30, 70, 90, 90, False, wx.EmptyString))

        form_sizer.Add(self.m_staticText301, 0, wx.ALL | wx.EXPAND, 5)

        bSizer27.Add(form_sizer, 3, wx.EXPAND, 5)

        right_spacer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        right_spacer.Add(self.m_staticText31, 0, wx.ALL, 5)

        bSizer27.Add(right_spacer, 1, wx.EXPAND, 5)

        container.Add(bSizer27, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Set the values of the textboxes
        self.user_id.SetValue(str(self.userdata['user_id']))
        self.first_name.SetValue(self.userdata['first_name'])
        self.last_name.SetValue(self.userdata['last_name'])
        self.surname.SetValue(self.userdata['surname'])
        self.email.SetValue(self.userdata['email'])
        self.username.SetValue(self.userdata['username'])

        if self.userdata['gender'] == "M":
            gen = "Male"
        else:
            gen = "Female"

        self.gender.SetValue(gen)

        # get wxPython datetime format
        day = self.userdata['dob'].day
        month = self.userdata['dob'].month
        year = self.userdata['dob'].year

        # -1 because the month counts from 0, whereas people count January as month #1.
        dateFormatted = wx.DateTimeFromDMY(day, month - 1, year)

        self.dob.SetValue(dateFormatted)

        # Disable edit
        self.first_name.Enable(False)
        self.last_name.Enable(False)
        self.surname.Enable(False)
        self.email.Enable(False)
        self.username.Enable(False)
        self.gender.Enable(False)
        self.dob.Enable(False)

        # Connect Events
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelEditProfile)
        self.edit_btn.Bind(wx.EVT_BUTTON, self.openEditForm)
        self.save_edit.Bind(wx.EVT_BUTTON, self.saveEditProfile)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def openEditForm(self, event):
        self.first_name.Enable(True)
        self.last_name.Enable(True)
        self.surname.Enable(True)
        self.email.Enable(True)
        self.username.Enable(True)
        self.gender.Enable(True)
        self.dob.Enable(True)

        self.edit_btn.Hide()
        self.cancel_btn.Show(True)
        self.save_edit.Show(True)
        self.Layout()

    def cancelEditProfile(self, event):
        self.first_name.Enable(False)
        self.last_name.Enable(False)
        self.surname.Enable(False)
        self.email.Enable(False)
        self.username.Enable(False)
        self.gender.Enable(False)
        self.dob.Enable(False)

        self.edit_btn.Show(True)
        self.cancel_btn.Hide()
        self.save_edit.Hide()
        self.Layout()

    def hasNumbers(self, inputString):  # checks for numbers in string, returns true if there is a number
        return any(char.isdigit() for char in inputString)

    def saveEditProfile(self, event):
        user_id = self.user_id.GetLineText(0)
        first_name = self.first_name.GetLineText(0)
        last_name = self.last_name.GetLineText(0)
        surname = self.surname.GetLineText(0)
        email = self.email.GetLineText(0)
        username = self.username.GetLineText(0)
        dob = self.dob.GetValue()
        genderIndex = self.gender.GetCurrentSelection()

        # Remove white spaces
        first_name = first_name.replace(" ", "")
        last_name = last_name.replace(" ", "")
        surname = surname.replace(" ", "")
        email = email.replace(" ", "")
        username = username.replace(" ", "")

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

            dob = str(dob)[:-9]
            dob = datetime.strptime(dob, "%d/%m/%Y").date()

            data = {
                "user_id": user_id,
                "first_name": first_name.lower().capitalize(),
                "last_name": last_name.lower().capitalize(),
                "surname": surname.lower().capitalize(),
                "email": email,
                "username": username,
                "dob": dob,
                "gender": gender,
            }

            if editProfile(data):
                dlg = wx.MessageDialog(None, "Profile Edited Successfully.", 'Success Message',
                                       wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
                self.cancelEditProfile("")
            else:
                dlg = wx.MessageDialog(None, "Edit Failed. Try Again.", 'Failed',
                                       wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()