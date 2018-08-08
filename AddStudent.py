import wx
from datetime import datetime
from db.save_student import saveStudent
from db.get_classes import getFormClasses, getClassNames, getClassNamesWithForm
# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')


class AddStudent(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"Add New Student", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText17, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 30)

        content_sizer = wx.BoxSizer(wx.HORIZONTAL)

        content_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Add Student Form"), wx.VERTICAL)

        wrapper_sizer = wx.BoxSizer(wx.HORIZONTAL)

        right_conrtols_sizer = wx.BoxSizer(wx.VERTICAL)

        fname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.fname_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"First Name", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.fname_label.Wrap(-1)
        fname_sizer.Add(self.fname_label, 1, wx.ALL, 8)

        self.first_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        fname_sizer.Add(self.first_name, 3, wx.ALL, 5)

        right_conrtols_sizer.Add(fname_sizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 10)

        lname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.lname_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Last Name", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.lname_label.Wrap(-1)
        lname_sizer.Add(self.lname_label, 1, wx.ALL, 8)

        self.last_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        lname_sizer.Add(self.last_name, 3, wx.ALL, 5)

        right_conrtols_sizer.Add(lname_sizer, 1, wx.ALL | wx.EXPAND, 10)

        surname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.surname_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Surname", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.surname_label.Wrap(-1)
        surname_sizer.Add(self.surname_label, 1, wx.ALL, 8)

        self.surname = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        surname_sizer.Add(self.surname, 3, wx.ALL, 5)

        right_conrtols_sizer.Add(surname_sizer, 1, wx.ALL | wx.EXPAND, 10)

        address_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.address_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Address", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.address_label.Wrap(-1)
        address_sizer.Add(self.address_label, 1, wx.ALL, 8)

        self.address = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        address_sizer.Add(self.address, 3, wx.ALL, 5)

        right_conrtols_sizer.Add(address_sizer, 1, wx.ALL | wx.EXPAND, 10)

        dob_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.dob_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Date of Birth", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.dob_label.Wrap(-1)
        dob_sizer.Add(self.dob_label, 1, wx.ALL, 8)

        self.dob = wx.DatePickerCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                     wx.DefaultSize, wx.DP_DEFAULT | wx.DP_DROPDOWN)
        dob_sizer.Add(self.dob, 3, wx.ALL, 5)

        right_conrtols_sizer.Add(dob_sizer, 1, wx.ALL | wx.EXPAND, 10)

        geder_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.gender_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Gender", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.gender_label.Wrap(-1)
        geder_sizer.Add(self.gender_label, 1, wx.ALL, 8)

        genderChoices = [u"Male", u"Female"]
        self.gender = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Female", wx.DefaultPosition, wx.DefaultSize,
                                  genderChoices, wx.CB_READONLY)
        self.gender.SetSelection(1)
        geder_sizer.Add(self.gender, 3, wx.ALL, 5)

        right_conrtols_sizer.Add(geder_sizer, 1, wx.ALL | wx.EXPAND, 10)

        wrapper_sizer.Add(right_conrtols_sizer, 1, wx.EXPAND, 5)

        left_controls_sizer = wx.BoxSizer(wx.VERTICAL)

        class_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.class_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Class", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.class_label.Wrap(-1)
        class_sizer.Add(self.class_label, 1, wx.ALL, 8)

        self.classes = getClassNamesWithForm()

        class_idChoices = self.classes['names']

        self.class_id = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, class_idChoices, wx.CB_READONLY)
        class_sizer.Add(self.class_id, 3, wx.ALL, 5)

        left_controls_sizer.Add(class_sizer, 1, wx.ALL | wx.EXPAND, 10)

        kin_names_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.kin_names_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Next of Kin Names", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.kin_names_label.Wrap(-1)
        kin_names_sizer.Add(self.kin_names_label, 1, wx.ALL, 8)

        self.kin_names = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        kin_names_sizer.Add(self.kin_names, 3, wx.ALL, 5)

        left_controls_sizer.Add(kin_names_sizer, 1, wx.ALL | wx.EXPAND, 10)

        kin_phone_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.kin_phone_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Next of Kin Phone",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.kin_phone_label.Wrap(-1)
        kin_phone_sizer.Add(self.kin_phone_label, 1, wx.ALL, 8)

        self.kin_phone = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        kin_phone_sizer.Add(self.kin_phone, 3, wx.ALL, 5)

        left_controls_sizer.Add(kin_phone_sizer, 1, wx.ALL | wx.EXPAND, 10)

        birth_cert_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.birth_cert_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Birth Certificate No",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.birth_cert_label.Wrap(-1)
        birth_cert_sizer.Add(self.birth_cert_label, 1, wx.ALL, 8)

        self.birth_cert_no = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        birth_cert_sizer.Add(self.birth_cert_no, 3, wx.ALL, 5)

        left_controls_sizer.Add(birth_cert_sizer, 1, wx.ALL | wx.EXPAND, 10)

        kcpe_marks_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.kcpe_marks_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"KCPE Marks", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.kcpe_marks_label.Wrap(-1)
        kcpe_marks_sizer.Add(self.kcpe_marks_label, 1, wx.ALL, 8)

        self.kcpe_marks = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        kcpe_marks_sizer.Add(self.kcpe_marks, 3, wx.ALL, 5)

        left_controls_sizer.Add(kcpe_marks_sizer, 1, wx.ALL | wx.EXPAND, 10)

        wrapper_sizer.Add(left_controls_sizer, 1, wx.EXPAND, 5)

        sbSizer2.Add(wrapper_sizer, 1, wx.EXPAND, 5)

        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        buttons_sizer.Add(self.m_staticText22, 1, wx.ALL, 5)

        self.cancel_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        buttons_sizer.Add(self.cancel_btn, 0, wx.ALL, 5)

        self.save_student = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        buttons_sizer.Add(self.save_student, 0, wx.ALL, 5)

        sbSizer2.Add(buttons_sizer, 3, wx.ALL | wx.EXPAND, 10)

        content_sizer.Add(sbSizer2, 2, wx.EXPAND, 5)

        content_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(content_sizer, 1, wx.EXPAND, 5)

        self.below_form_spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.below_form_spacer.Wrap(-1)
        container.Add(self.below_form_spacer, 0, wx.ALL, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelAddStudent)
        self.save_student.Bind(wx.EVT_BUTTON, self.saveStudent)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class

    def cancelAddStudent(self, event):
        self.first_name.SetValue("")
        self.last_name.SetValue("")
        self.surname.SetValue("")
        self.address.SetValue("")
        self.kin_names.SetValue("")
        self.kin_phone.SetValue("")
        self.birth_cert_no.SetValue("")
        self.kcpe_marks.SetValue("")

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

    def hasNumbers(self, inputString):  # checks for numbers in string, returns true if there is a number
        return any(char.isdigit() for char in inputString)

    def saveStudent(self, event):
        first_name = self.first_name.GetLineText(0)
        last_name = self.last_name.GetLineText(0)
        surname = self.surname.GetLineText(0)
        address = self.address.GetLineText(0)
        dob = self.dob.GetValue()
        kin_names = self.kin_names.GetLineText(0)
        kin_phone = self.kin_phone.GetLineText(0)
        birth_cert_no = self.birth_cert_no.GetLineText(0)
        kcpe_marks = self.kcpe_marks.GetLineText(0)
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

        if address == "":
            error = error + "The Address field is required.\n"

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

        if classIndex == -1:
            error = error + "The Class field is required.\n"

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

            # use class Index to match with class ID's list
            class_id = self.classes['ids'][classIndex]

            student_data = {
                "first_name": first_name,
                "last_name": last_name,
                "surname": surname,
                "address": address,
                "dob": dob,
                "gender": gender,
                "class_id": class_id,
                "kin_names": kin_names,
                "kin_phone": kin_phone,
                "birth_cert_no": birth_cert_no,
                "kcpe_marks": kcpe_marks
            }

            if saveStudent(student_data):
                dlg = wx.MessageDialog(None, "Student Added Successfully.", 'Success Message', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                self.cancelAddStudent("")
            else:
                dlg = wx.MessageDialog(None, "Student Not Saved. Try Again.", 'Failed',
                                       wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()