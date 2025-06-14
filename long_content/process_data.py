import os
import re
from datetime import datetime

# 定义输入和输出路径
input_file = 'd:\\Desktop\\Python Project\\ManualTransform\\long_content\\C0.3-6.3.txt'
output_folder = 'd:\\Desktop\\Python Project\\ManualTransform\\long_content\\output'

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 读取数据文件
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 提取标题行
header_lines = lines[:2]  # 假设前两行是标题行

# 按小时分组数据
hour_data = {}

for line in lines[2:]:  # 跳过标题行
    # 使用正则表达式提取时间
    time_match = re.search(r'(\d{4}/\d{1,2}/\d{1,2}/星期[一二三四五六日]\s+\d{2}):(\d{2}):(\d{2})', line)
    
    if time_match:
        date_str = time_match.group(0)
        hour = time_match.group(1)  # 提取日期和小时部分
        
        # 将数据添加到对应小时的组中
        if hour not in hour_data:
            hour_data[hour] = []
        
        hour_data[hour].append(line)

# 将分组数据写入文件
for hour, data in hour_data.items():
    # 创建文件名，替换非法字符
    safe_hour = hour.replace('/', '_').replace(' ', '_').replace(':', '_')
    output_file = os.path.join(output_folder, f'data_{safe_hour}.txt')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # 写入标题行
        f.writelines(header_lines)
        # 写入数据行
        f.writelines(data)

print(f'数据已按小时切分并保存到 {output_folder} 文件夹')