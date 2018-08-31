import wx
import wx.xrc


###########################################################################
# Class SetupClasses
###########################################################################

class SetupClasses(wx.Panel):

    def __init__(self, parent, form_streams):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(522, 459),
                          style=wx.TAB_TRAVERSAL)

        form_streams.insert(0, "No Streams")  # Add to top of list

        container = wx.BoxSizer(wx.VERTICAL)

        self.classes_title = wx.StaticText(self, wx.ID_ANY, u"Setup Classes", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.classes_title.Wrap(-1)
        self.classes_title.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.classes_title, 0, wx.ALL | wx.EXPAND, 30)

        self.navigation_disclaimer = wx.StaticText( self, wx.ID_ANY, u"(Please use buttons to navigate)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.navigation_disclaimer.Wrap(-1)

        container.Add(self.navigation_disclaimer, 0, wx.ALL | wx.EXPAND, 5)

        content_Sizer = wx.BoxSizer(wx.HORIZONTAL)

        content_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        formSizer = wx.BoxSizer(wx.VERTICAL)

        formSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.disclaimer = wx.StaticText(self, wx.ID_ANY, u"Select Streams in each Form", wx.DefaultPosition,
                                        wx.DefaultSize, wx.ALIGN_CENTRE)
        self.disclaimer.Wrap(-1)
        self.disclaimer.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer.Add(self.disclaimer, 0, wx.ALL | wx.EXPAND, 5)

        self.top_border_static_line = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                    wx.LI_HORIZONTAL)
        bSizer.Add(self.top_border_static_line, 0, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        wrapper_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.left_border_static_line = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                     wx.LI_VERTICAL)
        wrapper_sizer.Add(self.left_border_static_line, 0, wx.EXPAND | wx.LEFT, 5)

        left_sizer = wx.BoxSizer(wx.VERTICAL)

        form_one_sizer = wx.BoxSizer(wx.VERTICAL)

        self.form_one_label = wx.StaticText(self, wx.ID_ANY, u"Form 1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.form_one_label.Wrap(-1)
        self.form_one_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        form_one_sizer.Add(self.form_one_label, 1, wx.ALL | wx.EXPAND, 5)

        left_sizer.Add(form_one_sizer, 1, wx.EXPAND, 5)

        #

        self.fone_checkboxes = {}

        for key, value in enumerate(form_streams):
            self.fone_checkboxes[str(key)] = OneStreamCheckBox(self, value, 1)
            form_one_sizer.Add(self.fone_checkboxes[str(key)], 0, wx.EXPAND, 5)
        #
        #
        #

        form_three_sizer = wx.BoxSizer(wx.VERTICAL)

        self.form_three_label = wx.StaticText(self, wx.ID_ANY, u"Form 3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.form_three_label.Wrap(-1)
        self.form_three_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        form_three_sizer.Add(self.form_three_label, 0, wx.ALL, 5)

        #

        self.fthree_checkboxes = {}

        for key, value in enumerate(form_streams):
            self.fthree_checkboxes[str(key)] = OneStreamCheckBox(self, value, 3)
            form_three_sizer.Add(self.fthree_checkboxes[str(key)], 0, wx.EXPAND, 5)

        #
        #
        #

        left_sizer.Add(form_three_sizer, 1, wx.EXPAND| wx.TOP, 5)

        wrapper_sizer.Add(left_sizer, 2, wx.ALL | wx.EXPAND, 10)

        right_sizer = wx.BoxSizer(wx.VERTICAL)

        form_two_sizer = wx.BoxSizer(wx.VERTICAL)

        self.form_two_label = wx.StaticText(self, wx.ID_ANY, u"Form 2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.form_two_label.Wrap(-1)
        self.form_two_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        form_two_sizer.Add(self.form_two_label, 0, wx.ALL, 5)

        #

        self.ftwo_checkboxes = {}

        for key, value in enumerate(form_streams):
            self.ftwo_checkboxes[str(key)] = OneStreamCheckBox(self, value, 2)
            form_two_sizer.Add(self.ftwo_checkboxes[str(key)], 0, wx.EXPAND, 5)

        #
        #
        #

        right_sizer.Add(form_two_sizer, 1, wx.EXPAND, 5)

        form_four_sizer = wx.BoxSizer(wx.VERTICAL)

        self.form_four_label = wx.StaticText(self, wx.ID_ANY, u"Form 4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.form_four_label.Wrap(-1)
        self.form_four_label.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        form_four_sizer.Add(self.form_four_label, 0, wx.ALL, 5)

        right_sizer.Add(form_four_sizer, 1, wx.EXPAND | wx.TOP, 5)

        #

        self.ffour_checkboxes = {}

        for key, value in enumerate(form_streams):
            self.ffour_checkboxes[str(key)] = OneStreamCheckBox(self, value, 4)
            form_four_sizer.Add(self.ffour_checkboxes[str(key)], 0, wx.EXPAND, 5)

        #
        #
        #

        self.form_one_streams = []
        self.form_two_streams = []
        self.form_three_streams = []
        self.form_four_streams = []

        wrapper_sizer.Add(right_sizer, 1, wx.ALL | wx.EXPAND, 10)

        self.bottom_border_static_line = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                       wx.LI_VERTICAL)
        wrapper_sizer.Add(self.bottom_border_static_line, 0, wx.EXPAND | wx.RIGHT, 5)

        bSizer.Add(wrapper_sizer, 1, wx.EXPAND, 5)

        self.m_staticline18 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer.Add(self.m_staticline18, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        formSizer.Add(bSizer, 1, wx.EXPAND, 5)

        formSizer.AddSpacer((0, 0), 5, wx.EXPAND, 5)

        content_Sizer.Add(formSizer, 3, wx.EXPAND, 5)

        content_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(content_Sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

    def __del__(self):
        pass


class OneStreamCheckBox(wx.Panel):

    def __init__(self, parent, stream_name, form):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent
        self.stream_name = stream_name
        self.form = form

        checkbox_sizer = wx.BoxSizer(wx.VERTICAL)

        self.stream_name_checkbox = wx.CheckBox(self, wx.ID_ANY, stream_name, wx.DefaultPosition, wx.DefaultSize, 0)
        checkbox_sizer.Add(self.stream_name_checkbox, 0, wx.ALL, 5)

        self.SetSizer(checkbox_sizer)
        self.Layout()

        # Connect Events
        self.stream_name_checkbox.Bind(wx.EVT_CHECKBOX, self.streamClicked)

    def __del__(self):
        pass

    #
    # --------------------------------------------------
    def streamClicked(self, event):
        checked = self.stream_name_checkbox.IsChecked()
        stream = self.stream_name

        if checked:
            # If No Streams, Check that there are no other streams selected in respective form
            addStream = True
            if stream == "No Streams":
                if self.form == 1:
                    if len(self.parent.form_one_streams) > 0:
                        dlg = wx.MessageDialog(None, "Only select 'No Streams' if there are no other streams in form.", 'Validation Error', wx.OK | wx.ICON_WARNING)
                        dlg.ShowModal()
                        addStream = False
                if self.form == 2:
                    if len(self.parent.form_two_streams) > 0:
                        dlg = wx.MessageDialog(None, "Only select No streams if there are no other streams in form.", 'Validation Error', wx.OK | wx.ICON_WARNING)
                        dlg.ShowModal()
                        addStream = False
                if self.form == 3:
                    if len(self.parent.form_three_streams) > 0:
                        dlg = wx.MessageDialog(None, "Only select No streams if there are no other streams in form.", 'Validation Error', wx.OK | wx.ICON_WARNING)
                        dlg.ShowModal()
                        addStream = False
                if self.form == 4:
                    if len(self.parent.form_four_streams) > 0:
                        dlg = wx.MessageDialog(None, "Only select No streams if there are no other streams in form.", 'Validation Error', wx.OK | wx.ICON_WARNING)
                        dlg.ShowModal()
                        addStream = False
            else:
                # Check that no streams option hadn't been selected prior

                if self.form == 1:
                    if "No Streams" in self.parent.form_one_streams:
                        dlg = wx.MessageDialog(None, "Uncheck 'No Streams' in order to add streams.", 'Validation Error', wx.OK | wx.ICON_WARNING)
                        dlg.ShowModal()
                        addStream = False
                if self.form == 2:
                    if "No Streams" in self.parent.form_two_streams:
                        dlg = wx.MessageDialog(None, "Uncheck 'No Streams' in order to add streams.", 'Validation Error', wx.OK | wx.ICON_WARNING)
                        dlg.ShowModal()
                        addStream = False
                if self.form == 3:
                    if "No Streams" in self.parent.form_three_streams:
                        dlg = wx.MessageDialog(None, "Uncheck 'No Streams' in order to add streams.", 'Validation Error', wx.OK | wx.ICON_WARNING)
                        dlg.ShowModal()
                        addStream = False
                if self.form == 4:
                    if "No Streams" in self.parent.form_four_streams:
                        dlg = wx.MessageDialog(None, "Uncheck 'No Streams' in order to add streams.", 'Validation Error', wx.OK | wx.ICON_WARNING)
                        dlg.ShowModal()
                        addStream = False

            if addStream:
                self.addStreamToForm(stream, self.form)
            else:
                self.stream_name_checkbox.SetValue(False)

        else:
            self.removeStreamFromForm(stream, self.form)

    #
    # --------------------------------------------------
    def addStreamToForm(self, stream_name, form):
        if form == 1:
            self.parent.form_one_streams.append(stream_name)
        elif form == 2:
            self.parent.form_two_streams.append(stream_name)
        elif form == 3:
            self.parent.form_three_streams.append(stream_name)
        elif form == 4:
            self.parent.form_four_streams.append(stream_name)

    #
    # --------------------------------------------------
    def removeStreamFromForm(self, stream_name, form):
        # Fist confirm that the stream name is in list before trying to remove it
        # Because the no streams option can be unchecked without having been added

        if form == 1:
            self.parent.form_one_streams.remove(stream_name)

        elif form == 2:
            self.parent.form_two_streams.remove(stream_name)

        elif form == 3:
            self.parent.form_three_streams.remove(stream_name)

        elif form == 4:
            self.parent.form_four_streams.remove(stream_name)