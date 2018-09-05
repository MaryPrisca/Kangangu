import wx
import wx.xrc


###########################################################################
# Class SetupFormsClasses
###########################################################################


class SetupForms(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(743, 456),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.form_streams_label = wx.StaticText(self, wx.ID_ANY, u"Form Streams", wx.DefaultPosition, wx.DefaultSize,
                                                wx.ALIGN_CENTRE)
        self.form_streams_label.Wrap(-1)
        self.form_streams_label.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.form_streams_label, 0, wx.ALL | wx.EXPAND, 30)

        self.navigation_disclaimer = wx.StaticText( self, wx.ID_ANY, u"(Please use buttons to navigate)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.navigation_disclaimer.Wrap(-1)

        container.Add(self.navigation_disclaimer, 0, wx.ALL | wx.EXPAND, 5)

        content_Sizer = wx.BoxSizer(wx.HORIZONTAL)

        content_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        formSizer = wx.BoxSizer(wx.VERTICAL)

        formSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        bSizer260 = wx.BoxSizer(wx.HORIZONTAL)

        left_Sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.streams_disclaimer_one = wx.StaticText(left_Sizer.GetStaticBox(), wx.ID_ANY,
                                                    u"Enter all streams present in school. One by One.",
                                                    wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.streams_disclaimer_one.Wrap(-1)
        self.streams_disclaimer_one.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        left_Sizer.Add(self.streams_disclaimer_one, 0, wx.ALL | wx.EXPAND, 5)

        self.streams_disclaimer_two = wx.StaticText(left_Sizer.GetStaticBox(), wx.ID_ANY,
                                                    u"(Including those that might not be in all forms)",
                                                    wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.streams_disclaimer_two.Wrap(-1)
        self.streams_disclaimer_two.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        left_Sizer.Add(self.streams_disclaimer_two, 0, wx.ALL | wx.EXPAND, 5)

        self.stream_label = wx.StaticText(left_Sizer.GetStaticBox(), wx.ID_ANY, u"Stream Name", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.stream_label.Wrap(-1)
        left_Sizer.Add(self.stream_label, 0, wx.ALL, 5)

        self.stream_textfield = wx.TextCtrl(left_Sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.stream_textfield.SetToolTipString(u"Type one stream and click enter/Add to add, then continue")

        left_Sizer.Add(self.stream_textfield, 0, wx.ALL | wx.EXPAND, 5)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        btnSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.add_stream_btn = wx.Button(left_Sizer.GetStaticBox(), wx.ID_ANY, u"Add", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        btnSizer.Add(self.add_stream_btn, 0, wx.ALL, 5)

        left_Sizer.Add(btnSizer, 1, wx.EXPAND, 5)

        bSizer260.Add(left_Sizer, 1, wx.ALL | wx.EXPAND, 5)

        self.right_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.streams = []

        self.preview_panel = PreviewSetupForms(self, self.streams)
        self.preview_panel.Hide()
        self.right_sizer.Add(self.preview_panel, 1, wx.EXPAND, 5)

        bSizer260.Add(self.right_sizer, 1, wx.ALL | wx.EXPAND, 5)

        formSizer.Add(bSizer260, 1, wx.EXPAND, 5)

        formSizer.AddSpacer((0, 0), 5, wx.EXPAND, 5)

        content_Sizer.Add(formSizer, 7, wx.EXPAND, 5)

        content_Sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(content_Sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.stream_textfield.Bind(wx.EVT_TEXT_ENTER, self.streamAdded)
        self.add_stream_btn.Bind(wx.EVT_BUTTON, self.streamAdded)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def streamAdded(self, event):
        stream = self.stream_textfield.GetLineText(0)
        stream = stream.strip()

        # -----------  VALIDATION  -----------
        error = ""

        if stream == "":
            error = error + "Stream name cannot be blank.\n"
        else:
            if stream in self.streams:
                error = error + "A stream can only be entered once.\n"
            else:
                if len(stream) < 3:
                    error = error + "Enter full name of the stream.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
        else:
            self.streams.append(stream)

            self.stream_textfield.SetValue("")

            self.stream_textfield.SetFocus()

            self.refreshPreview("")

    def refreshPreview(self, event):
        self.preview_panel.Destroy()
        self.preview_panel = PreviewSetupForms(self, self.streams)
        self.right_sizer.Add(self.preview_panel, 1, wx.EXPAND, 5)

        self.Layout()


class PreviewSetupForms(wx.Panel):

    def __init__(self, parent, streams):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        self.parent = parent

        streams_list_sizer = wx.BoxSizer(wx.VERTICAL)

        self.preview_streams = {}

        for key, value in enumerate(streams):  # adding stream list dynamically
            self.preview_streams[str(key)] = OneStreamPanel(self, value)

            streams_list_sizer.Add(self.preview_streams[str(key)], 0, wx.EXPAND, 5)

        self.SetSizer(streams_list_sizer)
        self.Layout()

    def __del__(self):
        pass

    def removeStream(self, stream_name):
        self.parent.streams.remove(stream_name)

        self.parent.refreshPreview("")


class OneStreamPanel(wx.Panel):

    def __init__(self, parent, stream_name):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        self.parent = parent
        self.stream = stream_name

        streamSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.remove_btn = wx.BitmapButton(self, wx.ID_ANY,
                                          wx.Bitmap(u"images/minus_12x12.bmp", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, 0 | wx.NO_BORDER)
        streamSizer.Add(self.remove_btn, 0, wx.ALL, 6)

        self.stream_name = wx.StaticText(self, wx.ID_ANY, self.stream.lower().capitalize(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.stream_name.Wrap(-1)
        streamSizer.Add(self.stream_name, 0, wx.LEFT | wx.RIGHT | wx.TOP, 5)

        self.SetSizer(streamSizer)
        self.Layout()

        # Connect Events
        self.remove_btn.Bind(wx.EVT_BUTTON, self.removeButtonClicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def removeButtonClicked(self, event):
        self.parent.removeStream(self.stream)

