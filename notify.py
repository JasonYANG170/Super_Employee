# notify.py
import requests
import json
from UserDefined import poststate, UseResultPush, PushToken, shixiseng_state, yizhanchi_state, bosszhipin_state, \
    bosszhipin_poststate, yizhanchi_poststate, shixiseng_poststate
from bosszhipin import run_bosszhipin_script
from system import ResultUrl, successful_deliveries
from shixiseng import run_shixiseng_script
from yizhanchi import run_yizhanchi_script

def send_notifications():
    findCount=0
    successCount=0
    errorCount=0
    notify_shixiseng_findCount=0
    notify_shixiseng_successCount=0
    notify_shixiseng_errorCount=0
    notify_yizhanchi_findCount=0
    notify_yizhanchi_successCount=0
    notify_yizhanchi_errorCount=0
    notify_bosszhipin_findCount=0
    notify_bosszhipin_successCount=0
    notify_bosszhipin_errorCount=0
    notify = "------------Notify---------------\n"
    if poststate in [1, 2]:
        if(shixiseng_state==1):
            shixiseng_findCount, shixiseng_successCount, shixiseng_errorCount = run_shixiseng_script()
            findCount=findCount + shixiseng_findCount
            notify_shixiseng_findCount=shixiseng_findCount
            successCount=successCount + shixiseng_successCount
            notify_shixiseng_successCount=shixiseng_successCount
            errorCount=errorCount + shixiseng_errorCount
            notify_shixiseng_errorCount=shixiseng_errorCount
        if(yizhanchi_state==1):
            yizhanchi_findCount, yizhanchi_successCount, yizhanchi_errorCount = run_yizhanchi_script()
            findCount=findCount + yizhanchi_findCount
            notify_yizhanchi_findCount=yizhanchi_findCount
            successCount=successCount + yizhanchi_successCount
            notify_yizhanchi_successCount=yizhanchi_successCount
            errorCount=errorCount + yizhanchi_errorCount
            notify_yizhanchi_errorCount=yizhanchi_errorCount
        if(bosszhipin_state==1):
            bosszhipin_findCount, bosszhipin_successCount, bosszhipin_errorCount = run_bosszhipin_script()
            findCount=findCount + bosszhipin_findCount
            notify_bosszhipin_findCount=bosszhipin_findCount
            successCount=successCount + bosszhipin_successCount
            notify_bosszhipin_successCount=bosszhipin_successCount
            errorCount=errorCount + bosszhipin_errorCount
            notify_bosszhipin_errorCount=bosszhipin_errorCount
        notify += (f"今日总共找到{findCount}家公司\n"
                   f"投递成功{successCount}份，投递失败{errorCount}份\n"
                   f"-------------实习僧数据------------\n"
                   f"找到{notify_shixiseng_findCount}家公司\n"
                   f"投递成功{notify_shixiseng_successCount}份，投递失败{notify_shixiseng_errorCount}份\n")
        if(shixiseng_poststate==0):
            notify += ( f"您未开启实习僧投递，本次投递跳过\n")
        notify += ( f"-------------易展翅数据------------\n"
                   f"找到{notify_yizhanchi_findCount}家公司\n"
                   f"投递成功{notify_yizhanchi_successCount}份，投递失败{notify_yizhanchi_errorCount}份\n")
        if(yizhanchi_poststate==0):
            notify += ( f"您未开启易展翅投递，本次投递跳过\n")
        notify += ( f"-------------Boss直聘数据------------\n"
                    f"找到{notify_bosszhipin_findCount}家公司\n"
                    f"投递成功{notify_bosszhipin_successCount}份，投递失败{notify_bosszhipin_errorCount}份\n")
        if(bosszhipin_poststate==0):
            notify += ( f"您未开启Boss直聘投递，本次投递跳过\n")
        try:
            notify += "---------成功投递的岗位信息-------\n"
            for delivery in successful_deliveries:
                notify += (f"UUID: {delivery['UUID']}\n"
                           f"公司: {delivery['公司']}\n"
                           f"城市: {delivery['城市']}\n"
                           f"岗位: {delivery['岗位']}\n"
                           f"薪资: {delivery['薪资']}\n"
                           f"福利: {delivery['福利']}\n"
                          # f"投递来自: {delivery['投递来自']}\n"
                           )
            notify += "-------------------------------\n"

        except Exception as e:
            notify += "无\n"

        print(notify)
    else:
        notify += ("-------------------------------\n"
                   "未投递，您已选择不投递任何公司\n"
                   "-------------------------------\n")

    if UseResultPush == 1:
        print("您已经开启推送，即将为您推送投递通知")
        data = {"token": PushToken, "title": "Super Employees投递通知", "content": notify}
        body = json.dumps(data).encode(encoding='utf-8')
        Resultheaders = {'Content-Type': 'application/json'}
        requests.post(ResultUrl, data=body, headers=Resultheaders)
        print("推送完成，任务结束")
    else:
        print("未开启推送，任务结束")
