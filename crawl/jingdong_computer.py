from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium. webdriver. common. by import By
from selenium .webdriver.support import expected_conditions as EC
from selenium .webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time
import pymongo
from pymongo import MongoClient


b=webdriver.Chrome()
wait=WebDriverWait(b,10)
keyword="笔记本电脑"
produce={}
client=pymongo.MongoClient(host="localhost",port=27017)
db=client.jingdong_computer
collections=db.computer

b.get("https://www.jd.com/")
input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#key")))
input.send_keys(keyword)
button=b.find_element_by_xpath("//button['aria-label=搜索']")
button.click()


for i in range(1,101):
    print(i)
    time.sleep(2)
    # input_1 = b.find_element_by_xpath('//input["class=input-txt"]')
    input_1=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div#J_bottomPage input.input-txt')))
    # button_1 = b.find_element_by_xpath('//a["class=btn-default"]')
    button_1=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div#J_bottomPage a.btn-default')))
    input_1.send_keys(i)
    button_1.click()
    time.sleep(2)
    h=BeautifulSoup(b.page_source,features="html.parser")
    for i in h.select('div#J_goodsList .gl-warp li'):
        produce['name']=i.select('.p-name i')[0].string
        produce['price']=i.select('.p-price i')[0].string
        produce['commit']=i.select('.p-commit a')[0].string
        # produce['shop']=i.select('.J_im_icon a')[0].string
        collections.insert({"name": produce["name"], "price": produce["price"],'commit':produce['commit']})



#price=h.select("div#J_goodsList .gl-item div.p-price i")
#name=h.select("div#J_goodsList .gl-item .p-name em")
#commit=h.select("div#J_goodsList .gl-item .p-commit a")
#shop=h.select("div#J_goodsList .gl-item .J_im_icon a")

