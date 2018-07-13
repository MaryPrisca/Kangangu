import wx
import wx.xrc

from db.save_marks import saveMarks


class MarksForm(wx.Panel):

    def __init__(self, parent, students, exam_details):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(623, 482),
                          style=wx.TAB_TRAVERSAL)  # | wx.VSCROLL

        self.parent = parent
        self.students = students

        self.exam_title = exam_details

        self.exam_period = str(self.exam_title['year']) + ", Term " + self.exam_title['term']
        self.exam_name = self.exam_title['exam_name']
        self.subject = self.exam_title['subject']
        self.teacher = self.parent.userdata['first_name'] + " " + self.parent.userdata['surname']
        self.class_name_title = str(self.exam_title['form']) + " " + self.exam_title['class']

        outer_sizer = wx.BoxSizer(wx.VERTICAL)

        top_titles_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.titles_left_spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.titles_left_spacer.Wrap(-1)
        top_titles_sizer.Add(self.titles_left_spacer, 1, wx.ALL, 5)

        titles_content_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_titles = wx.BoxSizer(wx.VERTICAL)

        class_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.class_label = wx.StaticText(self, wx.ID_ANY, u"Class:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.class_label.Wrap(-1)
        self.class_label.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        class_sizer.Add(self.class_label, 1, wx.ALL, 5)

        self.class_name = wx.StaticText(self, wx.ID_ANY, self.class_name_title, wx.DefaultPosition, wx.DefaultSize, 0)
        self.class_name.Wrap(-1)
        self.class_name.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))

        class_sizer.Add(self.class_name, 2, wx.ALL, 5)

        left_titles.Add(class_sizer, 1, wx.EXPAND, 5)

        exam_period_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.exam_period_label = wx.StaticText(self, wx.ID_ANY, u"Exam Period:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.exam_period_label.Wrap(-1)
        self.exam_period_label.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        exam_period_sizer.Add(self.exam_period_label, 1, wx.ALL, 5)

        self.exam_period = wx.StaticText(self, wx.ID_ANY, self.exam_period, wx.DefaultPosition, wx.DefaultSize, 0)
        self.exam_period.Wrap(-1)
        self.exam_period.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))

        exam_period_sizer.Add(self.exam_period, 2, wx.ALL, 5)

        left_titles.Add(exam_period_sizer, 0, wx.EXPAND, 5)

        exam_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.exam_name_label = wx.StaticText(self, wx.ID_ANY, u"Exam Name:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.exam_name_label.Wrap(-1)
        self.exam_name_label.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        exam_name_sizer.Add(self.exam_name_label, 1, wx.ALL, 5)

        self.exam_name = wx.StaticText(self, wx.ID_ANY, self.exam_name, wx.DefaultPosition, wx.DefaultSize, 0)
        self.exam_name.Wrap(-1)
        self.exam_name.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))

        exam_name_sizer.Add(self.exam_name, 2, wx.ALL, 5)

        left_titles.Add(exam_name_sizer, 0, wx.EXPAND, 5)

        titles_content_sizer.Add(left_titles, 1, wx.EXPAND, 5)

        right_titles = wx.BoxSizer(wx.VERTICAL)

        subject_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.subject_label = wx.StaticText(self, wx.ID_ANY, u"Subject:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.subject_label.Wrap(-1)
        self.subject_label.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        subject_sizer.Add(self.subject_label, 1, wx.ALL, 5)

        self.subject_name = wx.StaticText(self, wx.ID_ANY, self.subject, wx.DefaultPosition, wx.DefaultSize, 0)
        self.subject_name.Wrap(-1)
        self.subject_name.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))

        subject_sizer.Add(self.subject_name, 2, wx.ALL, 5)

        right_titles.Add(subject_sizer, 1, wx.EXPAND, 5)

        teacher_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.teacher_label = wx.StaticText(self, wx.ID_ANY, u"Teacher:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.teacher_label.Wrap(-1)
        self.teacher_label.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        teacher_sizer.Add(self.teacher_label, 1, wx.ALL, 5)

        self.teacher_name = wx.StaticText(self, wx.ID_ANY, self.teacher, wx.DefaultPosition, wx.DefaultSize, 0)
        self.teacher_name.Wrap(-1)
        self.teacher_name.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))

        teacher_sizer.Add(self.teacher_name, 2, wx.ALL, 5)

        right_titles.Add(teacher_sizer, 1, wx.EXPAND, 5)

        titles_content_sizer.Add(right_titles, 1, wx.EXPAND, 5)

        top_titles_sizer.Add(titles_content_sizer, 4, wx.EXPAND, 5)

        self.titles_right_spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.titles_right_spacer.Wrap(-1)
        top_titles_sizer.Add(self.titles_right_spacer, 1, wx.ALL, 5)

        outer_sizer.Add(top_titles_sizer, 0, wx.ALL | wx.EXPAND, 5)

        container = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer10 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Student List"), wx.HORIZONTAL)

        form_sizer = wx.BoxSizer(wx.VERTICAL)

        self.exam_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TAB_TRAVERSAL)
        exam_id_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.exam_id_label = wx.StaticText(self.exam_panel, wx.ID_ANY, u"Exam ID", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.exam_id_label.Wrap(-1)
        exam_id_sizer.Add(self.exam_id_label, 3, wx.ALL, 5)

        self.exam_id = wx.TextCtrl(self.exam_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        exam_id_sizer.Add(self.exam_id, 0, wx.ALL, 5)
        self.exam_id.SetValue(str(self.exam_title['exam_id']))

        self.spacer = wx.StaticText(self.exam_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.spacer.Wrap(-1)
        exam_id_sizer.Add(self.spacer, 2, wx.ALL, 5)

        self.exam_panel.SetSizer(exam_id_sizer)
        self.exam_panel.Layout()
        exam_id_sizer.Fit(self.exam_panel)
        self.exam_panel.Hide()
        form_sizer.Add(self.exam_panel, 0, wx.EXPAND | wx.ALL, 5)

        #
        #
        #

        self.subject_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TAB_TRAVERSAL)
        subject_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.subject_label = wx.StaticText(self.subject_panel, wx.ID_ANY, u"Subject", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.subject_label.Wrap(-1)
        subject_sizer.Add(self.subject_label, 3, wx.ALL, 5)

        self.subject_alias = wx.TextCtrl(self.subject_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        subject_sizer.Add(self.subject_alias, 0, wx.ALL, 5)
        self.subject_alias.SetValue(self.exam_title['subject'])

        self.spacer = wx.StaticText(self.subject_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.spacer.Wrap(-1)
        subject_sizer.Add(self.spacer, 2, wx.ALL, 5)

        self.subject_panel.SetSizer(subject_sizer)
        self.subject_panel.Layout()
        subject_sizer.Fit(self.subject_panel)
        self.subject_panel.Hide()
        form_sizer.Add(self.subject_panel, 0, wx.EXPAND | wx.ALL, 5)

        #
        #
        # ------------------------ Add Student list ------------------------
        #
        #

        self.student_fields = {}
        for i, val in enumerate(self.students):  # adding student list dynamically
            self.student_fields[str(val['user_id'])] = StudentMarks(self, val['names'], val['mark'], val['result_id'])
            form_sizer.Add(self.student_fields[str(val['user_id'])], 0, wx.EXPAND | wx.ALL, 5)

        self.saveButtons = SaveMarksButtons(self)
        form_sizer.Add(self.saveButtons, 0, wx.EXPAND | wx.ALL, 5)

        #
        #
        #

        sbSizer10.Add(form_sizer, 1, wx.EXPAND, 5)

        container.Add(sbSizer10, 5, wx.ALL | wx.EXPAND, 15)

        outer_sizer.Add(container, 1, wx.EXPAND, 5)

        self.SetSizer(outer_sizer)
        self.Layout()

    def __del__(self):
        pass

    def cancelAddMarksForm(self, event):
        """"""

    def saveMarks(self, event):
        exam_id = self.exam_id.GetLineText(0)
        subject = self.subject_alias.GetLineText(0)

        student_data = self.student_fields

        update_data = {}
        insert_data = {}

        # k = user_id which = student_id in exam_results
        # v - to access the fields in each student row
        for (k, v) in student_data.iteritems():

            # separate students whose results are being updated and new ones
            if v.result_id.GetLineText(0) == "0":  # new record: exam_id, student_id, mark, subject which = column
                data = {
                    'exam_id': exam_id,
                    'student_id': k,
                    'mark': v.mark.GetLineText(0),
                    'subject': subject
                }

                insert_data[str(k)] = data

            else:  # to be updated, only exam_result_id, subject_alias which is the column name & mark needed
                data = {
                    'exam_result_id': v.result_id.GetLineText(0),
                    'mark': v.mark.GetLineText(0),
                    'subject': subject
                }
                update_data[str(k)] = data

        if saveMarks(insert_data, update_data):
            dlg = wx.MessageDialog(None, "Marks Entered Successfully.", 'Success Message',
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
        else:
            dlg = wx.MessageDialog(None, "Some marks may not have been saved, Confirm before exit.", 'Warning',
                                   wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()


class StudentMarks(wx.Panel):

    def __init__(self, parent, student_name, mark, result_id):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent
        self.student_name = student_name
        self.exam_mark = mark
        self.exam_result_id = result_id

        student_mark_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.student_name = wx.StaticText(self, wx.ID_ANY, self.student_name, wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.student_name.Wrap(-1)
        student_mark_sizer.Add(self.student_name, 3, wx.TOP, 1)

        self.mark = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        student_mark_sizer.Add(self.mark, 0, wx.TOP, 1)
        self.mark.SetValue(str(self.exam_mark))  # In case the field already had a mark entered

        self.result_id = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        # To get the result_id for update if the field already had a mark entered
        self.result_id.SetValue(str(self.exam_result_id))
        self.result_id.Hide()
        student_mark_sizer.Add(self.result_id, 0, wx.TOP, 1)

        self.spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.spacer.Wrap(-1)
        student_mark_sizer.Add(self.spacer, 2, wx.TOP, 1)

        self.SetSizer(student_mark_sizer)
        self.Layout()

        # Connect Events
        # self.marks.Bind(wx.EVT_COMBOBOX, self.parent.formSelected)


class SaveMarksButtons(wx.Panel):

            def __init__(self, parent):
                wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                                  style=wx.TAB_TRAVERSAL)
                self.parent = parent

                btns_sizer = wx.BoxSizer(wx.HORIZONTAL)

                self.left_spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
                self.left_spacer.Wrap(-1)
                btns_sizer.Add(self.left_spacer, 4, wx.ALL, 5)

                self.cancel_btn = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                            0)
                btns_sizer.Add(self.cancel_btn, 0, wx.ALL, 5)

                self.save_button = wx.Button(self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
                btns_sizer.Add(self.save_button, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 5)

                self.right_spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
                self.right_spacer.Wrap(-1)
                btns_sizer.Add(self.right_spacer, 3, wx.ALL, 5)

                self.SetSizer(btns_sizer)
                self.Layout()

                # Connect Events
                self.cancel_btn.Bind(wx.EVT_BUTTON, self.parent.cancelAddMarksForm)
                self.save_button.Bind(wx.EVT_BUTTON, self.parent.saveMarks)