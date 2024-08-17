# main_script.py
import requests
import json
from UserDefined import zhilianzhaopin_poststate, zhilianzhaopin_Cookie, zhilianzhaopin_Search, deviceName, \
    zhilianzhaopin_cvNumber, zhilianzhaopin_Chatstate, zhilianzhaopin_postnumber
from system import successful_deliveries, zhilianzhaopin_SearchUrl, zhilianzhaopin_PostUrl, zhilianzhaopin_Chat


def run_zhilianzhaopin_script():
    # 初始化变量
    zhilianzhaopin_successCount = 0
    zhilianzhaopin_errorCount = 0
    zhilianzhaopin_findCount = 0
    page = 1
    # 请求头
    zhilianzhaopin_headers = {

        'User-Agent': "okhttp/4.10.0",
        'Accept-Encoding': "gzip",
        'x-zp-utm-client-version': "u",
        'x-zp-departmentid': "",
        'x-zp-oaid': "",
        'x-zp-rt': "",
        'x-zp-client-id': "",
        'x-zp-version': "8.11.26",
        'x-zp-channel': "tengxun",
        'x-zp-t': "1723836321157",
        'x-zp-client-type': "a",
        'x-zp-page-code': "5019",
        'x-zp-business-system': "95",
        'x-zp-device-id': "",
        'x-zp-user-role': "PERSONALLY",
        'x-zp-at': "51fb6d8c840b490ebd3bb476dc53e229",
        'x-zp-user-agent': "Mozilla/5.0 (Linux; Android 14; "+deviceName+" Build/UQ1A.240105.004.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.25 Safari/537.36",
        'x-zp-rf': "t",
        'accept-language': "zh-SG,zh;q=0.8",
        'x-zp-zadi': "",
        'x-zp-platform': "4",
        'x-zp-action-id': "",
        'wtoken': "",
        'content-type': "application/json; charset=UTF-8",
        'Cookie': zhilianzhaopin_Cookie
    }
    while True:
        zhilianzhaopin_Search['pageIndex'] = str(page)  # 设置当前页码
        #  response = requests.get(yizhanchi_SearchUrl, params=yizhanchi_Search, headers=headers)
        # 发送 GET 请求
        payload = json.dumps(zhilianzhaopin_Search)
        zhilianzhaopin_SearchResponse = requests.post(zhilianzhaopin_SearchUrl, data=payload, headers=zhilianzhaopin_headers)
        # print(zhilianzhaopin_SearchResponse.text)

        # 检查请求是否成功
        if zhilianzhaopin_SearchResponse.status_code == 200:
            #  data = zhilianzhaopin_SearchResponse.json()

            try:
                data = zhilianzhaopin_SearchResponse.json()
                items = data['data']['list']

                if zhilianzhaopin_successCount>=zhilianzhaopin_postnumber:
                    break
                if not items:
                    break


                uuid_list = [item['number'] for item in items]
                company_list = [item['companyName'] for item in items]
                job_list = [item['name'] for item in items]
                salary_desc_list = [item['salary60'] for item in items]
                attraction_list = [item['welfareTagList'] for item in items]
                city_list = [item['workCity'] for item in items]
                rootCompanyNumber = [item['rootCompanyNumber'] for item in items]
                jobId = [item['jobId'] for item in items]
                companyId= [item['companyId'] for item in items]
                print("------------智联招聘-------------")
                print("在智联招聘平台找到以下岗位，即将为您投递:")
                print("---------------------------------")

                for uuid, company, job, salary_desc, attraction, city in zip(uuid_list, company_list, job_list, salary_desc_list, attraction_list, city_list):
                    attraction_str = json.dumps(attraction, ensure_ascii=False)
                  #  group_items = group_data['msg']['resume']
                  #  deliver_able_list = [item['deliver_able'] for item in group_items]
                  #  group_list = [item['group_uuid'] for item in group_items]

                 #   deliver_able_online = deliver_able_list[0] if len(deliver_able_list) > 0 else False
                 #   deliver_able_local = deliver_able_list[1] if len(deliver_able_list) > 1 else False
                    zhilianzhaopin_findCount=zhilianzhaopin_findCount + 1
                    print(f"------------第{zhilianzhaopin_findCount}家-------------")
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

                   # if (zhilianzhaopin_poststate == 1 and deliver_able_online) or (zhilianzhaopin_poststate == 2 and not deliver_able_local and deliver_able_online):
                   #      usegroup = group_list[0]
                   #  elif (zhilianzhaopin_poststate == 1 and not deliver_able_online and deliver_able_local) or (zhilianzhaopin_poststate == 2 and deliver_able_local):
                   #      usegroup = group_list[1]
                   #  elif (zhilianzhaopin_poststate == 0 and (deliver_able_online or deliver_able_local)):
                   #      usegroup = None

                    if(zhilianzhaopin_Chatstate==1):
                        zhilianzhaopin_Chatparams = {
                            'businessOperation': "POSITION_DETAIL_APPLY",
                            'jobTitle': job,
                            'stSourceCode': "5019",
                            'jobId': jobId,
                            'companyId': companyId,
                            'resumeId': "523222527",
                            'positionChatScene': "1",
                            'stAction': "601",
                            'rootCompanyId': rootCompanyNumber,
                            'resumeNumber': zhilianzhaopin_cvNumber,
                            'staffId': "1117787837",
                            'jobNumber': uuid,
                            'resumeLanguage': "0",
                            'x-zp-utm-client-version': "u",
                            'rt': "dcca32868511402db6106f553f231d3a",
                            'd': "00000000-0543-0650-ffff-ffffef05ac4a",
                            'os_version': "14",
                            'channel': "tengxun",
                            'version': "8.11.26",
                            'platform': "4",
                            'at': "51fb6d8c840b490ebd3bb476dc53e229",
                            'identity': "1",
                            'businessLine': "com.zhaopin.social",
                            'anonymous': "0",
                            'userRole': "0",
                            'oaid': ""
                        }
                        zhilianzhaopin_ChatResponse = requests.get(zhilianzhaopin_Chat, params=zhilianzhaopin_Chatparams, headers=zhilianzhaopin_headers)
                        data = zhilianzhaopin_ChatResponse.json()
                        zhilianzhaopin_zhilianzhaopin_Chatstate = data['message']
                        if zhilianzhaopin_zhilianzhaopin_Chatstate == '成功' and zhilianzhaopin_poststate==0:
                            zhilianzhaopin_successCount += 1
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
                        elif zhilianzhaopin_poststate==0:
                            zhilianzhaopin_errorCount += 1
                    if (zhilianzhaopin_poststate==1):
                        zhilianzhaopin_Postpayload = json.dumps({
                            "st_page": "5019",
                            "st_action": "601",
                            "stSourceCode": "5019",
                            "businessPlatformLabel": "",
                            "businessTagId": "",
                            "deliveryWay": "0",
                            "cycleType": "0",
                            "exposureType": "0",
                            "operatePageCode": "5021",
                            "positionNumbers": uuid,
                            "cityIds": "765",
                            "need5Dot0": "1",
                            "deliveryBusinessType": "0",
                            "ignoreIntention": "1",
                            "ignoreBlackType": "0",
                            "deliveryChannelType": "1",
                            "isfeedback": "1",
                            "attachmentDefaultType": "attachment",
                            "attachmentDefaultFileId": "",
                            "businessOperation": "POSITION_DETAIL_APPLY",
                            "resumeVersion": "1",
                            "resumeNumber": zhilianzhaopin_cvNumber,
                            "language": "3",
                            "x-zp-utm-client-version": "u",
                            "rt": "",
                            "d": "",
                            "os_version": "14",
                            "channel": "tengxun",
                            "version": "8.11.26",
                            "platform": "4",
                            "at": "",
                            "identity": "1",
                            "businessLine": "com.zhaopin.social",
                            "anonymous": "0",
                            "userRole": "0",
                            "oaid": ""
                        })

                        zhilianzhaopin_PostResponse = requests.post(zhilianzhaopin_PostUrl, data=zhilianzhaopin_Postpayload, headers=zhilianzhaopin_headers)
                        data = zhilianzhaopin_PostResponse.json()
                        zhilianzhaopin_zhilianzhaopin_poststate = data['data']['actionValue']
                        if zhilianzhaopin_zhilianzhaopin_poststate == 'SUCCESS':
                            zhilianzhaopin_successCount += 1
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
                            zhilianzhaopin_errorCount += 1
                        print(zhilianzhaopin_zhilianzhaopin_poststate)
                    else:
                        if zhilianzhaopin_poststate == 0:
                            print("您未开启智联招聘投递，本次投递跳过")
                       # elif zhilianzhaopin_poststate in [1, 2]:

                        #    print("您已投递过该公司,本次投递跳过")
                   # zhilianzhaopin_Groupid = {'inuuid': uuid}

                   # zhilianzhaopin_GroupResponse = requests.get(zhilianzhaopin_GroupUrl, params=zhilianzhaopin_Groupid, headers=zhilianzhaopin_headers)

                  #  if zhilianzhaopin_GroupResponse.status_code == 200:
                      #  group_data = zhilianzhaopin_GroupResponse.json()



                  #  except KeyError as e:
                      #  print(f"获取投递状态数据失败: {e}")
                   # else:
                 #       print(f"投递状态请求失败，HTTP状态码: {zhilianzhaopin_GroupResponse.status_code}")
            except Exception as e:
                print("智联招聘中没有相关工作，请尝试放宽筛选")
                print(f"错误信息: {e}")

        else:
            print(f"请求失败，HTTP状态码: {zhilianzhaopin_SearchResponse.status_code}")
        page += 1

    return zhilianzhaopin_findCount, zhilianzhaopin_successCount, zhilianzhaopin_errorCount
