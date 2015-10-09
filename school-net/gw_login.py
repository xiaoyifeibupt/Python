#!/usr/local/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import hashlib
import re, sys

def login(usr, pwd, url = "http://gw.bupt.edu.cn"):
    # 初始化表单
    data = {}
    data["DDDDD"] = usr
    data["upass"] = calpwd(pwd)
    data["R1"] = "0"
    data["R2"] = "1"
    data["para"] = "00"
    data["0MKKey"] = "123456"
    data = urllib.urlencode(data)
    req=urllib2.Request(url, data)
    response = urllib2.urlopen(req, data)
    rsp = response.read()

    temp = re.findall(r"You have successfully logged into our system.", rsp)
    if not temp:
        ip = re.findall(r"xsele=0;xip='(\d+\.\d+\.\d+\.\d+)\s*';", rsp)
        ans = raw_input("该账号正在IP为：%s 的机器上使用，是否断开它的连接并重新输入用户名和密码登陆本机。(Y / N)\n" % ip[0])
        if ans=='Y' or ans=='y':
            data = {}
            data["DDDDD"] = usr
            data["upass"] = pwd
            data["passplace"] = ""
            data["AMKKey"] = ""
            data = urllib.urlencode(data)
            req=urllib2.Request(url+"/all.htm", data)
            response = urllib2.urlopen(req, data)
            rsp = response.read()
            print "登陆成功"
        else:
            print "终止登陆，登录失败"
    else:
        print "登陆成功"

def calpwd(init_pwd):
    pid = '1'
    calg='12345678'
    tmp = pid + init_pwd + calg
    pwd = hashlib.md5(tmp).hexdigest() + calg + pid
    return pwd

if __name__=='__main__':
    if len(sys.argv)==3:
        usrname = sys.argv[1]
        passwd = sys.argv[2]
    else:
        usrname = ''
        passwd = ''
    login(usrname, passwd)