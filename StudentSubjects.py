import wx
import wx.xrc

from db.get_subjects import getSubjectByID
from db.subject_selection import updateSubjectsTakenOneStudent

###########################################################################
# Class StudentSubjects
###########################################################################

class StudentSubjects(wx.Panel):

    def __init__(self, parent, student):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(419, 256),
                          style=wx.TAB_TRAVERSAL)

        self.student = student

        self.subjectsNames = []
        self.subjectsIDs = []
        subjects = student['subjects_taken']
        if subjects is not None and subjects != "":
            self.subjects_ids = subjects.split(",")

            for subject_id in self.subjects_ids:
                subject_dets = getSubjectByID(subject_id)
                self.subjectsNames.append(subject_dets['subject_name'])
                self.subjectsIDs.append(subject_dets['subject_id'])

        container = wx.BoxSizer(wx.VERTICAL)

        self.student_subjects_label = wx.StaticText(self, wx.ID_ANY, u"Drop Subject", wx.DefaultPosition,
                                                    wx.DefaultSize, wx.ALIGN_CENTRE)
        self.student_subjects_label.Wrap(-1)
        self.student_subjects_label.SetFont(wx.Font(12, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.student_subjects_label, 0, wx.ALL | wx.EXPAND, 10)

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        outer_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        sbSizer14 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Select Subject to drop"), wx.VERTICAL)

        select_subjectChoices = self.subjectsNames
        self.select_subject = wx.ComboBox(sbSizer14.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, select_subjectChoices, wx.CB_READONLY)
        sbSizer14.Add(self.select_subject, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 25)

        btnsSizer = wx.BoxSizer(wx.HORIZONTAL)

        btnsSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.cancel_btn = wx.Button(sbSizer14.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        btnsSizer.Add(self.cancel_btn, 0, 0, 5)

        self.drop_btn = wx.Button(sbSizer14.GetStaticBox(), wx.ID_ANY, u"Drop", wx.DefaultPosition, wx.DefaultSize, 0)
        btnsSizer.Add(self.drop_btn, 0, wx.LEFT | wx.RIGHT, 10)

        sbSizer14.Add(btnsSizer, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 15)

        outer_sizer.Add(sbSizer14, 1, wx.ALL | wx.EXPAND, 5)

        outer_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(outer_sizer, 0, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelDropSubject)
        self.drop_btn.Bind(wx.EVT_BUTTON, self.submitDropSubject)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancelDropSubject(self, event):
        self.select_subject.SetSelection(-1)

    def submitDropSubject(self, event):
        subjectIndex = self.select_subject.GetCurrentSelection()

        if subjectIndex == -1:
            dlg = wx.MessageDialog(None, "Select Subject to drop first.",
                                       'Warning Message.',
                                       wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
        else:
            subject_id = self.subjectsIDs[subjectIndex]
            print subjectIndex
            print self.subjectsIDs
            print subject_id

            original_subjects_ids = self.subjects_ids[:]

            # Remove id from array
            original_subjects_ids.remove(str(subject_id))

            # stringify the array in order to update in DB
            subjects_taken = ','.join(map(str, original_subjects_ids))

            if updateSubjectsTakenOneStudent(self.student['user_id'], subjects_taken):
                dlg = wx.MessageDialog(None, "Subject Dropped Successfully",
                                       'Success Message.',
                                       wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()

                self.cancelDropSubject("")
            else:
                dlg = wx.MessageDialog(None, "Dropping subject failed. Try again later.",
                                       'Warning Message.',
                                       wx.OK | wx.ICON_WARNING)
                dlg.ShowModal()



