import wx
import wx.xrc

from AddExam import AddExam
from ExamResults import ExamResults
from ViewExams import ViewExams
from AddMarks import AddMarks


###########################################################################
# Class ExamsPanel
###########################################################################

class ExamsPanel(wx.Panel):

    def __init__(self, parent, userdata):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        self.userdata = userdata

        container = wx.BoxSizer(wx.VERTICAL)

        bSizer78 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_toolBar3 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)
        self.m_tool7 = self.m_toolBar3.AddLabelTool(wx.ID_ANY, u"View Exams",
                                                    wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW, wx.ART_TOOLBAR),
                                                    wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar3.AddSeparator()

        self.m_tool6 = self.m_toolBar3.AddLabelTool(wx.ID_ANY, u"Add Exam",
                                                    wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar3.AddSeparator()

        self.m_tool8 = self.m_toolBar3.AddLabelTool(wx.ID_ANY, u"Exam Results",
                                                    wx.ArtProvider.GetBitmap(wx.ART_HELP_SIDE_PANEL, wx.ART_TOOLBAR),
                                                    wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        if self.userdata['role'] == "teacher":
            self.m_toolBar3.AddSeparator()

            self.m_tool9 = self.m_toolBar3.AddLabelTool(wx.ID_ANY, u"Add Marks",
                                                        wx.ArtProvider.GetBitmap(wx.ART_FIND_AND_REPLACE,
                                                                                 wx.ART_TOOLBAR),
                                                        wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString,
                                                        None)

        self.m_toolBar3.Realize()

        bSizer78.Add(self.m_toolBar3, 1, wx.EXPAND, 5)

        self.m_toolBar4 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TB_FLAT | wx.TB_HORIZONTAL | wx.TB_TEXT)
        self.m_tool5 = self.m_toolBar4.AddLabelTool(wx.ID_ANY, u"My Profile",
                                                    wx.ArtProvider.GetBitmap(wx.ART_TIP, wx.ART_TOOLBAR), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar4.Realize()

        bSizer78.Add(self.m_toolBar4, 0, wx.EXPAND, 5)

        container.Add(bSizer78, 0, wx.EXPAND, 5)

        # ------------ ADD PANELS ------------------
        self.add_exam = AddExam(self)
        self.exam_results = ExamResults(self)
        self.view_exams = ViewExams(self)

        self.add_marks_panel_added = 0

        # Add Marks only for teachers
        if self.userdata['role'] == "teacher":
            self.add_marks = AddMarks(self, self.userdata)
            self.add_marks.Hide()
            container.Add(self.add_marks, 1, wx.EXPAND)

            self.add_marks_panel_added = 1

        self.add_exam.Hide()
        self.exam_results.Hide()

        container.Add(self.add_exam, 1, wx.EXPAND)
        container.Add(self.exam_results, 1, wx.EXPAND)
        container.Add(self.view_exams, 1, wx.EXPAND)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.Bind(wx.EVT_TOOL, self.switchToViewExams, id=self.m_tool7.GetId())
        self.Bind(wx.EVT_TOOL, self.switchToAddExam, id=self.m_tool6.GetId())
        self.Bind(wx.EVT_TOOL, self.switchToAllResults, id=self.m_tool8.GetId())
        if self.userdata['role'] == "teacher":
            self.Bind(wx.EVT_TOOL, self.switchToAddMarks, id=self.m_tool9.GetId())

    def __del__(self):
        pass

    def switchToViewExams(self, event):
        self.add_exam.Hide()
        self.exam_results.Hide()

        if self.add_marks_panel_added:
            self.add_marks.Hide()

        self.view_exams.Show()

        self.Layout()

    def switchToAddExam(self, event):
        self.exam_results.Hide()
        self.view_exams.Hide()

        if self.add_marks_panel_added:
            self.add_marks.Hide()

        self.add_exam.Show()

        self.Layout()

    def switchToAllResults(self, event):
        self.add_exam.Hide()
        self.view_exams.Hide()

        if self.add_marks_panel_added:
            self.add_marks.Hide()

        self.exam_results.Show()

        self.Layout()

    def switchToAddMarks(self, event):
        self.add_exam.Hide()
        self.view_exams.Hide()
        self.exam_results.Hide()

        self.add_marks.Show()

        self.Layout()
