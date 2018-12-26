import wx
import wx.xrc
from ObjectListView import ObjectListView, ColumnDefn
from datetime import datetime

from db.get_events import getEvents
from db.save_event import editEvent, deleteEvent
# import sys
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')

###########################################################################
# Class ViewEvents
###########################################################################


class ViewEvents(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(669, 428),
                          style=wx.TAB_TRAVERSAL)

        container = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"All Events", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))

        container.Add(self.m_staticText17, 0, wx.TOP | wx.EXPAND, 25)

        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_sizer = wx.BoxSizer(wx.HORIZONTAL)
        OLV_sizer = wx.BoxSizer(wx.VERTICAL)

        #
        # Events Object list View
        # ----------------------------------------------------------------
        # Search
        # ----------------------------------------------------------------
        search_container = wx.BoxSizer(wx.HORIZONTAL)

        self.refresh_btn = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"images/reload_16x16.bmp", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)

        self.refresh_btn.SetBitmapHover(wx.Bitmap(u"images/reload_16x16_rotated.bmp", wx.BITMAP_TYPE_ANY))
        search_container.Add(self.refresh_btn, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT, 5)

        self.m_staticText53 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText53.Wrap(-1)
        search_container.Add(self.m_staticText53, 1, wx.ALL, 5)

        self.search_events = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                             wx.TE_PROCESS_ENTER)
        self.search_events.ShowSearchButton(True)
        self.search_events.ShowCancelButton(False)
        search_container.Add(self.search_events, 0, wx.BOTTOM, 8)

        self.search_events.Bind(wx.EVT_TEXT, self.searchEvents)
        self.search_events.Bind(wx.EVT_TEXT_ENTER, self.searchEvents)

        OLV_sizer.Add(search_container, 0, wx.EXPAND, 5)
        #
        #
        # ----------------------------------------------------------------
        # Table
        # ----------------------------------------------------------------
        self.events = getEvents()

        self.eventsOLV = ObjectListView(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.setEventsData()

        OLV_sizer.Add(self.eventsOLV, 1, wx.EXPAND | wx.ALL, 5)

        # ----------------------------------------------------------------
        #
        #

        left_btns_sizer = wx.BoxSizer(wx.VERTICAL)

        self.edit_event_btn = wx.Button(self, wx.ID_ANY, u"Edit Event", wx.DefaultPosition, wx.DefaultSize, 0)
        self.edit_event_btn.Bind(wx.EVT_BUTTON, self.getEventInfo)
        left_btns_sizer.Add(self.edit_event_btn, 0, wx.ALL | wx.EXPAND, 5)

        self.delete_event_btn = wx.Button(self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        self.delete_event_btn.Bind(wx.EVT_BUTTON, self.deleteEvent)
        left_btns_sizer.Add(self.delete_event_btn, 0, wx.ALL | wx.EXPAND, 5)

        #
        #
        left_sizer.Add(OLV_sizer, 5, wx.EXPAND | wx.ALL, 5)
        left_sizer.Add(left_btns_sizer, 1, wx.ALL, 5)

        horizontal_sizer.Add(left_sizer, 1, wx.EXPAND, 5)

        right_sizer = wx.BoxSizer(wx.VERTICAL)

        self.edit_event_panel = EditEvent(self)

        #
        #
        #
        right_sizer.Add(self.edit_event_panel, 1, wx.EXPAND)

        horizontal_sizer.Add(right_sizer, 1, wx.EXPAND, 5)

        container.Add(horizontal_sizer, 1, wx.ALL | wx.EXPAND, 10)

        self.SetSizer(container)
        self.Layout()

        # Connect Events
        self.refresh_btn.Bind(wx.EVT_BUTTON, self.refreshTable)

    def setEventsData(self, data=None):
        self.eventsOLV.SetColumns([
            ColumnDefn("ID", "left", 50, "event_id"),
            ColumnDefn("Name", "center", 120, "event_name"),
            ColumnDefn("Date", "center", 75, "event_date"),
            ColumnDefn("Description", "center", 300, "event_desc"),
        ])

        self.eventsOLV.SetObjects(self.events)

    def updateEventsOLV(self, event):  # Refresh events table
        """"""
        data = getEvents()
        self.eventsOLV.SetObjects(data)

    def refreshTable(self, event):
        self.updateEventsOLV("")

    def searchEvents(self, event):
        search = self.search_events.GetLineText(0)
        data = getEvents(search)
        self.eventsOLV.SetObjects(data)

    def getEventInfo(self, event):  # In order to edit
        if not self.eventsOLV.GetSelectedObject():
            dlg = wx.MessageDialog(None, "Click on a row in order to edit event.",
                                   'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            self.rowData = self.eventsOLV.GetSelectedObject()
            rowObj = self.eventsOLV.GetSelectedObject()

            self.edit_event_panel.event_id.SetValue(str(rowObj['event_id']))

            self.edit_event_panel.event_name.SetValue(rowObj['event_name'])
            self.edit_event_panel.event_desc.SetValue(rowObj['event_desc'])

            # get wxPython datetime format
            day = rowObj['event_date'].day
            month = rowObj['event_date'].month
            year = rowObj['event_date'].year

            # -1 because the month counts from 0, whereas people count January as month #1.
            dateFormatted = wx.DateTimeFromDMY(day, month - 1, year)

            self.edit_event_panel.event_date.SetValue(dateFormatted)

            self.edit_event_panel.Show()

    def deleteEvent(self, event):
        if self.eventsOLV.GetSelectedObject():
            rowObj = self.eventsOLV.GetSelectedObject()

            dlg = wx.MessageDialog(None, "Confirm delete", 'Warning Message.', wx.YES_NO | wx.ICON_WARNING)
            retCode = dlg.ShowModal()
            dlg.Destroy()

            if retCode == wx.ID_YES:
                if deleteEvent(rowObj["event_id"]):
                    dlg = wx.MessageDialog(None, "Event deleted successfully.", 'Success Message.',
                                           wx.OK | wx.ICON_EXCLAMATION)
                    dlg.ShowModal()
                    dlg.Destroy()

                    self.updateEventsOLV("")
            else:
                rowObj=""

        else:
            dlg = wx.MessageDialog(None, "Click on a row to delete an event.", 'Error Message.',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()


class EditEvent(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(579, 436),
                          style=wx.TAB_TRAVERSAL)
        self.parent = parent

        container = wx.BoxSizer(wx.VERTICAL)

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        outer_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        outer_form_sizer = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Edit Event Form"), wx.VERTICAL)

        #
        # hidden event_id
        #
        event_id_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.event_id = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.event_id.Hide()
        event_id_sizer.Add(self.event_id, 4, wx.ALL, 10)

        sbSizer2.Add(event_id_sizer, 1, wx.ALL | wx.EXPAND, 10)
        #
        #
        #

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

        self.cancel_edit_btn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        btns_sizer.Add(self.cancel_edit_btn, 0, wx.ALL, 10)

        self.save_edit_event = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        btns_sizer.Add(self.save_edit_event, 0, wx.ALL, 10)

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
        self.cancel_edit_btn.Bind(wx.EVT_BUTTON, self.cancelEditEvent)
        self.save_edit_event.Bind(wx.EVT_BUTTON, self.saveEditEvent)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cancelEditEvent(self, event):
        self.event_id.SetValue("")
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

    def saveEditEvent(self, event):
        self.save_edit_event.Enable(False)

        event_id = self.event_id.GetValue()
        event_name = self.event_name.GetValue()
        event_date = self.event_date.GetValue()
        event_desc = self.event_desc.GetValue()

        if event_id != "":
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
                    'event_id': event_id,
                    'event_name': event_name,
                    'event_date': event_date,
                    'event_desc': event_desc,
                }

                if editEvent(event_data):
                    dlg = wx.MessageDialog(None, "Event Added Successfully.", 'Success Message',
                                           wx.OK | wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    self.cancelEditEvent("")
                    dlg.Destroy()
                    self.parent.updateEventsOLV("")
                else:
                    dlg = wx.MessageDialog(None, "Event Not Saved. Try Again.", 'Failed',
                                           wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()
                    dlg.Destroy()

        else:
            dlg = wx.MessageDialog(None, "Click on a row to edit an event.", 'Validation Error', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        self.save_edit_event.Enable(True)