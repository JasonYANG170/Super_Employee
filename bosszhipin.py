
import time
import requests
import json
from UserDefined import bosszhipin_city, bosszhipin_Search, bosszhipin_poststate, bosszhipin_Cookie, \
    bosszhipin_postnumber
from system import Bosszhipin_CitylistUrl, Bosszhipin_SearchUrl, successful_deliveries, Bosszhipin_PostUrl


def run_bosszhipin_script():
    # 初始化计数器
    bosszhipin_findCount = 0
    bosszhipin_successCount = 0
    bosszhipin_errorCount = 0
    page = 1

    # 请求头
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 14; 21051182C Build/UQ1A.240105.004.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 XWEB/1160117 MMWEBSDK/20240501 MMWEBID/1136 MicroMessenger/8.0.49.2685(0x28003145) WeChat/arm64 Weixin GPVersion/1 Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
        'Accept-Encoding': "gzip, deflate",
        'traceid': "F-e38d9aCURcZEnWMK",
        'x-requested-with': "XMLHttpRequest",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.zhipin.com/",
        'accept-language': "zh-CN,zh-SG;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5",
        'Cookie': bosszhipin_Cookie  # 将这个替换为你的实际cookie
    }

    # 发送GET请求获取城市代码
    response = requests.get(Bosszhipin_CitylistUrl, headers=headers)
    data = response.json()

    # 遍历 cityGroup 查找 name 为bosszhipin_city的城市对应的 code
    city_code = None
    for group in data['zpData']['cityGroup']:
        for city in group['cityList']:
            if city['name'] == bosszhipin_city:
                city_code = city['code']
                break
        if city_code is not None:
            break

    print(f"{bosszhipin_city}的code值:", city_code)
    try:
        while True:
            bosszhipin_Search['page'] = str(page)  # 设置当前页码
            response = requests.get(Bosszhipin_SearchUrl, params=bosszhipin_Search, headers=headers)
            data = response.json()
            print(response.text)
            item_list = data['zpData']['jobList']

            if bosszhipin_successCount>=bosszhipin_postnumber:
                break
            if not item_list:
                break

            print("------------Boss直聘-------------")
            print("在Boss直聘平台找到以下岗位，即将为您投递:")
            print("---------------------------------")

            for item in item_list:
                bosszhipin_findCount += 1
                print(f"------------第{bosszhipin_findCount}家-------------")
                encryptJobId = item.get('encryptJobId')
                brandName = item.get('brandName')
                jobName = item.get('jobName')
                cityName = item.get('cityName')
                salaryDesc = item.get('salaryDesc')
                securityId = item.get('securityId')
                welfareList=item.get('welfareList')
                lid = item.get('lid')

                print(f"UUID: {encryptJobId}")
                print(f"公司: {brandName}")
                print(f"城市: {cityName}")
                print(f"岗位: {jobName}")
                print(f"薪资: {salaryDesc}")
                print(f"福利: {welfareList }")
               # print(f"HR刷新时间: {lid}")
                print("-------------Result---------------")
                if(bosszhipin_poststate==1):
                    bosszhipin_postparams = {
                        "securityId": securityId,
                        "jobId": encryptJobId,
                        "lid": lid
                    }
                    bosszhipin_Postresponse = requests.get(Bosszhipin_PostUrl, params=bosszhipin_postparams, headers=headers)
                    data = bosszhipin_Postresponse.json()
                    bosszhipin_bosszhipin_poststate = data['message']
                    if bosszhipin_bosszhipin_poststate == '投递成功':
                        bosszhipin_successCount += 1
                        delivery_info = {
                            "UUID": encryptJobId,
                            "公司": brandName,
                            "城市": cityName,
                            "岗位": jobName,
                            "薪资": salaryDesc,
                            "福利": welfareList,
                        }
                        successful_deliveries.append(delivery_info)
                    else:
                        bosszhipin_errorCount += 1
                        print("投递失败，请查看返回信息:")
                        print(bosszhipin_bosszhipin_poststate)
                else:
                    print("您未开启Boss直聘投递，本次投递跳过")
                # 投递逻辑在这里添加
           # time.sleep(10)
            page += 1  # 页码自增
    except Exception as e:
        print("Boss直聘Cookie失效，请更新Cookie")
        print(f"错误信息: {e}")

    return bosszhipin_findCount, bosszhipin_successCount, bosszhipin_errorCount
