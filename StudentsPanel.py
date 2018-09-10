import wx
from AddStudent import AddStudent
from ViewStudents import ViewStudents
from SubjectSelection import SubjectSelection
from StudentDashboard import StudentDashboard
from PromoteStudents import PromoteStudents
# locale = wx.Locale(wx.LANGUAGE_ENGLISH)


class StudentsPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        self.parent = parent

        self.container = wx.BoxSizer(wx.VERTICAL)

        bSizer78 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_toolBar1 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)

        self.m_tool2 = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"View All",
                                                    wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW, wx.ART_TOOLBAR),
                                                    wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar1.AddSeparator()

        self.m_tool1 = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"Add New",
                                                    wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar1.AddSeparator()

        self.subject_tool = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"Subject Selection",
                                                    wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar1.AddSeparator()

        self.m_tool15 = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"Dashboard",
                                                     wx.ArtProvider.GetBitmap(wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR),
                                                     wx.NullBitmap, wx.ITEM_NORMAL, u"View All Details Per Student",
                                                     wx.EmptyString, None)

        self.m_toolBar1.AddSeparator()

        self.m_tool16 = self.m_toolBar1.AddLabelTool(wx.ID_ANY, u"Promote Students",
                                                     wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_TOOLBAR),
                                                     wx.NullBitmap, wx.ITEM_NORMAL,
                                                     u"Move all students to their respective next classes.",
                                                     wx.EmptyString, None)

        self.m_toolBar1.Realize()

        bSizer78.Add(self.m_toolBar1, 1, wx.EXPAND, 5)

        self.m_toolBar4 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)
        self.logout_tool = self.m_toolBar4.AddLabelTool(wx.ID_ANY, u"Logout",
                                                        wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_TOOLBAR),
                                                        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                        None)

        self.m_toolBar4.Realize()

        bSizer78.Add(self.m_toolBar4, 0, wx.EXPAND, 5)

        self.container.Add(bSizer78, 0, wx.EXPAND, 5)

        # ------------ ADD PANELS ------------------
        self.add_student = AddStudent(self)
        self.view_students = ViewStudents(self)
        self.subject_selection = SubjectSelection(self)
        self.student_dashboard = StudentDashboard(self)
        self.promote_students = PromoteStudents(self)
        self.add_student.Hide()
        self.subject_selection.Hide()
        self.student_dashboard.Hide()
        self.promote_students.Hide()

        self.container.Add(self.add_student, 1, wx.EXPAND)
        self.container.Add(self.view_students, 1, wx.EXPAND)
        self.container.Add(self.subject_selection, 1, wx.EXPAND)
        self.container.Add(self.student_dashboard, 1, wx.EXPAND)
        self.container.Add(self.promote_students, 1, wx.EXPAND)

        self.SetSizer(self.container)
        self.Layout()

        # Connect Events
        self.Bind(wx.EVT_TOOL, self.switchToAddStudent, id=self.m_tool1.GetId())
        self.Bind(wx.EVT_TOOL, self.switchToViewStudents, id=self.m_tool2.GetId())
        self.Bind(wx.EVT_TOOL, self.switchToSubjectSelection, id=self.subject_tool.GetId())
        self.Bind(wx.EVT_TOOL, self.switchToStudentDashboard, id=self.m_tool15.GetId())
        self.Bind(wx.EVT_TOOL, self.switchToPromoteStudents, id=self.m_tool16.GetId())
        self.Bind(wx.EVT_TOOL, self.parent.Logout, id=self.logout_tool.GetId())

    def switchToAddStudent(self, event):
        self.view_students.Hide()
        self.subject_selection.Hide()
        self.student_dashboard.Hide()
        self.promote_students.Hide()

        self.add_student.Destroy()

        self.add_student = AddStudent(self)
        self.container.Add(self.add_student, 1, wx.EXPAND)
        self.Layout()

        self.add_student.Show()

        self.Layout()

    def switchToViewStudents(self, event):
        self.add_student.Hide()
        self.subject_selection.Hide()
        self.student_dashboard.Hide()
        self.promote_students.Hide()
        self.view_students.Show()

        self.Layout()

    def switchToSubjectSelection(self, event):
        self.add_student.Hide()
        self.view_students.Hide()
        self.student_dashboard.Hide()
        self.promote_students.Hide()
        self.subject_selection.Show()

        self.Layout()

    def switchToStudentDashboard(self, event):
        self.add_student.Hide()
        self.view_students.Hide()
        self.subject_selection.Hide()
        self.promote_students.Hide()
        self.student_dashboard.Show()

        self.Layout()

    def switchToPromoteStudents(self, event):
        self.add_student.Hide()
        self.view_students.Hide()
        self.subject_selection.Hide()
        self.student_dashboard.Hide()
        self.promote_students.Show()

        self.Layout()