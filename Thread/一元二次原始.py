# -*- coding: utf-8 -*-
 
import math
import sys
import datetime
import time
import numpy as np

def printStar(n):
        for i in range(n):
            sys.stdout.flush()
            time.sleep(1)

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
 
if __name__=="__main__":
    a=300
    b=-18
    c=2
    oldtime=time.time()
    for i in range(10000):
        a = np.random.randint(1,10)
        b = np.random.randint(0,10)
        c = np.random.randint(0,10)        
        root_of_square(float(a),float(b),float(c))
    newtime=time.time()
    print (f"相差：{(newtime-oldtime)*1000}ms")
    printStar(1) 