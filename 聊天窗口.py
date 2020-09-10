# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import wx
import time
class qijie(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None,
            title="qijie",
            size=(520, 450),
            pos=(800, 300))
        panel = wx.Panel(frame, -1)
        labelall = wx.StaticText(panel, -1,
            '主窗口',
            pos=(210, 5))
        self.text_all = wx.TextCtrl(panel, -1,
            size=(480, 200),
            pos=(10, 30),
            style=wx.TE_READONLY | wx.TE_MULTILINE)
        labelin = wx.StaticText(panel, -1, '对话框',
            pos=(230, 230))
        self.textlogin = wx.TextCtrl(panel, -1,
            size=(480, 100),
            pos=(10, 260),
            style=wx.TE_MULTILINE)

        self.bt_Sent = wx.Button(panel, -1, "发送",
            size=(75, 25), pos=(130, 370))
        self.Bind(wx.EVT_BUTTON,
            self.OnButtonSent, self.bt_Sent)
        
        self.bt_Clear = wx.Button(panel, -1, "清除",
            size=(75, 25), pos=(230, 370)) 
         
        self.Bind(wx.EVT_BUTTON,
            self.OnButtonClear, self.bt_Clear)
        
        self.bt_Quit = wx.Button(panel, -1, "退出",
            size=(75, 25), pos=(330, 370))
         
        self.Bind(wx.EVT_BUTTON,
            self.OnExit, self.bt_Quit)
         

        frame.Show()
        return True

    def OnButtonSent(self, event):
        userinput = self.textlogin.GetValue()
        self.textlogin.Clear()
        nowtime = time.ctime()
        inmsg = "You (%s) :\n%s \n" % (nowtime, userinput)
        self.text_all.AppendText(inmsg)

    def OnButtonClear(self, event):
        self.text_all.Clear()

   
    
    def OnExit(self,event):
        self.text_all.Close(True)  


if __name__ == "__main__":
    app = qijie()
    app.MainLoop()
