import wx
from datetime import datetime
from db.save_student import saveStudent
from db.get_classes import getFormClasses, getClassNames
# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')


class AddStudent(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(641, 689),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"Add New Student", wx.DefaultPosition, wx.DefaultSize,
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

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Add Student Form"), wx.VERTICAL)

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

        self.cancel_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        bSizer271.Add(self.cancel_btn, 0, wx.ALL, 5)

        self.save_student = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        bSizer271.Add(self.save_student, 0, wx.ALL, 5)

        sbSizer2.Add(bSizer271, 3, wx.ALL | wx.EXPAND, 10)

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
        self.form.Bind(wx.EVT_COMBOBOX, self.get_classes)
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelAddStudent)
        self.save_student.Bind(wx.EVT_BUTTON, self.saveStudent)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def get_classes(self, event):
        """"""
        # form = self.form.GetCurrentSelection()
        # classes = getFormClasses(form)
        # print classes

    def cancelAddStudent(self, event):
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

    def saveStudent(self, event):
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

            class_id = classIndex + 1

            student_data = {
                "first_name": first_name,
                "last_name": last_name,
                "surname": surname,
                "dob": dob,
                "gender": gender,
                "class_id": class_id
            }

            if saveStudent(student_data):
                dlg = wx.MessageDialog(None, "Student Added Successfully.", 'Success Message', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                self.cancelAddStudent("")
            else:
                dlg = wx.MessageDialog(None, "Student Not Saved. Try Again.", 'Failed',
                                       wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()