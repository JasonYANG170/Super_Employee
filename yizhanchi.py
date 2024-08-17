import json
import requests
from datetime import datetime
import time
from UserDefined import yizhanchi_Search, yizhanchi_city, deviceName, yizhanchi_poststate, yizhanchi_Cookie, \
    yizhanchi_postnumber
from system import yizhanchi_SearchUrl, yizhanchi_PostUrl, successful_deliveries, yizhanchi_CitylistUrl

def run_yizhanchi_script():
    yizhanchi_findCount = 0
    yizhanchi_successCount = 0
    yizhanchi_errorCount = 0
    page = 1
    headers = {
        'User-Agent': f"Mozilla/5.0 (Linux; Android 14; {deviceName} Build/UQ1A.240505.004.A1; wv) AppleWebKit/539.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36 XWEB/1170117 MMWEBSDK/20240301 MMWEBID/1139 MicroMessenger/8.0.49.2685(0x28003145) WeChat/arm64 Weixin GPVersion/1 Android Tablet NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        'Accept-Encoding': "gzip,compress,br,deflate",
        'charset': "utf-8",
        'content-type': "application/json; charset=UTF-8",
        'timestamp': str(int(time.time() * 1000)),
        'Cookie': yizhanchi_Cookie,
        'appkey': "yizhanchi",
        'version': "H5_3.3.3",
        'Referer': "https://m.izhanchi.com/",
        'Accept-Language': "zh-CN,zh-SG;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5"
    }

    response = requests.get(yizhanchi_CitylistUrl, headers=headers)
    data = response.json()

    yizhanchi_city_id = None
    for item in data["data"]:
        if item["name"] == yizhanchi_city:
            yizhanchi_city_id = item["id"]
            break

    if yizhanchi_city_id is not None:
        print(f'{yizhanchi_city}的id值是: {yizhanchi_city_id}')
    else:
        print(f'没有找到 name 为 "{yizhanchi_city}" 的数据')
        return yizhanchi_findCount, yizhanchi_successCount, yizhanchi_errorCount

    yizhanchi_Search['region_id'] = f"{yizhanchi_city_id}"

    while True:
        yizhanchi_Search['page'] = str(page)  # 设置当前页码
        response = requests.get(yizhanchi_SearchUrl, params=yizhanchi_Search, headers=headers)
        data = response.json()
        items = data['data']['data']

        if yizhanchi_successCount>=yizhanchi_postnumber:
            break
        if not items:
            break

        sorted_items = sorted(items, key=lambda x: datetime.strptime(x['refreshtime'], "%Y-%m-%d %H:%M:%S"), reverse=True)
        print("------------易展翅-------------")
        print("在易展翅平台找到以下岗位，即将为您投递:")
        print("---------------------------------")

        for item in sorted_items:
            city_name = item['city_name']
            area_name = item['area_name']
            second_area_name = item['second_area_name']

            if '深圳' in [city_name, area_name, second_area_name]:
                yizhanchi_findCount += 1
                print(f"------------第{yizhanchi_findCount}家-------------")
                positionid = item['positionid']
                companyname = item['companyname']
                positionname = item['positionname']
                salary_name = item['salary_name']
                refreshtime = item['refreshtime']
                position_strongpoint = item['position_strongpoint']
                print(f"UUID: {positionid}")
                print(f"公司: {companyname}")
                print(f"城市: {city_name}")
                print(f"岗位: {positionname}")
                print(f"薪资: {salary_name}")
                print(f"福利: {position_strongpoint}")
                print(f"HR刷新时间: {refreshtime}")
                print("-------------Result---------------")

                if yizhanchi_poststate == 1:
                    yizhanchi_postparams = {
                        'attachment_id': "",
                        'qiniu_id': "",
                        'is_top': "1",
                        'deliery_source': "4",
                        'specific_source': "",
                        'source': ""
                    }
                    yizhanchi_Postresponse = requests.get(yizhanchi_PostUrl + positionid, params=yizhanchi_postparams, headers=headers)
                    data = yizhanchi_Postresponse.json()
                    yizhanchi_yizhanchi_poststate = data['message']
                    if yizhanchi_yizhanchi_poststate == '投递成功':
                        yizhanchi_successCount += 1
                        delivery_info = {
                            "UUID": positionid,
                            "公司": companyname,
                            "城市": city_name,
                            "岗位": positionname,
                            "薪资": salary_name,
                            "福利": position_strongpoint,
                        }
                        successful_deliveries.append(delivery_info)
                    else:
                        yizhanchi_errorCount += 1
                        print("投递失败，请查看返回信息:")
                        print(yizhanchi_yizhanchi_poststate)
                else:
                    print("您未开启易展翅投递，本次投递跳过")

        page += 1  # 页码自增

    return yizhanchi_findCount, yizhanchi_successCount, yizhanchi_errorCount
