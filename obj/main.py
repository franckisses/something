import wx,time
import smtplib
from MyWeather import *
from create_database import WeatherDate
from email.mime.text import MIMEText


# todayInfo=u"12月8日星期四 小雨转多云7℃/-1℃ 北风5-6级 img/07.gif img/01.gif".split()
# daysInfo=[todayInfo,todayInfo,todayInfo,todayInfo]


class MyApp(wx.App):
    """应用程序类wx.App的子类"""

    def __init__(self, title, sText):  # 重构构造方法，其中title、sText分别是传递给主窗口的标题参数和状态栏参数
        wx.App.__init__(self)  # 调用wx.App的构造方法
        frame = MyFrame(title, sText)  # 创建主窗口对象
        frame.Show(True)  # 显示主窗口


class MyFrame(wx.Frame):

    def __init__(self, title, sText):
        wx.Frame.__init__(self, None, -1, title=title,
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.MAXIMIZE_BOX | wx.RESIZE_BORDER))
        self.panel = wx.Panel(self)
        self.timer=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.sendToUsers, self.timer)
        self.timer.Start(1000)
        t = time.localtime(time.time())
        st = time.strftime("%I:%M:%S", t)
        stBar = self.CreateStatusBar()  # 创建状态栏

        stBar.SetStatusText(st)  # 状态栏显示友情提示

        hdLeft = self.LayoutHeadLeft(todayInfo)
        hdRight = self.LayoutHeadRight()
        head = self.LayoutHead(hdLeft, hdRight)
        days = self.LayoutDaysWeather(daysInfo)
        sizer = self.LayoutPanel(head, days)


        self.panel.SetSizer(sizer)
        sizer.Fit(self)
        sizer.SetSizeHints(self)

    def Tbl(self):
        tLbl = wx.StaticText(self.panel, -1)
        return [tLbl]

    def LayoutHeadLeft(self, todayInfo):
        """窗口上半部分左侧布局，主要是今日天气信息。
        todayInfo=[日期,图片1,图片2,天气,风力]"""
        # ['24日星期二', '晴', '温度:低温 27℃~高温 39℃', '西南风:<3级']

        # 一个静态文本控件
        # tLbl = wx.StaticText(self.panel,-1, name='tLb1')
        tLb1 = self.Tbl()[0]
        tLb1.SetLabel('     当前天气:' + todayInfo[2] + '  温度:' + todayInfo[
                      1] + '\n 温度范围:' + todayInfo[3] + todayInfo[4])

        # 从文件载入图像
        img1 = wx.Image(
            "img/a_" + todayInfo[2].rstrip() + '.png', wx.BITMAP_TYPE_PNG)
        img2 = wx.Image(
            "img/a_" + todayInfo[2].rstrip() + '.png', wx.BITMAP_TYPE_PNG)

        # 转换为静态图像控件
        sb1 = wx.StaticBitmap(self.panel, -1, wx.Bitmap(img1))
        sb2 = wx.StaticBitmap(self.panel, -1, wx.Bitmap(img2))

        # 使用GridBagSizer来放置两个图片和两个文本控件
        GBSizer = wx.GridBagSizer(vgap=5, hgap=5)  # Grid之间水平、竖直方向间距都是5个像素
        GBSizer.Add(sb1, pos=(0, 0), span=(1, 1),
                    flag=0)  # 天气图片1，放置在第1行第1列，占一行一列
        GBSizer.Add(sb2, pos=(0, 1), span=(1, 1),
                    flag=0)  # 天气图片2，放置在第1行第2列，占一行一列
        GBSizer.Add(tLb1, pos=(1, 0), span=(1, 2),
                    flag=0)  # 天气文字信息，放置在第2行第1列，占一行两列

        # 再使用Static Box Sizer来放置上面的GridBagSizer
        sbox = wx.StaticBox(self.panel, -1, todayInfo[0])
        sbsizer = wx.StaticBoxSizer(sbox, wx.VERTICAL)
        sbsizer.Add(GBSizer, 0, wx.ALL, 2)

        return sbsizer

    def LayoutHeadRight(self):
        """放置3个按钮"""

        # 三个按钮控件
        self.updateBtn = wx.Button(self.panel, -1, label=u"更新")
        self.setupBtn = wx.Button(self.panel, -1, label=u"设置")
        self.sendBtn = wx.Button(self.panel, -1, label=u"发送")
        self.Bind(wx.EVT_BUTTON, self.OnRefresh, self.updateBtn)  # 更新按钮绑定事件处理器
        self.Bind(wx.EVT_BUTTON, self.OnConfig, self.setupBtn)  # 设置按钮绑定事件处理器
        self.Bind(wx.EVT_BUTTON, self.OnSend, self.sendBtn)  # 发送按钮绑定事件处理器

        # 使用Static Box Sizer来放置上面的GridBagSizer
        sbox = wx.StaticBox(self.panel, -1, u"个性化")
        sbsizer = wx.StaticBoxSizer(sbox, wx.VERTICAL)
        sbsizer.Add(self.updateBtn, 0, wx.ALL, 2)
        sbsizer.Add(self.setupBtn, 0, wx.ALL, 2)
        sbsizer.Add(self.sendBtn, 0, wx.ALL, 2)

        return sbsizer

    def LayoutHead(self, headLeft, headRight):
        box = wx.BoxSizer(wx.HORIZONTAL)  # 使用水平BoxSizer放置今日天气信息和3个按钮
        box.Add(headLeft, 1, flag=wx.EXPAND)
        box.Add(headRight, flag=wx.EXPAND)

        return box

    def LayoutDayWeather(self, dayInfo):
        """放置未来4天每天的天气信息"""
        # 两个静态文本控件
        dLbl = wx.StaticText(self.panel, -1, label=dayInfo[0])
        tLbl = wx.StaticText(
            self.panel, -1, label=dayInfo[1] + dayInfo[2] + dayInfo[3])
        # wLbl=wx.StaticText(self.panel,-1,label=todayInfo[2])

        # 从文件载入图像
        img1 = wx.Image(
            "img/" + dayInfo[1].rstrip() + '.png', wx.BITMAP_TYPE_PNG)
        img2 = wx.Image(
            "img/" + dayInfo[1].rstrip() + '.png', wx.BITMAP_TYPE_PNG)
        # 转换为静态图像控件
        sb1 = wx.StaticBitmap(self.panel, -1, wx.Bitmap(img1))
        sb2 = wx.StaticBitmap(self.panel, -1, wx.Bitmap(img2))

        # 使用GridBagSizer来放置两个图片和两个文本控件
        GBSizer = wx.GridBagSizer(vgap=5, hgap=5)
        GBSizer.Add(dLbl, pos=(0, 0), span=(1, 3), flag=0)
        GBSizer.Add(sb1, pos=(1, 0), flag=0)
        GBSizer.Add(sb2, pos=(1, 1), flag=0)
        GBSizer.Add(tLbl, pos=(1, 2), flag=0)

        return GBSizer

    def LayoutDaysWeather(self, daysInfo):
        """使用竖直方向的StaticBoxSizer放置未来4天的天气信息"""
        sbox = wx.StaticBox(self.panel, -1, u"未来4日天气")
        sbsizer = wx.StaticBoxSizer(sbox, wx.VERTICAL)
        for dayInfo in daysInfo:
            sz = self.LayoutDayWeather(dayInfo)
            sbsizer.Add(sz, flag=wx.EXPAND)
        return sbsizer

    def LayoutPanel(self, head, days):
        """使用竖直方向的BoxSizer放置窗口上半部分内容和下半部分内容"""
        bsizer = wx.BoxSizer(wx.VERTICAL)
        bsizer.Add(head, flag=wx.EXPAND)
        bsizer.Add(days, flag=wx.EXPAND)
        return bsizer

    def OnRefresh(self, event):
        self.updateWeather()  # 更新主面板天气信息

    def OnConfig(self, event):
        cfgFrame = cfgMyFrame(self)  # 打开配置窗口
        cfgFrame.Show(True)  # 显示配置窗口

    def OnSend(self,event):
        #self.sendToUsers()  # 给预定义的用户发送各自的天气信息
        msg_form = '511152002@qq.com'
        passwd = 'cppzrzeadvgabghi'
        # 从数据库读取出邮箱的信息，类型为列表中存储的元组
        for date_info in WeatherDate().read_date():
            city,email=date_info[3],date_info[1]
            msg_to=email
            a=MyWeahter(city)
            a.get_weather()
            # date_info 格式:(1, 'franck_gxu@outlook.com', '小鸡', '西安')
            subject = '来自Just do IT天气助手的温馨提醒'

            msg0='今天是%d年%d月%d日，Just do IT天气助手提醒您：'%(time.localtime()[0], time.localtime()[1], time.localtime()[2])
            msg1=",".join(a.other())
            msg2='%s,%s,温度%s,风力%s.'%(a.today()[0],a.today()[2],a.today()[3],a.today()[4])
            msg3=",".join(a.otherday(1))+"."
            msg4=",".join(a.otherday(2))+"."
            msg5=",".join(a.otherday(3))+",非常感谢订阅Just do IT的产品，祝您生活愉快！"
            content=msg0+msg1+msg2+msg3+msg4+msg5
            msg = MIMEText(content)
            msg['Subject'] = subject
            msg['From'] = msg_form
            msg['to'] = msg_to
            try:
                s = smtplib.SMTP_SSL('smtp.qq.com', 465)
                s.login(msg_form, passwd)
                s.sendmail(msg_form,msg_to,msg.as_string())
            except:
                print('发送失败')
            finally:
                s.quit()

    def updateWeather(self):
        a = MyWeahter('成都')
        a.get_weather()
        todayInfo = a.today()
        # print(a.today())
        # wInfo = ["1", "2", "3", "4", "5", "6", "7"]
        wTitle = "当前城市:" + a.other()[0]  # 当前城市天气预报
        wTime = a.other()[1]  # 友情提醒
        daysInfo = [a.otherday(1), a.otherday(2), a.otherday(3), a.otherday(4)]
        # daysInfo = wInfo[3:7]

        # self.stBar.SetStatusText(wTime, 0)
        # ###显示今日天气###
        # self.weatherLabels[0].SetLabel(todayInfo[1])
        # # 从文件载入图像
        # todayImg1 = wx.Image("img/a_" + todayInfo[2], wx.BITMAP_TYPE_GIF)
        # todayImg2 = wx.Image("img/a_" + todayInfo[3], wx.BITMAP_TYPE_GIF)
        # # 转换为静态图像控件
        # self.weatherIcons[0].SetBitmap(wx.Bitmap(todayImg1))
        # self.weatherIcons[1].SetBitmap(wx.Bitmap(todayImg2))
        #
        # ###显示未来4日天气###
        # i = 0
        # for dayInfo in daysInfo:
        #     self.weatherLabels[2 * i + 1].SetLabel(dayInfo[0])
        #     self.weatherLabels[2 * i + 2].SetLabel(dayInfo[1])
        #     img1 = wx.Image("img/" + dayInfo[2], wx.BITMAP_TYPE_GIF)
        #     img2 = wx.Image("img/" + dayInfo[3], wx.BITMAP_TYPE_GIF)
        #     self.weatherIcons[2 * i + 2].SetBitmap(wx.Bitmap(img1))
        #     self.weatherIcons[2 * i + 3].SetBitmap(wx.Bitmap(img2))
        #     i += 1
        # self.hdLeft.Fit(self)
        # self.hdRight.Fit(self)
        # self.head.Fit(self)
        # self.days.Fit(self)
        # self.sizer.Fit(self)
        return True

    def sendToUsers(self,evt):
        with open("time.txt","r") as r:
            read_time=r.read().split()
            while True:
                time.sleep(1)
                if time.localtime()[3] == read_time[0]:
                    if time.localtime()[4]==read_time[1]:
                        if time.localtime()[3]==read_time[2]:
                            self.OnSend()
                            print("hahah")




