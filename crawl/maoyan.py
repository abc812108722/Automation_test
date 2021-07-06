import requests
import re
from bs4 import BeautifulSoup
import time
import json
import redis
import pymongo
from pymongo import MongoClient

headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45',
    "Cookie": "__mta=49569433.1615345823475.1615359425069.1615359425805.16; uuid_n_v=v1; uuid=26C4B570814E11EB92A4F73F3B1C16A524B26F03D4CA44C1AA6D1D08EDACD5A3; _csrf=5c955765c08d19f3aa8293b6953df21469fe146dc29598e70c3205526cd916c9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1615345823; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1781a1d2d2fc8-0fc7ebe1e6ab3a-5c3f124d-e1000-1781a1d2d2fc8; _lxsdk=26C4B570814E11EB92A4F73F3B1C16A524B26F03D4CA44C1AA6D1D08EDACD5A3; __mta=49569433.1615345823475.1615345823475.1615345826432.2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1615359426; _lxsdk_s=1781ada9363-e72-eb9-4b5%7C%7C23",
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://maoyan.com/board/4?offset=10',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}


film={}
num=1
for i in range(1,10000000):
    time.sleep(1)
    try:
        response=requests.get('https://maoyan.com/films/%s' % i,headers=headers)


        s = BeautifulSoup(response.text,features="html.parser")

        if s.select('div.wrapper'):
            film['序号'] = num
            film['名称']=s.select('h1.name')[0].text
            a=''
            for i in s.select('a.text-link'):
                a=a+str(i.text)
            film['标签']=a.replace(' ','')
            film['产地/时长']=s.select('li.ellipsis')[1].text
            film['上映日期地点']=s.select('li.ellipsis')[2].text
            film['简介']=s.select('span.dra')[0].text
            film['评分']=s.select('span.stonefont')[0].text
            # pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
            # r = redis.Redis(connection_pool=pool)

            # r.set(film['名称'],"标签:"+film['标签']+'   '+'产地/时长:'+film['产地/时长']+'   '+'上映:'+film['上映日期地点']+'   '+'简介:'+film['简介'])
            # with open('film.txt','a',encoding='utf-8') as f:
                # f.write(json.dumps(film,ensure_ascii=False)+'\n')
            client=pymongo.MongoClient(host="localhost",port=27017)
            db=client.test
            collections=db.t

            collections.insert({"名称":film["名称"],"标签":film["标签"]})
            num += 1
            print(num)
        else:
            continue
    except Exception as e:
        print(e)


