import wx
import wx.xrc

from SetupSchoolDetails import SetupSchoolDetails
from SetupForms import SetupForms
from SetupClasses import SetupClasses
from SetupSubjects import SetupSubjects
from PreviewSetup import PreviewSetup

###########################################################################
# Class SetupMainFrame
###########################################################################


class SetupMainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="SYSTEM INITIALIZATION", pos=wx.DefaultPosition,
                          size=wx.Size(550, 650), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        # self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        container = wx.BoxSizer(wx.VERTICAL)

        self.setup_gauge = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.gauge_pos = 0
        self.range = 20
        self.setup_gauge.SetValue(self.gauge_pos)
        container.Add(self.setup_gauge, 0, wx.EXPAND, 5)

        self.notebook_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        notebookSizer = wx.BoxSizer(wx.VERTICAL)

        self.notebook = wx.Notebook(self.notebook_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.NB_FIXEDWIDTH)

        self.setup_data = {
            'school_name': "",
            'school_logo_path': "",
            'form_streams': [],
            'class_names': [],
            'subjects': []
        }

        # Create the tab windows
        self.tab1 = SetupSchoolDetails(self.notebook)
        # self.tab2 = SetupForms(self.notebook)
        # self.tab3 = SetupClasses(self.notebook)
        # self.tab4 = SetupSubjects(self.notebook)

        self.forms_tab_created = 0
        self.classes_tab_created = 0
        self.subjects_tab_created = 0
        self.preview_tab_created = 0

        # Add the windows to tabs and name them.
        self.notebook.AddPage(self.tab1, "School Details")
        # self.notebook.AddPage(self.tab2, "Forms")
        # self.notebook.AddPage(self.tab3, "Classes")
        # self.notebook.AddPage(self.tab4, "Subjects")

        notebookSizer.Add(self.notebook, 1, wx.EXPAND, 5)

        self.notebook_panel.SetSizer(notebookSizer)
        self.notebook_panel.Layout()
        notebookSizer.Fit(self.notebook_panel)
        container.Add(self.notebook_panel, 1, wx.EXPAND, 5)

        btnsSizer = wx.BoxSizer(wx.HORIZONTAL)

        btnsSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.back_btn = wx.Button(self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0)

        self.back_btn.Disable()
        btnsSizer.Add(self.back_btn, 0, wx.ALL, 10)

        self.cancel_btn = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        btnsSizer.Add(self.cancel_btn, 0, wx.ALL, 10)

        self.next_button = wx.Button(self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0)
        btnsSizer.Add(self.next_button, 0, wx.ALL, 10)

        container.Add(btnsSizer, 0, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.back_btn.Bind(wx.EVT_BUTTON, self.goToPreviousTab)
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelTab)
        self.next_button.Bind(wx.EVT_BUTTON, self.openNextTab)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def goToPreviousTab(self, event):
        # Order of tabs
        # 0. Sch Details
        # 1. Forms
        # 2. Classes
        # 3. Subjects

        curr_page = self.notebook.GetSelection()

        if curr_page == 0:  # Sch Details Tab
            self.cancelSchoolDetails()

        elif curr_page == 1:  # Forms Tab, go back to Sch Dets Tab
            self.gauge_pos -= self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Disable back button because we're opening first tab
            self.back_btn.Enable(False)

            # Re-enable previous tab
            self.tab1.Enable(True)

            # Disable current tab
            self.tab2.Enable(False)

            self.notebook.SetSelection(0)

        elif curr_page == 2:  # Classes Tab
            self.gauge_pos -= self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Re-enable previous tab
            self.tab2.Enable(True)

            # Disable current tab
            self.tab3.Enable(False)

            self.notebook.SetSelection(1)

        elif curr_page == 3:  # Subjects Tab
            self.gauge_pos -= self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Re-enable previous tab
            self.tab3.Enable(True)

            # Disable current tab
            self.tab4.Enable(False)

            self.notebook.SetSelection(2)

    #
    # --------------------------------------------------
    def cancelTab(self, event):
        # Order of tabs
        # 0. Sch Details
        # 1. Forms
        # 2. Classes
        # 3. Subjects

        curr_page = self.notebook.GetSelection()

        if curr_page == 0:  # Sch Details Tab
            self.cancelSchoolDetails()

        elif curr_page == 1:  # Forms Tab
            self.cancelSetupForms()

        elif curr_page == 2:  # Classes Tab
            self.cancelSetupClasses()

        elif curr_page == 3:  # Open Forms Tab
            self.cancelSetupSubjects()

    #
    # --------------------------------------------------
    def cancelSchoolDetails(self):
        self.tab1.school_name.SetValue("")

    #
    # --------------------------------------------------
    def cancelSetupForms(self):
        self.tab2.form_one.SetValue("")
        self.tab2.form_two.SetValue("")
        self.tab2.form_three.SetValue("")
        self.tab2.form_four.SetValue("")

    #
    # --------------------------------------------------
    def cancelSetupClasses(self):
        self.tab3.form_one.SetValue("")
        self.tab3.form_two.SetValue("")
        self.tab3.form_three.SetValue("")
        self.tab3.form_four.SetValue("")

    #
    # --------------------------------------------------
    def cancelSetupSubjects(self):
        self.tab4.subjects = []
        self.tab4.subject_textfield.SetValue("")
        self.tab4.subject_alias_textfield.SetValue("")

        self.tab4.refreshPreview("")

    #
    # --------------------------------------------------
    def openNextTab(self, event):
        # Order of tabs
        # 0. Sch Details
        # 1. Forms
        # 2. Classes
        # 3. Subjects

        curr_page = self.notebook.GetSelection()

        if curr_page == 0:  # Save first tab, sch details and move to forms
            # Function saves details, navigates to next tab if successful
            self.saveSchoolDetails()

        elif curr_page == 1:  # Save 2nd tab, forms and move to classes
            self.saveSetupForms()

        elif curr_page == 2:  # Save classes (3rd tab) and move to subjects
            # Save Details
            self.saveSetupClasses()

        elif curr_page == 3:  # Save subjects
            self.saveSetupSubjects()

    #
    # --------------------------------------------------
    def hasNumbers(self, inputString):  # checks for numbers in string, returns true if there is a number
        return any(char.isdigit() for char in inputString)

    #
    # --------------------------------------------------
    def saveSchoolDetails(self):  # Save Tab 1
        school_name = self.tab1.school_name.GetLineText(0)

        # ---------- VALIDATION ----------
        error = ""

        if school_name == "" or school_name.replace(" ", "") == "":
            error = error + "School Name is required.\n"

        if self.hasNumbers(school_name):
            error = error + "School name cannot have numeric characters.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()

        else:
            self.setup_data['school_name'] = school_name

            # Navigate

            # Disable current page
            self.tab1.Enable(False)

            self.gauge_pos += self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Enable back button
            self.back_btn.Enable(True)

            if not self.forms_tab_created:  # Create if tab hadn't been created, otherwise move to page
                self.tab2 = SetupForms(self.notebook)
                self.notebook.InsertPage(1, self.tab2, "Forms", select=True)

                self.forms_tab_created = 1

            else:  # When using back btn
                self.tab2.Enable(True)
                self.notebook.SetSelection(1)

    #
    # --------------------------------------------------
    def saveSetupForms(self):
        form_one = self.tab2.form_one.GetLineText(0)
        form_two = self.tab2.form_two.GetLineText(0)
        form_three = self.tab2.form_three.GetLineText(0)
        form_four = self.tab2.form_four.GetLineText(0)

        form_one = form_one.replace(" ", "")
        form_two = form_two.replace(" ", "")
        form_three = form_three.replace(" ", "")
        form_four = form_four.replace(" ", "")

        # ---------- VALIDATION ----------
        error = ""

        if form_one == "":
            error = error + "The Form 1 field is required.\n"
        else:
            if not form_one.isdigit():
                error = error + "Non-numeric value in Form 1 field.\n"

        if form_two == "":
            error = error + "The Form 2 field is required.\n"
        else:
            if not form_two.isdigit():
                error = error + "Non-numeric value in Form 2 field.\n"

        if form_three == "":
            error = error + "The Form 3 field is required.\n"
        else:
            if not form_two.isdigit():
                error = error + "Non-numeric value in Form 3 field.\n"

        if form_four == "":
            error = error + "The Form 4 field is required.\n"
        else:
            if not form_four.isdigit():
                error = error + "Non-numeric value in Form 4 field.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()

        else:
            self.setup_data['form_streams'] = [form_one, form_two, form_three, form_four]

            # Navigate

            # Disable current page
            self.tab2.Enable(False)

            self.gauge_pos += self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Enable back button
            self.back_btn.Enable(True)

            if not self.classes_tab_created:  # Create if tab hadn't been created, otherwise move to page

                self.tab3 = SetupClasses(self.notebook)
                self.notebook.InsertPage(2, self.tab3, "Classes", select=True)

                self.classes_tab_created = 1
            else:
                self.tab3.Enable(True)
                self.notebook.SetSelection(2)

    #
    # --------------------------------------------------
    def saveSetupClasses(self):
        form_one = self.tab3.form_one.GetLineText(0)
        form_two = self.tab3.form_two.GetLineText(0)
        form_three = self.tab3.form_three.GetLineText(0)
        form_four = self.tab3.form_four.GetLineText(0)

        # ---------- VALIDATION ----------
        error = ""

        if form_one == "":
            error = error + "The Form 1 field is required.\n"

        if form_two == "":
            error = error + "The Form 2 field is required.\n"

        if form_three == "":
            error = error + "The Form 3 field is required.\n"

        if form_four == "":
            error = error + "The Form 4 field is required.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()

        else:
            form_one = form_one.split(",")
            form_two = form_two.split(",")
            form_three = form_three.split(",")
            form_four = form_four.split(",")

            # Remove spaces at beginning and end of string
            form_one = self.refineClassNames(form_one)
            form_two = self.refineClassNames(form_two)
            form_three = self.refineClassNames(form_three)
            form_four = self.refineClassNames(form_four)

            f1classes = self.setup_data['form_streams'][0]
            f2classes = self.setup_data['form_streams'][1]
            f3classes = self.setup_data['form_streams'][2]
            f4classes = self.setup_data['form_streams'][3]

            # Confirm whether no of streams match
            if len(form_one) != int(f1classes):
                error = error + f1classes + (" class" if f1classes == "1" else " classes") + " expected in form 1.\n"

            if len(form_two) != int(f2classes):
                error = error + f2classes + (" class" if f2classes == "1" else " classes") + " expected in form 2.\n"

            if len(form_three) != int(f3classes):
                error = error + f3classes + (" class" if f3classes == "1" else " classes") + " expected in form 3.\n"

            if len(form_four) != int(f4classes):
                error = error + f4classes + (" class" if f4classes == "1" else " classes") + " expected in form 4.\n"

            if error:
                dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
                dlg.ShowModal()

            else:
                self.setup_data['class_names'] = [form_one, form_two, form_three, form_four]

                # Navigate

                # Disable current page
                self.tab3.Enable(False)

                self.gauge_pos += self.range
                self.setup_gauge.SetValue(self.gauge_pos)

                # Enable back button
                self.back_btn.Enable(True)

                if not self.subjects_tab_created:  # Create if tab hadn't been created, otherwise move to page

                    self.tab4 = SetupSubjects(self.notebook)
                    self.notebook.InsertPage(3, self.tab4, "Subjects", select=True)

                    self.subjects_tab_created = 1
                else:
                    self.tab4.Enable(True)
                    self.notebook.SetSelection(3)

    #
    # --------------------------------------------------
    def refineClassNames(self, classArray):
        for key, value in enumerate(classArray):
            item = value.strip()
            if item == "":
                del classArray[key]
            else:
                classArray[key] = item

        return classArray

    #
    # --------------------------------------------------
    def saveSetupSubjects(self):
        if len(self.tab4.subjects) < 8:
            dlg = wx.MessageDialog(None, "At least 8 subjects expected, only " + str(len(self.tab4.subjects)) + " given", 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
        else:
            self.setup_data['subjects'] = self.tab4.subjects

            # Navigate

            # Disable current page
            self.tab4.Enable(False)

            self.gauge_pos += self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Enable back button
            self.back_btn.Enable(True)

            if not self.preview_tab_created:  # Create if tab hadn't been created, otherwise move to page

                self.tab5 = PreviewSetup(self.notebook, self.setup_data)
                self.notebook.InsertPage(4, self.tab5, "Preview", select=True)

                self.preview_tab_created = 1
            else:
                self.tab5.Enable(True)
                self.notebook.SetSelection(4)

            # Change next button to finish
            self.next_button.SetLabel("Finish")


# Run the program
if __name__ == "__main__":
    app = wx.App()
    frame = SetupMainFrame(None)
    frame.Show()
    app.MainLoop()
