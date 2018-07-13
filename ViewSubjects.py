import wx
import wx.xrc

from ObjectListView import ObjectListView, ColumnDefn

from db.get_subjects import getSubjects
from db.save_subject import editSubject, deleteSubject

# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')



###########################################################################
# Class ViewSubjects
###########################################################################


class ViewSubjects(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(642, 406),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"All Subjects", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText17, 0, wx.TOP | wx.EXPAND, 25)

        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_sizer = wx.BoxSizer(wx.HORIZONTAL)

        OLV_sizer = wx.BoxSizer(wx.VERTICAL)

        #
        # Subjects Object list View
        # ----------------------------------------------------------------
        # Search
        # ----------------------------------------------------------------

        search_container = wx.BoxSizer(wx.HORIZONTAL)

        self.refresh_btn = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"images/reload_16x16.bmp", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)

        self.refresh_btn.SetBitmapHover(wx.Bitmap(u"images/reload_16x16_rotated.bmp", wx.BITMAP_TYPE_ANY))
        search_container.Add(self.refresh_btn, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT, 5)

        self.m_staticText53 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText53.Wrap(-1)
        search_container.Add(self.m_staticText53, 1, wx.ALL, 5)

        self.m_staticText54 = wx.StaticText(self, wx.ID_ANY, u"Search:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText54.Wrap(-1)
        search_container.Add(self.m_staticText54, 0, wx.ALL, 5)

        self.search_subjects = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_PROCESS_ENTER)
        search_container.Add(self.search_subjects, 0, wx.BOTTOM | wx.RIGHT, 8)

        OLV_sizer.Add(search_container, 0, wx.EXPAND, 5)

        #
        #
        # ----------------------------------------------------------------
        # Table
        # ----------------------------------------------------------------
        self.classes = getSubjects()

        self.subjectsOLV = ObjectListView(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.setSubjectsData()

        OLV_sizer.Add(self.subjectsOLV, 1, wx.EXPAND | wx.ALL, 5)

        # ----------------------------------------------------------------
        #
        #
        left_sizer.Add(OLV_sizer, 1, wx.EXPAND, 5)

        left_btns_sizer = wx.BoxSizer(wx.VERTICAL)

        self.edit_subject_btn = wx.Button(self, wx.ID_ANY, u"Edit Subject", wx.DefaultPosition, wx.DefaultSize, 0)
        left_btns_sizer.Add(self.edit_subject_btn, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 5)

        self.delete_subject_btn = wx.Button(self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        left_btns_sizer.Add(self.delete_subject_btn, 0, wx.ALL | wx.EXPAND, 5)

        left_sizer.Add(left_btns_sizer, 0, wx.EXPAND, 5)

        horizontal_sizer.Add(left_sizer, 1, wx.ALL | wx.EXPAND, 10)

        right_sizer = wx.BoxSizer(wx.VERTICAL)

        #
        # ------------------------------------------------------------------------
        #                                EDIT FORM
        # ------------------------------------------------------------------------
        #

        self.edit_subject_panel = EditSubject(self)
        right_sizer.Add(self.edit_subject_panel, 1, wx.EXPAND)

        horizontal_sizer.Add(right_sizer, 1, wx.ALL | wx.EXPAND, 8)

        container.Add(horizontal_sizer, 1, wx.ALL | wx.EXPAND, 10)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.refresh_btn.Bind(wx.EVT_BUTTON, self.refreshTable)
        self.search_subjects.Bind(wx.EVT_TEXT, self.searchSubjects)
        self.search_subjects.Bind(wx.EVT_TEXT_ENTER, self.searchSubjects)

        self.edit_subject_btn.Bind(wx.EVT_BUTTON, self.getSubjectInfo)
        self.delete_subject_btn.Bind(wx.EVT_BUTTON, self.deleteSubject)

    def setSubjectsData(self, data=None):
        self.subjectsOLV.SetColumns([
            ColumnDefn("ID", "left", 90, "subject_id"),
            ColumnDefn("Name", "center", 150, "subject_name"),
            ColumnDefn("Alias", "center", 100, "subject_alias"),
            ColumnDefn("Compulsory", "center", 110, "compulsory"),
        ])

        self.subjectsOLV.SetObjects(self.classes)

    def updateSubjectsOLV(self, event):  # Refresh classes table
        """"""
        data = getSubjects()
        print data
        self.subjectsOLV.SetObjects(data)

    def refreshTable(self, event):
        self.updateSubjectsOLV("")


    def searchSubjects(self, event):
        search = self.search_subjects.GetLineText(0)
        data = getSubjects(search)
        self.subjectsOLV.SetObjects(data)

    def getSubjectInfo(self, event):  # In order to edit
        if not self.subjectsOLV.GetSelectedObject():
            dlg = wx.MessageDialog(None, "Click on a row in order to edit subject.",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
        else:
            self.rowData = self.subjectsOLV.GetSelectedObject()
            rowObj = self.subjectsOLV.GetSelectedObject()

            self.edit_subject_panel.subject_id.SetValue(str(rowObj['subject_id']))
            self.edit_subject_panel.subject_name.SetValue(rowObj['subject_name'])
            self.edit_subject_panel.subject_alias.SetValue(rowObj['subject_alias'])
            self.edit_subject_panel.compulsory.SetValue(rowObj['compulsory'])

    def deleteSubject(self, event):
        if self.subjectsOLV.GetSelectedObject():
            rowObj = self.subjectsOLV.GetSelectedObject()

            dlg = wx.MessageDialog(None, "Are you sure? \nThis action cannot be reversed.", 'Warning Message.', wx.YES_NO | wx.ICON_WARNING)
            retCode = dlg.ShowModal()

            if retCode == wx.ID_YES:
                if deleteSubject(rowObj["subject_id"]):
                    dlg = wx.MessageDialog(None, "Subject deleted successfully.", 'Success Message.',
                                           wx.OK | wx.ICON_EXCLAMATION)
                    dlg.ShowModal()

                    self.updateSubjectsOLV("")
            else:
                dlg.Destroy()
                rowObj=""


        else:
            dlg = wx.MessageDialog(None, "Click on a row to delete a subject.", 'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()


class EditSubject(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(561, 458),
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        container = wx.BoxSizer(wx.VERTICAL)

        bSizer73 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer28 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        bSizer28.Add(self.m_staticText30, 1, wx.ALL | wx.EXPAND, 5)

        bSizer73.Add(bSizer28, 1, wx.EXPAND, 5)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Edit Subject Form"), wx.VERTICAL)

        #
        # hidden subject id field
        #
        subject_id_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.subject_id = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.subject_id.Hide()

        subject_id_sizer.Add(self.subject_id, 0, wx.ALL, 10)

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

        self.edit_subject = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        btns_sizer.Add(self.edit_subject, 0, wx.ALL, 10)

        sbSizer2.Add(btns_sizer, 3, wx.ALL | wx.EXPAND, 10)

        bSizer36.Add(sbSizer2, 1, 0, 50)

        bSizer73.Add(bSizer36, 1, wx.ALL | wx.EXPAND, 5)

        bSizer281 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText302 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText302.Wrap(-1)
        bSizer281.Add(self.m_staticText302, 1, wx.ALL | wx.EXPAND, 5)

        bSizer73.Add(bSizer281, 1, wx.EXPAND, 5)

        container.Add(bSizer73, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelEditSubject)
        self.edit_subject.Bind(wx.EVT_BUTTON, self.saveEditSubject)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancelEditSubject(self, event):
        self.subject_id.SetValue("")
        self.subject_name.SetValue("")
        self.subject_alias.SetValue("")
        self.compulsory.SetSelection(-1)

    def saveEditSubject(self, event):
        subject_id = self.subject_id.GetLineText(0)
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

        else:
            compulsory = self.compulsory.GetString(compulsory_index)

            if compulsory == "Yes":
                compulsory = 1
            else:
                compulsory = 0

            data = {
                "subject_id": subject_id,
                "subject_name": subject_name,
                "subject_alias": subject_alias,
                "compulsory": compulsory
            }

            if editSubject(data):
                dlg = wx.MessageDialog(None, "Subject Edited Successfully.", 'Success Message',
                                       wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                self.parent.updateSubjectsOLV("")
                self.cancelEditSubject("")
            else:
                dlg = wx.MessageDialog(None, "Edit Failed. Try Again.", 'Failed.',
                                       wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()




