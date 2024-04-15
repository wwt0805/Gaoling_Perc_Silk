# @time:  2024/3/12  11:38
# @File:  statistic0312-2.py
# @Software:  PyCharm
# @Author:    wuwentong
import re
from datetime import datetime, timedelta

# 获取当前日期的前一天
yesterday = datetime.now() - timedelta(days=1)
# 格式化日期为文件名中的日期格式
file_date = yesterday.strftime('%Y-%m-%d')
file_name = f'{file_date}log.txt'  # 生成文件名，例如 "2024-2-25log.txt"

# 读取文件数据
with open('2024-2-26log.txt', 'r', encoding='utf-8') as f:
# with open(file_name, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 定义存储状态及时间的字典
status_dict = {}
time_dict = {}

# 遍历所有行
for i in range(len(lines)):
    line = lines[i]

    # 匹配时间、状态
    # match = re.match(r'(\d+/\d+/\d+ \d+:\d+:\d+)=([\d]*)', line)
    match = re.match(r'(\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{2}:\d{2})=(\d+)', line)
    if match:
        dt_str, status = match.groups()
        dt_obj = datetime.strptime(dt_str, '%Y/%m/%d %H:%M:%S')

        # 记录状态及其出现次数
        if status in status_dict:
            status_dict[status] += 1
        else:
            status_dict[status] = 1

        # 计算每种状态的累计时间
        if i != 0:  # 不是第一条记录
            last_dt_str = lines[i - 1].split("=")[0]
            last_dt_obj = datetime.strptime(last_dt_str, '%Y/%m/%d %H:%M:%S')
            delta_time = (dt_obj - last_dt_obj).total_seconds()
            if status in time_dict:
                time_dict[status] += delta_time
            else:
                time_dict[status] = delta_time

# 状态码注释字典
status_info_comments = {
    0: "升降轴伺服异常",
    1: "平移轴伺服异常",
    2: "刮刀轴伺服异常",
    3: "墨刀轴伺服异常",
    4: "丝网X轴伺服异常",
    5: "丝网Y轴伺服异常",
    6: "丝网T轴伺服异常",
    7: "夹片1伺服异常",
    8: "夹片2伺服异常",
    9: "CV1伺服异常",
    10: "CV2伺服异常",
    11: "A工位伺服异常",
    12: "D工位伺服异常",
    13: "C工位伺服异常",
    14: "B工位伺服异常",
    15: "CV3伺服异常",
    16: "CV4伺服异常",
    17: "CV5伺服异常",
    18: "CV6伺服异常",
    19: "气压检测异常",
    20: "设备紧急停止中",
    21: "转台伺服异常",
    22: "A工位相机通讯超时",
    23: "B工位相机通讯超时",
    24: "C工位相机通讯超时",
    25: "D工位相机通讯超时",
    26: "进片激光传感器检测警报",
    27: "A工位吸真空异常",
    28: "B工位吸真空异常",
    29: "C工位吸真空异常",
    30: "D工位吸真空异常",
    31: "CV1进片异常",
    32: "CV2进片异常",
    33: "CV3进片异常",
    34: "CV4进片异常",
    35: "CV5_1进片异常",
    36: "CV1顶片气缸异常",
    37: "转台伺服异常",
    38: "水冷机异常",
    39: "左前门锁异常",
    40: "CV6顶片气缸异常",
    41: "左后门锁异常",
    42: "CV6进片异常",
    43: "请切换到手动模式",
    44: "请切换到自动模式",
    45: "丝网检测异常",
    46: "门检1异常",
    47: "门检2异常",
    48: "安全光幕异常",
    49: "A工位卷纸复位失败",
    50: "B工位卷纸复位失败",
    51: "C工位卷纸复位失败",
    52: "D工位卷纸复位失败",
    53: "总线异常",
    54: "CJ模块异常",
    55: "接炉卡片异常",
    56: "A工位卷纸需更换警示",
    57: "B工位卷纸需更换警示",
    58: "C工位卷纸需更换警示",
    59: "D工位卷纸需更换警示",
    60: "AOI通讯超时",
    61: "出片检测异常",
    62: "AOI检测印刷连续异常",
    63: "爆网异常",
    64: "预留",
    65: "预留",
    66: "预留",
    67: "预留",
    68: "预留",
    69: "预留",
    70: "左前门锁检测异常",
    71: "左后门锁检测异常",
    72: "后左门锁检测异常",
    73: "后右门锁检测异常",
    100: "测试报警",
}

# 打印结果
for status, count in status_dict.items():
    try:
        print('Status: ', status, status_info_comments[int(status)])
        print('Count: ', count)
        print('Total time: ', time_dict.get(status, 0), ' seconds')
        print("=" * 50)
    except:
        pass
