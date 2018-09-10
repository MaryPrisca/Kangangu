import wx
import wx.xrc

from db.save_class import saveClass

# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')


###########################################################################
# Class AddClass
###########################################################################

class AddClass(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(637, 452),
                          style=wx.TAB_TRAVERSAL)

        bSizer48 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"Add New Class", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))

        bSizer48.Add(self.m_staticText17, 0, wx.ALL | wx.EXPAND, 25)

        bSizer73 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer28 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        bSizer28.Add(self.m_staticText30, 1, wx.ALL | wx.EXPAND, 5)

        bSizer73.Add(bSizer28, 1, wx.EXPAND, 5)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Add Class Form"), wx.VERTICAL)

        bSizer2651 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2951 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Form", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText2951.Wrap(-1)
        bSizer2651.Add(self.m_staticText2951, 1, wx.ALL, 10)

        formChoices = [u"One", u"Two", u"Three", u"Four"]
        self.form = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                formChoices, wx.CB_READONLY)
        bSizer2651.Add(self.form, 4, wx.ALL, 10)

        sbSizer2.Add(bSizer2651, 1, wx.ALL | wx.EXPAND, 10)

        bSizer26 = wx.BoxSizer(wx.HORIZONTAL)

        self.statictext = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Class Name", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.statictext.Wrap(-1)
        bSizer26.Add(self.statictext, 1, wx.ALL, 10)

        self.class_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bSizer26.Add(self.class_name, 4, wx.ALL, 10)

        sbSizer2.Add(bSizer26, 1, wx.ALL | wx.EXPAND | wx.TOP, 10)

        bSizer271 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        bSizer271.Add(self.m_staticText22, 1, wx.ALL, 5)

        self.cancel_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        bSizer271.Add(self.cancel_btn, 0, wx.ALL, 10)

        self.save_class = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer271.Add(self.save_class, 0, wx.ALL, 10)

        sbSizer2.Add(bSizer271, 3, wx.ALL | wx.EXPAND, 10)

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

        bSizer48.Add(bSizer73, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer48)
        self.Layout()

        # Connect Events
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelAddClass)
        self.save_class.Bind(wx.EVT_BUTTON, self.saveClass)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancelAddClass(self, event):
        self.form.SetSelection(-1)
        self.class_name.SetValue("")

    def saveClass(self, event):
        self.save_class.Enable(False)
        class_name = self.class_name.GetLineText(0)
        formIndex = self.form.GetCurrentSelection()

        error = ""

        if class_name == "":
            error = error + "The Class Name field is required.\n"
        if formIndex == -1:
            error = error + "The Form field is required.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error.', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            data = {
                "class_name": class_name,
                "form_name": formIndex + 1
            }

            if saveClass(data):
                dlg = wx.MessageDialog(None, "Class saved successfully.", 'Success Message.', wx.OK | wx.ICON_EXCLAMATION)
                retCode = dlg.ShowModal()
                if retCode == wx.ID_OK:
                    self.cancelAddClass("")
                dlg.Destroy()

            else:
                dlg = wx.MessageDialog(None, "Class not saved. Try again.", 'Error Message.', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
        self.save_class.Enable(True)

