# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 19:28:50 2023

@author: laksh
"""

from tkinter import *
from tkinter import ttk
import datetime
import time
import psutil
from psutil._common import BatteryTime

root = Tk()
root.geometry("500x250")
root.title("Laptop Battery Percentage")

style = ttk.Style(root)
style.layout("ProgressBarStyle",
             [("Horizontal.Progressbar.trough",
               {"children": [("Horizontal.Progressbar.pbar",
                              {"side": "right", "sticky": "ns"})],
                "sticky": "nsew"}),
              ("")]
             )