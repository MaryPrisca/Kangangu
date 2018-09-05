import wx
import wx.xrc
from AddClass import AddClass
from ViewClasses import ViewClasses


class ClassesPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        self.parent = parent

        container = wx.BoxSizer(wx.VERTICAL)

        bSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_toolBar1 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)

        self.m_tool2 = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"View All",
                                                    wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW, wx.ART_TOOLBAR),
                                                    wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar1.AddSeparator()

        self.m_tool1 = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"Add New",
                                                    wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar1.AddSeparator()

        self.m_toolBar1.Realize()

        bSizer.Add(self.m_toolBar1, 1, wx.EXPAND, 5)

        self.m_toolBar4 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)
        self.logout_tool = self.m_toolBar4.AddLabelTool(wx.ID_ANY, u"Logout",
                                                        wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_TOOLBAR),
                                                        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                        None)

        self.m_toolBar4.Realize()

        bSizer.Add(self.m_toolBar4, 0, wx.EXPAND, 5)

        container.Add(bSizer, 0, wx.EXPAND, 5)

        # ------------ ADD PANELS ------------------
        self.add_class = AddClass(self)
        self.view_classes = ViewClasses(self)
        self.add_class.Hide()

        container.Add(self.add_class, 1, wx.EXPAND)
        container.Add(self.view_classes, 1, wx.EXPAND)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.Bind(wx.EVT_TOOL, self.switchToViewClasses, id=self.m_tool2.GetId())
        self.Bind(wx.EVT_TOOL, self.switchToAddClass, id=self.m_tool1.GetId())
        self.Bind(wx.EVT_TOOL, self.parent.Logout, id=self.logout_tool.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def switchToViewClasses(self, event):
        self.add_class.Hide()
        self.view_classes.Show()

        self.Layout()

    def switchToAddClass(self, event):
        self.view_classes.Hide()
        self.add_class.Show()

        self.Layout()



