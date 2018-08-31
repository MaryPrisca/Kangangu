import wx
import wx.xrc

from db.save_subject import saveSubject
from db.get_subjects import checkIfSubjectExists

# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')


###########################################################################
# Class AddSubject
###########################################################################

class AddSubject(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(561, 458),
                          style=wx.TAB_TRAVERSAL)

        bSizer48 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"Add New Subject", wx.DefaultPosition, wx.DefaultSize,
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

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Add Subject Form"), wx.VERTICAL)

        full_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.statictext = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Full Name", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.statictext.Wrap(-1)
        full_name_sizer.Add(self.statictext, 1, wx.ALL, 10)

        self.subject_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        full_name_sizer.Add(self.subject_name, 4, wx.ALL, 10)

        sbSizer2.Add(full_name_sizer, 1, wx.ALL | wx.EXPAND, 10)

        alias_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.statictext1 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Subject Alias", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.statictext1.Wrap(-1)
        alias_sizer.Add(self.statictext1, 1, wx.ALL, 10)

        self.subject_alias = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        alias_sizer.Add(self.subject_alias, 4, wx.ALL, 10)

        sbSizer2.Add(alias_sizer, 1, wx.ALL | wx.EXPAND, 10)

        compulsory_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.staticText2 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Compulsory", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.staticText2.Wrap(-1)
        compulsory_sizer.Add(self.staticText2, 1, wx.ALL, 10)

        compulsoryChoices = [u"Yes", u"No", u"Partially"]
        self.compulsory = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, compulsoryChoices, wx.CB_READONLY)
        compulsory_sizer.Add(self.compulsory, 4, wx.ALL, 10)

        sbSizer2.Add(compulsory_sizer, 1, wx.ALL | wx.EXPAND, 10)

        btns_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        btns_sizer.Add(self.m_staticText22, 1, wx.ALL, 5)

        self.cancel_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        btns_sizer.Add(self.cancel_btn, 0, wx.ALL, 10)

        self.save_subject = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        btns_sizer.Add(self.save_subject, 0, wx.ALL, 10)

        sbSizer2.Add(btns_sizer, 3, wx.ALL | wx.EXPAND, 10)

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
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelAddSubject)
        self.save_subject.Bind(wx.EVT_BUTTON, self.saveSubject)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancelAddSubject(self, event):
        self.subject_name.SetValue("")
        self.subject_alias.SetValue("")
        self.compulsory.SetSelection(-1)

    def saveSubject(self, event):
        subject_name = self.subject_name.GetLineText(0)
        subject_alias = self.subject_alias.GetLineText(0)
        compulsory_index = self.compulsory.GetCurrentSelection()

        subject_alias = subject_alias.replace(" ", "")

        # ---------- VALIDATION ----------
        error = ""

        if subject_name == "":
            error = error + "The Full Name field is required.\n"

        if subject_alias == "":
            error = error + "The Subject Alias field required.\n"

        if compulsory_index == -1:
            error = error + "The Compulsory field is required.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        else:
            if checkIfSubjectExists(subject_alias):  # Check if subject is already in the results table
                dlg = wx.MessageDialog(None, "Subject or it's alias already exists.", 'Validation Error',
                                       wx.OK | wx.ICON_WARNING)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                compulsory = self.compulsory.GetString(compulsory_index)

                if compulsory == "Yes":
                    compulsory = 1
                elif compulsory == "No":
                    compulsory = 0
                elif compulsory == "Partially":
                    compulsory = 2

                data = {
                    "subject_name": subject_name,
                    "subject_alias": subject_alias,
                    "compulsory": compulsory
                }

                if saveSubject(data):
                    dlg = wx.MessageDialog(None, "Subject Added Successfully.", 'Success Message',
                                           wx.OK | wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    dlg.Destroy()
                    self.cancelAddSubject("")
                else:
                    dlg = wx.MessageDialog(None, "Subject Not Saved. Try Again.", 'Failed.',
                                           wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()
                    dlg.Destroy()


