import wx
from MyWeather import *
from create_database import WeatherDate


class cfgMyApp(wx.App):
    '''应用程序类wx.App的子类'''

    def __init__(self):  # 重新构造放,其中title,sText分别是传递给主窗口的标题参数和状态栏参数
        wx.App.__init__(self)  # 调用wx.App的构造方法
        frame = cfgMyFrame()  # 创建主窗口对象
        frame.Show(True)  # 显示主窗口


class cfgMyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, title='设置窗口', size=(300, 500),
                          style=wx.DEFAULT_DIALOG_STYLE ^ (wx.MAXIMIZE_BOX | wx.RESIZE_BORDER))
        self.panel = wx.Panel(self)
        self.WeatherDate = WeatherDate()
        # stBar = self.CreateStatusBar()  # 创建状态栏
        # stBar.SetStatusText(sText)  # 状态栏显示发布时间
        self.text = wx.StaticText(self.panel, -1, "当前城市", (10, 10))
        self.list = wx.ListCtrl(self.panel, -1, (0, 30), (300, 300),
                                style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)
        self.list.InsertColumn(0, u'ID', format=wx.LIST_FORMAT_LEFT, width=30)
        self.list.InsertColumn(1, u'邮箱', format=wx.LIST_FORMAT_LEFT, width=120)
        self.list.InsertColumn(2, u'姓名', format=wx.LIST_FORMAT_LEFT, width=60)
        self.list.InsertColumn(3, u'城市', format=wx.LIST_FORMAT_LEFT, width=70)
        # self.list.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)
        userInfo = WeatherDate().read_date()

        row = 0

        for info in userInfo:
            print(info[0], info[1], info[2], info[3])
            # self.list.SetStringItem(info[0],info[1],info[2],info[3])
            self.list.InsertStringItem(row, str(row + 1))
            self.list.SetStringItem(row, 1, info[1])
            self.list.SetStringItem(row, 2, info[2])
            self.list.SetStringItem(row, 3, info[3])
            row += 1

        self.nm = wx.StaticBox(self.panel, -1, '定时发送', (0, 330), (300, 170))
        self.nmSizer = wx.StaticBoxSizer(self.nm, wx.VERTICAL)
        nmbox = wx.BoxSizer(wx.HORIZONTAL)
        fn = wx.StaticText(self.nm, -1, ':', (110, 50))
        fn = wx.StaticText(self.nm, -1, ':', (190, 50))
        self.setTimeChk = wx.CheckBox(self.nm, -1, u'定时发送', (20, 30))
        nmbox.Add(fn, 1, wx.ALL | wx.CENTER)
        nmbox.Add(self.setTimeChk, 1, wx.ALL | wx.CENTER, 5)
        m_choice1Choices = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"12", u"13", u"14",
                            u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23", u"24"]
        m_choice2Choices = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"12", u"13", u"14",
                            u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23", u"24", u"25", u"26", u"27",
                            u"28", u"29", u"30", u"31", u"32", u"33", u"34", u"35", u"36", u"37", u"38", u"39", u"40",
                            u"41", u"42", u"43", u"44", u"45", u"46", u"47", u"48", u"49", u"50", u"51", u"52", u"53",
                            u"54", u"55", u"56", u"57", u"58", u"59"]
        self.hourCho = wx.Choice(self.nm, 1, (50, 50),
                                 choices=m_choice1Choices)
        self.hourCho.SetSelection(7)
        self.minuteCho = wx.Choice(
            self.nm, 1, (130, 50), choices=m_choice2Choices)
        self.minuteCho.SetSelection(29)
        self.secondCho = wx.Choice(
            self.nm, 1, (210, 50), choices=m_choice2Choices)
        self.secondCho.SetSelection(29)
        self.Bind(wx.EVT_CHECKBOX, self.OnSetTimeChk, self.setTimeChk)

        self.hourCho.Disable()
        self.minuteCho.Disable()
        self.secondCho.Disable()

    def OnSetTimeChk(self, event):
        if self.setTimeChk.IsChecked():
            self.hourCho.Enable()
            self.minuteCho.Enable()
            self.secondCho.Enable()
        else:
            self.hourCho.Disable()
            self.minuteCho.Disable()
            self.secondCho.Disable()


# a = MyWeahter('西安')
# a.get_weather()
# weather = a.today()
# # b=WeatherDate()
# # b.read_date()
# # print(a.today(),a.second())
# print(weather)
# app = cfgMyApp(weather[0] + '天气预报', weather[1])
# app.MainLoop()
