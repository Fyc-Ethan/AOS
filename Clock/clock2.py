#!/usr/bin/python
#-*- coding:utf-8 -*-


import os
import threading
import time


def start_cache():
    global t
    #os.popen('cp a.txt a.txt'+str(t))
    os.system("python E:\Anaconda\Code\操作系统作业\Count_time.py")
    global timer
    timer = threading.Timer(3,start_cache,[])
    print('start again ...')
    print(f'运行次数为：第{t}次')
    t += 1
    timer.start()
    if(t > 3):
        print('''

quit ...
        ''')
        os._exit(0)
def main():
    timer = threading.Timer(3,start_cache,[])
    print('start...')
    timer.start()


if __name__=='__main__':
    t = 1
    main()