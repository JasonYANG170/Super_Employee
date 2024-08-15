# update.py
import requests
from packaging.version import Version

def check_for_update(version):
    needupdate = 0
    tag_name = ""
    html_url = ""
    body = ""

    # 发送GET请求到GitHub API以获取最新的release信息
    response = requests.get("https://api.github.com/repos/JasonYANG170/Super_Employee/releases/latest")

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析JSON数据
        release_data = response.json()

        # 获取需要的字段
        tag_name = release_data.get("tag_name", "")
        html_url = release_data.get("html_url", "")
        body = release_data.get("body", "")

        # 比较版本号
        if Version(tag_name.lstrip('V')) > Version(version.lstrip('V')):
            needupdate = 1
        else:
            needupdate = 0
    else:
        print("---------------警告----------------")
        print("检查更新错误！使用旧版本可能无法完成投递！", response.status_code)
        print("-----------------------------------")

    return needupdate, tag_name, html_url, body
