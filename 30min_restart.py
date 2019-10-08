#!/usr/bin/python
#  -*- coding: UTF-8 -*-
import psutil
import time
import os
i = 1
while i < 99:
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    command = 'taskkill /F /IM TeamViewer.exe'
    os.system(command)
    time.sleep(3)
    app_dir = r"C:\Program Files (x86)\TeamViewer\TeamViewer.exe"
    os.popen(app_dir)
    print(nowtime + ":  重新启动程序")
    time.sleep(30)