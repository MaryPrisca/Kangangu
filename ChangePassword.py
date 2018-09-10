import wx
import wx.xrc

from db.change_password import changePassword
from db.change_password import checkOldPassword

###########################################################################
# Class ChangePassword
###########################################################################


class ChangePassword(wx.Panel):

    def __init__(self, parent, userdata):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(569, 463),
                          style=wx.TAB_TRAVERSAL)

        self.userdata = userdata

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"Change Password", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText17, 0, wx.ALL | wx.EXPAND, 25)

        bSizer73 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer28 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        bSizer28.Add(self.m_staticText30, 1, wx.ALL | wx.EXPAND, 5)

        bSizer73.Add(bSizer28, 1, wx.EXPAND, 5)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Change Password Form"), wx.VERTICAL)

        user_id_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.user_id = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.user_id.Hide()

        user_id_sizer.Add(self.user_id, 3, wx.ALL, 5)

        sbSizer2.Add(user_id_sizer, 1, wx.EXPAND, 5)

        old_password_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.old_pwd_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Old Password", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.old_pwd_label.Wrap(-1)
        old_password_sizer.Add(self.old_pwd_label, 1, wx.ALL, 10)

        self.old_pwd = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, wx.TE_PASSWORD )
        old_password_sizer.Add(self.old_pwd, 3, wx.ALL, 10)

        sbSizer2.Add(old_password_sizer, 1, wx.ALL | wx.EXPAND, 10)

        new_password_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.new_pwd_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"New Password", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.new_pwd_label.Wrap(-1)
        new_password_sizer.Add(self.new_pwd_label, 1, wx.ALL, 10)

        self.new_pwd = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, wx.TE_PASSWORD )
        new_password_sizer.Add(self.new_pwd, 3, wx.ALL, 10)

        sbSizer2.Add(new_password_sizer, 1, wx.ALL | wx.EXPAND, 10)

        conf_password_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.statictext = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Confirm Password", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.statictext.Wrap(-1)
        conf_password_sizer.Add(self.statictext, 1, wx.ALL, 10)

        self.confirm_pwd = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_PASSWORD )
        conf_password_sizer.Add(self.confirm_pwd, 3, wx.ALL, 10)

        sbSizer2.Add(conf_password_sizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 10)

        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        buttons_sizer.Add(self.m_staticText22, 1, wx.ALL, 5)

        self.cancel_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        buttons_sizer.Add(self.cancel_btn, 0, wx.ALL, 10)

        self.change_pwd_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Change", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        buttons_sizer.Add(self.change_pwd_btn, 0, wx.ALL, 10)

        sbSizer2.Add(buttons_sizer, 3, wx.ALL | wx.EXPAND, 10)

        bSizer36.Add(sbSizer2, 0, 0, 50)

        self.m_staticText301 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText301.Wrap(-1)
        self.m_staticText301.SetFont(wx.Font(30, 70, 90, 90, False, wx.EmptyString))

        bSizer36.Add(self.m_staticText301, 0, wx.ALL | wx.EXPAND, 5)

        bSizer73.Add(bSizer36, 1, wx.ALL | wx.EXPAND, 5)

        bSizer281 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText302 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText302.Wrap(-1)
        bSizer281.Add(self.m_staticText302, 1, wx.ALL | wx.EXPAND, 5)

        bSizer73.Add(bSizer281, 1, wx.EXPAND, 5)

        container.Add(bSizer73, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        self.user_id.SetValue(str(self.userdata['user_id']))

        # Connect Events
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelChangePwd)
        self.change_pwd_btn.Bind(wx.EVT_BUTTON, self.changePassword)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancelChangePwd(self, event):
        self.old_pwd.SetValue("")
        self.new_pwd.SetValue("")
        self.confirm_pwd.SetValue("")

    def changePassword(self, event):
        self.change_pwd_btn.Enable(False)

        user_id = self.user_id.GetLineText(0)
        old_password = self.old_pwd.GetLineText(0)
        new_password = self.new_pwd.GetLineText(0)
        conf_password = self.confirm_pwd.GetLineText(0)

        # Remove white space
        old_password = old_password.replace(" ", "")
        new_password = new_password.replace(" ", "")
        conf_password = conf_password.replace(" ", "")

        # ---------- VALIDATION ----------
        error = ""

        if old_password == "":
            error = error + "The Old Password field is required.\n"
        else:
            # Check if password matches to that in DB
            if not checkOldPassword(user_id, old_password):
                error = error + "The Password youy keyed in does not match your current password.\n"

        if new_password == "":
            error = error + "The New Password field is required.\n"

        if conf_password == "":
            error = error + "The Confirm Password field is required.\n"

        if conf_password != new_password:
            error = error + "Passwords do not match.\n"
        else:
            if len(new_password) < 5:
                error = error + "The Password should have at least 5 characters.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        else:
            data = {
                "user_id": user_id,
                "password": new_password,
            }

            if changePassword(data):
                dlg = wx.MessageDialog(None, "Password Changed Successfully.", 'Success Message',
                                       wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
                self.cancelChangePwd("")
            else:
                dlg = wx.MessageDialog(None, "Password Not Changed. Try Again.", 'Failed',
                                       wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()

        self.change_pwd_btn.Enable(True)


