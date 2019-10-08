#!/usr/bin/python
#  -*- coding: UTF-8 -*-
import os
import time
'''
command = 'taskkill /F /IM TeamViewer.exe'
#比如这里关闭QQ进程
os.system(command)

'''

num = "1"
while num < "99":
    exit_code = os.system('ping www.baidu.com')
    if exit_code:
        print("网络异常")
        print(exit_code)
    else:
        pass
        print("网络正常")
        print(exit_code)
        time.sleep(5)
