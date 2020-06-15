#-*- coding:utf-8 -*-

import socket
import struct
import time
import win32api
import os
import re


def getTime(TimeServerAddresses):
    TIME_1970 = 2208988800L
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(3)
    data = '\x1b' + 47 * '\0'
    #TimeServer_ip=socket.gethostbyname('cn.pool.ntp.org')
    #TimeServer_ip='202.118.1.130'
    Port=123
    for address in TimeServerAddresses:
        success=False
        count=0
        while not success and count<3:
            print address,count
            try:
                client.sendto(data, (address, Port))
                data, address = client.recvfrom(1024)
                success=True
            except socket.timeout:
                print 'Request timed out!'
                count=count+1
        if success==True:a
            break
    data_result = struct.unpack('!12I', data)[10]
    data_result -= TIME_1970
    return data_result

def setSystemTime(now_time):
    tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = time.gmtime(now_time)
    win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, 0)
    print "Set System OK!"

def getServerIP():
    res1=os.popen('nslookup cn.pool.ntp.org')
    result1=res1.read()
    addresses=result1.split('\n\n')[1].split('\n')[1][12:].split(',')
    return addresses
    #for address in addresses:
    #    res=os.popen('ping -n 2 '+address)
    #    result=res.read()
    #    received_num=int(re.findall('Received = [0-9]',result)[0].split('=')[1])
    #    if received_num > 1:
    #        break
    #TimeServer=address


if __name__ == '__main__':
    addresses=getServerIP()
    now_time=getTime(addresses)
    setSystemTime(now_time)
    print "%d-%d-%d %d:%d:%d" % time.localtime(now_time)[:6]