import wx
import wx.xrc

###########################################################################
# Class AdminSetup
###########################################################################


class AdminSetup(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 437),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.setup_admin_label = wx.StaticText(self, wx.ID_ANY, u"Administrator Setup", wx.DefaultPosition,
                                               wx.DefaultSize, wx.ALIGN_CENTRE)
        self.setup_admin_label.Wrap(-1)
        self.setup_admin_label.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.setup_admin_label, 0, wx.ALL | wx.EXPAND, 5)

        self.navigation_disclaimer = wx.StaticText( self, wx.ID_ANY, u"(Please use buttons to navigate)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.navigation_disclaimer.Wrap(-1)

        container.Add(self.navigation_disclaimer, 0, wx.ALL | wx.EXPAND, 5)

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        outer_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        form_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        first_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.first_name_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Firstname", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.first_name_label.Wrap(-1)
        first_name_sizer.Add(self.first_name_label, 1, wx.ALL, 5)

        self.first_name = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        first_name_sizer.Add(self.first_name, 2, wx.ALL, 5)

        form_sizer.Add(first_name_sizer, 1, wx.EXPAND, 5)

        last_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.last_name_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Lastname", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.last_name_label.Wrap(-1)
        last_name_sizer.Add(self.last_name_label, 1, wx.ALL, 5)

        self.last_name = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        last_name_sizer.Add(self.last_name, 2, wx.ALL, 5)

        form_sizer.Add(last_name_sizer, 1, wx.EXPAND, 5)

        surname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.surname_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Surname", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.surname_label.Wrap(-1)
        surname_sizer.Add(self.surname_label, 1, wx.ALL, 5)

        self.surname = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        surname_sizer.Add(self.surname, 2, wx.ALL, 5)

        form_sizer.Add(surname_sizer, 1, wx.EXPAND, 5)

        phone_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.phone_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Phone", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.phone_label.Wrap(-1)
        phone_sizer.Add(self.phone_label, 1, wx.ALL, 5)

        self.phone = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        phone_sizer.Add(self.phone, 2, wx.ALL, 5)

        form_sizer.Add(phone_sizer, 1, wx.EXPAND, 5)

        email_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.email_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Email", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.email_label.Wrap(-1)
        email_sizer.Add(self.email_label, 1, wx.ALL, 5)

        self.email = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        email_sizer.Add(self.email, 2, wx.ALL, 5)

        form_sizer.Add(email_sizer, 1, wx.EXPAND, 5)

        dob_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.dob_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"DOB", wx.DefaultPosition, wx.DefaultSize,
                                       0)
        self.dob_label.Wrap(-1)
        dob_sizer.Add(self.dob_label, 1, wx.ALL, 5)

        self.dob = wx.DatePickerCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                     wx.DefaultSize, wx.DP_DEFAULT | wx.DP_DROPDOWN)
        dob_sizer.Add(self.dob, 2, wx.ALL, 5)

        form_sizer.Add(dob_sizer, 1, wx.EXPAND, 5)

        gender_szier = wx.BoxSizer(wx.HORIZONTAL)

        self.gender_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Gender", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.gender_label.Wrap(-1)
        gender_szier.Add(self.gender_label, 1, wx.ALL, 5)

        genderChoices = [u"Male", u"Female"]
        self.gender = wx.ComboBox(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                  wx.DefaultSize, genderChoices, wx.CB_READONLY)
        gender_szier.Add(self.gender, 2, wx.ALL, 5)

        form_sizer.Add(gender_szier, 1, wx.EXPAND, 5)

        username_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.username_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Username", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.username_label.Wrap(-1)
        username_sizer.Add(self.username_label, 1, wx.ALL, 5)

        self.username = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        username_sizer.Add(self.username, 2, wx.ALL, 5)

        form_sizer.Add(username_sizer, 1, wx.EXPAND, 5)

        password_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.password_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.password_label.Wrap(-1)
        password_sizer.Add(self.password_label, 1, wx.ALL, 5)

        self.password = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, wx.TE_PASSWORD)
        password_sizer.Add(self.password, 2, wx.ALL, 5)

        form_sizer.Add(password_sizer, 1, wx.EXPAND, 5)

        conf_password_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.conf_password_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Confirm Password", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.conf_password_label.Wrap(-1)
        conf_password_sizer.Add(self.conf_password_label, 1, wx.ALL, 5)

        self.conf_password = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, wx.TE_PASSWORD)
        conf_password_sizer.Add(self.conf_password, 2, wx.ALL, 5)

        form_sizer.Add(conf_password_sizer, 1, wx.EXPAND, 5)

        outer_sizer.Add(form_sizer, 3, wx.EXPAND | wx.TOP | wx.BOTTOM, 10)

        outer_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(outer_sizer, 1, wx.EXPAND | wx.BOTTOM, 5)

        self.SetSizer(container)
        self.Layout()

    def __del__(self):
        pass


