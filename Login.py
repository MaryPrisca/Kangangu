import wx
import wx.xrc
from HomePage import HomePage

from db.login import login
# import sys
#
# sys.path.insert(0, r'/F:/PythonApps/Kangangu')


from wx.lib.embeddedimage import PyEmbeddedImage

appIcon = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAAA3NCSV QICAjb4U/gAAAG9ElE"
    "QVRIia2WWWxcVxnHv7PdOzN37p2xPbbHHsd27PESL0mIs+KSkMgEiUIaJMSmSkEKoognHnhA"
    "qkBQBAjxUFVFooJGqpB4KSk0hDbQClJSh8SJSdI4TmzHicceb7N4ZjzL3e85PATSEHmqWOr3"
    "eI/O/6fz/b/7Pwd5niGETYgGH3Nx215jrIYKYY1fe0NiLd1d/YpSB0ABBAAHEAAyAHoCLdvz"
    "LIQQxhQAua6RXVuauHUt1hzo2/ZF6npWKmX/5rdvtzS/2x3XgoqkG5ZteZiyoT1bOtr7FUWV"
    "JD9lEiEUIywECME9z3Fd27KMYjF7+eqVmTt5gl2CkSSzctmduWcXSvpPfnTEcUt0cXHi/X8l"
    "OuP9WOClJVMvlylRBCDTQ3OJqanJsUhEBIOIMWAMY4woJbbDMcalopVatVzuI37bx7bWapi7"
    "nEmUyUpNWFpJz717/oOu+A7keeb03X/fvDm5slQwdBNjgTGSZeZ4aPZe5u9/48PDWzSV5PJF"
    "iZFQSOWcAwJM0Mpy/vKl+aAWHD5kRWobQip1LM/1gAsU1Pwd8ejwgQONDV1ICPGgj7Zdcl0b"
    "BGBCEMKua46+/+pbZ6+rasDjUc59kkQxwQjAMC3BBUI6Rslw2Dx+fFtH/HsAsus5nHsIYVlW"
    "KFUBMADQ/xklSVKdJH1onCzdEvZd27Q/9ZnZnZ/IK9pBRLoBhQAEhiKIudL6jbGx3NvnQtnU"
    "RE/PDUSflh43Hx4FPFbJOzd/+eJL9M508+hocPtgbs/uM/E4CoeYEJDL8+lpNDau3L4dNfRg"
    "NuvFYr9v7+pHuP3JAZVMJpdKt1JilCv0wsW68xfCksTDYUkIKBRs18UYE0owpWJpOVBYX0fI"
    "3VCoGqBnx87dPd2TY1dUBMIn4/0HBg4M9+/c2SWEGB+feuevVycn5xECztGO7bme3mFA8U0B"
    "kBba2RW/cnlMRQBciIHBrd967hhjDAB6erckF1ITEwlMAED09ph+ZaCKDuBqC4iENY0DEoCQ"
    "43h/PnNxdWXtwZJp2pqmYIQAAGPQNIRwqJpOtRMACNu2kOAAGIQQzbFIJluoqdUAQGJsW1/7"
    "gxDhHCwTQNjVMqUqwLFXLYv096GpO0AInrh5/8SzPzt8ZJdt2fl8+eChHQghIUBVXdvxXDdD"
    "NxzSjwAU1+8V1tWjRxtnZxO2gwzD0XX7zT+NCiF8PimZzAAAF7Bnl+46SC/PabUb61TzoLS8"
    "NH/rtnZ/rkjpg2QVqupTFJ+mBRBCCwtpIYQs8aaoe/FybTYzB2Bs6gT55KKezqg+ab2xAc/e"
    "dwe3tz337S+MX52qrw+HQsFfvfzm6mqhvsnzPHR/XllZLXb0lAD8Tw4wSyVuWcQ0jZaWUrG8"
    "5ccvnNy7r2/XUG8g4ItEQpSxHzz/2ta28tKy3zJJpewBWJtqEWEMEIJ0xoo2rj/11ODefX0A"
    "vLU1GomEQcDnnt7f29sUa3LmEhIhQBkCIJtqkdZQz3yys7Lq798mVtLmSy/+wXVzkuSbX6gY"
    "utHW1hhUcDJBM1karnUidTKAsilAeOvWxqboWmLef/6fzYnElbNnLyMkAIBzAACEEKMYI4Vz"
    "3NpSisW6AdRNtYhFY8NHPp22bZRIyFwAIRhjgjGhlFBKCMFcgMcRId7RkfWayP5qUlWjgkgj"
    "X/9a8+6hlOuC4Bv8ppwjLuDgweyx43FMP1lN5+GNtmFNzd5+4dSry/94T11J+QAAPYgHARiJ"
    "1hZrZKRy4kRHW+f3Ed44SjcEeACuEJ5llSuVoq5PS/i99Ors6dOZP56pKxQkAGiot778pbWR"
    "EdbWcVgLf0WSOwFItWY8BIhM5u6ND64vzK9UyrphmOWSk0xmLCd/5EjnN09+xzXPvXPu9Z/+"
    "QgkEvB8+D9sGh1773VQyqUQi0aamOllmTJJr62ri8Y72tj5CPjT8v1M0PTP6yqnztlkX9GuR"
    "2milXAqq/tb2q5O3Vu/dzecKFb/vmcNHfZLv1wG/tGvfd5PLoRvXbyOc7+joTK02GIZR1t1S"
    "ZWk5de2ZYy0nnv1qwN/4KEAEAqw7rqRTaiG3xDkKBu1wjWQ7bDEZzabXT37j5wE/6+pp1tSh"
    "5EL+5Vfe0nVrLUsprRsYKDBGKGN19apuhFLZgqI4jl2C/wegaLSrPnKhqZEP9B2qjzRLsl+W"
    "pVOnXk+nbjgO4zOmx/VypWn79qGZu7PjV6cJwRTLoRqye+++/fsO6EbF0EuLi4vMJ3fHm0Oh"
    "zsc9sJ2c6xQDgdZHvbp06S9vnB7NrxVNy3RdLkk0pAVsx3FdVwn6wmElFot8/thnW2KDD7fY"
    "Tq5cSoTDfRj7qk3Ro+V4nu66tue5QnAhBAiBCSGEESIRwhBiAHSjB7J4+PGjAR9D/QevpkOk"
    "f7H8iAAAAABJRU5ErkJggg==")


