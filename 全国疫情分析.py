# -- coding: utf-8 --
import requests
import json
import datetime
import time


def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,30,0);



while (1):
    #疫情API
    json_text = requests.get("https://tianqiapi.com/api?version=epidemic&appid=88239943&appsecret=3oPsPEGO", params={'appid':'88239943' ,'appsecret':'3oPsPEGO'}).content
    # 取出疫情API json格式里的部分数据
    data = json.loads(json_text)
    city=data['data']['list']
    city_t=str(city)
    city_o=city_t.replace('[',' ').replace(',','\n ')
    #area=data['data']['area']['cityName']
    print(city_o)
   # print(area)
    time.sleep(second)
    break
