import threading
import time

g_num = 0


def time1():
    global g_num
    while(True):
        mutex.acquire()
        if g_num > 10:
            # print(g_num)
            mutex.release()
            break
        g_num += 1
        # print(g_num)
        mutex.release()
    # print('---第一个进程改动的值,g_num in %d---' % g_num)


def time2():
    global g_num
    while(True):
        mutex.acquire()
        if g_num > 10:
               # print(g_num)
            mutex.release()
            break
        g_num += 2
        # print(g_num)
        mutex.release()
            
    # print('---第二个进程改动的值,g_num in %d---' % g_num)


print('---线程创建之前g_num: %d' % g_num)

mutex = threading.Lock()
t1 = threading.Thread(target=time1)
t2 = threading.Thread(target=time2)
t1.start()
t2.start()

while len(threading.enumerate()) != 1:
    time.sleep(0.00000000000000000000000001)
    # print(g_num)


print('2个线程对同一个变量操作之后的最终结果：%d' % g_num)

'''
g_num: 0
---in work1,g_num in 1000000---
---in work2,g_num in 2000000---
2个线程对同一个变量操作之后的最终结果：2000000
'''
