#coding=utf-8
from datetime import datetime
import random
import xml.dom.minidom
import json
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
class PushRecord(leancloud.Object):
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
    a = 0
    while 1 == 1:
        r = requests.get("https://journo.com.tr/")
        # # driver = webdriver.PhantomJS(executable_path='/bin/phantomjs/bin/phantomjs')  # 如果不方便配置环境变量。就使用phantomjs的绝对路径也可以
        # # driver.get('http://image.baidu.com/i?ie=utf-8&word=%E5%91%A8%E6%9D%B0%E4%BC%A6')  # 抓取了百度图片，query：周杰伦
        #   # 这就是返回的页面内容了，与urllib2.urlopen().read()的效果是类似的，但比urllib2强在能抓取到动态渲染后的内容。
        # # time.sleep(20)
        # # lis = browser.find_element_by_xpath('/html/body/div[6]/header/div[1]/div/div[2]/div/div[4]/div')
        print r.text

        f = open("HTML", "r")
        sql = ''
        while True:
            line = f.readline()
            if line:
                # pass  # do something here
                line = line.strip()
                p = line.rfind('.')
                filename = line[0:p]
                sql = sql + ' ' + line
            else:
                break
        f.close()
        root = etree.HTML(sql)
        print root
        doc = etree.HTML(sql)
        htmls = doc.xpath('/html')
        edata = []
        pushTime = htmls[0].xpath('//*[@id="base-main"]/div[2]/div/div/div[3]/div[2]/div/div[1]/ul/li[1]')
        # data = doc.xpath('//*[@id="base-main"]/div[2]/div/div/div[3]/div[2]/div[3]/div[1]/ul/li[1]')
        targetUser = htmls[0].xpath('//*[@id="base-main"]/div[2]/div/div/div[3]/div[2]/div/div[1]/ul/li[4]/span/span[1]')
        arriveUser = htmls[0].xpath('//*[@id="base-main"]/div[2]/div/div/div[3]/div[2]/div/div[1]/ul/li[4]/span/span[3]')
        clickUser = htmls[0].xpath('//*[@id="base-main"]/div[2]/div/div/div[3]/div[2]/div/div[2]/div[1]/ul/li[4]/span[1]')
        test = htmls[0].xpath('//*[@id="base-main"]/div[2]/div/div/div[3]/div[2]/div/div[2]/div[2]/ul/li[4]/span[1]')
        c = 0
        for item in pushTime:
            b = str((a+50) % 50)
            pushContent = htmls[0].xpath('//*[@id="notify' + b + '"]/text()')
            content = json.loads(pushContent[int(a/50)])
            clickUser1 = htmls[0].xpath('//*[@id="base-main"]/div[2]/div/div/div[3]/div[2]/div[' + str(
                a+2) + ']/div[2]/div[2]/ul/li[4]/span[1]')
            if len(clickUser1) > 0:
                if test[c].text != int(clickUser1[0].text):
                    click = int(clickUser[a].text)
                    if click > 700:
                        aa = 1
                else:
                    #clickUser1 = html.xpath('//*[@id="base-main"]/div[2]/div/div/div[3]/div[2]/div[' + str(a) + ']/div[2]/div[2]/ul/li[4]/span[1]')
                    click = int(clickUser1[0].text)
                    c+=1
            if pushContent[int(a/50)].find('news_id') >= 0:
                newsid = content.get("ios").get("extras").get("news_id")
            else:
                newsid = 0
            ed = (item.text, int(str(arriveUser[a].text)), int(targetUser[a].text), click, newsid,
                  pushContent[int(a/50)].split('"alert":')[1].replace('"', '').replace('}', ''))
            edata.append(ed)
            a += 1
        import xlwt
        workbook = xlwt.Workbook(encoding='utf-8')
        booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
        for i, row in enumerate(edata):
            for j, col in enumerate(row):
                booksheet.write(i, j, col)
        workbook.save('d:\grade.xls')




        return 1
        # todo = PushRecord()
        # todo.set('rightOption', dd[0].replace(',', '.'))
        # # a = a + 1
        # # todo.set('rightOption', str(a))
        # dd = doc.xpath('//*[@id="mainChart"]/div/div/div[1]/div[1]/span[2]/text()')
        # print dd
        # todo.set('leftOption', dd[0].replace(',', '.'))
        # todo.save()
        # time.sleep(30)
        # # driver.quit()

scoreDedicate()