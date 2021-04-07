import wx
import telnetlib
from time import sleep
import _thread as thread
import random
import Mywxpython
# import zoom
class MainPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.frame = parent
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        
       
        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1,1), 0, wx.ALL, 75)
        self.SetSizer((hSizer))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # self.SetTransparent(1000)  # 设置透明
        # self.SetMaxSize((320, 250))
        # self.SetMinSize((320, 250))
    #字体对象
        labelfont = wx.Font(18,family =wx.SWISS,style=wx.NORMAL,weight=wx.LIGHT,underline=False,faceName ="", encoding = wx.FONTENCODING_DEFAULT)
	#放置正中央
        
        # self.logo = Mywxpython.TransparentStaticText(self, label="闪指", pos=(155, 20), size=(240, 50),style=wx.ALIGN_CENTRE_HORIZONTAL)
        # self.logo.SetForegroundColour("#ffffff")
        
        
	#服务器地址框标签
        self.serverAddressLabel = Mywxpython.TransparentStaticText(self, label="密码", pos=(40, 120), size=(120, 25))
        self.serverAddressLabel.SetFont(labelfont)
        self.serverAddressLabel.SetForegroundColour("#ffffff")
	#用户名框标签        	
        self.userNameLabel = Mywxpython.TransparentStaticText(self, label="用户名", pos=(40, 70), size=(120, 25))
        self.userNameLabel.SetFont(labelfont)
        self.userNameLabel.SetForegroundColour("#ffffff")
	#服务器地址框        
        self.serverAddress = wx.TextCtrl(self, pos=(120, 117), size=(150, 25))
        self.serverAddress.SetDefaultStyle(wx.TextAttr(wx.WHITE))

	#用户名框        
        self.userName = wx.TextCtrl(self, pos=(120, 67), size=(150, 25))
        self.userName.SetDefaultStyle(wx.TextAttr(wx.WHITE))
	#登录按钮        
        self.createButton = wx.Button(self, label='注册', pos=(100, 155), size=(60, 30))
        #登录按钮上绑定登录方法
        self.createButton.Bind(wx.EVT_BUTTON, self.create)
	#登录按钮        
        self.loginButton = wx.Button(self, label='登录', pos=(170, 155), size=(60, 30))
        #登录按钮上绑定登录方法
        self.loginButton.Bind(wx.EVT_BUTTON, self.login)
    
    #----------------------------------------------------------------------
    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()
                
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("shangwu.png")
        dc.DrawBitmap(bmp, 0, 0)
            
        
    #显示组件        
       
    # def OnEraseBack(self,event):
    #     dc = event.GetDC()
    #     if not dc:
    #         dc = wx.ClientDC(self)
    #         rect = self.GetUpdateRegion().GetBox()
    #         dc.SetClippingRect(rect)
    #     dc.Clear()
    #     bmp = wx.Bitmap("shangwu.png")

    #     dc.DrawBitmap(bmp, 0, 0)

    def create(self,event):
         # 登录处理
        try:
            Address = "47.98.40.28:8000"
            serverAddress = Address.split(':')
            con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)
            response = con.read_some()
            
            if response != '连接成功'.encode('utf-8'):
                self.showDialog('Error', '连接失败!', (200, 100))
                return
            con.write(('creat ' + str(self.userName.GetLineText(0))+"$$"+str(self.serverAddress.GetLineText(0)) + '\n').encode("utf-8"))
            response = con.read_some()
            self.showDialog("ajfidj", response, (800, 100))
            if response == '用户名重复'.encode('utf-8'):
                self.showDialog('Error', '用户名重复!', (200, 100))
            # elif response == '用户名已存在':
            #     self.showDialog('Error', '用户名已存在!', (200, 100))
            else:
                self.showDialog('Congratulation', '注册成功!', (195, 120))
                self.Close()
                ServerFrame()
        except Exception:
            self.showDialog('Error', '连接失败!', (195, 120))

    def login(self, event):
        # 登录处理
        try:
            Address = "47.98.40.28:8000"
            serverAddress = Address.split(':')
            con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)
            response = con.read_some()
            
            if response != '连接成功'.encode('utf-8'):
                self.showDialog('Error', '连接失败!', (200, 100))
                return
            con.write(('login ' + str(self.userName.GetLineText(0))+"$$"+str(self.serverAddress.GetLineText(0)) + '\n').encode("utf-8"))
            response = con.read_some()
            
            if response == '用户名不正确'.encode('utf-8'):
                self.showDialog('Error', '用户名不正确!', (200, 100))
            elif response == '无此用户名'.encode('utf-8'):
                self.showDialog('Error', '无此用户!', (200, 100))
            else:
                # self.showDialog('Error', response, (200, 100))
                self.Close()
                ServerFrame()
        except Exception:
            self.showDialog('Error', '连接失败!', (195, 120))

    def showDialog(self, title, content, size):
        # 显示错误信息对话框
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label=content)
	#显示对话窗口
        dialog.ShowModal() 
