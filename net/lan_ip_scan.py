#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix
# created time: Fri 10 Feb 2017 03:34:36 PM CST

import platform
import sys
import os
import time
import thread

ip_list = []
ip_list_lock = thread.allocate_lock()

def check_ip(ipaddr):
    addr = ipaddr.strip().split('.')  #切割IP地址为一个列表
    if len(addr) != 4:  #切割后列表必须有4个参数
        print "check ip address failed!"
        sys.exit()

    for i in range(4):
        try:
            addr[i] = int(addr[i])  #每个参数必须为数字，否则校验失败
        except:
            print "check ip address failed!"
            sys.exit()
        if addr[i] <= 255 and addr[i] >= 0:    #每个参数值必须在0-255之间
            pass
        else:
            print "check ip address failed!"
            sys.exit()
        i += 1
    else:
        print "check ip address success!"

def get_os():
    '''
    get os
    '''
    os = platform.system()
    if os == "Windows":
        return "n"
    else:
        return "c"

def ping_ip(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),
           "1", ip_str]
    output = os.popen(" ".join(cmd)).readlines()

    flag = False
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >= 0:
            flag = True
            break
    if flag:
        ip_list_lock.acquire()
        ip_list.append(ip_str)
        ip_list_lock.release()

def find_ip(ip_prefix):
    '''
    给出当前的127.0.0 ，然后扫描整个段所有地址
    '''
    sys.stdout.write("Scanning start ")
    sys.stdout.flush()
    for i in range(1, 256):
        ip = '%s.%s'%(ip_prefix, i)
        thread.start_new_thread(ping_ip, (ip,))
        time.sleep(0.3)
        sys.stdout.write(".")
        sys.stdout.flush()
    print ""

if __name__ == "__main__":
    if  len(sys.argv) != 2:  #传参加本身长度必须为2
        print "Example: %s 10.0.0.1 "%sys.argv[0]
        sys.exit()
    else:
        check_ip(sys.argv[1])  #满足条件调用校验IP函数

    print "start time %s"%time.ctime()
    args = sys.argv[1]

    ip_prefix = '.'.join(args.split('.')[:-1])
    find_ip(ip_prefix)

    print "All alive IPs:"
    ip_list_lock.acquire()
    for ip in ip_list:
        print ip
    ip_list_lock.release()
    print "end time %s"%time.ctime()
