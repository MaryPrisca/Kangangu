import wx
import wx.xrc

from db.get_classes import getClassNamesWithForm
from db.get_subjects import getOptionalSubjects, getNumberOfCompulsorySubjects
from db.subject_selection import *
from db.login import getSchoolDetails

###########################################################################
# Class SubjectSelection
###########################################################################


class SubjectSelection(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText98 = wx.StaticText(self, wx.ID_ANY, u"Subject Selection", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText98.Wrap(-1)
        self.m_staticText98.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText98, 0, wx.EXPAND | wx.TOP, 25)

        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_sizer = wx.BoxSizer(wx.VERTICAL)

        form_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Fill in the following details"), wx.VERTICAL)

        self.class_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Select Class", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.class_label.Wrap(-1)
        form_sizer.Add(self.class_label, 0, wx.ALL, 10)

        self.classes = getClassNamesWithForm()

        class_nameChoices = self.classes['names']

        self.class_name = wx.ComboBox(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, class_nameChoices, wx.CB_READONLY)
        form_sizer.Add(self.class_name, 0, wx.ALL | wx.EXPAND, 10)

        self.subject_label = wx.StaticText(form_sizer.GetStaticBox(), wx.ID_ANY, u"Select Subject", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.subject_label.Wrap(-1)
        form_sizer.Add(self.subject_label, 0, wx.ALL, 10)

        self.subjects = getOptionalSubjects()

        subjectChoices = self.subjects['names']
        self.subject = wx.ComboBox(form_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, subjectChoices, wx.CB_READONLY)
        form_sizer.Add(self.subject, 0, wx.ALL | wx.EXPAND, 10)

        btns_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.cancel_button = wx.Button(form_sizer.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        btns_sizer.Add(self.cancel_button, 0, wx.TOP, 10)

        self.get_list_btn = wx.Button(form_sizer.GetStaticBox(), wx.ID_ANY, u"Get Student List", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        btns_sizer.Add(self.get_list_btn, 0, wx.TOP, 10)

        form_sizer.Add(btns_sizer, 1, wx.ALL | wx.EXPAND, 10)

        left_sizer.Add(form_sizer, 1, wx.LEFT | wx.TOP | wx.RIGHT | wx.EXPAND, 30)

        horizontal_sizer.Add(left_sizer, 0, wx.ALL | wx.EXPAND, 5)

        right_sizer = wx.BoxSizer(wx.HORIZONTAL)

        #
        #
        #  ADD SELECTION PANEL
        self.selection_panel_added = 0

        self.selection_sizer = wx.BoxSizer(wx.VERTICAL)

        sample_data = {
            "class_id": 0,
            "class_name": "",
            "subject_id": 0,
            "subject_name": "",
        }

        self.selection_panel = SelectionPanel(self, [], sample_data)
        self.selection_panel.Hide()

        self.selection_sizer.Add(self.selection_panel, 1, wx.ALL, 5)

        right_sizer.Add(self.selection_sizer, 1, wx.EXPAND, 5)
        #
        #
        # ------------------------------------------------------

        #
        #
        #  ADD PREVIEW PANEL
        self.preview_sizer = wx.BoxSizer(wx.VERTICAL)

        self.preview_panel = PreviewPanel(self, [], sample_data)
        self.preview_panel.Hide()

        self.preview_sizer.Add(self.preview_panel, 1, wx.ALL, 5)

        right_sizer.Add(self.preview_sizer, 1, wx.EXPAND, 5)
        #
        #
        # ------------------------------------------------------

        #
        horizontal_sizer.Add(right_sizer, 1, wx.EXPAND, 5)

        container.Add(horizontal_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.class_name.Bind(wx.EVT_COMBOBOX, self.classChanged)
        self.subject.Bind(wx.EVT_COMBOBOX, self.subjectChanged)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.cancelSubjectSelection)
        self.get_list_btn.Bind(wx.EVT_BUTTON, self.getStudentList)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def classChanged(self, event):  # To reload student list if class is changed when a list has already been loaded
        subjectIndex = self.subject.GetCurrentSelection()
        if subjectIndex != -1:
            self.getStudentList("")

            self.Layout()

    # -------------------------------------
    def subjectChanged(self, event):
        classIndex = self.class_name.GetCurrentSelection()
        if classIndex != -1:  # To reload student list if subject is changed when a list has already been loaded
            self.getStudentList("")

            self.Layout()

    # -------------------------------------
    def cancelSubjectSelection(self, event):
        self.class_name.SetSelection(-1)
        self.subject.SetSelection(-1)

        self.selection_panel.Hide()
        self.preview_panel.Hide()

    # -------------------------------------
    def getStudentList(self, event):
        classIndex = self.class_name.GetCurrentSelection()
        subjectIndex = self.subject.GetCurrentSelection()

        error = ""

        if classIndex == -1:
            error = error + "The class field is required.\n"
        if subjectIndex == -1:
            error = error + "The subject field is required.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        else:
            class_id = self.classes['ids'][classIndex]
            form = self.classes['forms'][classIndex]
            class_name = self.class_name.GetStringSelection()
            subject_id = self.subjects['ids'][subjectIndex]
            subject_name = self.subject.GetStringSelection()

            students = getStudentList(class_id, subject_id)
            preview_students = students['students_present']
            selection_students = students['student_list']

            # Calculate the limit of subject choices
            schDets = getSchoolDetails()

            # Get number of compulsory subjects in system
            compulsory_subjects = getNumberOfCompulsorySubjects(form)

            # Subjects must be 8 for upper forms, for lower forms we get from the system
            if int(form) < 3:
                # Get number of subjects done by lower forms
                subjects_lower_forms = schDets['lower_subjects']
                subject_limit = int(subjects_lower_forms) - compulsory_subjects

            else:
                subject_limit = 8 - int(compulsory_subjects)

            data = {
                "class_id": class_id,
                "class_name": class_name,
                "subject_id": subject_id,
                "subject_name": subject_name,
                "subject_limit": subject_limit
            }

            self.selection_panel.Hide()
            self.selection_panel = SelectionPanel(self, selection_students, data)
            self.selection_panel.Show()

            self.selection_sizer.Add(self.selection_panel, 1, wx.ALL, 5)

            self.Layout()

            #
            #

            self.preview_panel.Hide()
            self.preview_panel = PreviewPanel(self, preview_students, data)
            self.preview_panel.Show()

            self.preview_sizer.Add(self.preview_panel, 1, wx.ALL, 5)

            self.Layout()

    # -------------------------------------
    def reRenderPreviewPanel(self, data):

        if data in self.preview_panel.preview_students:  # If it's there remove it
            self.preview_panel.preview_students.remove(data)
        else:
            self.preview_panel.preview_students.append(data)  # If not it's added

        # Re-render the panel
        self.preview_panel.Hide()
        self.preview_panel = PreviewPanel(self, self.preview_panel.preview_students, self.preview_panel.data)
        self.preview_panel.Show()

        self.preview_sizer.Add(self.preview_panel, 1, wx.ALL, 5)

        self.Layout()


#
#
class SelectionPanel(wx.Panel):

    def __init__(self, parent, students, data):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        self.parent = parent
        self.students = students
        self.data = data

        self.subject_id = self.data['subject_id']

        self.title = "Form " + self.data['class_name'] + "          Tick student to add to the " + self.data['subject_name'] + " option"

        container = wx.BoxSizer(wx.VERTICAL)

        titles_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.spacer.Wrap(-1)
        titles_sizer.Add(self.spacer, 0, wx.ALL, 5)

        self.title_text = wx.StaticText(self, wx.ID_ANY, self.title, wx.DefaultPosition, wx.DefaultSize, 0)
        self.title_text.Wrap(-1)
        self.title_text.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))
        titles_sizer.Add(self.title_text, 0, wx.ALL, 5)

        container.Add(titles_sizer, 0, wx.EXPAND, 5)

        #
        #
        #

        student_list = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.student_fields = {}
        for key, value in enumerate(self.students):  # adding student list dynamically
            self.student_fields[str(value['user_id'])] = OneStudent(self, value['student_name'], value['user_id'], value['subject_ticked'], value['subjects'])
            student_list.Add(self.student_fields[str(value['user_id'])], 0, wx.EXPAND, 5)

        self.buttons = SaveSubjectsChosenButtons(self)
        student_list.Add(self.buttons, 1, wx.EXPAND, 5)

        container.Add(student_list, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

    def __del__(self):
        pass

    def callRenderPreviewPanel(self, data):
        self.parent.reRenderPreviewPanel(data)

    def cancelChosenSubjects(self, event):
        self.parent.cancelSubjectSelection("")

    def saveChosenSubjects(self, event):
        student_data = self.student_fields

        subject_id = self.subject_id

        stud_subject_data = []

        for (key, value) in student_data.iteritems():

            # Check if subjects had been chosen before, ie the subjects array is not empty
            if value.subjects != "":

                # If subject chosen is already saved in db so it's already ticked
                if value.subjects.count(str(subject_id)) != 0:

                    # check if subject has been de-selected
                    if not value.selected.GetValue():  # Subject has been de-selected
                        # print "remove subject - " + value.student_name
                        subjects_taken = value.subjects[:]

                        subjects_taken.remove(str(subject_id))

                        data = {
                            "user_id": key,
                            "subject_taken": subjects_taken
                        }

                        stud_subject_data.append(data)

                else:  # if subject is new to subjects array, ie needs to be added

                    # check that all slots aren't filled, ie if the student needs to drop one first
                    if len(value.subjects) < 4:
                        # print "add to array - " + value.student_name

                        # Add to array if subject got ticked ie value.selected == True
                        if value.selected.GetValue():
                            subjects_taken = value.subjects[:]  # Copy value.subjects to new array
                            subjects_taken.append(subject_id)

                            data = {
                                "user_id": key,
                                "subject_taken": subjects_taken
                            }

                            stud_subject_data.append(data)
            else:
                # print "add first subject - " + value.student_name

                # Add first subject if it got ticked ie value.selected == True
                if value.selected.GetValue():

                    subjects_taken = [subject_id]

                    data = {
                        "user_id": key,
                        "subject_taken": subjects_taken
                    }

                    stud_subject_data.append(data)

        # Check if there's data to be updated
        if stud_subject_data:
            dlg = wx.MessageDialog(None, "Save changes?", 'Confirm Action.',
                                   wx.YES_NO | wx.ICON_INFORMATION)
            retCode = dlg.ShowModal()

            if retCode == wx.ID_YES:
                if chooseSubjects(stud_subject_data):
                    dlg = wx.MessageDialog(None, "Students' subjects updated successfully.",
                                           'Success Message.',
                                           wx.OK | wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    dlg.Destroy()
                    self.cancelChosenSubjects("")
                else:
                    dlg = wx.MessageDialog(None, "Some students' subjects may not have been saved. Try again later.",
                                           'Warning Message.',
                                           wx.OK | wx.ICON_WARNING)
                    dlg.ShowModal()
                    dlg.Destroy()
            else:
                dlg.Close()
            dlg.Destroy()


#
#
# Called for every student in the selection list. == one list item
class OneStudent(wx.Panel):

    def __init__(self, parent, student_name, user_id, subject_ticked, subjects):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        self.parent = parent
        self.student_name = student_name
        self.user_id = user_id
        self.subject_ticked = subject_ticked
        self.subjects = subjects

        student_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.selected = wx.CheckBox(self, wx.ID_ANY, "  " + self.student_name, wx.DefaultPosition, wx.DefaultSize, 0)
        self.selected.SetValue(self.subject_ticked)
        student_name_sizer.Add(self.selected, 0, wx.ALL, 5)

        self.SetSizer(student_name_sizer)
        self.Layout()

        self.selected.Bind(wx.EVT_CHECKBOX, self.checkboxClicked)

    def __del__(self):
        pass

    # If there's no slot to add subject, and the subject in question isn't in array so one needs to be dropped first
    def checkboxClicked(self, event):
        if len(self.subjects) == self.parent.data['subject_limit'] and self.subjects.count(str(self.parent.subject_id)) == 0:
            dlg = wx.MessageDialog(None, "Maximum number of subjects chosen for student, drop some to continue.",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()

            self.selected.SetValue(False)
        else:
            """Add/remove from preview panel"""
            data = {
                "user_id": self.user_id,
                "student_name": self.student_name
            }

            self.parent.callRenderPreviewPanel(data)


#
#
class SaveSubjectsChosenButtons(wx.Panel):

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
        btns_sizer.Add(self.right_spacer, 1, wx.ALL, 5)

        self.SetSizer(btns_sizer)
        self.Layout()

        # Connect Events
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.parent.cancelChosenSubjects)
        self.save_button.Bind(wx.EVT_BUTTON, self.parent.saveChosenSubjects)


#
#
class PreviewPanel(wx.Panel):
    def __init__(self, parent, preview_students, data):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        self.preview_students = preview_students
        self.data = data

        self.subject_id = self.data['subject_id']

        self.title = "Form " + self.data['class_name'] + "   " + self.data['subject_name'] + " option students"

        container = wx.BoxSizer(wx.VERTICAL)

        titles_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.spacer.Wrap(-1)
        titles_sizer.Add(self.spacer, 1, wx.ALL, 5)

        self.title_text = wx.StaticText(self, wx.ID_ANY, self.title, wx.DefaultPosition, wx.DefaultSize, 0)
        self.title_text.Wrap(-1)
        self.title_text.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))
        titles_sizer.Add(self.title_text, 1, wx.ALL, 5)

        self.spacer = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.spacer.Wrap(-1)
        titles_sizer.Add(self.spacer, 1, wx.ALL, 5)

        container.Add(titles_sizer, 0, wx.EXPAND, 5)

        #
        #
        #

        student_list = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.preview_student_fields = {}

        count = 1

        for key, value in enumerate(self.preview_students):  # adding student list dynamically
            self.preview_student_fields[str(value['user_id'])] = OnePreviewStudent(self, str(count) + ". " + value['student_name'])

            student_list.Add(self.preview_student_fields[str(value['user_id'])], 0, wx.EXPAND, 5)

            count = count + 1

        # self.buttons = SaveSubjectsChosenButtons(self)
        # student_list.Add(self.buttons, 1, wx.EXPAND, 5)

        container.Add(student_list, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

    def __del__(self):
        pass


#
# Called for every student in the preview list. == one list item
class OnePreviewStudent(wx.Panel):

    def __init__(self, parent, student_name):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        self.parent = parent
        self.student_name = student_name

        student_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.student_text = wx.StaticText(self, wx.ID_ANY, self.student_name, wx.DefaultPosition, wx.DefaultSize, 0)
        self.student_text.Wrap(-1)
        student_name_sizer.Add(self.student_text, 0, wx.ALL, 5)

        self.SetSizer(student_name_sizer)
        self.Layout()

    def __del__(self):
        pass