'''
@Description: 
@Author: Sp4ce
@Github: https://github.com/NS-Sp4ce
@Date: 2019-07-15 22:28:12
@LastEditors: Sp4ce
@LastEditTime: 2019-07-17 11:29:50
'''
# -*- coding:utf-8 -*-

import datetime
import os
import re
from random import choice
import requests
from bs4 import BeautifulSoup
import cqplus
'''
USER_AGENTS 随机头信息
为未来做准备
'''

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

headers = {'User-Agent': choice(USER_AGENTS)}  # 随机UA

MAX_TIME_OUT = 3  #超时时间

today = datetime.date.today()  #当前日期

FILENAME = 'C:\\Users\\Administrator\\Desktop\\' + str(today) + '.txt'  #文件名

patternstr = r'(((https|http)?:\/\/)[^\s|(\[\u4e00-\u9fa5\])|\,|\]]+)'  #URL正则


class MainHandler(cqplus.CQPlusHandler):
    def handle_event(self, event, params):
        if event == "on_group_msg":
            msg = params.get("msg")
            from_qq = params.get("from_qq")
            from_group = params.get("from_group")
            msg_id = params.get("msg_id")
            if "[CQ:share" in msg:
                msg = msg.split(",")
                try:
                    pattern = re.compile(patternstr)
                    urls = re.findall(pattern, msg[1])
                    for url in urls:
                        self.logging.debug('模式1检测到URL: ' + url[0])
                        if self.checkFileExists(FILENAME):
                            self.checkUrlInFile(FILENAME, url[0], from_qq,
                                                from_group)
                except:
                    pass
            else:
                try:
                    pattern = re.compile(patternstr)
                    urls = re.findall(pattern, msg)
                    for url in urls:
                        self.logging.debug('模式2检测到URL: ' + url[0])
                        if self.checkFileExists(FILENAME):
                            self.checkUrlInFile(FILENAME, url[0], from_qq,
                                                from_group)
                except:
                    pass

    '''
    检查文件是否存在
    filename 要检查的文件
    '''

    def checkFileExists(self, filename):
        if os.path.exists(filename):
            self.logging.debug('文件' + filename + ' 已存在')
            return True
        else:
            f = open(filename, "w")
            f.close
            self.logging.debug('文件' + filename + ' 不存在，已创建')
            return True

    '''
    检查URL是否在文件中,不存在就写入
    filename 文件名
    url 要检查的url
    '''

    def checkUrlInFile(self, filename, url, from_qq, from_group):
        self.urls = set()
        urls = self.urls  #set() hash自动去重
        #先用set装入url
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                urls.add(line.split("  ")[5])
        self.logging.debug(str(urls))
        if url in urls:
            self.logging.debug('URL: ' + url + ' 已存在')
            self.api.send_group_msg(
                from_group,
                str(datetime.datetime.now()) + "<----> QQ群:" +
                str(from_group) + "<----> QQ: " + str(from_qq) + " <----> " +
                'URL: ' + str(url) + ' 已存在')
        else:
            self.logging.debug('URL: ' + url + ' 不存在于文件' + filename + '中')
            self.logging.debug('文件' + filename + ' 正在写入')
            with open(filename, 'a+') as f:
                f.writelines(
                    str(datetime.datetime.now()) + "  QQ群:  " +
                    str(from_group) + "  QQ:  " + str(from_qq) + "  " +
                    str(url) + "  \n")
            self.logging.debug('文件' + filename + ' 写入成功')
            self.api.send_group_msg(
                from_group,
                str(datetime.datetime.now()) + '<----> QQ群:' +
                str(from_group) + '<----> QQ: ' + str(from_qq) + ' <---->' +
                'URL: ' + str(url) + ' 保存成功')
