import wx
import wx.xrc
from ObjectListView import ObjectListView, ColumnDefn

from db.get_classes import getClassDets
from db.save_class import editClass, deleteClass
from db.get_students import getStudents

# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')

###########################################################################
# Class ViewClasses
###########################################################################


class ViewClasses(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(669, 428),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"All Classes", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText17, 0, wx.TOP | wx.EXPAND, 25)

        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_sizer = wx.BoxSizer(wx.HORIZONTAL)
        OLV_sizer = wx.BoxSizer(wx.VERTICAL)

        #
        # Classes Object list View
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

        self.search_classes = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                             wx.TE_PROCESS_ENTER)
        self.search_classes.ShowSearchButton(True)
        self.search_classes.ShowCancelButton(False)
        search_container.Add(self.search_classes, 0, wx.BOTTOM, 8)

        self.search_classes.Bind(wx.EVT_TEXT, self.searchClasses)
        self.search_classes.Bind(wx.EVT_TEXT_ENTER, self.searchClasses)

        OLV_sizer.Add(search_container, 0, wx.EXPAND, 5)
        #
        #
        # ----------------------------------------------------------------
        # Table
        # ----------------------------------------------------------------
        self.classes = getClassDets()

        self.classesOLV = ObjectListView(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.setClassesData()

        OLV_sizer.Add(self.classesOLV, 1, wx.EXPAND | wx.ALL, 5)

        # ----------------------------------------------------------------
        #
        #

        left_btns_sizer = wx.BoxSizer(wx.VERTICAL)

        self.view_students_btn = wx.Button(self, wx.ID_ANY, u"View Students", wx.DefaultPosition, wx.DefaultSize, 0)
        self.view_students_btn.Bind(wx.EVT_BUTTON, self.getClassStudents)
        left_btns_sizer.Add(self.view_students_btn, 0, wx.EXPAND | wx.ALL, 5)

        self.edit_class_btn = wx.Button(self, wx.ID_ANY, u"Edit Class", wx.DefaultPosition, wx.DefaultSize, 0)
        self.edit_class_btn.Bind(wx.EVT_BUTTON, self.getClassInfo)
        left_btns_sizer.Add(self.edit_class_btn, 0, wx.ALL | wx.EXPAND, 5)

        self.delete_class_btn = wx.Button(self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        self.delete_class_btn.Bind(wx.EVT_BUTTON, self.deleteClass)
        left_btns_sizer.Add(self.delete_class_btn, 0, wx.ALL | wx.EXPAND, 5)

        #
        #
        left_sizer.Add(OLV_sizer, 3, wx.EXPAND | wx.ALL, 5)
        left_sizer.Add(left_btns_sizer, 1, wx.ALL, 5)

        horizontal_sizer.Add(left_sizer, 1, wx.EXPAND, 5)

        right_sizer = wx.BoxSizer(wx.VERTICAL)

        # self.m_staticText59 = wx.StaticText(self, wx.ID_ANY, u"Exams", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_staticText59.Wrap(-1)
        # right_sizer.Add(self.m_staticText59, 0, wx.ALL, 5)

        self.edit_class_panel = EditClass(self)

        self.show_students = ViewClassStudents(self)

        #
        #
        #
        right_sizer.Add(self.edit_class_panel, 1, wx.EXPAND)
        right_sizer.Add(self.show_students, 1, wx.EXPAND)
        self.show_students.Hide()

        horizontal_sizer.Add(right_sizer, 1, wx.EXPAND, 5)

        container.Add(horizontal_sizer, 1, wx.ALL | wx.EXPAND, 10)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.refresh_btn.Bind(wx.EVT_BUTTON, self.refreshTable)

    def setClassesData(self, data=None):
        self.classesOLV.SetColumns([
            ColumnDefn("ID", "left", 80, "class_id"),
            ColumnDefn("Form", "center", 80, "form_name"),
            ColumnDefn("Stream", "center", 100, "class_name"),
            ColumnDefn("Students", "center", 100, "students"),
        ])

        self.classesOLV.SetObjects(self.classes)

    def updateClassesOLV(self, event):  # Refresh classes table
        """"""
        data = getClassDets()
        self.classesOLV.SetObjects(data)

    def refreshTable(self, event):
        self.updateClassesOLV("")

    def searchClasses(self, event):
        search = self.search_classes.GetLineText(0)
        data = getClassDets(search)
        self.classesOLV.SetObjects(data)

    def getClassInfo(self, event):  # In order to edit
        if not self.classesOLV.GetSelectedObject():
            dlg = wx.MessageDialog(None, "Click on a row in order to edit class.",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            self.rowData = self.classesOLV.GetSelectedObject()
            rowObj = self.classesOLV.GetSelectedObject()

            self.edit_class_panel.class_id.SetValue(str(rowObj['class_id']))

            if rowObj['form_name'] == 1:
                form = "One"
            elif rowObj['form_name'] == 2:
                form = "Two"
            elif rowObj['form_name'] == 3:
                form = "Three"
            elif rowObj['form_name'] == 4:
                form = "Four"

            self.edit_class_panel.class_name.SetValue(rowObj['class_name'])
            self.edit_class_panel.form.SetValue(form)

            self.show_students.HideWithEffect(wx.SHOW_EFFECT_SLIDE_TO_TOP, 1000)
            self.edit_class_panel.Show()

    def getClassStudents(self, event):
        if not self.classesOLV.GetSelectedObject():
            dlg = wx.MessageDialog(None, "Click on a row to view students.", 'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            rowObj = self.classesOLV.GetSelectedObject()
            self.show_students.class_id = rowObj['class_id']
            self.show_students.updateStudentsOLV("")

            self.edit_class_panel.HideWithEffect(wx.SHOW_EFFECT_SLIDE_TO_TOP, 1000)
            self.show_students.ShowWithEffect(wx.SHOW_EFFECT_SLIDE_TO_BOTTOM, 1000)
            self.Layout()

    def deleteClass(self, event):
        if self.classesOLV.GetSelectedObject():
            rowObj = self.classesOLV.GetSelectedObject()

            dlg = wx.MessageDialog(None, "Are you sure?", 'Warning Message.', wx.YES_NO | wx.ICON_WARNING)
            retCode = dlg.ShowModal()
            dlg.Destroy()

            if retCode == wx.ID_YES:
                # check whether class has students
                if int(rowObj['students']) != 0:
                    dlg = wx.MessageDialog(None, "You cannot delete a class that has students.", 'Error Message.',
                                           wx.OK | wx.ICON_EXCLAMATION)
                    dlg.ShowModal()
                    dlg.Destroy()
                else:
                    if deleteClass(rowObj["class_id"]):
                        dlg = wx.MessageDialog(None, "Class deleted successfully.", 'Success Message.',
                                               wx.OK | wx.ICON_EXCLAMATION)
                        dlg.ShowModal()
                        dlg.Destroy()

                        self.updateClassesOLV("")
            else:
                rowObj=""

        else:
            dlg = wx.MessageDialog(None, "Click on a row to delete a class.", 'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()


class EditClass(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(567, 444),
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        bSizer48 = wx.BoxSizer(wx.VERTICAL)

        bSizer73 = wx.BoxSizer(wx.HORIZONTAL)

        left_spacer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        left_spacer.Add(self.m_staticText30, 1, wx.ALL | wx.EXPAND, 5)

        bSizer73.Add(left_spacer, 1, wx.EXPAND, 5)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        form_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Edit Class Form"), wx.VERTICAL)

        #
        # hidden class id field
        #
        class_id_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.class_id = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.class_id.Hide()

        class_id_sizer.Add(self.class_id, 0, wx.ALL, 10)

        form_sizer.Add(class_id_sizer, 1, wx.EXPAND, 5)
        #
        #
        #

        form_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2951 = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Form", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText2951.Wrap(-1)
        form_name_sizer.Add(self.m_staticText2951, 1, wx.ALL, 10)

        formChoices = [u"One", u"Two", u"Three", u"Four"]
        self.form = wx.ComboBox(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                wx.DefaultSize, formChoices, wx.CB_READONLY)
        form_name_sizer.Add(self.form, 4, wx.ALL, 10)

        form_sizer.Add(form_name_sizer, 1, wx.ALL | wx.EXPAND, 10)

        class_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.statictext = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Class Name", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.statictext.Wrap(-1)
        class_name_sizer.Add(self.statictext, 1, wx.ALL, 10)

        self.class_name = wx.TextCtrl(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        class_name_sizer.Add(self.class_name, 4, wx.ALL, 10)

        form_sizer.Add(class_name_sizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 10)

        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        buttons_sizer.Add(self.m_staticText22, 1, wx.ALL, 5)

        self.cancel_edit_btn = wx.Button(form_sizer.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        buttons_sizer.Add(self.cancel_edit_btn, 0, wx.ALL, 10)

        self.edit_class_btn = wx.Button(form_sizer.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        buttons_sizer.Add(self.edit_class_btn, 0, wx.ALL, 10)

        form_sizer.Add(buttons_sizer, 4, wx.ALL | wx.EXPAND, 10)

        bSizer36.Add(form_sizer, 1, 0, 50)

        bSizer73.Add(bSizer36, 1, wx.ALL | wx.EXPAND, 5)

        right_spacer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText302 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText302.Wrap(-1)
        right_spacer.Add(self.m_staticText302, 1, wx.ALL | wx.EXPAND, 5)

        bSizer73.Add(right_spacer, 1, wx.EXPAND, 5)

        bSizer48.Add(bSizer73, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer48)
        self.Layout()

        # Connect Events
        self.cancel_edit_btn.Bind(wx.EVT_BUTTON, self.cancelEditClass)
        self.edit_class_btn.Bind(wx.EVT_BUTTON, self.editClass)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancelEditClass(self, event):
        self.class_id.SetValue("")
        self.form.SetSelection(-1)
        self.class_name.SetValue("")

    def editClass(self, event):
        class_id = self.class_id.GetLineText(0)
        class_name = self.class_name.GetLineText(0)
        formIndex = self.form.GetCurrentSelection()

        if class_id == "":  # Check that a class has been selected before starting validation
            dlg = wx.MessageDialog(None, "Please select a class to edit.", 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
            self.cancelEditClass("")
        else:
            error = ""

            if class_name == "":
                error = error + "The Class Name field is required.\n"
            if formIndex == -1:
                error = error + "The Form field is required.\n"

            if error:
                dlg = wx.MessageDialog(None, error, 'Validation Error.', wx.OK | wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                data = {
                    "class_id": class_id,
                    "class_name": class_name,
                    "form_name": formIndex + 1
                }

                if editClass(data):
                    dlg = wx.MessageDialog(None, "Class edited successfully.", 'Success Message.',
                                           wx.OK | wx.ICON_EXCLAMATION)
                    retCode = dlg.ShowModal()
                    if retCode == wx.ID_OK:
                        """"""
                        self.parent.updateClassesOLV("")
                        self.cancelEditClass("")
                    dlg.Destroy()

                else:
                    dlg = wx.MessageDialog(None, "Edit Failed. Try again.", 'Error Message.',
                                           wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()
                    dlg.Destroy()


class ViewClassStudents(wx.Panel):
    # ----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        self.class_id = ""
        self.products = getStudents(self.class_id)

        self.dataOlv = ObjectListView(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.setBooks()

        # Create some sizers
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)

        mainSizer.Add(self.dataOlv, 1, wx.ALL | wx.EXPAND, 5)
        # mainSizer.Add(viewStudentBtn, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(mainSizer)

    # ----------------------------------------------------------------------
    def updateStudentsOLV(self, event):
        """"""
        data = getStudents(self.class_id)
        self.dataOlv.SetObjects(data)

    # ----------------------------------------------------------------------
    def setBooks(self, data=None):
        self.dataOlv.SetColumns([
            ColumnDefn("ID", "center", 50, "user_id"),
            ColumnDefn("Full Name", "left", 150, "full_names"),
            ColumnDefn("Form", "center", 50, "form"),
            ColumnDefn("Stream", "center", 70, "class"),
            ColumnDefn("Date of Birth", "center", 150, "dob"),
            ColumnDefn("Gender", "center", 70, "gender")
        ])

        self.dataOlv.SetObjects(self.products)