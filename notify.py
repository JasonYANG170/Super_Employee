# notify.py
import requests
import json
from UserDefined import poststate, UseResultPush, PushToken, shixiseng_state, yizhanchi_state, bosszhipin_state, \
    bosszhipin_poststate, yizhanchi_poststate, shixiseng_poststate, zhilianzhaopin_state, zhilianzhaopin_poststate, \
    maimai_state, maimai_poststate, wubatongcheng_state, wubatongcheng_poststate
from bosszhipin import run_bosszhipin_script
from maimai import run_maimai_script
from system import ResultUrl, successful_deliveries
from shixiseng import run_shixiseng_script
from wubatongcheng import run_wubatongcheng_script
from yizhanchi import run_yizhanchi_script
from zhilianzhaopin import run_zhilianzhaopin_script


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
    notify_zhilianzhaopin_findCount=0
    notify_zhilianzhaopin_successCount=0
    notify_zhilianzhaopin_errorCount=0
    notify_maimai_findCount=0
    notify_maimai_successCount=0
    notify_maimai_errorCount=0
    notify_wubatongcheng_findCount=0
    notify_wubatongcheng_successCount=0
    notify_wubatongcheng_errorCount=0
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
        if(zhilianzhaopin_state==1):
            zhilianzhaopin_findCount, zhilianzhaopin_successCount, zhilianzhaopin_errorCount = run_zhilianzhaopin_script()
            findCount=findCount + zhilianzhaopin_findCount
            notify_zhilianzhaopin_findCount=zhilianzhaopin_findCount
            successCount=successCount + zhilianzhaopin_successCount
            notify_zhilianzhaopin_successCount=zhilianzhaopin_successCount
            errorCount=errorCount + zhilianzhaopin_errorCount
            notify_zhilianzhaopin_errorCount=zhilianzhaopin_errorCount
        if(maimai_state==1):
            maimai_findCount, maimai_successCount,maimai_errorCount = run_maimai_script()
            findCount=findCount + maimai_findCount
            notify_maimai_findCount=maimai_findCount
            successCount=successCount + maimai_successCount
            notify_maimai_successCount=maimai_successCount
            errorCount=errorCount + maimai_errorCount
            notify_maimai_errorCount=maimai_errorCount
        if(wubatongcheng_state==1):
            wubatongcheng_findCount, wubatongcheng_successCount,wubatongcheng_errorCount = run_wubatongcheng_script()
            findCount=findCount + wubatongcheng_findCount
            notify_wubatongcheng_findCount=wubatongcheng_findCount
            successCount=successCount + wubatongcheng_successCount
            notify_wubatongcheng_successCount=wubatongcheng_successCount
            errorCount=errorCount + wubatongcheng_errorCount
            notify_wubatongcheng_errorCount=wubatongcheng_errorCount
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
        notify += ( f"-------------智联招聘数据------------\n"
                    f"找到{notify_zhilianzhaopin_findCount}家公司\n"
                    f"投递成功{notify_zhilianzhaopin_successCount}份，投递失败{notify_zhilianzhaopin_errorCount}份\n")
        if(zhilianzhaopin_poststate==0):
            notify += ( f"您未开启智联招聘投递，本次投递跳过\n")
        notify += ( f"-------------脉脉数据------------\n"
                        f"找到{notify_maimai_findCount}家公司\n"
                        f"投递成功{notify_maimai_successCount}份，投递失败{notify_maimai_errorCount}份\n")
        if(maimai_poststate==0):
            notify += ( f"您未开启脉脉投递，本次投递跳过\n")
        notify += ( f"-------------58同城数据------------\n"
                    f"找到{notify_wubatongcheng_findCount}家公司\n"
                    f"投递成功{notify_wubatongcheng_successCount}份，投递失败{notify_wubatongcheng_errorCount}份\n")
        if(wubatongcheng_poststate==0):
            notify += ( f"您未开启58同城投递，本次投递跳过\n")
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
