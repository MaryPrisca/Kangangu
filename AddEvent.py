import wx
import wx.xrc

from datetime import datetime

from db.save_event import saveEvent

###########################################################################
# Class AddEvent
###########################################################################


class AddEvent(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(579, 436),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.add_events_title = wx.StaticText(self, wx.ID_ANY, u"Add New Event", wx.DefaultPosition, wx.DefaultSize,
                                              wx.ALIGN_CENTRE)
        self.add_events_title.Wrap(-1)
        self.add_events_title.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.add_events_title, 0, wx.ALL | wx.EXPAND, 25)

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        outer_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        outer_form_sizer = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Add Event Form"), wx.VERTICAL)

        event_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.event_name_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Event Name", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.event_name_label.Wrap(-1)
        event_name_sizer.Add(self.event_name_label, 1, wx.ALL, 10)

        self.event_name = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)

        event_name_sizer.Add(self.event_name, 4, wx.ALL, 10)

        sbSizer2.Add(event_name_sizer, 1, wx.ALL | wx.EXPAND, 10)

        event_date_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.event_date_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Event Date", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.event_date_label.Wrap(-1)
        event_date_sizer.Add(self.event_date_label, 1, wx.ALL, 10)

        self.event_date = wx.DatePickerCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                            wx.DefaultSize, wx.DP_DEFAULT | wx.DP_DROPDOWN)
        event_date_sizer.Add(self.event_date, 4, wx.ALL, 10)

        sbSizer2.Add(event_date_sizer, 1, wx.ALL | wx.EXPAND, 10)

        events_desc_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.event_desc_label = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Description", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.event_desc_label.Wrap(-1)
        events_desc_sizer.Add(self.event_desc_label, 1, wx.ALL, 10)

        self.event_desc = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_MULTILINE)
        events_desc_sizer.Add(self.event_desc, 4, wx.ALL, 10)

        sbSizer2.Add(events_desc_sizer, 1, wx.ALL | wx.EXPAND, 10)

        btns_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        btns_sizer.Add(self.m_staticText22, 1, wx.ALL, 5)

        self.cancel_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        btns_sizer.Add(self.cancel_btn, 0, wx.ALL, 10)

        self.save_event = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        btns_sizer.Add(self.save_event, 0, wx.ALL, 10)

        sbSizer2.Add(btns_sizer, 3, wx.ALL | wx.EXPAND, 10)

        outer_form_sizer.Add(sbSizer2, 0, 0, 50)

        self.m_staticText301 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText301.Wrap(-1)
        self.m_staticText301.SetFont(wx.Font(30, 70, 90, 90, False, wx.EmptyString))

        outer_form_sizer.Add(self.m_staticText301, 0, wx.ALL | wx.EXPAND, 5)

        outer_sizer.Add(outer_form_sizer, 1, wx.ALL | wx.EXPAND, 5)

        outer_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        container.Add(outer_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.cancelAddEvent)
        self.save_event.Bind(wx.EVT_BUTTON, self.saveEvent)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancelAddEvent(self, event):
        self.event_name.SetValue("")
        self.event_desc.SetValue("")

        td = datetime.today()

        # get wxPython datetime format
        day = td.day
        month = td.month
        year = td.year

        # -1 because the month counts from 0, whereas people count January as month #1.
        tdFormatted = wx.DateTimeFromDMY(day, month - 1, year)

        self.event_date.SetValue(tdFormatted)

    def saveEvent(self, event):
        self.save_event.Enable(False)

        event_name = self.event_name.GetValue()
        event_date = self.event_date.GetValue()
        event_desc = self.event_desc.GetValue()

        # ---------- VALIDATION ----------
        error = ""

        if event_name == "":
            error = error + "The Event Name field is required.\n"

        if event_desc == "":
            error = error + "The Description field is required.\n"

        # check that date has been changed
        td = datetime.today()

        # get wxPython datetime format
        day = td.day
        month = td.month
        year = td.year

        # -1 because the month counts from 0, whereas people count January as month #1.
        tdFormatted = wx.DateTimeFromDMY(day, month - 1, year)
        if str(event_date) == str(tdFormatted):
            error = error + "The Event Date field is required.\n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        else:
            event_data = {
                'event_name': event_name,
                'event_date': event_date,
                'event_desc': event_desc,
            }

            if saveEvent(event_data):
                dlg = wx.MessageDialog(None, "Event Added Successfully.", 'Success Message', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                self.cancelAddEvent("")
                dlg.Destroy()
            else:
                dlg = wx.MessageDialog(None, "Event Not Saved. Try Again.", 'Failed',
                                       wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()

        self.save_event.Enable(True)


