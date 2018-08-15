import wx
import wx.xrc


###########################################################################
# Class SetupFormsClasses
###########################################################################

class SetupForms(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 456),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.forms_title = wx.StaticText(self, wx.ID_ANY, u"Setup Forms", wx.DefaultPosition, wx.DefaultSize,
                                         wx.ALIGN_CENTRE)
        self.forms_title.Wrap(-1)
        self.forms_title.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.forms_title, 0, wx.ALL | wx.EXPAND, 30)

        content_Sizer = wx.BoxSizer(wx.HORIZONTAL)

        content_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        formSizer = wx.BoxSizer(wx.VERTICAL)

        formSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        bSizer260 = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer15 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Enter Number of Streams"), wx.VERTICAL)

        self.form_one_label = wx.StaticText(sbSizer15.GetStaticBox(), wx.ID_ANY, u"Form 1", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.form_one_label.Wrap(-1)
        sbSizer15.Add(self.form_one_label, 0, wx.ALL, 5)

        self.form_one = wx.TextCtrl(sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        sbSizer15.Add(self.form_one, 0, wx.ALL | wx.EXPAND, 5)

        self.form_two_label = wx.StaticText(sbSizer15.GetStaticBox(), wx.ID_ANY, u"Form 2", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.form_two_label.Wrap(-1)
        sbSizer15.Add(self.form_two_label, 0, wx.ALL, 5)

        self.form_two = wx.TextCtrl(sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        sbSizer15.Add(self.form_two, 0, wx.ALL | wx.EXPAND, 5)

        self.form_three_label = wx.StaticText(sbSizer15.GetStaticBox(), wx.ID_ANY, u"Form 3", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.form_three_label.Wrap(-1)
        sbSizer15.Add(self.form_three_label, 0, wx.ALL, 5)

        self.form_three = wx.TextCtrl(sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        sbSizer15.Add(self.form_three, 0, wx.ALL | wx.EXPAND, 5)

        self.form_four_label = wx.StaticText(sbSizer15.GetStaticBox(), wx.ID_ANY, u"Form 4", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.form_four_label.Wrap(-1)
        sbSizer15.Add(self.form_four_label, 0, wx.ALL, 5)

        self.form_four = wx.TextCtrl(sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        sbSizer15.Add(self.form_four, 0, wx.ALL | wx.EXPAND, 5)

        bSizer260.Add(sbSizer15, 1, wx.ALL | wx.EXPAND, 5)

        formSizer.Add(bSizer260, 1, wx.EXPAND, 5)

        formSizer.AddSpacer((0, 0), 5, wx.EXPAND, 5)

        content_Sizer.Add(formSizer, 3, wx.EXPAND, 5)

        content_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(content_Sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

    def __del__(self):
        pass



