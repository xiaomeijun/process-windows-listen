#!/usr/bin/python
#  -*- coding: UTF-8 -*-
import psutil
import time
import os
from tkinter import *
import threading




def prco():
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == "TeamViewer.exe":
            name="yes"
            return name

def jk():
    a = 1
    while a < 99:
        name=prco()
        if name=="yes":
            print("程序运行正常")
        else:
            nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            app_dir = r"C:\Program Files (x86)\TeamViewer\TeamViewer.exe"
            os.popen(app_dir)
            print(nowtime + ":  程序启动了")
        time.sleep(60)

jk()

'''
top = Tk()
Button(top, width=8,height=2,text='启动监控',anchor='c',relief='ridge',compound='bottom',command=jk).pack()
top.mainloop()
'''

