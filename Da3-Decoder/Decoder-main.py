#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-11-10 11:07 PM
# @Author  : William Ji
# @File    : Decoder.py
# @Software: PyCharm

import wx
import wx.html
import wx.lib.agw.hyperlink as hl
import html
from urllib.parse import unquote
import webbrowser
import base64

class Frame(wx.Frame):
    def __init__(self, parent):
        super(Frame, self).__init__(parent, title="Da3-解码器(Decoder)", size=(500, 400))
        self.Center()
        self.Show()

        self.InitUI()

    def InitUI(self):
        self.menubar_0()
        self.dropbox_0()

    def menubar_0(self):
        menubar = wx.MenuBar()

        # 菜单栏
        # 设置文件栏
        filemenu = wx.Menu()

        filemenu.Append(wx.ID_OPEN, '打开(Open)')
        # self.Bind(wx.EVT_MENU, self.open_0)

        filemenu.Append(wx.ID_SAVE, '保存(Save)')
        # self.Bind(wx.EVT_MENU, self.save_0)

        filemenu.AppendSeparator()

        menubar.Append(filemenu, '&文件(File)')

        # 设置编辑栏
        editmenu = wx.Menu()
        editmenu.Append(wx.ID_COPY, '复制(Copy)')
        editmenu.Append(wx.ID_PASTE, '粘贴(Paste)')
        editmenu.Append(wx.ID_CLEAR, '清除(Clear)')
        menubar.Append(editmenu, '&编辑(Edit)')

        # 设置帮助栏
        helpmenu = wx.Menu()

        helpmenu.Append(10, '关于我们(About us)')
        self.Bind(wx.EVT_MENU, self.about_0, id=10)
        helpmenu.Append(11, '支持我们(Support us)')
        self.Bind(wx.EVT_MENU, self.support_0, id=11)
        menubar.Append(helpmenu, '&帮助(Help)')
        self.SetMenuBar(menubar)

    def dropbox_0(self):
        panel = wx.Panel(self, size=(500, 400))
        self.hyperlink_0(panel)
        type_0 = ['HTML Decoder', 'Base64 Decoder', 'URL Decoder']
        cbb_0 = wx.ComboBox(panel, -1, value='Choose Decode Type', pos=(10, 10), choices=type_0, style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.Bind(wx.EVT_COMBOBOX, self.on_cbb0, cbb_0)
        self.apply_button_0(panel)
        self.inputbox_0(panel)
        self.outputbox_0(panel)

    def hyperlink_0(self, panel):
        hyper = hl.HyperLinkCtrl(panel, -1, "Support us", pos=(420, 10), URL="https://paypal.me/pools/c/89vNrrr09D")
        hyper.AutoBrowse(False)
        hyper.SetColours("blue", "blue", "blue")
        hyper.EnableRollover(True)
        self.Bind(hl.EVT_HYPERLINK_LEFT, self.support_0)

    def inputbox_0(self, panel):
        self.t1 = wx.TextCtrl(panel, pos=(10, 60), size=(480, 150), style=wx.TE_MULTILINE)

    def get_input_box_0(self):
        return self.t1.GetValue()

    def outputbox_0(self, panel):
        self.t2 = wx.TextCtrl(panel, pos=(10, 220), size=(480, 150), style=wx.TE_READONLY | wx.TE_MULTILINE)

    def apply_button_0(self, panel):
        apply_button = wx.Button(panel, pos=(405, 30), label="Decode")
        self.Bind(wx.EVT_BUTTON, self.check_decodes, apply_button)

    def check_decodes(self, e):
        type_0 = self.get_type_0()
        text_0 = self.get_input_box_0()

        if type_0 == 'HTML Decoder':
            self.t2.Clear()
            self.t2.SetValue(self.html_decoder(text_0))
        if type_0 == 'Base64 Decoder':
            self.t2.Clear()
            self.t2.SetValue(self.base64_decoder(text_0))
        if type_0 == 'URL Decoder':
            self.t2.Clear()
            self.t2.SetValue(self.URL_decoder(text_0))

    def on_cbb0(self, e):
        self.type_0 = e.GetString()

    def get_type_0(self):
        try:
            return self.type_0
        except:
            pass

    def base64_decoder(self, text):
        try:
            return base64.b64decode(text)
        except:
            self.t2.SetValue('Your Input is Invalid!')

    def html_decoder(self, text):
        try:
            return html.unescape(text)
        except:
            self.t2.SetValue('Your Input is Invalid!')

    def URL_decoder(self, text):
        try:
            return unquote(text)
        except:
            self.t2.SetValue('Your Input is Invalid!')

    def about_0(self, e):
        wx.MessageBox("Author: William Ji\nOrganization: Da3monic Games Inc."
                      "\nDescription: This program is free. Having fun with it.",
                      caption="Author and Credits", style=wx.OK | wx.ICON_INFORMATION)

    def support_0(self, e):
        href = "https://paypal.me/pools/c/89vNrrr09D"
        webbrowser.open(href)

    def doc_0(self, e):
        html = wx.html.HtmlWindow(self)
        html.LoadPage(r"Documentation.html")


'''
    #事件处理？
    def new_0(self, e):

    def open_0(self, e):

    def save_0(self, e):

'''


def main():
    app = wx.App()
    Frame(None)
    app.MainLoop()


if __name__ == '__main__':
    main()



