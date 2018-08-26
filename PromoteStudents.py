import wx
import wx.xrc

from db.promote_students import promoteStudents


###########################################################################
# Class PromoteStudents
###########################################################################

class PromoteStudents(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.panel_title = wx.StaticText(self, wx.ID_ANY, u"Promote students to next class", wx.DefaultPosition,
                                         wx.DefaultSize, wx.ALIGN_CENTRE)
        self.panel_title.Wrap(-1)
        self.panel_title.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.panel_title, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 30)

        self.disclaimer = wx.StaticText(self, wx.ID_ANY, u"Please do this only when necessary, it cannot be reversed",
                                        wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.disclaimer.Wrap(-1)
        self.disclaimer.SetForegroundColour(wx.Colour(255, 0, 0))

        container.Add(self.disclaimer, 0, wx.ALL | wx.EXPAND, 5)

        content_sizer = wx.BoxSizer(wx.VERTICAL)

        content_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        btnSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.promote_students_btn = wx.Button(self, wx.ID_ANY, u"Move all students to the next class",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        btnSizer.Add(self.promote_students_btn, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

        btnSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        content_sizer.Add(btnSizer, 1, wx.EXPAND, 5)

        content_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(content_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.promote_students_btn.Bind(wx.EVT_BUTTON, self.promoteStudents)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def promoteStudents(self, event):
        promoteStudents()


