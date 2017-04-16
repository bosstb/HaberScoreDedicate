#coding=utf-8
from datetime import datetime
import random
import xml.dom.minidom
import os
import time
import requests
from lxml import etree
import leancloud
import xml.dom.minidom
leancloud.init("m52EwT9QyiY7nhoQyR1H1tWI-MdYXbMMI", "KnNNLKrS3XkKHh5jEyfBj5xT")
from selenium import webdriver
#生成100个随机0,1之间的浮点数序列l
l=0.1
l = random.randint(1, 100)
l=float(l)/100
class RealtimeScore(leancloud.Object):
    pass




def test():
    xx = """<xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[fromUser]]></FromUserName>
         <CreateTime>1348831860</CreateTime>
         <MsgType><![CDATA[text]]></MsgType>
         <Content><![CDATA[this is a test]]></Content>
         <MsgId>1234567890123456</MsgId>
         </xml>"""
    doc = xml.dom.minidom.parseString(xx)
    ToUserName = doc.getElementsByTagName("ToUserName")[0].firstChild.data
    FromUserName = doc.getElementsByTagName("FromUserName")[0].firstChild.data
    CreateTime = doc.getElementsByTagName("CreateTime")[0].firstChild.data
    MsgType = doc.getElementsByTagName("MsgType")[0].firstChild.data
    Content = doc.getElementsByTagName("Content")[0].firstChild.data
    MsgId = doc.getElementsByTagName("MsgId")[0].firstChild.data


def scoreDedicate():

    ##这里使用PhantomJS，并配置了一些参数
    # chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # os.environ["webdriver.chrome.driver"] = chromedriver
    # browser = webdriver.Chrome(chromedriver)
    # browser.get("http://www.cnnturk.com/referandum-2017")
    # ##窗口的大小，不设置的话，默认太小，会有问题
    # browser.set_window_size(1400, 900)

    # wait = WebDriverWait(browser, 10)
    a = 1
    while 1 == 1:
        r = requests.get("http://secim.haberler.com/2017/referandum/")
        # driver = webdriver.PhantomJS(executable_path='/bin/phantomjs/bin/phantomjs')  # 如果不方便配置环境变量。就使用phantomjs的绝对路径也可以
        # driver.get('http://image.baidu.com/i?ie=utf-8&word=%E5%91%A8%E6%9D%B0%E4%BC%A6')  # 抓取了百度图片，query：周杰伦
          # 这就是返回的页面内容了，与urllib2.urlopen().read()的效果是类似的，但比urllib2强在能抓取到动态渲染后的内容。
        # time.sleep(20)
        # lis = browser.find_element_by_xpath('/html/body/div[6]/header/div[1]/div/div[2]/div/div[4]/div')
        doc = etree.HTML(r.text)
        dd = doc.xpath('//*[@id="mainChart"]/div/div/div[1]/div[2]/span[3]/text()')
        print dd
        Todo = leancloud.Object.extend('RealtimeScore')
        todo = Todo.create_without_data('58ef1b27827459005245ade6')
        # 这里修改 location 的值
        todo.set('rightOption', dd[0].replace(',', '.'))
        # a = a + 1
        # todo.set('rightOption', str(a))
        dd = doc.xpath('//*[@id="mainChart"]/div/div/div[1]/div[1]/span[2]/text()')
        print dd
        todo.set('leftOption', dd[0].replace(',', '.'))
        todo.save()
        time.sleep(30)
        # driver.quit()

scoreDedicate()