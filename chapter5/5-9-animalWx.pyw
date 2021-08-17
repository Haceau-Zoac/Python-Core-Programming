#!/usr/bin/env python

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, title=''):
        wx.Frame.__init__(self, parent, id, title,
            size=(200, 140))
        top = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD)
        lb = wx.StaticText(top, -1,
            '动物（成对的；最少：一对；最多：一打）')
        sizer.Add(lb)
        
        c1 = wx.StaticText(top, -1, '数量：')
        c1.SetFont(font)
        ct = wx.SpinCtrl(top, -1, '2', min=2, max=12)
        sizer.Add(c1)
        sizer.Add(ct)

        c2 = wx.StaticText(top, -1, '种类：')
        c2.SetFont(font)
        cb = wx.ComboBox(top, -1, '',
            choices=('狗', '猫', '仓鼠', '蟒蛇'))
        sizer.Add(c2)
        sizer.Add(cb)

        qb = wx.Button(top, -1, '退出')
        qb.SetBackgroundColour('red')
        qb.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON,
            lambda _: self.Close(True), qb)
        sizer.Add(qb)

        top.SetSizer(sizer)
        self.Layout()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(title='wxWidgets')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

def main():
    app = MyApp()
    app.MainLoop()

if __name__ == '__main__':
    main()