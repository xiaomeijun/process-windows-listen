#!/usr/bin/python
#  -*- coding: UTF-8 -*-
import psutil
import time
import os
class Process:
    def prco(self):
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            if p.name() == "TeamViewer.exe":
                name="yes"
                return name

class Listens(Process):
    def listening(self):
        a = 1
        while a < 99:
            name = Process.prco(self)
            if name == "yes":
                print("程序运行正常")
            else:
                nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                app_dir = r"C:\Program Files (x86)\TeamViewer\TeamViewer.exe"
                os.popen(app_dir)
                print(nowtime + ":  程序启动了")
            time.sleep(5)
start=Listens()
start.listening()

'''
def start():
    startup = Listens
    startup.listening()
if __name__ == '__start__':
    start()
'''