class LoginFrame(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    #初始化，添加控件
    def __init__(self):
        # real_resolution = zoom.get_real_resolution()
        # screen_size = zoom.get_screen_size()


        
        # screen_scale_rate = round(screen_size[0] / 1950, 2)
        # screen_scale_rate1 = round(screen_size[1] / 1060, 2)

        wx.Frame.__init__(self, None, -1,"Login",size=(320, 250), style = wx.DEFAULT_FRAME_STYLE)


        panel =MainPanel(self)
        self.Center()

        self.Show()


class MainPanelS(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.frame = parent
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        
       
        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1,1), 0, wx.ALL, 75)
        self.SetSizer((hSizer))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # self.SetTransparent(1000)  # 设置透明
        # self.SetMaxSize((320, 250))
        # self.SetMinSize((320, 250))
     #字体对象
        labelfont = wx.Font(18,family =wx.SWISS,style=wx.NORMAL,weight=wx.LIGHT,underline=False,faceName ="", encoding = wx.FONTENCODING_DEFAULT)
	#放置正中央
        
        # self.logo = Mywxpython.TransparentStaticText(self, label="闪指", pos=(155, 20), size=(240, 50),style=wx.ALIGN_CENTRE_HORIZONTAL)
        # self.logo.SetForegroundColour("#ffffff")
        
        
	#服务器地址框标签
        self.serverAddressLabel = Mywxpython.TransparentStaticText(self, label="会议号", pos=(40, 70), size=(120, 25))
        self.serverAddressLabel.SetFont(labelfont)
        self.serverAddressLabel.SetForegroundColour("#ffffff")

	#服务器地址框        
        self.serverAddress = wx.TextCtrl(self, pos=(120, 67), size=(150, 25))
        self.serverAddress.SetDefaultStyle(wx.TextAttr(wx.WHITE))


	#创建会议按钮        
        self.loginButton = wx.Button(self, label='创建会议', pos=(100, 155), size=(60, 30))
        #登录按钮上绑定登录方法
        self.loginButton.Bind(wx.EVT_BUTTON, self.createmeeting)
	#加入会议按钮        
        self.loginButton = wx.Button(self, label='加入会议', pos=(170, 155), size=(60, 30))
        #登录按钮上绑定登录方法
        self.loginButton.Bind(wx.EVT_BUTTON, self.joinmeeting)
        

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()
                
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("shangwu.png")
        dc.DrawBitmap(bmp, 0, 0)

    def createmeeting(self, event):
        # 登录处理
        try:
            
            serverAddress = self.serverAddress.GetLineText(0).split(':')
            con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)
            response = con.read_some()
           
            if response != '连接成功'.encode('utf-8'):
                self.showDialog('Error', '连接失败!', (200, 100))
                return
            con.write(('create ' + str(self.userName.GetLineText(0)) + '\n').encode("utf-8"))
            response = con.read_some()

            if response == '用户名为空'.encode('utf-8'):
                self.showDialog('Error', '用户名为空!', (200, 100))
            elif response == '用户名已存在':
                self.showDialog('Error', '用户名已存在!', (200, 100))
            else:
                self.Close()
                ChatFrame(None, 2, title='QT聊天室', size=(500, 400))
        except Exception:
            self.showDialog('Error', '连接失败!', (195, 120))
    def joinmeeting(self, event):
        # 登录处理
        try:
            serverAddress = self.serverAddress.GetLineText(0).split(':')
            con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)
            response = con.read_some()
            if response != '连接成功'.encode('utf-8'):
                self.showDialog('Error', '连接失败!', (200, 100))
                return
            con.write(('login ' + str(self.userName.GetLineText(0)) + '\n').encode("utf-8"))
            response = con.read_some()
            if response == '用户名为空'.encode('utf-8'):
                self.showDialog('Error', '用户名为空!', (200, 100))
            elif response == '用户名已存在':
                self.showDialog('Error', '用户名已存在!', (200, 100))
            else:
                self.Close()
                ChatFrame(None, 2, title='QT聊天室', size=(500, 400))
        except Exception:
            self.showDialog('Error', '连接失败!', (195, 120))

    def showDialog(self, title, content, size):
        # 显示错误信息对话框
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label=content)
	#显示对话窗口
        dialog.ShowModal()

