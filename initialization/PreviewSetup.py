import wx
import wx.xrc


###########################################################################
# Class PreviewSetup
###########################################################################

class PreviewSetup(wx.Panel):

    def __init__(self, parent, setup_data):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(654, 436),
                          style=wx.TAB_TRAVERSAL)

        form_one = setup_data['class_names'][0]
        form_one_classes = ""
        for form in form_one:
            form_one_classes = form_one_classes + form.lower().capitalize() + "\n"

        form_two = setup_data['class_names'][1]
        form_two_classes = ""
        for form in form_two:
            form_two_classes = form_two_classes + form.lower().capitalize() + "\n"

        form_three = setup_data['class_names'][2]
        form_three_classes = ""
        for form in form_three:
            form_three_classes = form_three_classes + form.lower().capitalize() + "\n"

        form_four = setup_data['class_names'][3]
        form_four_classes = ""
        for form in form_four:
            form_four_classes = form_four_classes + form.lower().capitalize() + "\n"

        subject_data = setup_data['subjects']
        subjects = ""
        count = 1
        for subject in subject_data:
            subjects =  subjects + str(count) + ". " + subject['name'] + " - " + subject['alias'] + "\n"
            count = count+1

        container = wx.BoxSizer(wx.VERTICAL)

        self.school_subjects_label = wx.StaticText(self, wx.ID_ANY, u"Preview Setup", wx.DefaultPosition,
                                                   wx.DefaultSize, wx.ALIGN_CENTRE)
        self.school_subjects_label.Wrap(-1)
        self.school_subjects_label.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.school_subjects_label, 0, wx.ALL | wx.EXPAND, 25)

        content = wx.BoxSizer(wx.HORIZONTAL)

        content.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        sbSizer20 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        content_sizer = wx.BoxSizer(wx.VERTICAL)

        self.school_name_label = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"School Name", wx.DefaultPosition,
                                               wx.DefaultSize, wx.ALIGN_CENTRE)
        self.school_name_label.Wrap(-1)
        self.school_name_label.SetFont(wx.Font(11, 70, 90, 92, False, wx.EmptyString))

        content_sizer.Add(self.school_name_label, 0, wx.BOTTOM | wx.EXPAND, 5)

        self.sch_name_static_line = wx.StaticLine( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        content_sizer.Add(self.sch_name_static_line, 0, wx.EXPAND | wx.ALL, 5)

        self.school_name_text = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, setup_data['school_name'].upper(), wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.school_name_text.Wrap(-1)
        content_sizer.Add(self.school_name_text, 0, wx.BOTTOM | wx.LEFT, 15)

        self.classes_label = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"Classes", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_CENTRE)
        self.classes_label.Wrap(-1)
        self.classes_label.SetFont(wx.Font(11, 70, 90, 92, False, wx.EmptyString))

        content_sizer.Add(self.classes_label, 0, wx.BOTTOM | wx.EXPAND, 5)

        self.classes_static_line = wx.StaticLine( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        content_sizer.Add( self.classes_static_line, 0, wx.EXPAND|wx.ALL, 5 )

        wrapper_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_sizer = wx.BoxSizer(wx.VERTICAL)

        form_one_sizer = wx.BoxSizer(wx.VERTICAL)

        self.form_one_label = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"Form 1", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.form_one_label.Wrap(-1)
        self.form_one_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        form_one_sizer.Add(self.form_one_label, 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.form_one_classes = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, form_one_classes, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.form_one_classes.Wrap(-1)
        form_one_sizer.Add(self.form_one_classes, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        left_sizer.Add(form_one_sizer, 1, wx.EXPAND, 5)

        form_three_sizer = wx.BoxSizer(wx.VERTICAL)

        self.form_three_label = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"Form 3", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.form_three_label.Wrap(-1)
        self.form_three_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        form_three_sizer.Add(self.form_three_label, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.form_three_classes = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, form_three_classes, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.form_three_classes.Wrap(-1)
        form_three_sizer.Add(self.form_three_classes, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        left_sizer.Add(form_three_sizer, 1, wx.EXPAND | wx.TOP, 5)

        wrapper_sizer.Add(left_sizer, 2, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 10 )

        right_sizer = wx.BoxSizer(wx.VERTICAL)

        form_two_sizer = wx.BoxSizer(wx.VERTICAL)

        self.form_two_label = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"Form 2", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.form_two_label.Wrap(-1)
        self.form_two_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        form_two_sizer.Add(self.form_two_label, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.form_two_classes = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, form_two_classes, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.form_two_classes.Wrap(-1)
        form_two_sizer.Add(self.form_two_classes, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        right_sizer.Add(form_two_sizer, 1, wx.EXPAND, 5)

        form_four_sizer = wx.BoxSizer(wx.VERTICAL)

        self.form_four_label = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"Form 4", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.form_four_label.Wrap(-1)
        self.form_four_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        form_four_sizer.Add(self.form_four_label, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.form_four_classes = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, form_four_classes, wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.form_four_classes.Wrap(-1)
        form_four_sizer.Add(self.form_four_classes, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        right_sizer.Add(form_four_sizer, 1, wx.EXPAND | wx.TOP, 5)

        wrapper_sizer.Add(right_sizer, 1, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 10 )

        content_sizer.Add(wrapper_sizer, 0, wx.EXPAND, 5)

        self.subjects_label = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, u"Subjects", wx.DefaultPosition,
                                            wx.DefaultSize, wx.ALIGN_CENTRE)
        self.subjects_label.Wrap(-1)
        self.subjects_label.SetFont(wx.Font(11, 70, 90, 92, False, wx.EmptyString))

        content_sizer.Add(self.subjects_label, 0, wx.EXPAND | wx.ALL, 5)

        self.subjects_static_line = wx.StaticLine( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        content_sizer.Add(self.subjects_static_line, 0, wx.EXPAND | wx.ALL, 5)

        self.subjects_list = wx.StaticText(sbSizer20.GetStaticBox(), wx.ID_ANY, subjects, wx.DefaultPosition,
                                           wx.DefaultSize, wx.TE_MULTILINE)
        self.subjects_list.Wrap(-1)
        content_sizer.Add(self.subjects_list, 0, wx.LEFT, 15 )

        sbSizer20.Add(content_sizer, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 50)

        content.Add(sbSizer20, 2, wx.EXPAND | wx.BOTTOM, 20)

        content.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(content, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

    def __del__(self):
        pass


