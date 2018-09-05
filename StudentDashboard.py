import wx
import wx.xrc

from DashboardContent import DashboardContent

from db.get_students import getStudents, getStudentByIDAllDetails


###########################################################################
# Class StudentDashboard
###########################################################################

class StudentDashboard(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(669, 458),
                          style=wx.TAB_TRAVERSAL)

        self.container = wx.BoxSizer(wx.VERTICAL)

        self.page_title = wx.StaticText(self, wx.ID_ANY, u"Student Dashboard", wx.DefaultPosition, wx.DefaultSize,
                                        wx.ALIGN_CENTRE)
        self.page_title.Wrap(-1)
        self.page_title.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        self.container.Add(self.page_title, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)

        search_sizer = wx.BoxSizer(wx.HORIZONTAL)

        search_sizer.AddSpacer((0, 0), 7, wx.EXPAND, 5)

        self.search_students = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.search_students.ShowSearchButton(True)
        self.search_students.ShowCancelButton(True)
        self.search_students.SetToolTipString(u"Type name or Reg No. to view student details")
        search_sizer.Add(self.search_students, 3, wx.EXPAND | wx.ALL, 5)

        search_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.container.Add(search_sizer, 0, wx.EXPAND, 5)

        #
        #
        #

        self.search_results_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.search_results_sizer.AddSpacer((0, 0), 7, wx.EXPAND, 5)

        self.search_results_panel = SearchResultsPanel(self, [])
        self.search_results_panel.Hide()

        self.search_results_sizer.Add(self.search_results_panel, 4, wx.EXPAND | wx.ALL, 5)

        self.container.Add(self.search_results_sizer, 0, wx.EXPAND, 5)

        #
        #
        #
        sample_student = {
            'user_id': 0,
            'reg_no': 0,
            'first_name': "",
            'last_name': "",
            'surname': "",
            'dob': "",
            'gender': "",
            'class_id': 0,
            'subjects_taken': "",
            'kcpe_marks': 0,
            'birth_cert_no': "",
            'next_of_kin_name': "",
            'next_of_kin_phone': "",
            'address': "",
            'created_at': "",
            'class': "",
            'form': ""
        }

        self.content_panel = DashboardContent(self, sample_student)
        self.content_panel.Hide()
        self.container.Add(self.content_panel, 4, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.container)
        self.Layout()

        # Connect Events
        self.search_students.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN, self.cancelSearchStudents)
        self.search_students.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.searchStudents)
        self.search_students.Bind(wx.EVT_TEXT, self.searchStudents)
        self.search_students.Bind(wx.EVT_TEXT_ENTER, self.searchStudents)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class

    def cancelSearchStudents(self, event):
        self.search_students.SetValue("")

        self.search_results_panel.Hide()

    def searchStudents(self, event):
        search_text = self.search_students.GetValue()
        if len(search_text) > 2:
            results = getStudents(search=search_text)

            # If the search returns results
            if len(results) > 0:
                self.search_results_panel.Hide()

                self.search_results_panel = SearchResultsPanel(self, results)

                self.search_results_sizer.Add(self.search_results_panel, 4, wx.EXPAND | wx.ALL, 5)

                self.Layout()

        else:
            self.search_results_panel.Hide()

    # Load the content panel with details of the student clicked
    def getStudentDetails(self, user_id):
        self.cancelSearchStudents("")
        self.search_results_panel.Hide()

        self.content_panel.Hide()

        student = getStudentByIDAllDetails(user_id)

        self.content_panel = DashboardContent(self, student)
        self.container.Add(self.content_panel, 4, wx.EXPAND | wx.ALL, 5)

        self.Layout()


class SearchResultsPanel(wx.Panel):

    def __init__(self, parent, results):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent
        self.results = results

        sizer = wx.BoxSizer(wx.VERTICAL)

        container = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        list_sizer = wx.BoxSizer(wx.VERTICAL)

        self.search_results = {}
        for value in self.results:
            self.search_results[str(value['user_id'])] = OneSearchResult(self, value['user_id'], value['reg_no'], value['full_names'], value['class'], value['form'])
            list_sizer.Add(self.search_results[str(value['user_id'])], 0, wx.EXPAND, 5)

        self.spacer = wx.StaticText(self, wx.ID_ANY, u"   ", wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.spacer.Wrap(-1)
        list_sizer.Add(self.spacer, 0, wx.EXPAND, 5)

        container.Add(list_sizer, 0, wx.EXPAND, 5)

        sizer.Add(container, 1, wx.EXPAND | wx.RIGHT, 100)

        self.SetSizer(sizer)
        self.Layout()

    def __del__(self):
        pass

    def getStudentIDClicked(self, user_id):
        self.parent.getStudentDetails(user_id)


class OneSearchResult(wx.Panel):

    def __init__(self, parent, user_id, reg_no, student_name, class_name, form):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        self.parent = parent
        self.user_id = user_id

        # To avoid an instance of form = 1 Form 1 ie if the form has only on stream hence nno class name
        if "Form" in class_name:
            full_name = str(reg_no) + " " + student_name + ", " + class_name
        else:
            full_name = str(reg_no) + " " + student_name + ", " + str(form) + " " + class_name

        name_sizer = wx.BoxSizer(wx.VERTICAL)

        self.student_name_btn = wx.Button(self, wx.ID_ANY, full_name, wx.DefaultPosition, wx.DefaultSize,
                                          wx.NO_BORDER)
        self.student_name_btn.SetBackgroundColour(wx.Colour(255, 255, 255))

        name_sizer.Add(self.student_name_btn, 0, 0, 5)

        # self.user_id_hidden = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        # self.user_id_hidden.SetValue(str(user_id))
        # self.user_id_hidden.Hide()

        # name_sizer.Add(self.user_id_hidden, 0, wx.ALL, 5)

        self.separator_static_line = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.LI_HORIZONTAL)
        name_sizer.Add(self.separator_static_line, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        self.SetSizer(name_sizer)
        self.Layout()

        # Connect Events
        self.student_name_btn.Bind(wx.EVT_BUTTON, self.studentClicked)

    def __del__(self):
        pass

    def studentClicked(self, event):

        self.parent.getStudentIDClicked(self.user_id)






