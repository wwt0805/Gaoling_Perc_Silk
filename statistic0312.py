# @time:  2024/3/12  11:33
# @File:  statistic0312.py
# @Software:  PyCharm
# @Author:    wuwentong
import re
from datetime import datetime, timedelta

# 读取文件数据
with open('2024-2-26log.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 定义存储状态及时间的字典
status_dict = {}
time_dict = {}

# 遍历所有行
for i in range(len(lines)):
    line = lines[i]

    # 匹配时间、状态和描述
    match = re.match(r'(\d+/\d+/\d+ \d+:\d+:\d+)=([A-Za-z\d]*) (.*$)', line)
    if match:
        dt_str, status, description = match.groups()
        dt_obj = datetime.strptime(dt_str, '%Y/%m/%d %H:%M:%S')

        # 记录状态及其出现次数
        if status in status_dict:
            status_dict[status]['count'] += 1
            status_dict[status]['desc'].add(description)
        else:
            status_dict[status] = {'count': 1, 'desc': {description}}

        # 计算每种状态的累计时间
        if i != 0:  # 不是第一条记录
            last_dt_str = lines[i - 1].split("=")[0]
            last_dt_obj = datetime.strptime(last_dt_str, '%Y/%m/%d %H:%M:%S')
            delta_time = (dt_obj - last_dt_obj).total_seconds()
            if status in time_dict:
                time_dict[status] += delta_time
            else:
                time_dict[status] = delta_time

# 打印结果
for status, info in status_dict.items():
    print('Status: ', status)
    print('Count: ', info['count'])
    print('Descriptions: ', info['desc'])
    print('Total time: ', time_dict.get(status, 0), ' seconds')