class cfgMyApp(wx.App):
    '''应用程序类wx.App的子类'''

    def __init__(self):  # 重新构造放,其中title,sText分别是传递给主窗口的标题参数和状态栏参数
        wx.App.__init__(self)  # 调用wx.App的构造方法
        frame = cfgMyFrame(self)  # 创建主窗口对象
        frame.Show(True)  # 显示主窗口


class cfgMyFrame(MyFrame):

    def __init__(self,parent):
        wx.Frame.__init__(self, parent, -1, title='设置窗口', size=(300, 500),
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
        # 获取用户信息,得到一个列表
        userInfo = WeatherDate().read_date()
        # 初始化row,从第0项开始循环
        row = 0
        # 插入用户信息
        for info in userInfo:
            self.list.InsertItem(row, str(row + 1))
            self.list.SetItem(row, 1, info[1])
            self.list.SetItem(row, 2, info[2])
            self.list.SetItem(row, 3, info[3])
            row += 1
        self.totaluser = row

        self.nm = wx.StaticBox(self.panel, -1, '定时发送', (0, 330), (300, 170))
        self.nmSizer = wx.StaticBoxSizer(self.nm, wx.VERTICAL)
        nmbox = wx.BoxSizer(wx.HORIZONTAL)
        fn = wx.StaticText(self.nm, -1, ':', (110, 50))
        fn = wx.StaticText(self.nm, -1, ':', (190, 50))
        self.setTimeChk = wx.CheckBox(self.nm, -1, u'定时发送', (20, 30))
        nmbox.Add(fn, 1, wx.ALL | wx.CENTER)
        nmbox.Add(self.setTimeChk, 1, wx.ALL | wx.CENTER, 5)
        m_choice1Choices = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10",u"11",u"12", u"13", u"14",
                            u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23",u"24"]
        m_choice2Choices = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10",u"11" ,u"12", u"13", u"14",
                            u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23", u"24", u"25", u"26",
                            u"27",
                            u"28", u"29", u"30", u"31", u"32", u"33", u"34", u"35", u"36", u"37", u"38", u"39",
                            u"40",
                            u"41", u"42", u"43", u"44", u"45", u"46", u"47", u"48", u"49", u"50", u"51", u"52",
                            u"53",
                            u"54", u"55", u"56", u"57", u"58", u"59"]
        self.hourCho = wx.Choice(self.nm, 1, (50, 50),
                                 choices=m_choice1Choices)
        self.hourCho.SetSelection(7)
        self.minuteCho = wx.Choice(
            self.nm, 1, (130, 50), choices=m_choice2Choices)
        self.minuteCho.SetSelection(30)
        self.secondCho = wx.Choice(
            self.nm, 1, (210, 50), choices=m_choice2Choices)
        self.secondCho.SetSelection(30)
        self.Bind(wx.EVT_CHECKBOX, self.OnSetTimeChk, self.setTimeChk)

        self.hourCho.Disable()
        self.minuteCho.Disable()
        self.secondCho.Disable()


    def OnSetTimeChk(self, event):
        if self.setTimeChk.IsChecked():
            self.hourCho.Enable()
            self.minuteCho.Enable()
            self.secondCho.Enable()
            # self.Bind(wx.EVT_CLOSE,self.getSetTime)
        else:
            self.hourCho.Disable()
            self.minuteCho.Disable()
            self.secondCho.Disable()

    def getSetTime(self,event):
        if self.setTimeChk.IsChecked():
            a = self.hourCho.GetSelection()
            b = self.minuteCho.GetSelection()
            c = self.secondCho.GetSelection()
            time=str(a)+" "+str(b)+" "+str(c)
            with open("time.txt", "w") as f:
                f.write(time)
            self.Bind(wx.EVT_CLOSE,self.Parent.sendToUsers)
        if self.Parent.sendToUsers():
            self.Destroy()






if __name__ == "__main__":
    a = MyWeahter("西安")
    a.get_weather()
    todayInfo = a.today()
    # print(a.other())
    # wInfo=["1","2","3","4","5","6","7"]
    wTitle = "当前城市:" + a.other()[0]  # 南京天气预报
    wTime = a.other()[1]  # 发布时间
    daysInfo = [a.otherday(1), a.otherday(2), a.otherday(3), a.otherday(4)]
    app = MyApp(wTitle, wTime)  # 应用程序类的一个实例
    app.MainLoop()  # 进入主循环
