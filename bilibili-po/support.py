# -*- coding: utf-8 -*-
"""
Created on Mon May 26 23:59:09 2014

@author: Administrator
"""
import urllib
import urllib2
import json
import re
from biclass import * 
def GetRE(content,regexp):
    return re.findall(regexp, content)

def getURLContent(url):
    while True:    	
        flag = 1;
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
            req = urllib2.Request(url = url,headers = headers);   
            content = urllib2.urlopen(req).read();
        except:
        	flag = 0;
        	time.sleep(5)
        if flag == 1:
        	break;
    return content;

def FromJson(url):
    return json.loads(getURLContent(url))

def GetString(t):
    if type(t) == int:
        return str(t)
    return t

#从视频源码获取视频信息
def GetVedioFromRate(content):
    #av号和标题
    regular1 = r'<a href="/video/av(\d+)/" target="_blank" class="title">([^/]+)</a>';
    info1 = GetRE(content,regular1)
    #观看数
    regular2 = r'<i class="gk" title=".*">(\d+)</i>';
    info2 = GetRE(content,regular2)
    #收藏
    regular3 = r'<i class="sc" title=".*">(\d+)</i>';
    info3 = GetRE(content,regular3)
    #弹幕
    regular4 = r'<i class="dm" title=".*">(\d+)</i>';
    info4 = GetRE(content,regular4)
    #日期
    regular5 = r'<i class="date" title=".*">(\d+-\d+-\d+ \d+:\d+)</i>';
    info5 = GetRE(content,regular5)
    #封面
    regular6 = r'<img src="(.+)">';
    info6 = GetRE(content,regular6)
    #Up的id和名字
    regular7 = r'<a class="up r10000" href="http://space.bilibili.tv/(\d+)" target="_blank">(.+)</a>'
    info7 = GetRE(content,regular7)
    #!!!!!!!!这里可以断言所有信息长度相等
    vedioNum = len(info1);#视频长度
    vedioList = [];
    for i in range(vedioNum):
        vedio_t = Vedio();
        vedio_t.aid = int(info1[i][0]);
        vedio_t.title = info1[i][1];
        vedio_t.guankan = int(info2[i]);
        vedio_t.shoucang = int(info3[i]);
        vedio_t.danmu = int(info4[i]);
        vedio_t.date = info5[i];
        vedio_t.cover = info6[i];
        vedio_t.po = User(info7[i][0],info7[i][1])
        vedioList.append(vedio_t);
    return vedioList
