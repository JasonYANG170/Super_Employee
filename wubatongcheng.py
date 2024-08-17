# main_script.py
import requests
import json
from UserDefined import wubatongcheng_poststate, wubatongcheng_clientid, wubatongcheng_Search,deviceName
from system import successful_deliveries,wubatongcheng_SearchUrl,wubatongcheng_PostUrl
def run_wubatongcheng_script():
    # 初始化变量
    wubatongcheng_successCount = 0
    wubatongcheng_errorCount = 0
    wubatongcheng_findCount = 0
    page = 1
    # 请求头
    wubatongcheng_headers = {
        'User-Agent': "okhttp/3.11.0",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip,deflate",
        'net-msg-id': "",
        'x-microservice-name': "APMS",
        'apkbus': "",
        'coordinateType': "10",
        'official': "true",
        'xxzl-cid': "",
        'ua': "21051182C",
        'uuid': "",
        'dirname': "sz",
        'productorid': "1",
        'jumpextra': "{\"spm\":\"\",\"utm_source\":\"\"}",
        'marketchannelid': "1366",
        'osv': "14",
        '58clientid': wubatongcheng_clientid,
        'brand': "Xiaomi",
        'apn': "WIFI",
        'deny': "1.875",
        'firstopentime': "",
        'netType': "wifi",
        'rnsoerror': "-1",
        'switchrecommend': "",
        'version': "13.10.2",
        'jumppid': "",
        'push': "0",
        'homemodel': "normal",
        'currentcid': "",
        'buildtime': "",
        'bangbangid': "",
        'xxwxtoken': "",
        'cid': "4",
        'ajkAuthTicket': "",
        'xxzlsid': "",
        'scale': "1",
        'guestImei': "",
        'platform': "android",
        'openudid': "",
        'manufacturer': deviceName,
        'id58': "",
        'PPU': "",
        'sh': "2500",
        'osarch': "arm64-v8a",
        'xxzlcid': "",
        'webua': "Mozilla/5.0 (Linux; U; Android 14; "+deviceName+" Build/UQ1A.240105.004.A1; wv) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/534.30",
        'bundle': "com.wuba",
        'uniqueid': "",
        'totalsize': "",
        'xxaqrid': "",
        'xxwxtokenp': "",
        'product': "58app",
        'sw': "",
        'os': "android",
        'vlocalid': "",
        'r': "",
        'xxzl_deviceid': "",
        'xxzl_smartid': "",
        'xxzl_cid': "",
        '58ua': "58app",
        'clinkid': "",
        'maptype': "2",
        'tp': "",
        'channelid': "",
        'jobreferer': "",
        'bgtype': "58app",
        'ZPBEntryLogType': "",
        'xxzlbbid': "",
        'xxzlxxid': "",
        'zpbpubver': "2.10.0",
        'gsparam': ""
    }
    while True:
        wubatongcheng_Search['page'] = str(page)  # 设置当前页码
        #  response = requests.get(yizhanchi_SearchUrl, params=yizhanchi_Search, headers=headers)
        # 发送 GET 请求
        wubatongcheng_SearchResponse = requests.get(wubatongcheng_SearchUrl, params=wubatongcheng_Search, headers=wubatongcheng_headers)
        # payload = json.dumps(wubatongcheng_Search)
        # wubatongcheng_SearchResponse = requests.post(wubatongcheng_SearchUrl, data=payload, headers=wubatongcheng_headers)
     #   print(wubatongcheng_SearchResponse.text)

        # 检查请求是否成功
        if wubatongcheng_SearchResponse.status_code == 200:
            #  data = wubatongcheng_SearchResponse.json()

            try:
                data = wubatongcheng_SearchResponse.json()
                items = data['jobList']['data']

                if not items:
                    break


                uuid_list = [item['infoID'] for item in items]
                company_list = [item['qyname'] for item in items]
                job_list = [item['title'] for item in items]
                salary_desc_list = [item['xinzi'] for item in items]
                attraction_list = [item['signsList'] for item in items]
                city_list = [item['quyu'] for item in items]

                print("------------58同城-------------")
                print("在58同城平台找到以下岗位，即将为您投递:")
                print("---------------------------------")

                for uuid, company, job, salary_desc, attraction, city in zip(uuid_list, company_list, job_list, salary_desc_list, attraction_list, city_list):
                    attraction_str = json.dumps(attraction, ensure_ascii=False)
                    #  group_items = group_data['msg']['resume']
                    #  deliver_able_list = [item['deliver_able'] for item in group_items]
                    #  group_list = [item['group_uuid'] for item in group_items]

                    #   deliver_able_online = deliver_able_list[0] if len(deliver_able_list) > 0 else False
                    #   deliver_able_local = deliver_able_list[1] if len(deliver_able_list) > 1 else False
                    wubatongcheng_findCount=wubatongcheng_findCount + 1
                    print(f"------------第{wubatongcheng_findCount}家-------------")
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

                    # if (wubatongcheng_poststate == 1 and deliver_able_online) or (wubatongcheng_poststate == 2 and not deliver_able_local and deliver_able_online):
                    #      usegroup = group_list[0]
                    #  elif (wubatongcheng_poststate == 1 and not deliver_able_online and deliver_able_local) or (wubatongcheng_poststate == 2 and deliver_able_local):
                    #      usegroup = group_list[1]
                    #  elif (wubatongcheng_poststate == 0 and (deliver_able_online or deliver_able_local)):
                    #      usegroup = None
                    if (wubatongcheng_poststate==1):
                        wubatongcheng_Postpayload  = {
                            "infoId=uuid&os=android&pt=0&ceping=0&format=json&wechat=0&aiScene=4&ct=4&resumeId=&completeResume=0&deliverySource=8&v=1&curVer=13.10.2&downloadApp=0&appId=1&tjfrom=&synYingcai=0&sidDict="
                        }


                        wubatongcheng_PostResponse = requests.post(wubatongcheng_PostUrl, data=wubatongcheng_Postpayload, headers=wubatongcheng_headers)
                        try:
                            data = wubatongcheng_PostResponse.json()
                            wubatongcheng_wubatongcheng_poststate = data['result']
                            if wubatongcheng_wubatongcheng_poststate == 'ok':
                                wubatongcheng_successCount += 1
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
                            print("58同城中没有相关工作，请尝试放宽筛选")
                            print(f"错误信息: {e}")
                            wubatongcheng_errorCount += 1
                        # print(wubatongcheng_wubatongcheng_poststate)
                    else:
                        if wubatongcheng_poststate == 0:
                            print("您未开启58同城投递，本次投递跳过")
                    # elif wubatongcheng_poststate in [1, 2]:

                    #    print("您已投递过该公司,本次投递跳过")
                # wubatongcheng_Groupid = {'inuuid': uuid}

                # wubatongcheng_GroupResponse = requests.get(wubatongcheng_GroupUrl, params=wubatongcheng_Groupid, headers=wubatongcheng_headers)

                #  if wubatongcheng_GroupResponse.status_code == 200:
                #  group_data = wubatongcheng_GroupResponse.json()



                #  except KeyError as e:
                #  print(f"获取投递状态数据失败: {e}")
                # else:
                #       print(f"投递状态请求失败，HTTP状态码: {wubatongcheng_GroupResponse.status_code}")
            except Exception as e:
                print("58同城中没有相关工作，请尝试放宽筛选")
                print(f"错误信息: {e}")

        else:
            print(f"请求失败，HTTP状态码: {wubatongcheng_SearchResponse.status_code}")
        page += 1

    return wubatongcheng_findCount, wubatongcheng_successCount, wubatongcheng_errorCount
