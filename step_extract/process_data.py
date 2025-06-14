import os
import re
from datetime import datetime

# 获取当前目录
base_dir = os.path.dirname(os.path.abspath(__file__))

# 确保output文件夹存在
output_dir = os.path.join(base_dir, 'output')
os.makedirs(output_dir, exist_ok=True)

# 获取所有txt文件
txt_files = [f for f in os.listdir(base_dir) if f.endswith('.txt') and f.startswith('data_')]

# 处理每个文件
for txt_file in txt_files:
    input_file_path = os.path.join(base_dir, txt_file)
    output_file_path = os.path.join(output_dir, txt_file)
    
    # 读取文件内容
    with open(input_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 提取表头（前两行）
    header_lines = lines[:2]
    
    # 初始化结果列表和上一秒时间
    result_lines = header_lines.copy()
    last_second = None
    
    # 遍历数据行
    for line in lines[2:]:
        # 使用正则表达式提取时间部分
        match = re.search(r'(\d+/\d+/\d+/星期.\s+\d+:\d+:(\d+))', line)
        if match:
            time_str = match.group(1)
            current_second = match.group(2)
            
            # 如果秒发生变化或者是第一条数据，则保留该行
            if current_second != last_second:
                result_lines.append(line)
                last_second = current_second
    
    # 写入结果到输出文件
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.writelines(result_lines)
    
    print(f'处理完成: {txt_file} -> {output_file_path}')

print('所有文件处理完成！')