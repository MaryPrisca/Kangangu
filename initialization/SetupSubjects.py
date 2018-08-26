import wx
import wx.xrc


###########################################################################
# Class SetupSubjects
###########################################################################

class SetupSubjects(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(539, 464),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.school_subjects_label = wx.StaticText(self, wx.ID_ANY, u"Subjects Offered", wx.DefaultPosition,
                                                   wx.DefaultSize, wx.ALIGN_CENTRE)
        self.school_subjects_label.Wrap(-1)
        self.school_subjects_label.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.school_subjects_label, 0, wx.ALL | wx.EXPAND, 30)

        self.navigation_disclaimer = wx.StaticText( self, wx.ID_ANY, u"(Please use buttons to navigate)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.navigation_disclaimer.Wrap(-1)

        container.Add(self.navigation_disclaimer, 0, wx.ALL | wx.EXPAND, 5)

        content_Sizer = wx.BoxSizer(wx.HORIZONTAL)

        content_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        formSizer = wx.BoxSizer(wx.VERTICAL)

        formSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        bSizer260 = wx.BoxSizer(wx.HORIZONTAL)

        left_Sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.subject_name_label = wx.StaticText(left_Sizer.GetStaticBox(), wx.ID_ANY, u"Subject Name",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.subject_name_label.Wrap(-1)
        left_Sizer.Add(self.subject_name_label, 0, wx.ALL, 5)

        self.subject_textfield = wx.TextCtrl(left_Sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, wx.TE_PROCESS_ENTER)
        left_Sizer.Add(self.subject_textfield, 0, wx.ALL | wx.EXPAND, 5)

        self.subject_alias_label = wx.StaticText(left_Sizer.GetStaticBox(), wx.ID_ANY, u"Subject Alias (E.g. Eng)",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self.subject_alias_label.Wrap(-1)
        left_Sizer.Add(self.subject_alias_label, 0, wx.ALL, 5)

        self.subject_alias_textfield = wx.TextCtrl(left_Sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                   wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
        left_Sizer.Add(self.subject_alias_textfield, 0, wx.ALL | wx.EXPAND, 5)

        checkboxes_sizer = wx.BoxSizer(wx.VERTICAL)

        compulsory_radio_boxChoices = [u"Yes", u"No", u"Partially (Only in lower forms)"]
        self.compulsory_radio_box = wx.RadioBox(left_Sizer.GetStaticBox(), wx.ID_ANY, u"Subject Compulsory?",
                                                wx.DefaultPosition, wx.DefaultSize, compulsory_radio_boxChoices, 1, 0)
        self.compulsory_radio_box.SetSelection(0)
        checkboxes_sizer.Add(self.compulsory_radio_box, 0, wx.ALL | wx.EXPAND, 5)

        left_Sizer.Add(checkboxes_sizer, 1, wx.EXPAND | wx.TOP, 5)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        btnSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.add_subject_btn = wx.Button(left_Sizer.GetStaticBox(), wx.ID_ANY, u"Add", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        btnSizer.Add(self.add_subject_btn, 0, wx.ALL, 5)

        left_Sizer.Add(btnSizer, 1, wx.EXPAND, 5)

        bSizer260.Add(left_Sizer, 1, wx.ALL | wx.EXPAND, 5)

        self.right_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        #
        #
        self.subjects = []

        self.preview_panel = PreviewSetUpSubjects(self, self.subjects)
        self.preview_panel.Hide()
        self.right_sizer.Add(self.preview_panel, 1, wx.ALL | wx.EXPAND, 5)

        #
        #

        bSizer260.Add(self.right_sizer, 1, wx.ALL | wx.EXPAND, 5)

        formSizer.Add(bSizer260, 1, wx.EXPAND, 5)

        formSizer.AddSpacer((0, 0), 5, wx.EXPAND, 5)

        content_Sizer.Add(formSizer, 7, wx.EXPAND, 5)

        content_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(content_Sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.add_subject_btn.Bind(wx.EVT_BUTTON, self.subjectAdded)

    def __del__(self):
        pass

    #
    # --------------------------------------------------
    def hasNumbers(self, inputString):  # checks for numbers in string, returns true if there is a number
        return any(char.isdigit() for char in inputString)

    #
    # ---------------------------------------------
    def subjectAdded(self, event):
        subject_name = self.subject_textfield.GetLineText(0)
        subject_alias = self.subject_alias_textfield.GetLineText(0)
        compulsory = self.compulsory_radio_box.GetSelection()

        # ----- VALIADATION -----
        error = ""

        if subject_name.strip() == "" or subject_alias.strip() == "":
            error = error + "Both the subject name and alias are required.\n"
        else:
            if self.hasNumbers(subject_name) or self.hasNumbers(subject_alias):
                error = error + "The subject name and alias cannot contain numbers.\n"

            if subject_name.strip() == subject_alias.strip():
                error = error + "The subject name and alias cannot be the same.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
        else:
            subject = {
                'name': subject_name,
                'alias': subject_alias,
                'compulsory': compulsory
            }

            self.subjects.append(subject)

            self.subject_textfield.SetValue("")
            self.subject_alias_textfield.SetValue("")
            self.compulsory_radio_box.SetSelection(0)

            self.subject_textfield.SetFocus()

            self.refreshPreview("")

    #
    # ---------------------------------------------
    def refreshPreview(self, event):
        self.preview_panel.Hide()

        self.preview_panel = PreviewSetUpSubjects(self, self.subjects)
        self.right_sizer.Add(self.preview_panel, 1, wx.ALL | wx.EXPAND, 5)

        self.Layout()


class PreviewSetUpSubjects(wx.Panel):

    def __init__(self, parent, subjects):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        self.parent = parent

        subject_list_sizer = wx.BoxSizer(wx.VERTICAL)

        self.preview_subjects = {}

        count = 1

        for key, value in enumerate(subjects):  # adding subject list dynamically
            self.preview_subjects[str(key)] = OneSubjectPreviewPanel(self, value, count)

            subject_list_sizer.Add(self.preview_subjects[str(key)], 0, wx.EXPAND, 5)

            count += 1

        self.SetSizer(subject_list_sizer)
        self.Layout()

    def __del__(self):
        pass

    #
    # ---------------------------------------------
    def removeSubject(self, subject):
        self.parent.subjects.remove(subject)

        self.parent.refreshPreview("")


class OneSubjectPreviewPanel(wx.Panel):

    def __init__(self, parent, subject, count):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent
        self.subject = subject

        compulsory = ""
        if subject['compulsory'] == 0:
            compulsory = "Compulsory"
        elif subject['compulsory'] == 1:
            compulsory = "Optional"
        elif subject['compulsory'] == 2:
            compulsory = "Partial"

        subject_name = str(count) + ". " + subject['name'] + " - " + subject['alias'] + ", " + compulsory

        subjectSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.remove_btn = wx.BitmapButton(self, wx.ID_ANY,
                                          wx.Bitmap(u"../images/minus_12x12.bmp", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, 0 | wx.NO_BORDER)
        subjectSizer.Add(self.remove_btn, 0, wx.ALL, 6)

        self.subject_name = wx.StaticText(self, wx.ID_ANY, subject_name, wx.DefaultPosition, wx.DefaultSize, 0)
        self.subject_name.Wrap(-1)
        subjectSizer.Add(self.subject_name, 0, wx.LEFT | wx.RIGHT | wx.TOP, 5)

        self.SetSizer(subjectSizer)
        self.Layout()

        # Connect Events
        self.remove_btn.Bind(wx.EVT_BUTTON, self.removeButtonClicked)

    def __del__(self):
        pass

    #
    # ---------------------------------------------
    def removeButtonClicked(self, event):
        self.parent.removeSubject(self.subject)





