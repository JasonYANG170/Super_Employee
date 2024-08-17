# main_script.py
import requests
import json
from UserDefined import shixiseng_poststate, shixiseng_Cookie, shixiseng_Search, deviceName, shixiseng_postnumber
from system import successful_deliveries,shixiseng_SearchUrl,shixiseng_GroupUrl,shixiseng_PostUrl
def run_shixiseng_script():
    # 初始化变量
    shixiseng_successCount = 0
    shixiseng_errorCount = 0
    shixiseng_findCount = 0
    page = 1
    # 请求头
    shixiseng_headers = {
        'User-Agent': "sxsandroidapp/4.50.3",
        'devicetoken': "",
        'utm_source': deviceName,
        'jg': "130c83f76128e8b0774",
        'content-type': "application/json; charset=UTF-8",
        'priority': "u=1, i",
        'Cookie': shixiseng_Cookie
    }
    while True:
        shixiseng_Search['p'] = str(page)  # 设置当前页码
      #  response = requests.get(yizhanchi_SearchUrl, params=yizhanchi_Search, headers=headers)
    # 发送 GET 请求
        shixiseng_SearchResponse = requests.get(shixiseng_SearchUrl, params=shixiseng_Search, headers=shixiseng_headers)
   # print(shixiseng_SearchResponse.text)

    # 检查请求是否成功
        if shixiseng_SearchResponse.status_code == 200:
          #  data = shixiseng_SearchResponse.json()

            try:
                data = shixiseng_SearchResponse.json()
                items = data['msg']['data']
                if shixiseng_successCount>=shixiseng_postnumber:
                    break
                if not items:
                    break


                uuid_list = [item['uuid'] for item in items]
                company_list = [item['company'] for item in items]
                job_list = [item['job'] for item in items]
                salary_desc_list = [item['salary_desc'] for item in items]
                attraction_list = [item['attraction'] for item in items]
                city_list = [item['city'] for item in items]

                print("------------实习僧-------------")
                print("在实习僧平台找到以下岗位，即将为您投递:")
                print("---------------------------------")

                for uuid, company, job, salary_desc, attraction, city in zip(uuid_list, company_list, job_list, salary_desc_list, attraction_list, city_list):
                    attraction_str = json.dumps(attraction, ensure_ascii=False)
                    shixiseng_Groupid = {'inuuid': uuid}

                    shixiseng_GroupResponse = requests.get(shixiseng_GroupUrl, params=shixiseng_Groupid, headers=shixiseng_headers)

                    if shixiseng_GroupResponse.status_code == 200:
                        group_data = shixiseng_GroupResponse.json()

                        try:
                            group_items = group_data['msg']['resume']
                            deliver_able_list = [item['deliver_able'] for item in group_items]
                            group_list = [item['group_uuid'] for item in group_items]

                            deliver_able_online = deliver_able_list[0] if len(deliver_able_list) > 0 else False
                            deliver_able_local = deliver_able_list[1] if len(deliver_able_list) > 1 else False
                            shixiseng_findCount=shixiseng_findCount + 1
                            print(f"------------第{shixiseng_findCount}家-------------")
                            print(f"UUID: {uuid}")
                            print(f"公司: {company}")
                            print(f"城市: {city}")
                            print(f"岗位: {job}")
                            print(f"薪资: {salary_desc}")
                            print(f"福利: {attraction_str}")
                            print(f"在线简历投递状态: {'可投递' if deliver_able_online else '不可投递'}")
                            print(f"本地简历投递状态: {'可投递' if deliver_able_local else '不可投递'}")
                            print("-------------Result---------------")
                            usegroup = None  # 初始化 usegroup

                            if (shixiseng_poststate == 1 and deliver_able_online) or (shixiseng_poststate == 2 and not deliver_able_local and deliver_able_online):
                                usegroup = group_list[0]
                            elif (shixiseng_poststate == 1 and not deliver_able_online and deliver_able_local) or (shixiseng_poststate == 2 and deliver_able_local):
                                usegroup = group_list[1]
                            elif (shixiseng_poststate == 0 and (deliver_able_online or deliver_able_local)):
                                usegroup = None
                            if usegroup:
                                shixiseng_Postpayload = json.dumps({
                                    "inuuid": uuid,
                                    "group_uuid": usegroup,
                                    "stype": "attach",
                                    "report_time": "1周内",
                                    "internship_time": "6个月以上",
                                    "days": "5",
                                    "mxa_data": "",
                                    "position": "app_search_xgzw",
                                    "deliver_type": 0
                                })

                                shixiseng_PostResponse = requests.post(shixiseng_PostUrl, data=shixiseng_Postpayload, headers=shixiseng_headers)
                                data = shixiseng_PostResponse.json()
                                shixiseng_shixiseng_poststate = data['msg']['cont']
                                if shixiseng_shixiseng_poststate == 'success':
                                    shixiseng_successCount += 1
                                    delivery_info = {
                                        "UUID": uuid,
                                        "公司": company,
                                        "城市": city,
                                        "岗位": job,
                                        "薪资": salary_desc,
                                        "福利": attraction_str,
                                    #    "投递来自": "在线简历" if usegroup == group_list[0] else "本地简历"
                                    }
                                    successful_deliveries.append(delivery_info)
                                else:
                                    shixiseng_errorCount += 1
                                print(shixiseng_shixiseng_poststate)
                            else:
                                if shixiseng_poststate == 0:
                                    print("您未开启实习僧投递，本次投递跳过")
                                elif shixiseng_poststate in [1, 2]:

                                    print("您已投递过该公司,本次投递跳过")
                        except KeyError as e:
                            print(f"获取投递状态数据失败: {e}")
                    else:
                        print(f"投递状态请求失败，HTTP状态码: {shixiseng_GroupResponse.status_code}")
            except Exception as e:
                print("实习僧中没有相关工作，请尝试放宽筛选")
                print(f"错误信息: {e}")

        else:
            print(f"请求失败，HTTP状态码: {shixiseng_SearchResponse.status_code}")
        page += 1

    return shixiseng_findCount, shixiseng_successCount, shixiseng_errorCount
