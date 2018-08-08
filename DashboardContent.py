import wx
import wx.xrc

from StudentPersonalDetails import StudentPersonalDetails
from ProgressReport import ProgressReport
from StudentSubjects import StudentSubjects

###########################################################################
# Class DashboardContentPanel
###########################################################################


class DashboardContent(wx.Panel):

    def __init__(self, parent, student):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent
        self.student = student

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # outer_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        left_menu_sizer = wx.BoxSizer(wx.VERTICAL)

        self.personal_dets_btn = wx.Button(self, wx.ID_ANY, u"Personal Details", wx.DefaultPosition, wx.DefaultSize, 0)
        left_menu_sizer.Add(self.personal_dets_btn, 1, wx.EXPAND, 5)

        self.progress_report_btn = wx.Button(self, wx.ID_ANY, u"Progress Report", wx.DefaultPosition, wx.DefaultSize, 0)
        left_menu_sizer.Add(self.progress_report_btn, 1, wx.EXPAND, 5)

        self.drop_subject_btn = wx.Button(self, wx.ID_ANY, u"Drop Subject", wx.DefaultPosition, wx.DefaultSize, 0)
        left_menu_sizer.Add(self.drop_subject_btn, 1, wx.EXPAND, 5)

        self.m_button51 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        left_menu_sizer.Add(self.m_button51, 1, wx.EXPAND, 5)

        left_menu_sizer.AddSpacer((0, 0), 12, wx.EXPAND, 5)

        outer_sizer.Add(left_menu_sizer, 0, wx.EXPAND | wx.LEFT, 15)

        right_side_sizer = wx.BoxSizer(wx.HORIZONTAL)

        right_side_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        wrapper_sizer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline21 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        wrapper_sizer.Add(self.m_staticline21, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        profile_sizer = wx.BoxSizer(wx.HORIZONTAL)

        profile_left_sizer = wx.BoxSizer(wx.VERTICAL)

        names_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.names_label = wx.StaticText(self, wx.ID_ANY, u"Names:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.names_label.Wrap(-1)
        self.names_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        names_sizer.Add(self.names_label, 0, wx.ALL, 5)

        self.names_text = wx.StaticText(self, wx.ID_ANY, student['first_name'] + " " + student['last_name'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.names_text.Wrap(-1)
        names_sizer.Add(self.names_text, 0, wx.ALL, 5)

        self.m_staticline12 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        names_sizer.Add(self.m_staticline12, 0, wx.EXPAND | wx.ALL, 5)

        profile_left_sizer.Add(names_sizer, 0, wx.EXPAND, 5)

        self.m_staticline7 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        profile_left_sizer.Add(self.m_staticline7, 0, wx.EXPAND | wx.LEFT, 5)

        surname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.surname_label = wx.StaticText(self, wx.ID_ANY, u"Surname:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.surname_label.Wrap(-1)
        self.surname_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        surname_sizer.Add(self.surname_label, 0, wx.ALL, 5)

        self.surname_text = wx.StaticText(self, wx.ID_ANY, student['surname'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.surname_text.Wrap(-1)
        surname_sizer.Add(self.surname_text, 0, wx.ALL, 5)

        profile_left_sizer.Add(surname_sizer, 0, wx.EXPAND, 5)

        self.m_staticline72 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        profile_left_sizer.Add(self.m_staticline72, 0, wx.EXPAND | wx.LEFT, 5)

        kcpe_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.kcpe_label = wx.StaticText(self, wx.ID_ANY, u"KCPE:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.kcpe_label.Wrap(-1)
        self.kcpe_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        kcpe_sizer.Add(self.kcpe_label, 0, wx.ALL, 5)

        self.kcpe_text = wx.StaticText(self, wx.ID_ANY, str(student['kcpe_marks']), wx.DefaultPosition, wx.DefaultSize, 0)
        self.kcpe_text.Wrap(-1)
        kcpe_sizer.Add(self.kcpe_text, 0, wx.ALL, 5)

        profile_left_sizer.Add(kcpe_sizer, 1, wx.EXPAND, 5)

        profile_sizer.Add(profile_left_sizer, 1, wx.EXPAND, 5)

        profile_right_sizer = wx.BoxSizer(wx.VERTICAL)

        form_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.form_label = wx.StaticText(self, wx.ID_ANY, u"Form:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.form_label.Wrap(-1)
        self.form_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        form_sizer.Add(self.form_label, 0, wx.ALL, 5)

        self.form_text = wx.StaticText(self, wx.ID_ANY, str(student['form']), wx.DefaultPosition, wx.DefaultSize, 0)
        self.form_text.Wrap(-1)
        form_sizer.Add(self.form_text, 0, wx.ALL, 5)

        profile_right_sizer.Add(form_sizer, 0, wx.EXPAND, 5)

        self.m_staticline71 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        profile_right_sizer.Add(self.m_staticline71, 0, wx.EXPAND | wx.RIGHT, 5)

        class_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.class_label = wx.StaticText(self, wx.ID_ANY, u"Class:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.class_label.Wrap(-1)
        self.class_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        class_sizer.Add(self.class_label, 0, wx.ALL, 5)

        self.class_text = wx.StaticText(self, wx.ID_ANY, student['class'], wx.DefaultPosition, wx.DefaultSize, 0)
        self.class_text.Wrap(-1)
        class_sizer.Add(self.class_text, 0, wx.ALL, 5)

        profile_right_sizer.Add(class_sizer, 0, wx.EXPAND, 5)

        self.m_staticline711 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        profile_right_sizer.Add(self.m_staticline711, 0, wx.EXPAND | wx.RIGHT, 5)

        profile_sizer.Add(profile_right_sizer, 1, wx.EXPAND, 5)

        wrapper_sizer.Add(profile_sizer, 0, wx.EXPAND, 5)

        content_sizer = wx.BoxSizer(wx.VERTICAL)

        self.border_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.border_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        content_panel_sizer = wx.BoxSizer(wx.VERTICAL)

        #
        #
        # --------------- ADD PANELS ---------------
        self.personal_dets = StudentPersonalDetails(self.border_panel, student)
        self.personal_dets.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.progress_report = ProgressReport(self.border_panel, student)
        self.progress_report.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.student_subjects = StudentSubjects(self.border_panel, student)
        self.student_subjects.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.progress_report.Hide()
        self.student_subjects.Hide()

        content_panel_sizer.Add(self.personal_dets, 1, wx.EXPAND | wx.ALL, 2)
        content_panel_sizer.Add(self.progress_report, 1, wx.EXPAND | wx.ALL, 2)
        content_panel_sizer.Add(self.student_subjects, 1, wx.EXPAND | wx.ALL, 2)
        #
        #

        self.border_panel.SetSizer(content_panel_sizer)
        self.border_panel.Layout()
        content_panel_sizer.Fit(self.border_panel)
        content_sizer.Add(self.border_panel, 1, wx.EXPAND | wx.ALL, 5)

        wrapper_sizer.Add(content_sizer, 1, wx.EXPAND, 5)

        right_side_sizer.Add(wrapper_sizer, 18, wx.EXPAND, 5)

        right_side_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        outer_sizer.Add(right_side_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(outer_sizer)
        self.Layout()

        # Connect Events
        self.personal_dets_btn.Bind(wx.EVT_BUTTON, self.switchDashboardPanels)
        self.progress_report_btn.Bind(wx.EVT_BUTTON, self.switchDashboardPanels)
        self.drop_subject_btn.Bind(wx.EVT_BUTTON, self.switchDashboardPanels)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def switchDashboardPanels(self, event):
        obj = event.GetEventObject()
        label = obj.GetLabel()

        self.personal_dets.Hide()
        self.progress_report.Hide()
        self.student_subjects.Hide()

        if label == "Personal Details":
            self.personal_dets.Show()
        elif label == "Progress Report":
            self.progress_report.Show()
        elif label == "Drop Subject":
            self.student_subjects.Show()
        self.Layout()




