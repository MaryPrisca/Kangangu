import wx
import wx.xrc

from datetime import datetime
import re  # Regex

from AdminSetup import AdminSetup
from SetupSchoolDetails import SetupSchoolDetails
from SetupForms import SetupForms
from SetupClasses import SetupClasses
from SetupSubjects import SetupSubjects
from PreviewSetup import PreviewSetup

from HomePage import HomePage

from system_setup import *

from wx.lib.embeddedimage import PyEmbeddedImage

appIcon = PyEmbeddedImage(
    "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"
    "f7H8iAAAAABJRU5ErkJggg==")

###########################################################################
# Class SetupMainFrame
###########################################################################


class SetupMainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="SYSTEM INITIALIZATION", pos=wx.DefaultPosition,
                          size=wx.Size(550, 650), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)

        ico = appIcon.getIcon()
        self.SetIcon(ico)

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
            'adminDets': {},
            'school_name': "",
            'subjects_lower_form': "",
            'form_streams': [],
            'class_names': [],
            'subjects': [],
            'streams': [],
            'saved': False
        }

        # Create the tab windows
        self.adminSetupTab = AdminSetup(self.notebook)
        # self.schDetsTab = SetupSchoolDetails(self.notebook)
        # self.formsTab = SetupForms(self.notebook)
        # self.classesTab = SetupClasses(self.notebook)
        # self.subjectsTab = SetupSubjects(self.notebook)

        self.sch_dets_tab_created = 0
        self.forms_tab_created = 0
        self.classes_tab_created = 0
        self.subjects_tab_created = 0
        self.preview_tab_created = 0

        # Add the windows to tabs and name them.
        self.notebook.AddPage(self.adminSetupTab, "Admin")
        # self.notebook.AddPage(self.schDetsTab, "School Details")
        # self.notebook.AddPage(self.formsTab, "Forms")
        # self.notebook.AddPage(self.classesTab, "Classes")
        # self.notebook.AddPage(self.subjectsTab, "Subjects")

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
        self.Bind( wx.EVT_CLOSE, self.closeFrame )
        self.back_btn.Bind(wx.EVT_BUTTON, self.goToPreviousTab)
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelTab)
        self.next_button.Bind(wx.EVT_BUTTON, self.openNextTab)

    def __del__(self):
        pass

    def closeFrame(self, event):
        wx.Exit()

    # Virtual event handlers, overide them in your derived class
    def goToPreviousTab(self, event):
        # Order of tabs
        # 0. Admin Dets
        # 1. Sch Details
        # 2. Forms
        # 3. Classes
        # 4. Subjects

        curr_page = self.notebook.GetSelection()

        if curr_page == 0:  # Admin Details Tab
            """"""
            # self.cancelSchoolDetails()

        if curr_page == 1:  # Disable Sch Details Tab, go back to admin
            self.gauge_pos -= self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Disable back button because we're opening first tab
            self.back_btn.Enable(False)

            # Re-enable previous tab
            self.adminSetupTab.Enable(True)

            # Disable current tab
            self.schDetsTab.Enable(False)

            self.notebook.SetSelection(0)

        elif curr_page == 2:  # Disable Forms Tab, go back to Sch Dets Tab
            self.gauge_pos -= self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Re-enable previous tab
            self.schDetsTab.Enable(True)

            # Disable current tab
            self.formsTab.Enable(False)

            self.notebook.SetSelection(1)

        elif curr_page == 3:  # Classes Tab, prev is forms
            self.gauge_pos -= self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Re-enable previous tab
            self.formsTab.Enable(True)

            # Disable current tab
            self.classesTab.Enable(False)

            self.notebook.SetSelection(2)

        elif curr_page == 4:  # Subjects Tab, prev is classes
            self.gauge_pos -= self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Re-enable previous tab
            self.classesTab.Enable(True)

            # Disable current tab
            self.subjectsTab.Enable(False)

            self.notebook.SetSelection(3)

            # Change Finish button back to Next
            self.next_button.SetLabel("Next")

        # elif curr_page == 5:  # Preview Tab, prev is subjects
        #     self.gauge_pos -= self.range
        #     self.setup_gauge.SetValue(self.gauge_pos)
        #
        #     # Re-enable previous tab
        #     self.subjectsTab.Enable(True)
        #
        #     # Disable current tab
        #     self.previewTab.Enable(False)
        #
        #     self.notebook.SetSelection(4)

    #
    # --------------------------------------------------
    def cancelTab(self, event):
        # Order of tabs
        # 0. Admin Dets
        # 1. Sch Details
        # 2. Forms
        # 3. Classes
        # 4. Subjects

        curr_page = self.notebook.GetSelection()

        if curr_page == 0:  # Admin Tab
            self.cancelAdminSetup()

        elif curr_page == 1:  # Sch Details Tab
            self.cancelSchoolDetails()

        elif curr_page == 2:  # Forms Tab
            self.cancelSetupForms()

        elif curr_page == 3:  # Classes Tab
            self.cancelSetupClasses()

        elif curr_page == 4:  # Subjects Tab
            self.cancelSetupSubjects()

    #
    # --------------------------------------------------
    def cancelAdminSetup(self):
        self.adminSetupTab.first_name.SetValue("")
        self.adminSetupTab.last_name.SetValue("")
        self.adminSetupTab.surname.SetValue("")
        self.adminSetupTab.phone.SetValue("")
        self.adminSetupTab.email.SetValue("")

        self.adminSetupTab.gender.SetSelection(-1)
        self.adminSetupTab.username.GetLineText(0)
        self.adminSetupTab.username.SetValue("")
        self.adminSetupTab.password.SetValue("")
        self.adminSetupTab.conf_password.SetValue("")

        td = datetime.today()

        # get wxPython datetime format
        day = td.day
        month = td.month
        year = td.year

        # -1 because the month counts from 0, whereas people count January as month #1.
        tdFormatted = wx.DateTimeFromDMY(day, month - 1, year)

        self.adminSetupTab.dob.SetValue(tdFormatted)

    #
    # --------------------------------------------------
    def cancelSchoolDetails(self):
        self.schDetsTab.school_name.SetValue("")
        self.schDetsTab.no_of_subjects.SetValue("")

    #
    # --------------------------------------------------
    def cancelSetupForms(self):
        self.formsTab.streams = []
        self.formsTab.stream_textfield.SetValue("")

        self.formsTab.refreshPreview("")

    #
    # --------------------------------------------------
    def cancelSetupClasses(self):
        self.classesTab.form_one_streams = []
        self.classesTab.form_two_streams = []
        self.classesTab.form_three_streams = []
        self.classesTab.form_four_streams = []

    #
    # --------------------------------------------------
    def cancelSetupSubjects(self):
        self.subjectsTab.subjects = []
        self.subjectsTab.subject_textfield.SetValue("")
        self.subjectsTab.subject_alias_textfield.SetValue("")

        self.subjectsTab.refreshPreview("")

    #
    # --------------------------------------------------
    def openNextTab(self, event):
        # Order of tabs
        # 0. Sch Details
        # 1. Forms
        # 2. Classes
        # 3. Subjects

        curr_page = self.notebook.GetSelection()

        if curr_page == 0:  # Admin tab
            self.saveAdminSetup() # Save then navigate

        elif curr_page == 1: # Save 2nd tab, sch details and move to forms
            # Function saves details, navigates to next tab if successful
            self.saveSchoolDetails()

        elif curr_page == 2: # Save 3rd tab, forms and move to classes
            self.saveSetupForms()

        elif curr_page == 3: # Save classes (4th tab) and move to subjects
            # Save Details
            self.saveSetupClasses()

        elif curr_page == 4:  # Save subjects
            self.saveSetupSubjects()

    #
    # --------------------------------------------------
    def hasNumbers(self, inputString):  # checks for numbers in string, returns true if there is a number
        return any(char.isdigit() for char in inputString)

    #
    # ---------------------------------------------------
    def saveAdminSetup(self):
        first_name = self.adminSetupTab.first_name.GetLineText(0)
        last_name = self.adminSetupTab.last_name.GetLineText(0)
        surname = self.adminSetupTab.surname.GetLineText(0)
        phone = self.adminSetupTab.phone.GetLineText(0)
        email = self.adminSetupTab.email.GetLineText(0)
        dob = self.adminSetupTab.dob.GetValue()
        genderIndex = self.adminSetupTab.gender.GetCurrentSelection()
        username = self.adminSetupTab.username.GetLineText(0)
        password = self.adminSetupTab.password.GetLineText(0)
        conf_password = self.adminSetupTab.conf_password.GetLineText(0)

        # Remove white spaces
        first_name = first_name.replace(" ", "")
        last_name = last_name.replace(" ", "")
        surname = surname.replace(" ", "")
        username = username.strip()
        password = password.strip()
        conf_password = conf_password.strip()

        # ---------- VALIDATION ----------
        error = ""

        if first_name == "" or last_name == "" or surname == "":
            error = error + "All name fields are required.\n"

        if self.hasNumbers(first_name) or self.hasNumbers(last_name) or self.hasNumbers(surname):
            error = error + "Names cannot have numeric characters.\n"

        # check that date has been changed
        td = datetime.today()

        # get wxPython datetime format
        day = td.day
        month = td.month
        year = td.year

        # -1 because the month counts from 0, whereas people count January as month #1.
        tdFormatted = wx.DateTimeFromDMY(day, month - 1, year)
        if str(dob) == str(tdFormatted):
            error = error + "The Date of Birth field is required.\n"

        if genderIndex == -1:
            error = error + "The Gender field is required.\n"

        if email == "":
            error = error + "The Email Address field is required.\n"
        else:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                error = error + "Enter a valid email address.\n"

        if phone == "":
            error = error + "The Phone field is required.\n"
        else:
            if not phone.isdigit():
                error = error + "The Phone field expects numeric characters. \n"
            else:
                if len(phone) != 10:
                    error = error + "The Phone field expects ten digits. \n"

        if username == "":
            error = error + "The Username field is required.\n"

        if password == "":
            error = error + "The Password field is required.\n"

        if conf_password == "":
            error = error + "The Confirm Password field is required.\n"

        if conf_password != password:
            error = error + "Passwords do not match.\n"
        else:
            if len(password) < 5:
                error = error + "The Password should have at least 5 characters.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()

        else:
            data = {
                'first_name': first_name,
                'last_name': last_name,
                'surname': surname,
                'phone': phone,
                'email': email,
                'dob': dob,
                'gender': "M" if genderIndex == 0 else "F",
                'username': username,
                'password': password
            }

            self.setup_data['adminDets'] = data

            # Navigate

            # Disable current page
            self.adminSetupTab.Enable(False)

            self.gauge_pos += self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Enable back button
            self.back_btn.Enable(True)

            if not self.sch_dets_tab_created:  # Create if tab hadn't been created, otherwise move to page

                self.schDetsTab = SetupSchoolDetails(self.notebook, )
                self.notebook.InsertPage(1, self.schDetsTab, "School Details", select=True)

                self.sch_dets_tab_created = 1
            else:
                self.schDetsTab.Enable(True)
                self.notebook.SetSelection(1)

    #
    # --------------------------------------------------
    def saveSchoolDetails(self):  # Save Tab 2
        school_name = self.schDetsTab.school_name.GetLineText(0)
        no_of_subjects = self.schDetsTab.no_of_subjects.GetLineText(0)

        # -------------------- VALIDATION --------------------
        error = ""

        if school_name == "" or school_name.replace(" ", "") == "":
            error = error + "School Name is required.\n"
        else:
            if self.hasNumbers(school_name):
                error = error + "School Name cannot have numeric characters.\n"

        if no_of_subjects.replace("", "") == "":
            error = error + "The No of subjects field is required.\n"
        else:
            if not no_of_subjects.isdigit():
                error = error + "The No of subjects field expects a number.\n"
            else:
                if int(no_of_subjects) < 9:
                    error = error + "No of subjects in lower forms are expected to be more than 8.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()

        else:
            self.setup_data['school_name'] = school_name
            self.setup_data['subjects_lower_form'] = no_of_subjects

            # Navigate

            # Disable current page
            self.schDetsTab.Enable(False)

            self.gauge_pos += self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Enable back button
            self.back_btn.Enable(True)

            if not self.forms_tab_created:  # Create if tab hadn't been created, otherwise move to page
                self.formsTab = SetupForms(self.notebook)

                self.formsTab.SetToolTipString("Navigate using buttons to avoid inconsistency.")
                self.notebook.InsertPage(2, self.formsTab, "Forms", select=True)

                self.forms_tab_created = 1

            else:  # When using back btn
                self.formsTab.Enable(True)
                self.notebook.SetSelection(2)

    #
    # --------------------------------------------------
    def saveSetupForms(self):
        form_streams = self.formsTab.streams

        navigate = True
        if len(form_streams) == 0:
            dlg = wx.MessageDialog(None, "Proceed without adding streams?\nThe system will default to one stream per form.", 'Warning Message.',
                                   wx.YES_NO | wx.ICON_WARNING)
            retCode = dlg.ShowModal()

            if retCode == wx.ID_YES:
                form_streams = []

            else:
                dlg.Destroy()
                navigate = False

        if navigate:
            self.setup_data['form_streams'] = form_streams

            # Navigate

            # Disable current page
            self.formsTab.Enable(False)

            self.gauge_pos += self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Enable back button
            self.back_btn.Enable(True)

            if not self.classes_tab_created:  # Create if tab hadn't been created, otherwise move to page

                self.classesTab = SetupClasses(self.notebook, form_streams)
                self.notebook.InsertPage(3, self.classesTab, "Classes", select=True)

                self.classes_tab_created = 1
            else:
                self.notebook.DeletePage(3)
                self.notebook.SendSizeEvent()

                self.classesTab = SetupClasses(self.notebook, form_streams)
                self.notebook.InsertPage(3, self.classesTab, "Classes", select=True)
                self.classesTab.Enable(True)
                self.notebook.SetSelection(3)

    #
    # --------------------------------------------------
    def saveSetupClasses(self):
        form_one = self.classesTab.form_one_streams
        form_two = self.classesTab.form_two_streams
        form_three = self.classesTab.form_three_streams
        form_four = self.classesTab.form_four_streams

        # ---------- VALIDATION ----------
        error = ""
        if len(form_one) == 0 or len(form_two) == 0 or len(form_three) == 0 or len(form_four) == 0:
            error = error + "All forms must have at least one stream selected. \n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()

        else:
            self.setup_data['class_names'] = [form_one, form_two, form_three, form_four]

            # Navigate

            # Disable current page
            self.classesTab.Enable(False)

            self.gauge_pos += self.range
            self.setup_gauge.SetValue(self.gauge_pos)

            # Enable back button
            self.back_btn.Enable(True)

            if not self.subjects_tab_created:  # Create if tab hadn't been created, otherwise move to page

                self.subjectsTab = SetupSubjects(self.notebook)
                self.notebook.InsertPage(4, self.subjectsTab, "Subjects", select=True)

                self.subjects_tab_created = 1
            else:
                self.subjectsTab.Enable(True)
                self.notebook.SetSelection(4)

            # Change next button to finish
            self.next_button.SetLabel("Finish")

    #
    # --------------------------------------------------
    def saveSetupSubjects(self):
        if len(self.subjectsTab.subjects) < 8:
            dlg = wx.MessageDialog(None, "At least 8 subjects expected, " + str(len(self.subjectsTab.subjects)) + " given", 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
        else:
            self.setup_data['subjects'] = self.subjectsTab.subjects

            if self.setup_data['saved']:
                dlg = wx.MessageDialog(None, "Data already saved.", 'Success Message.',
                                       wx.OK | wx.ICON_EXCLAMATION)
                dlg.ShowModal()

                self.gauge_pos += self.range
                self.setup_gauge.SetValue(self.gauge_pos)

                self.Close()
            else:
                dlg = wx.MessageDialog(None, "Click YES to proceed finish setup.", 'Setup Almost Complete.', wx.YES_NO | wx.ICON_INFORMATION)
                retCode = dlg.ShowModal()

                if retCode == wx.ID_YES:
                    # Save all setup data to Database
                    loggedInUser = getSetupData(self.setup_data)

                    self.setup_data['saved'] = True

                    self.gauge_pos += self.range
                    self.setup_gauge.SetValue(self.gauge_pos)

                    dlg = wx.MessageDialog(None, "Data saved successfully.", 'Success Message.',
                                           wx.OK | wx.ICON_EXCLAMATION)
                    dlg.ShowModal()

                    self.Close()

                    hp = HomePage(None, loggedInUser)
                    hp.Show()
                    self.Destroy()
                else:
                    dlg.Destroy()


            # # Navigate
            #
            # # Disable current page
            # self.subjectsTab.Enable(False)
            #
            # self.gauge_pos += self.range
            # self.setup_gauge.SetValue(self.gauge_pos)
            #
            # # Enable back button
            # self.back_btn.Enable(True)
            #
            # if not self.preview_tab_created:  # Create if tab hadn't been created, otherwise move to page
            #
            #     self.previewTab = PreviewSetup(self.notebook, self.setup_data)
            #     self.notebook.InsertPage(5, self.previewTab, "Preview", select=True)
            #
            #     self.preview_tab_created = 1
            # else:
            #     self.previewTab.Enable(True)
            #     self.notebook.SetSelection(5)


# class MyApp(wx.App):
#     def OnInit(self):
#
#         self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
#
#         return True
#
#
# # Run the program
# if __name__ == "__main__":
#     app = MyApp()
#     frame = SetupMainFrame(None)
#     frame.Show()
#     app.MainLoop()

