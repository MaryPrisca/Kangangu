import wx
from AddTeacher import AddTeacher
from ViewTeachers import ViewTeachers


class TeachersPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        bSizer78 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_toolBar1 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)

        self.m_tool2 = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"View All",
                                                    wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW, wx.ART_TOOLBAR),
                                                    wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar1.AddSeparator()

        self.m_tool1 = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"Add New",
                                                    wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar1.Realize()

        bSizer78.Add(self.m_toolBar1, 1, wx.EXPAND, 5)

        self.m_toolBar4 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)
        self.m_tool5 = self.m_toolBar4.AddLabelTool(wx.ID_ANY, u"My Profile",
                                                    wx.ArtProvider.GetBitmap(wx.ART_TIP, wx.ART_TOOLBAR), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar4.Realize()

        bSizer78.Add(self.m_toolBar4, 0, wx.EXPAND, 5)

        container.Add(bSizer78, 0, wx.EXPAND, 5)

        # Add Panels
        self.add_teacher = AddTeacher(self)
        self.view_teachers = ViewTeachers(self)
        self.add_teacher.Hide()

        container.Add(self.add_teacher, 1, wx.EXPAND)
        container.Add(self.view_teachers, 1, wx.EXPAND)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.Bind(wx.EVT_TOOL, self.switchToAddTeacher, id=self.m_tool1.GetId())
        self.Bind(wx.EVT_TOOL, self.switchToViewTeachers, id=self.m_tool2.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def switchToAddTeacher(self, event):
        self.view_teachers.Hide()
        self.add_teacher.Show()

        self.Layout()

    def switchToViewTeachers(self, event):
        self.add_teacher.Hide()
        self.view_teachers.Show()

        self.Layout()