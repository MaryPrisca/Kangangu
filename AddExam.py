import wx
import wx.xrc

from db.save_exam import saveExam
# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')

from datetime import datetime


###########################################################################
# Class AddExam
###########################################################################

class AddExam(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(676, 427),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"Add New Exam", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText17, 0, wx.EXPAND | wx.TOP, 25)

        bSizer73 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer28 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        bSizer28.Add(self.m_staticText30, 1, wx.ALL | wx.EXPAND, 5)

        bSizer73.Add(bSizer28, 1, wx.EXPAND, 5)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Add Exam Form"), wx.VERTICAL)

        exam_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.statictext = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Exam Name", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.statictext.Wrap(-1)
        exam_name_sizer.Add(self.statictext, 1, wx.ALL, 10)

        self.exam_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        exam_name_sizer.Add(self.exam_name, 4, wx.ALL, 10)

        sbSizer2.Add(exam_name_sizer, 1, wx.ALL | wx.EXPAND | wx.TOP, 10)

        year_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.year_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.year_label.Wrap(-1)
        year_sizer.Add(self.year_label, 1, wx.ALL, 10)

        # td = datetime.today()
        current_year = int(datetime.now().year)
        self.year = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, str(current_year), wx.DefaultPosition, wx.DefaultSize,
                                wx.TE_READONLY)
        year_sizer.Add(self.year, 4, wx.ALL, 10)

        sbSizer2.Add(year_sizer, 1, wx.ALL | wx.EXPAND, 10)

        term_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.term_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Term", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.term_label.Wrap(-1)
        term_sizer.Add(self.term_label, 1, wx.ALL, 10)

        termChoices = [u"One", u"Two", u"Three"]
        self.term = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                termChoices, wx.CB_READONLY)
        term_sizer.Add(self.term, 4, wx.ALL, 10)

        sbSizer2.Add(term_sizer, 1, wx.ALL | wx.EXPAND, 10)

        form_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.form_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Form", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.form_label.Wrap(-1)
        form_sizer.Add(self.form_label, 1, wx.ALL, 10)

        formChoices = [u"All", u"One", u"Two", u"Three", u"Four"]
        self.form = wx.ComboBox(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                formChoices, wx.CB_READONLY)
        form_sizer.Add(self.form, 4, wx.ALL, 10)

        sbSizer2.Add(form_sizer, 1, wx.ALL | wx.EXPAND, 10)

        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.spacer = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.spacer.Wrap(-1)
        buttons_sizer.Add(self.spacer, 1, wx.ALL, 5)

        self.cancel_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        buttons_sizer.Add(self.cancel_btn, 0, wx.ALL, 10)

        self.save_exam = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        buttons_sizer.Add(self.save_exam, 0, wx.ALL, 10)

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

        container.Add(bSizer73, 1, wx.EXPAND | wx.TOP, 8)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelAddExam)
        self.save_exam.Bind(wx.EVT_BUTTON, self.saveExam)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancelAddExam(self, event):
        self.exam_name.SetValue("")
        self.form.SetSelection(-1)
        self.term.SetSelection(-1)

    def saveExam(self, event):
        self.save_exam.Enable(False)
        exam_name = self.exam_name.GetLineText(0)
        year = self.year.GetLineText(0)
        termIndex = self.term.GetCurrentSelection()
        formIndex = self.form.GetCurrentSelection()

        # Remove white spaces
        exam_name = exam_name.replace(" ", "")

        #
        # ---------- VALIDATION ----------
        error = ""

        if exam_name == "":
            error = error + "The Exam Name field  is required.\n"

        if formIndex == -1:
            error = error + "The Form field is required.\n"

        if termIndex == -1:
            error = error + "The Term field is required.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        else:
            form = formIndex
            term = self.term.GetString(termIndex)

            data = {
                "exam_name": exam_name,
                "year": year,
                "form": form,
                "term": term
            }

            if saveExam(data):
                dlg = wx.MessageDialog(None, "Exam Added Successfully.", 'Success Message',
                                       wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
                self.cancelAddExam("")
            else:
                dlg = wx.MessageDialog(None, "Exam may not have been saved correctly. \n "
                                             "Refresh exams table on the previous tab to confirm before trying again.", 'Failed',
                                       wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
        self.save_exam.Enable(True)



