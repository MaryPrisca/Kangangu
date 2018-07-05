import wx
import wx.xrc

from ChangePassword import ChangePassword
from MyProfile import MyProfile


###########################################################################
# Class ProfilePanel
###########################################################################

class ProfilePanel(wx.Panel):

    def __init__(self, parent, userdata):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        self.userdata = userdata

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_toolBar7 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)
        self.m_tool14 = self.m_toolBar7.AddLabelTool(wx.ID_ANY, u"My Profile",
                                                     wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_TOOLBAR),
                                                     wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                     None)

        self.m_toolBar7.AddSeparator()

        self.m_tool13 = self.m_toolBar7.AddLabelTool(wx.ID_ANY, u"Change Password",
                                                     wx.ArtProvider.GetBitmap(wx.ART_FIND_AND_REPLACE, wx.ART_TOOLBAR),
                                                     wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                     None)

        self.m_toolBar7.Realize()

        container.Add(self.m_toolBar7, 0, wx.EXPAND, 5)

        # Add Panels
        self.my_profile = MyProfile(self, self.userdata)
        self.change_password = ChangePassword(self, self.userdata)
        self.change_password.Hide()

        container.Add(self.my_profile, 1, wx.EXPAND)
        container.Add(self.change_password, 1, wx.EXPAND)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.Bind(wx.EVT_TOOL, self.swtichToMyProfile, id=self.m_tool14.GetId())
        self.Bind(wx.EVT_TOOL, self.switchToChangePassword, id=self.m_tool13.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def swtichToMyProfile(self, event):
        self.change_password.Hide()
        self.my_profile.Show()

        self.Layout()

    def switchToChangePassword(self, event):
        self.my_profile.Hide()
        self.change_password.Show()

        self.Layout()


