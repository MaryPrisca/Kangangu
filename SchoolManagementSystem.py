import wx

from Login import LoginFrame
from initialization.SetupMainFrame import SetupMainFrame
from initialization.system_setup import checkIfSetupIsComplete


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
# ---------------------------------------------------------------------- #

    def OnExit(self, evt):
        self.Destroy()

        # Check if setup is complete
        setup_complete = checkIfSetupIsComplete()

        # Open login frame if setup is complete, else open SetupMainFrame
        if setup_complete:
            mainFrame = LoginFrame(None)
        else:
            mainFrame = SetupMainFrame(None)
        app.SetTopWindow(mainFrame)
        mainFrame.Show()

        # The program will freeze without this line.
        evt.Skip()  # Make sure the default handler runs too...


class MyApp(wx.App):
    def OnInit(self):
        MySplash = MySplashScreen()
        MySplash.Show()

        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

        return True


# ---------------------------------------------------------------------- #


# app = MyApp(redirect=True, filename = "demo.log")
app = MyApp(False)
app.MainLoop()

