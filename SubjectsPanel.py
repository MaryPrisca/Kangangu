import wx
import wx.xrc
from AddSubject import AddSubject
from ViewSubjects import ViewSubjects


###########################################################################
# Class SubjectsPanel
###########################################################################

class SubjectsPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        self.parent = parent

        container = wx.BoxSizer(wx.VERTICAL)

        bSizer78 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_toolBar3 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)
        self.m_tool7 = self.m_toolBar3.AddLabelTool(wx.ID_ANY, u"View All",
                                                    wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW, wx.ART_TOOLBAR),
                                                    wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar3.AddSeparator()

        self.m_tool6 = self.m_toolBar3.AddLabelTool(wx.ID_ANY, u"Add New",
                                                    wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar3.Realize()

        bSizer78.Add(self.m_toolBar3, 1, wx.EXPAND, 5)

        self.m_toolBar4 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)
        self.logout_tool = self.m_toolBar4.AddLabelTool(wx.ID_ANY, u"Logout",
                                                        wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_TOOLBAR),
                                                        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                        None)
        self.m_toolBar4.Realize()

        bSizer78.Add(self.m_toolBar4, 0, wx.EXPAND, 5)

        container.Add(bSizer78, 0, wx.EXPAND, 5)

        # ------------ ADD PANELS ------------------
        self.add_subject = AddSubject(self)
        self.view_subjects = ViewSubjects(self)
        self.add_subject.Hide()

        container.Add(self.add_subject, 1, wx.EXPAND)
        container.Add(self.view_subjects, 1, wx.EXPAND)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.Bind(wx.EVT_TOOL, self.switchToViewSubjects, id=self.m_tool7.GetId())
        self.Bind(wx.EVT_TOOL, self.switchToAddSubject, id=self.m_tool6.GetId())
        self.Bind(wx.EVT_TOOL, self.parent.Logout, id=self.logout_tool.GetId())

    def __del__(self):
        pass

    def switchToViewSubjects(self, event):
        self.add_subject.Hide()
        self.view_subjects.Show()

        self.Layout()

    def switchToAddSubject(self, event):
        self.view_subjects.Hide()
        self.add_subject.Show()

        self.Layout()
