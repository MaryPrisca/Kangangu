import wx
import wx.xrc

from AddEvent import AddEvent
from ViewEvents import ViewEvents


###########################################################################
# Class EventsPanel
###########################################################################


class EventsPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_toolBar1 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)
        # self.m_toolBar1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.m_tool1 = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"Add New",
                                                    wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar1.AddSeparator()

        self.m_tool2 = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"View All",
                                                    wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW, wx.ART_TOOLBAR),
                                                    wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar1.Realize()

        container.Add(self.m_toolBar1, 0, wx.EXPAND, 5)

        # ------------ ADD PANELS ------------------
        self.add_event = AddEvent(self)
        self.view_events = ViewEvents(self)
        # self.add_event.Hide()
        self.view_events.Hide()

        container.Add(self.add_event, 1, wx.EXPAND)
        container.Add(self.view_events, 1, wx.EXPAND)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.Bind(wx.EVT_TOOL, self.switchToAddEvent, id=self.m_tool1.GetId())
        self.Bind(wx.EVT_TOOL, self.switchToViewEvents, id=self.m_tool2.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def switchToAddEvent(self, event):
        self.view_events.Hide()
        self.add_event.Show()

        self.Layout()

    def switchToViewEvents(self, event):
        self.add_event.Hide()
        self.view_events.Show()

        self.Layout()