###########################################################################
# Class Login
###########################################################################

class LoginFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(450, 600), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)

        ico = appIcon.getIcon()
        self.SetIcon(ico)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText55 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText55.Wrap(-1)
        bSizer.Add(self.m_staticText55, 1, wx.ALL, 5)

        bSizer72 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText58 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText58.Wrap(-1)
        self.m_staticText58.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer72.Add(self.m_staticText58, 1, wx.ALL | wx.EXPAND, 5)

        bSizer73 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap4 = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"images\\kangangu logo-254x254.bmp",
                                                   wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer73.Add(self.m_bitmap4, 0, wx.EXPAND | wx.ALL, 5)

        bSizer74 = wx.BoxSizer(wx.VERTICAL)

        uname_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText29 = wx.StaticText(self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)
        uname_sizer.Add(self.m_staticText29, 1, wx.ALL, 8)

        self.username = wx.TextCtrl(self, wx.ID_ANY, u"abdul", wx.DefaultPosition, wx.Size(-1, -1), 0)
        uname_sizer.Add(self.username, 3, wx.ALL, 5)

        bSizer74.Add(uname_sizer, 1, wx.EXPAND | wx.TOP, 10)

        pwd_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText291 = wx.StaticText(self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText291.Wrap(-1)
        pwd_sizer.Add(self.m_staticText291, 1, wx.ALL, 8)

        self.password = wx.TextCtrl(self, wx.ID_ANY, u"kashem", wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        pwd_sizer.Add(self.password, 3, wx.ALL, 5)

        bSizer74.Add(pwd_sizer, 1, wx.EXPAND | wx.TOP, 10)

        btns_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText68 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText68.Wrap(-1)
        btns_sizer.Add(self.m_staticText68, 2, wx.ALL, 5)

        self.login_btn = wx.Button(self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0)
        btns_sizer.Add(self.login_btn, 5, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_staticText69 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText69.Wrap(-1)
        btns_sizer.Add(self.m_staticText69, 0, wx.ALL, 5)

        bSizer74.Add(btns_sizer, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.TOP, 20)

        bSizer73.Add(bSizer74, 1, wx.EXPAND, 5)

        bSizer72.Add(bSizer73, 6, wx.EXPAND, 5)

        self.m_staticText59 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.m_staticText59.Wrap(-1)
        bSizer72.Add(self.m_staticText59, 2, wx.ALL | wx.EXPAND, 5)

        bSizer.Add(bSizer72, 8, wx.EXPAND, 5)

        self.m_staticText56 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText56.Wrap(-1)
        bSizer.Add(self.m_staticText56, 1, wx.ALL, 5)

        self.SetSizer(bSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.login_btn.Bind(wx.EVT_BUTTON, self.submitLogin)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def submitLogin(self, event):
        username = self.username.GetLineText(0)
        password = self.password.GetLineText(0)

        # Remove white spaces
        username = username.replace(" ", "")
        password = password.replace(" ", "")

        error = ""

        if username == "" or password == "":
            error = error + "Insert username and password to log in. \n"

        if error:
            dlg = wx.MessageDialog(None, error, 'Validation Error.', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
        else:
            data={
                "username": username,
                "password": password
            }

            loggedInUser = login(data)

            if not loggedInUser:
                dlg = wx.MessageDialog(None, "Login failed. Check your credentials and try again.", 'Login Failed.', wx.OK | wx.ICON_WARNING)
                dlg.ShowModal()
            else:
                hp = HomePage(None, loggedInUser)
                hp.Show()
                self.Hide()


# # Run the program
# if __name__ == "__main__":
#     app = wx.App()
#     frame = LoginFrame(None)
#     frame.Show()
#     app.MainLoop()


class MySplashScreen(wx.SplashScreen):
    """
        Create a splash screen widget.
    """
    def __init__(self, parent=None):
        aBitmap = wx.Image(name = "images/Kangangu.jpg").ConvertToBitmap()
        splashStyle = wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT
        splashDuration = 2800 # milliseconds

        wx.SplashScreen.__init__(self, aBitmap, splashStyle,
                                 splashDuration, parent)
        self.Bind(wx.EVT_CLOSE, self.OnExit)

        wx.Yield()
# ----------------------------------------------------------------------#

    def OnExit(self, evt):
        self.Hide()
        # LoginFrame is the main frame.
        loginFrame = LoginFrame(None)
        app.SetTopWindow(loginFrame)
        loginFrame.Show()
        # The program will freeze without this line.
        evt.Skip()  # Make sure the default handler runs too...
# ----------------------------------------------------------------------#


class MyApp(wx.App):
    def OnInit(self):
        MySplash = MySplashScreen()
        MySplash.Show()

        return True
# ----------------------------------------------------------------------#


# app = MyApp(redirect=True, filename = "demo.log")
app = MyApp(False)
app.MainLoop()


