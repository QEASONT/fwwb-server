import wx
class TransparentStaticText(wx.StaticText):
    """
    重写StaticText控件
    """
    def __init__(self, parent, id=wx.ID_ANY, label='', pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TRANSPARENT_WINDOW, name='TransparentStaticText'):
        wx.StaticText.__init__(self, parent, id, label, pos, size, style, name)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
        self.Bind(wx.EVT_SIZE, self.OnSize)
 
    def OnPaint(self, event):
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)
        font_face = self.GetFont()
        font_color = self.GetForegroundColour()
        dc.SetFont(font_face)
        dc.SetTextForeground(font_color)
        dc.DrawText(self.GetLabel(), 0, 0)
    
 
    def OnSize(self, event):
        self.Refresh()
        event.Skip()

class MyText:
    """自定义文本框"""
    def __init__(self, parent, pos, size=(80, 36), readOnly=False):
        self.defaultFontSize = 10  #默认字体大小
        self.TextCtrlColor = 'white'  #文本框的背景色
        self.defaultBorderColoe = '#EAEAEA'  #默认边框颜色

        self.textCtrl, self.border, self.bg = self.__CreateTextCtrl(
            parent, pos, size, self.defaultBorderColoe, readOnly)

    def __CreateTextCtrl(self,
                         parent,
                         pos,
                         size,
                         borderColor,
                         readOnly=True,
                         borderSize=1):
        """创建文本框"""
        border = wx.StaticText(parent, -1, '', size=size, pos=pos)  #创建边框
        border.SetBackgroundColour(borderColor)  #设置边框要展现的颜色
        bg = wx.StaticText(border,
                           -1,
                           '',
                           size=((size[0] - borderSize * 2),
                                 (size[1] - borderSize * 2)),
                           pos=(borderSize, borderSize))
        if readOnly:  #设置文本框是否只读，还有去自带的边框
            style = wx.TE_READONLY | wx.NO_BORDER
        else:
            style = wx.NO_BORDER

        textCtrl = wx.TextCtrl(
            bg,
            -1,
            size=((size[0] - 10), self.defaultFontSize * 2),
            pos=(5, (size[1] - 2 * self.defaultFontSize - borderSize * 2) / 2),
            style=style)
        font = wx.Font(self.defaultFontSize, wx.DEFAULT, wx.NORMAL, wx.NORMAL,
                       False, '微软雅黑')
        textCtrl.SetFont(font)

        if readOnly:
            bg.SetBackgroundColour('rgb(240,240,240)')
            self.TextCtrlColor = 'rgb(240,240,240)'
        else:
            bg.SetBackgroundColour(textCtrl.GetBackgroundColour())
            self.TextCtrlColor = textCtrl.GetBackgroundColour()
        bg.Bind(wx.EVT_LEFT_UP, self.__ClickEvent)
        return textCtrl, border, bg

    def __ClickEvent(self, evt):
        """点击时焦点设置在文本框上"""
        self.textCtrl.SetFocus()

    def SetValue(self, value):
        if not value:
            value = ''
        self.textCtrl.SetValue(value)

    def GetValue(self):
        return self.textCtrl.GetValue()

    def SetBorderColor(self, color):
        self.border.SetBackgroundColour(color)
        self.border.Refresh()

    def SetFontColor(self, color):
        self.textCtrl.SetForegroundColour(color)
        self.textCtrl.SetBackgroundColour(self.TextCtrlColor)

    def SetFont(self, font):
        self.textCtrl.SetFont(font)

    def SetBackgroundColour(self, color):
        self.bg.SetBackgroundColour(color)
        self.textCtrl.SetBackgroundColour(color)
        self.textCtrl.Refresh()


########################################################################
