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
            nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            exit_code = os.system('ping www.baidu.com>con')
            name = Process.prco(self)
            if name == "yes":
                #print("程序运行正常")
                if exit_code:
                    #print("网络异常")
                    command = 'taskkill /F /IM TeamViewer.exe'
                    os.system(command)
                    print("网络异常TV进程结束，一分钟后重启TV")
                    time.sleep(60)
                else:
                    pass
                    #print("网络正常")

            else:
                command = 'taskkill /F /IM TeamViewer.exe'
                os.system(command)
                time.sleep(3)
                app_dir = r"C:\Program Files (x86)\TeamViewer\TeamViewer.exe"
                os.popen(app_dir)
                print(nowtime + ":  重新启动程序")
                time.sleep(30)
            #time.sleep(30)
start=Listens()
start.listening()