class ServerFrame(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    #初始化，添加控件
    def __init__(self):
        wx.Frame.__init__(self, None, 1,"Meeting",size=(320, 250), style = wx.DEFAULT_FRAME_STYLE)


       
        # self.SetTransparent(1000)  # 设置透明
        self.SetMaxSize((320, 250))
        self.SetMinSize((320, 250))
        panel =MainPanelS(self)
        self.Center()
            #显示组件        
        self.Show()
   
class ChatFrame(wx.Frame):
    """
    聊天窗口类，继承wx.Frame类
    """

    def __init__(self, parent, id, title, size):
        # 初始化，添加控件
        wx.Frame.__init__(self, parent, id, title)
        self.SetSize(size)
        self.Center()
	#显示对话文本框，style设置其文本高亮显示和只读
        self.chatFrame = wx.TextCtrl(self, pos=(5, 5), size=(490, 310), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.message = wx.TextCtrl(self, pos=(5, 320), size=(300, 25))
        self.sendButton = wx.Button(self, label="Send", pos=(310, 320), size=(58, 25))
        self.usersButton = wx.Button(self, label="Users", pos=(373, 320), size=(58, 25))
        self.closeButton = wx.Button(self, label="Close", pos=(436, 320), size=(58, 25))
        # 发送按钮绑定发送消息方法
        self.sendButton.Bind(wx.EVT_BUTTON, self.send)
        # Users按钮绑定获取在线用户数量方法
        self.usersButton.Bind(wx.EVT_BUTTON, self.lookUsers)
        # 关闭按钮绑定关闭方法
        self.closeButton.Bind(wx.EVT_BUTTON, self.close)
	#调用thread模块中的start_new_thread()来产生新线程负责接收服务器信息
	#第一个参数为线程要执行函数的函数名，第二个参数为需要传递给函数的实参，为tuple，若该函数不需要参数也要传入空tuple       
        thread.start_new_thread(self.receive, ())
        self.Show()

    def send(self, event):
        # 发送消息
        message = str(self.message.GetLineText(0)).strip()
        if message != '':
	    #这里的'say '不可随意变动，为呼应server.py中命令处理类定义的handle(),实现文字聊天协议而存在
            con.write(('say ' + message + '\n').encode("utf-8"))
            self.message.Clear()

    def lookUsers(self, event):
        #查看当前在线用户
        con.write(b'look\n')

    def close(self, event):
        # 关闭窗口
        con.write(b'logout\n')
        con.close()
        self.Close()

    def receive(self):
        # 接受服务器的消息
        while True:
            sleep(0.6)
	    #在I/O中读取数据，存在result变量中
            result = con.read_very_eager()
            if result != '':
                self.chatFrame.AppendText(result)

if __name__ == '__main__':
    #应用程序对象
    app = wx.App()
    #客户端使用telnetlib连接目标主机
    con = telnetlib.Telnet()
    #顶级窗口对象
    LoginFrame()
    #进入应用程序的主事件循环
    app.MainLoop()



