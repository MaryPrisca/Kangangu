import wx


class SetupSchoolDetails(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(533, 374),
                          style=wx.TAB_TRAVERSAL)

        self.parent = parent

        container = wx.BoxSizer(wx.VERTICAL)

        self.school_dets_label = wx.StaticText(self, wx.ID_ANY, u"School Details", wx.DefaultPosition, wx.DefaultSize,
                                               wx.ALIGN_CENTRE)
        self.school_dets_label.Wrap(-1)
        self.school_dets_label.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.school_dets_label, 0, wx.ALL | wx.EXPAND, 30)

        self.navigation_disclaimer = wx.StaticText( self, wx.ID_ANY, u"(Please use buttons to navigate)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.navigation_disclaimer.Wrap(-1)

        container.Add(self.navigation_disclaimer, 0, wx.ALL | wx.EXPAND, 5)

        content_Sizer = wx.BoxSizer(wx.HORIZONTAL)

        content_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        formSizer = wx.BoxSizer(wx.VERTICAL)

        formSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        sbSizer15 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.school_name_label = wx.StaticText(sbSizer15.GetStaticBox(), wx.ID_ANY, u"School Name", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.school_name_label.Wrap(-1)
        sbSizer15.Add(self.school_name_label, 0, wx.ALL, 10)

        self.school_name = wx.TextCtrl(sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        sbSizer15.Add(self.school_name, 0, wx.ALL | wx.EXPAND, 10)

        self.no_of_subjects_label = wx.StaticText(sbSizer15.GetStaticBox(), wx.ID_ANY,
                                                  u"Number of subjects done by lower forms", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.no_of_subjects_label.Wrap(-1)
        sbSizer15.Add(self.no_of_subjects_label, 0, wx.ALL, 10)

        self.no_of_subjects = wx.TextCtrl(sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        sbSizer15.Add(self.no_of_subjects, 0, wx.ALL | wx.EXPAND, 10)

        formSizer.Add(sbSizer15, 1, wx.EXPAND, 5)

        formSizer.AddSpacer((0, 0), 5, wx.EXPAND, 5)

        content_Sizer.Add(formSizer, 3, wx.EXPAND, 5)

        content_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(content_Sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

    def __del__(self):
        pass
