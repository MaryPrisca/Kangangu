import wx

import lxml.etree
import lxml.builder

import os
from selenium import webdriver

from StudentsPanel import StudentsPanel
from TeachersPanel import TeachersPanel
from ClassesPanel import ClassesPanel
from SubjectsPanel import SubjectsPanel
from ExamsPanel import ExamsPanel
from ProfilePanel import ProfilePanel
from EventsPanel import EventsPanel

from db.uploading_data import *

try:
    import httplib
except:
    import http.client as httplib


# from db.get_logged_user import get_logged_in_user
# import sys
#
# sys.path.insert(0, r'../Kangangu')

from wx.lib.embeddedimage import PyEmbeddedImage

appIcon = PyEmbeddedImage(
    "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"
    "f7H8iAAAAABJRU5ErkJggg==")


class HomePage(wx.Frame):

    def __init__(self, parent, userdata):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="KANGANGU SECONDARY SCHOOL MANAGEMENT SYSTEM", pos=wx.DefaultPosition,
                          size=wx.Size(651, 475), style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.TAB_TRAVERSAL)

        ico = appIcon.getIcon()
        self.SetIcon(ico)

        self.userdata = userdata

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        outer_sizer = wx.BoxSizer(wx.VERTICAL)

        content = wx.BoxSizer(wx.HORIZONTAL)

        side_nav = wx.BoxSizer(wx.VERTICAL)

        user_box = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap3 = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"images\\appIcon-96x96.bmp", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER)
        self.m_bitmap3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        user_box.Add(self.m_bitmap3, 3, wx.EXPAND, 5)

        side_nav.Add(user_box, 1, wx.EXPAND, 5)

        sidenav_buttons = wx.BoxSizer(wx.VERTICAL)

        self.students_button = wx.Button(self, wx.ID_ANY, u"Students", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.students_button.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.students_button.SetForegroundColour(wx.Colour(204, 204, 204))
        self.students_button.SetBackgroundColour(wx.Colour(48, 53, 62))

        sidenav_buttons.Add(self.students_button, 1, wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.m_staticline1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        self.m_staticline1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        sidenav_buttons.Add(self.m_staticline1, 0, wx.EXPAND, 5)

        self.techers_button = wx.Button(self, wx.ID_ANY, u"Teachers", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.techers_button.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.techers_button.SetForegroundColour(wx.Colour(204, 204, 204))
        self.techers_button.SetBackgroundColour(wx.Colour(48, 53, 62))

        sidenav_buttons.Add(self.techers_button, 1, wx.EXPAND, 5)

        self.m_staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.m_staticline2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_staticline2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        sidenav_buttons.Add(self.m_staticline2, 0, wx.EXPAND, 5)

        self.subjects_button = wx.Button(self, wx.ID_ANY, u"Subjects", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.subjects_button.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.subjects_button.SetForegroundColour(wx.Colour(204, 204, 204))
        self.subjects_button.SetBackgroundColour(wx.Colour(48, 53, 62))

        sidenav_buttons.Add(self.subjects_button, 1, wx.EXPAND, 5)

        self.m_staticline3 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        sidenav_buttons.Add(self.m_staticline3, 0, wx.EXPAND, 5)

        self.classes_button = wx.Button(self, wx.ID_ANY, u"Classes", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.classes_button.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.classes_button.SetForegroundColour(wx.Colour(204, 204, 204))
        self.classes_button.SetBackgroundColour(wx.Colour(48, 53, 62))

        sidenav_buttons.Add(self.classes_button, 1, wx.EXPAND, 5)

        self.m_staticline4 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        sidenav_buttons.Add(self.m_staticline4, 0, wx.EXPAND, 5)

        self.exams_button = wx.Button(self, wx.ID_ANY, u"Exams", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.exams_button.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.exams_button.SetForegroundColour(wx.Colour(204, 204, 204))
        self.exams_button.SetBackgroundColour(wx.Colour(48, 53, 62))

        sidenav_buttons.Add(self.exams_button, 1, wx.EXPAND, 5)

        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        sidenav_buttons.Add(self.m_staticline5, 0, wx.EXPAND, 5)

        self.events_button = wx.Button(self, wx.ID_ANY, u"Events", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.events_button.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.events_button.SetForegroundColour(wx.Colour(204, 204, 204))
        self.events_button.SetBackgroundColour(wx.Colour(48, 53, 62))

        sidenav_buttons.Add(self.events_button, 1, wx.EXPAND, 5)

        self.m_staticline6 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        sidenav_buttons.Add(self.m_staticline6, 0, wx.EXPAND, 5)

        #
        #

        self.profile_button = wx.Button(self, wx.ID_ANY, u"My Profile", wx.DefaultPosition, wx.DefaultSize,
                                        wx.NO_BORDER)
        self.profile_button.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.profile_button.SetForegroundColour(wx.Colour(204, 204, 204))
        self.profile_button.SetBackgroundColour(wx.Colour(48, 53, 62))

        sidenav_buttons.Add(self.profile_button, 1, wx.EXPAND, 5)

        self.m_staticline7 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        sidenav_buttons.Add(self.m_staticline7, 0, wx.EXPAND, 5)

        self.upload_button = wx.Button(self, wx.ID_ANY, u"Upload Data", wx.DefaultPosition, wx.DefaultSize,
                                       wx.NO_BORDER)
        self.upload_button.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.upload_button.SetForegroundColour(wx.Colour(204, 204, 204))
        self.upload_button.SetBackgroundColour(wx.Colour(150, 53, 62))
        self.upload_button.SetToolTipString(u"Click to sync local and online data")

        sidenav_buttons.Add(self.upload_button, 1, wx.EXPAND, 5)

        self.m_staticline8 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        sidenav_buttons.Add(self.m_staticline8, 0, wx.EXPAND, 5)

        #
        #

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        self.m_staticText12.SetBackgroundColour(wx.Colour(48, 53, 62))

        sidenav_buttons.Add(self.m_staticText12, 3, wx.EXPAND, 5)

        side_nav.Add(sidenav_buttons, 5, wx.EXPAND, 5)

        content.Add(side_nav, 1, wx.EXPAND, 5)

        main_content = wx.BoxSizer(wx.VERTICAL)

        # Add Panels
        self.students_panel = StudentsPanel(self)
        self.teachers_panel = TeachersPanel(self)
        self.classes_panel = ClassesPanel(self)
        self.subjects_panel = SubjectsPanel(self)
        self.exams_panel = ExamsPanel(self, self.userdata)
        self.profile_panel = ProfilePanel(self, self.userdata)
        self.events_panel = EventsPanel(self)

        self.teachers_panel.Hide()
        self.classes_panel.Hide()
        self.subjects_panel.Hide()
        self.exams_panel.Hide()
        self.profile_panel.Hide()
        self.events_panel.Hide()

        main_content.Add(self.students_panel, 1, wx.EXPAND)
        main_content.Add(self.teachers_panel, 1, wx.EXPAND)
        main_content.Add(self.classes_panel, 1, wx.EXPAND)
        main_content.Add(self.subjects_panel, 1, wx.EXPAND)
        main_content.Add(self.exams_panel, 1, wx.EXPAND)
        main_content.Add(self.profile_panel, 1, wx.EXPAND)
        main_content.Add(self.events_panel, 1, wx.EXPAND)

        content.Add(main_content, 7, wx.EXPAND, 5)

        outer_sizer.Add(content, 1, wx.EXPAND, 5)

        self.SetSizer(outer_sizer)
        self.Layout()

        # self.m_statusBar2 = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
        # self.m_statusBar2.SetBackgroundColour(wx.Colour(26, 29, 34))

        self.Centre(wx.BOTH)

        # Connect Events
        self.students_button.Bind(wx.EVT_BUTTON, self.onSwitchPanels)
        self.techers_button.Bind(wx.EVT_BUTTON, self.onSwitchPanels)
        self.classes_button.Bind(wx.EVT_BUTTON, self.onSwitchPanels)
        self.subjects_button.Bind(wx.EVT_BUTTON, self.onSwitchPanels)
        self.exams_button.Bind(wx.EVT_BUTTON, self.onSwitchPanels)
        self.profile_button.Bind(wx.EVT_BUTTON, self.onSwitchPanels)
        self.events_button.Bind(wx.EVT_BUTTON, self.onSwitchPanels)
        self.upload_button.Bind(wx.EVT_BUTTON, self.getUploadData)

    def onSwitchPanels(self, event):
            self.students_panel.Hide()
            self.teachers_panel.Hide()
            self.classes_panel.Hide()
            self.subjects_panel.Hide()
            self.exams_panel.Hide()
            self.profile_panel.Hide()
            self.events_panel.Hide()

            """ shows the panel corresponding to the button pressed """
            obj = event.GetEventObject()
            label = obj.GetLabel()
            if label == "Students":
                self.SetTitle("KANGANGU SECONDARY SCHOOL - STUDENTS")
                self.students_panel.Show()
            elif label == "Teachers":
                self.SetTitle("KANGANGU SECONDARY SCHOOL - TEACHERS")
                self.teachers_panel.Show()
            elif label == "Classes":
                self.SetTitle("KANGANGU SECONDARY SCHOOL - CLASSES")
                self.classes_panel.Show()
            elif label == "Subjects":
                self.SetTitle("KANGANGU SECONDARY SCHOOL - SUBJECTS")
                self.subjects_panel.Show()
            elif label == "Exams":
                self.SetTitle("KANGANGU SECONDARY SCHOOL - EXAMS")
                self.exams_panel.Show()
            elif label == "My Profile":
                self.SetTitle("KANGANGU SECONDARY SCHOOL - MY PROFILE")
                self.profile_panel.Show()
            elif label == "Events":
                self.SetTitle("KANGANGU SECONDARY SCHOOL - SCHOOL EVENTS")
                self.events_panel.Show()
            self.Layout()

    def Logout(self, event):
        dlg = wx.MessageDialog(None, "Are you sure you want to exit?", 'Confirm Action.',
                               wx.YES_NO | wx.ICON_INFORMATION)
        retCode = dlg.ShowModal()

        if retCode == wx.ID_YES:
            self.userdata = {}
            self.Destroy()
        else:
            dlg.Close()

        dlg.Destroy()

    def InternetConnection(self):
        conn = httplib.HTTPConnection("www.google.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:
            conn.close()
            return False

    def getUploadData(self, event):
        E = lxml.builder.ElementMaker()
        DATABASE = E.database

        # <exam_results>
        #     <exam_results_id>1</exam_results_id>
        #     <exam_id>1</exam_id>
        #     <student_id>11</student_id>
        #     .
        #     .
        #     .
        # </exam_results>

        #
        # CREATING CODE LIKE THE ONE ABOVE FOR EACH TABLE DYNAMICALLY
        # db_tables = ['classes', 'events', 'exams', 'exam_results', 'subjects', 'system_setup', 'users']
        db_tables = ['classes']

        # create string to append all xml file locations as will be used by selenium to upload to web app
        file_paths = ''

        # for table_name in db_tables:
        #
        #     data = getUploadData(table_name)
        #
        #     the_doc = DATABASE(
        #         name="Kangangu"
        #     )
        #
        #     for record in data:
        #         r = TABLE(name=table_name)  # Initialize the table tag for the row.
        #
        #         for key, value in record.iteritems(): # for each 'column' in the dict create a column tag
        #             col = column(str(value), name=key)
        #
        #             r.append(col)  # append the column tag to the table
        #
        #         the_doc.append(r)  # append the table tag to the database document
        #
        #     # Write to respective xml file for each table
        #     with open('uploads/' + table_name + '.xml', 'wb') as doc:
        #         doc.write(lxml.etree.tostring(the_doc, pretty_print=True))
        #
        #     file_paths = file_paths + os.getcwd() + '/uploads/'+table_name+'.xml \n'

        for table_name in db_tables:

            data = getUploadData(table_name)

            the_doc = DATABASE(
                name="Kangangu"
            )

            # Example: Creates <p key="value">text</p>
            # the_doc.append(E("p", "text", key="value"))

            for record in data:
                # Create the first tag with the table name eg. <exam_results></exam_results>
                one_row = E(table_name)

                # Create the tags for the columns and append them to the row
                for key, value in record.iteritems():
                    # key is the column name, (tag in this case) eg. <exam_id>1</exam_id> exam_id is the key, 1 is value
                    one_row.append(E(key, str(value)))

                the_doc.append(one_row)

            # Write to respective xml file for each table
            with open('uploads/' + table_name + '.xml', 'wb') as doc:
                doc.write(lxml.etree.tostring(the_doc, pretty_print=True))

            file_paths = file_paths + os.getcwd() + '/uploads/'+table_name+'.xml \n'

        #
        #
        # FILE UPLOAD
        if self.InternetConnection():
            dlg = wx.MessageDialog(None, "Uploading files...\nDo not close program or shut down for at least 5 minutes.\nClick okay to start the process.", 'File Upload Warning', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

            # Uploading files through selenium fails when files are large so upload is broken down into groups
            upload_groups = [
                {
                    'tables': ['classes', 'events', 'exams'],
                    'paths': os.getcwd() + '\uploads\classes.xml \n' + os.getcwd() + '\uploads\events.xml \n'+ os.getcwd() + '\uploads\exams.xml'
                },
                # {
                #     'tables': ['exam_results', 'subjects'],
                #     'paths': os.getcwd() + '\uploads\exam_results.xml \n' + os.getcwd() + '\uploads\subjects.xml'
                # },
                # {
                #     'tables': ['system_setup', 'users'],
                #     'paths': os.getcwd() + '\uploads\system_setup.xml \n' + os.getcwd() + '\uploads\users.xml'
                # },
            ]

            # Pass the data to be uploaded
            for group in upload_groups:
                self.uploadData(group)

            # Mark all those rows as uploaded
            for table_name in db_tables:
                markRowsAsUploaded(table_name)
        else:
            dlg = wx.MessageDialog(None, "File upload requires stable internet.\nTry again with internet connection",
                                   'File Upload Warning.', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

    #
    # ------------------------------------------------------
    def uploadData(self, data):
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        #
        # # set the window size
        # options.add_argument('window-size=1200x600')
        #
        # # your executable path is wherever you saved the chrome webdriver
        # chromedriver = "uploads/chromedriver-v2.42.exe"
        #
        # # initialize the driver
        # browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

        geckodriver = "uploads/geckodriver.exe"

        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')

        browser = webdriver.Firefox(executable_path=geckodriver, firefox_options=options)

        url = "http://127.0.0.1:8000/upload"
        browser.get(url)

        names_field = browser.find_element_by_name('name')
        upload_field = browser.find_element_by_id('file')

        table_names_string = ",".join(data['tables'])  # Comma separated string

        names_field.send_keys(table_names_string)
        upload_field.send_keys(data['paths'])

        submit_button = browser.find_element_by_css_selector("input[type=\"submit\"]")
        submit_button.click()


# # Run the program
# if __name__ == "__main__":
#     app = wx.App()
#     frame = HomePage(None)
#     frame.Show()
#     app.MainLoop()