import wx
import wx.xrc

from db.get_subjects import getSubjectByID

###########################################################################
# Class StudentProfile
###########################################################################


class StudentPersonalDetails(wx.Panel):

    def __init__(self, parent, student):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(735, 485),
                          style=wx.TAB_TRAVERSAL)

        subjects_taken = ""
        subjects = student['subjects_taken']
        if subjects is None or subjects == "":
            subjects_taken = "Not selected yet."
        else:
            subjects_ids = subjects.split(",")

            for subject_id in subjects_ids:
                subject_dets = getSubjectByID(subject_id)
                subjects_taken = subjects_taken + subject_dets['subject_name'] + "\n"

        container = wx.BoxSizer(wx.VERTICAL)

        self.student_profile_label = wx.StaticText(self, wx.ID_ANY, u"Student Profile", wx.DefaultPosition,
                                                   wx.DefaultSize, wx.ALIGN_CENTRE)
        self.student_profile_label.Wrap(-1)
        self.student_profile_label.SetFont(wx.Font(12, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.student_profile_label, 0, wx.ALL | wx.EXPAND, 10)

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        outer_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        content_sizer = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap5 = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"C:\\Users\\DELL\\Downloads\\person-icon.bmp", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(-1, -1), 0)
        content_sizer.Add(self.m_bitmap5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)

        self.m_staticline11 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        content_sizer.Add(self.m_staticline11, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        wrapper_sizer = wx.BoxSizer(wx.HORIZONTAL)

        right_side_sizer = wx.BoxSizer(wx.VERTICAL)

        firstname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.firstname_label = wx.StaticText(self, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.firstname_label.Wrap(-1)
        self.firstname_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        firstname_sizer.Add(self.firstname_label, 1, wx.ALL, 5)

        self.firstname = wx.StaticText(self, wx.ID_ANY, student['first_name'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.firstname.Wrap(-1)
        self.firstname.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        firstname_sizer.Add(self.firstname, 1, wx.ALL, 5)

        right_side_sizer.Add(firstname_sizer, 0, wx.EXPAND, 5)

        lastname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.lastname_label = wx.StaticText(self, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lastname_label.Wrap(-1)
        self.lastname_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        lastname_sizer.Add(self.lastname_label, 1, wx.ALL, 5)

        self.lastname = wx.StaticText(self, wx.ID_ANY, student['last_name'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.lastname.Wrap(-1)
        self.lastname.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        lastname_sizer.Add(self.lastname, 1, wx.ALL, 5)

        right_side_sizer.Add(lastname_sizer, 0, wx.EXPAND, 5)

        surname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.surname_label = wx.StaticText(self, wx.ID_ANY, u"Surname", wx.DefaultPosition, wx.DefaultSize, 0)
        self.surname_label.Wrap(-1)
        self.surname_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        surname_sizer.Add(self.surname_label, 1, wx.ALL, 5)

        self.surname = wx.StaticText(self, wx.ID_ANY, student['surname'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.surname.Wrap(-1)
        self.surname.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        surname_sizer.Add(self.surname, 1, wx.ALL, 5)

        right_side_sizer.Add(surname_sizer, 0, wx.EXPAND, 5)

        gender_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.gender_label = wx.StaticText(self, wx.ID_ANY, u"Gender", wx.DefaultPosition, wx.DefaultSize, 0)
        self.gender_label.Wrap(-1)
        self.gender_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        gender_sizer.Add(self.gender_label, 1, wx.ALL, 5)

        self.gender = wx.StaticText(self, wx.ID_ANY, student['gender'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.gender.Wrap(-1)
        self.gender.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        gender_sizer.Add(self.gender, 1, wx.ALL, 5)

        right_side_sizer.Add(gender_sizer, 0, wx.EXPAND, 5)

        dob_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.dob_label = wx.StaticText(self, wx.ID_ANY, u"Date of Birth", wx.DefaultPosition, wx.DefaultSize, 0)
        self.dob_label.Wrap(-1)
        self.dob_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        dob_sizer.Add(self.dob_label, 1, wx.ALL, 5)

        self.dob_text = wx.StaticText(self, wx.ID_ANY, str(student['dob']), wx.DefaultPosition, wx.DefaultSize, 0)
        self.dob_text.Wrap(-1)
        self.dob_text.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        dob_sizer.Add(self.dob_text, 1, wx.ALL, 5)

        right_side_sizer.Add(dob_sizer, 0, wx.EXPAND, 5)

        address_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.address_label = wx.StaticText(self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize, 0)
        self.address_label.Wrap(-1)
        self.address_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        address_sizer.Add(self.address_label, 1, wx.ALL, 5)

        self.address = wx.StaticText(self, wx.ID_ANY, student['address'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.address.Wrap(-1)
        self.address.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        address_sizer.Add(self.address, 1, wx.ALL, 5)

        right_side_sizer.Add(address_sizer, 0, wx.EXPAND, 5)

        wrapper_sizer.Add(right_side_sizer, 1, wx.EXPAND, 5)

        self.m_staticline17 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        wrapper_sizer.Add(self.m_staticline17, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        left_side_sixer = wx.BoxSizer(wx.VERTICAL)

        birth_cert_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.birth_cert_label = wx.StaticText(self, wx.ID_ANY, u"Birth Certificate No.", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.birth_cert_label.Wrap(-1)
        self.birth_cert_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        birth_cert_sizer.Add(self.birth_cert_label, 1, wx.ALL, 5)

        self.birth_cert = wx.StaticText(self, wx.ID_ANY, str(student['birth_cert_no']), wx.DefaultPosition, wx.DefaultSize, 0)
        self.birth_cert.Wrap(-1)
        self.birth_cert.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        birth_cert_sizer.Add(self.birth_cert, 0, wx.ALL, 5)

        left_side_sixer.Add(birth_cert_sizer, 0, wx.EXPAND, 5)

        kin_names_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.kin_names_label = wx.StaticText(self, wx.ID_ANY, u"Next of Kin Names", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.kin_names_label.Wrap(-1)
        self.kin_names_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        kin_names_sizer.Add(self.kin_names_label, 1, wx.ALL, 5)

        self.kin_names = wx.StaticText(self, wx.ID_ANY, student['next_of_kin_name'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.kin_names.Wrap(-1)
        self.kin_names.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        kin_names_sizer.Add(self.kin_names, 0, wx.ALL, 5)

        left_side_sixer.Add(kin_names_sizer, 0, wx.EXPAND, 5)

        kin_phone_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.kin_phone_label = wx.StaticText(self, wx.ID_ANY, u"Next of Kin Phone No.", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.kin_phone_label.Wrap(-1)
        self.kin_phone_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        kin_phone_sizer.Add(self.kin_phone_label, 1, wx.ALL, 5)

        self.kin_phone = wx.StaticText(self, wx.ID_ANY, student['next_of_kin_phone'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.kin_phone.Wrap(-1)
        self.kin_phone.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        kin_phone_sizer.Add(self.kin_phone, 0, wx.ALL, 5)

        left_side_sixer.Add(kin_phone_sizer, 0, wx.EXPAND, 5)

        kcpe_marks_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.kcpe_marks_label = wx.StaticText(self, wx.ID_ANY, u"KCPE Marks", wx.DefaultPosition, wx.DefaultSize, 0)
        self.kcpe_marks_label.Wrap(-1)
        self.kcpe_marks_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        kcpe_marks_sizer.Add(self.kcpe_marks_label, 1, wx.ALL, 5)

        self.kcpe_marks = wx.StaticText(self, wx.ID_ANY, str(student['kcpe_marks']), wx.DefaultPosition, wx.DefaultSize, 0)
        self.kcpe_marks.Wrap(-1)
        self.kcpe_marks.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        kcpe_marks_sizer.Add(self.kcpe_marks, 0, wx.ALL, 5)

        left_side_sixer.Add(kcpe_marks_sizer, 0, wx.EXPAND, 5)

        class_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.class_name_label = wx.StaticText(self, wx.ID_ANY, u"Class", wx.DefaultPosition, wx.DefaultSize, 0)
        self.class_name_label.Wrap(-1)
        self.class_name_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        class_name_sizer.Add(self.class_name_label, 1, wx.ALL, 5)

        self.class_name = wx.StaticText(self, wx.ID_ANY, str(student['form']) + " " + student['class'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.class_name.Wrap(-1)
        self.class_name.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        class_name_sizer.Add(self.class_name, 0, wx.ALL, 5)

        left_side_sixer.Add(class_name_sizer, 0, wx.EXPAND, 5)

        subject_choice_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.subject_choice_label = wx.StaticText(self, wx.ID_ANY, u"Subject Choices", wx.DefaultPosition, wx.DefaultSize, 0)
        self.subject_choice_label.Wrap(-1)
        self.subject_choice_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        subject_choice_sizer.Add(self.subject_choice_label, 1, wx.ALL, 5)

        self.subject_choice = wx.StaticText(self, wx.ID_ANY, subjects_taken, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.ALIGN_RIGHT )
        self.subject_choice.Wrap(-1)
        self.subject_choice.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        subject_choice_sizer.Add(self.subject_choice, 0, wx.ALL, 5)

        left_side_sixer.Add(subject_choice_sizer, 0, wx.EXPAND, 5)

        wrapper_sizer.Add(left_side_sixer, 1, wx.EXPAND, 5)

        content_sizer.Add(wrapper_sizer, 1, wx.EXPAND, 5)

        outer_sizer.Add(content_sizer, 4, wx.EXPAND, 5)

        outer_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(outer_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

    def __del__(self):
        pass


