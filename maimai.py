# main_script.py
import requests
import json
from UserDefined import maimai_poststate, maimai_Cookie, maimai_Search, deviceName, maimai_Token
from system import successful_deliveries,maimai_SearchUrl,maimai_PostUrl
def run_maimai_script():
    # 初始化变量
    maimai_successCount = 0
    maimai_errorCount = 0
    maimai_findCount = 0
    page = 1
    # 请求头
    maimai_headers = {
        'User-Agent': "ReactNative//{"+deviceName+"} [Android 14/34]/MaiMai 6.6.10(60610)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'content-type': "application/x-www-form-urlencoded",
        'x-maimai-reqid': "776e6ed0252b42bfba9c0772b4d574cf",
        'Cookie': maimai_Cookie
    }
    while True:
        maimai_Search['page'] = str(page)  # 设置当前页码
        #  response = requests.get(yizhanchi_SearchUrl, params=yizhanchi_Search, headers=headers)
        # 发送 GET 请求
        maimai_SearchResponse = requests.get(maimai_SearchUrl, params=maimai_Search, headers=maimai_headers)
    # payload = json.dumps(maimai_Search)
    # maimai_SearchResponse = requests.post(maimai_SearchUrl, data=payload, headers=maimai_headers)
        # print(maimai_SearchResponse.text)

        # 检查请求是否成功
        if maimai_SearchResponse.status_code == 200:
            #  data = maimai_SearchResponse.json()

            try:
                data = maimai_SearchResponse.json()
                items = data['data']

                if not items:
                    break


                uuid_list = [item['ejid'] for item in items]
                company_list = [item['company'] for item in items]
                job_list = [item['position'] for item in items]
                salary_desc_list = [item['salary_info'] for item in items]
                attraction_list = [item['custom_text'] for item in items]
                city_list = [item['city'] for item in items]

                print("------------脉脉-------------")
                print("在脉脉平台找到以下岗位，即将为您投递:")
                print("---------------------------------")

                for uuid, company, job, salary_desc, attraction, city in zip(uuid_list, company_list, job_list, salary_desc_list, attraction_list, city_list):
                    attraction_str = json.dumps(attraction, ensure_ascii=False)
                    #  group_items = group_data['msg']['resume']
                    #  deliver_able_list = [item['deliver_able'] for item in group_items]
                    #  group_list = [item['group_uuid'] for item in group_items]

                    #   deliver_able_online = deliver_able_list[0] if len(deliver_able_list) > 0 else False
                    #   deliver_able_local = deliver_able_list[1] if len(deliver_able_list) > 1 else False
                    maimai_findCount=maimai_findCount + 1
                    print(f"------------第{maimai_findCount}家-------------")
                    print(f"UUID: {uuid}")
                    print(f"公司: {company}")
                    print(f"城市: {city}")
                    print(f"岗位: {job}")
                    print(f"薪资: {salary_desc}")
                    print(f"福利: {attraction_str}")
                    #  print(f"在线简历投递状态: {'可投递' if deliver_able_online else '不可投递'}")
                    #  print(f"本地简历投递状态: {'可投递' if deliver_able_local else '不可投递'}")
                    print("-------------Result---------------")
                    # usegroup = None  # 初始化 usegroup

                    # if (maimai_poststate == 1 and deliver_able_online) or (maimai_poststate == 2 and not deliver_able_local and deliver_able_online):
                    #      usegroup = group_list[0]
                    #  elif (maimai_poststate == 1 and not deliver_able_online and deliver_able_local) or (maimai_poststate == 2 and deliver_able_local):
                    #      usegroup = group_list[1]
                    #  elif (maimai_poststate == 0 and (deliver_able_online or deliver_able_local)):
                    #      usegroup = None
                    if (maimai_poststate==1):
                        maimai_Postpayload  = {
                            'access_token': maimai_Token,
                            'appid': "3",
                            'channel': "MyAPP",
                            'ejid': uuid,
                            'fr': "big_search_job_tab",
                            'resume_check': "0",
                            'rn': "1",
                            'u': "",
                            'version': "6.6.10",
                            'webviewUserAgent': "Mozilla/5.0 (Linux; Android 14; 21051182C Build/UQ1A.240105.004.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.40 Safari/537.36"
                        }


                        maimai_PostResponse = requests.post(maimai_PostUrl, data=maimai_Postpayload, headers=maimai_headers)
                        try:
                            data = maimai_PostResponse.json()
                            maimai_maimai_poststate = data['result']
                            if maimai_maimai_poststate == 'ok':
                                maimai_successCount += 1
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
                        except Exception as e:
                            print("脉脉中没有相关工作，请尝试放宽筛选")
                            print(f"错误信息: {e}")
                            maimai_errorCount += 1
                           # print(maimai_maimai_poststate)
                    else:
                        if maimai_poststate == 0:
                            print("您未开启脉脉投递，本次投递跳过")
                    # elif maimai_poststate in [1, 2]:

                    #    print("您已投递过该公司,本次投递跳过")
                # maimai_Groupid = {'inuuid': uuid}

                # maimai_GroupResponse = requests.get(maimai_GroupUrl, params=maimai_Groupid, headers=maimai_headers)

                #  if maimai_GroupResponse.status_code == 200:
                #  group_data = maimai_GroupResponse.json()



                #  except KeyError as e:
                #  print(f"获取投递状态数据失败: {e}")
                # else:
                #       print(f"投递状态请求失败，HTTP状态码: {maimai_GroupResponse.status_code}")
            except Exception as e:
                print("脉脉中没有相关工作，请尝试放宽筛选")
                print(f"错误信息: {e}")

        else:
            print(f"请求失败，HTTP状态码: {maimai_SearchResponse.status_code}")
        page += 1

    return maimai_findCount, maimai_successCount, maimai_errorCount
