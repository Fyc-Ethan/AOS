import threading
import time
import math
import numpy as np


def root_of_square(a,b,c):
    '''solve the quadratic equation'''
    discr=pow(b,2)-4*a*c
    if a!=0 and  discr>0:
        x1=(-b+math.sqrt(discr))/(2*a)
        x2=(-b-math.sqrt(discr))/(2*a)
        return x1,x2
    elif a!=0 and discr==0:
        return -b/(2*a)
    elif a!=0 and discr<0:
        x1=str(-b/(2*a))+"+"+str(math.sqrt(-discr)/(2*a))+"i"
        x2=str(-b/(2*a))+"-"+str(math.sqrt(-discr)/(2*a))+"i"
        return x1,x2
    elif a==0 and b!=0:
        return -c/b
    else:
        return "no solution"


def time1():
    global g_num
    while(True):
        mutex.acquire()
        if g_num > 100000:
            mutex.release()
               # print(g_num)
            break
        g_num += 1
            # print(g_num)
        a = np.random.randint(1,10)
        b = np.random.randint(0,10)
        c = np.random.randint(0,10)
        num = root_of_square(a,b,c)
        # print(num)
        mutex.release()
    # print('---第一个进程改动的值,g_num in %d---' % g_num)


def time2():
    global g_num
    while(True):
        mutex.acquire()
        if g_num > 100000:
            mutex.release()
               # print(g_num)
            break
        g_num += 1
            # print(g_num)
        a = np.random.randint(1,10)
        b = np.random.randint(0,10)
        c = np.random.randint(0,10)
        num = root_of_square(a,b,c)
        # print(num)
        mutex.release()
            
    # print('---第二个进程改动的值,g_num in %d---' % g_num)

if __name__=="__main__":
    g_num = 0
    a=300
    b=-18
    c=2
    
    mutex = threading.Lock()
    oldtime=time.time()
    
    t1 = threading.Thread(target=time1)
    t1.start()

    newtime=time.time() 
    while len(threading.enumerate()) != 1:
        time.sleep(0.00000000000000000000000001)
        # print(g_num)
    print (f"相差：{(newtime-oldtime)*1000}ms")

'''
g_num: 0
---in work1,g_num in 1000000---
---in work2,g_num in 2000000---
2个线程对同一个变量操作之后的最终结果：2000000
'''
