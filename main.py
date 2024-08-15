from notify import send_notifications
from system import ResultUrl, successful_deliveries,version
from update import check_for_update
needupdate, tag_name, html_url, body = check_for_update(version)
if(needupdate==0):
    send_notifications()
else:
    print("-------------发现新版本--------------")
    # 打印结果
    print("当前版本:", version)
    print("新版本:", tag_name)
    print("更新地址:", html_url)
    print("更新内容:", body)
    print("------------------------------------")
