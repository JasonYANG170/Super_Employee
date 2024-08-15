# --------------------感谢您使用Super Employees自动投递程序---------------------
# 应用版本V1.0
# 应用作者: JasonYANG17
# 仓库地址: https://github.com/JasonYANG170/Super_Employee
# Wiki教程: https://github.com/JasonYANG170/Super_Employee/wiki
# -------------用户配置选项-----------------------
poststate = 1  # 不投递0;投递1;
UseResultPush = 0  # 是否启用推送
PushToken = ''  # 在pushpush网站中可以找到
# 自定义请求的设备名称
deviceName='HUAWEI'


# --------------平台选择--------------------
# 开启的平台请务必下滑找到该平台的配置项并填入对应配置
# 是否启用实习僧
shixiseng_state = 1
yizhanchi_state = 1

# --------------实习僧配置项--------------------
# 是否投递(不投递:0,投递优先在线简历:1,投递优先离线简历:2)
shixiseng_poststate = 0
# Cookie(参考wiki说明获取)
shixiseng_Cookie = ''
# 筛选条件(带‘*’号的为必填项)
shixiseng_Search = {
    'p': "1",
    't': "1",  # 智能排序:0，最近发布优先:1      *
    'city': "",  # 地区(全国或其他省市)      *
    'nature': "",  # 类型：股份制企业|合伙企业
    'scale': "",  # 规模：50-150人|500-2000人
    'ipo': "",  # 融资：B轮|A轮
    'k': "",  # 岗位                     *
    'degree': "",  # 学历：大专|本科
    'emp_chance': "",  # 空间：提供转正|面议
    'intention': "",  # 需求：校招|实习
    'internship_duration': "",  # 在岗时间：1个月|3个月以上
    'days_per_week': "",  # 工作时间：4天|1天
    'payment_per_day': ""  # 日薪：200-300|100以下
}
# --------------翼展翅配置项--------------------
# 吐槽一下，翼展翅的数据非常的混乱，有小概率会出现城市筛选失效
yizhanchi_poststate = 0
yizhanchi_city=""
yizhanchi_Token =""
yizhanchi_Search = {
    'page_size': "50",#查询范围  *
    'page': "1",#当前页面        *
    'positiontype': "",
    'minsalary': "",#最低工资
    'maxsalary': "",#最高工资
    'show_third_position': "",
    'keyword': "",#岗位     *
    'region_id': "",
    'intern_time_id': "",
    'intern_cycle_id': "",
    'correct_id': "",
    'parttime_duration': "",
    'jianzhitype': "",
    'classid': "",
    'financid': "",
    'natureid': "",
    'scaleid': "",
    'areaid': "",
    'location': "",
    'port': "",
    'region_type': "",
    'sort': ""
}