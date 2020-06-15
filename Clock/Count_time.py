#python 的标准库手册推荐在任何情况下尽量使用time.clock().
#只计算了程序运行CPU的时间，返回值是浮点数
import time
import os
start =time.time()
os.system("python E:\Anaconda\Code\操作系统作业\subcode.py")
end = time.time()
print('Running time: %s Seconds'%(end-start))