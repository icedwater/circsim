#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the GUI for the resistor app.
"""
import resistor
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show(True)
app.MainLoop()
