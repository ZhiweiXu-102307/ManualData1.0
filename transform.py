import os
import pandas as pd
import re

def detect_delimiter(file_path):
    """检测文件使用的分隔符"""
    with open(file_path, 'r', encoding='gb2312') as f:
        # 读取前几行来分析
        lines = [f.readline() for _ in range(5) if f.readline()]
    
    # 根据示例文件，数据似乎是使用多个空格作为分隔符
    # 使用正则表达式将多个空格作为分隔符
    return r'\s+'

def convert_txt_to_excel(input_file, output_file):
    """将文本文件转换为Excel文件"""
    try:
        # 检测分隔符
        delimiter = detect_delimiter(input_file)
        
        # 使用pandas读取文本文件
        df = pd.read_csv(input_file, sep=delimiter, engine='python', encoding = "gb2312")
        
        # 保存为Excel文件
        df.to_excel(output_file, index=False)
        
        print(f"成功转换: {os.path.basename(input_file)} -> {os.path.basename(output_file)}")
        return True
    except Exception as e:
        print(f"转换失败: {os.path.basename(input_file)}, 错误: {str(e)}")
        return False

def main():
    # 获取当前脚本所在目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 设置输入和输出文件夹路径
    input_dir = os.path.join(base_dir, 'input')
    output_dir = os.path.join(base_dir, 'output')
    
    # 确保输出文件夹存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            input_file = os.path.join(input_dir, filename)
            # 将输出文件扩展名改为.xlsx
            output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + '.xlsx')
            
            # 转换文件
            convert_txt_to_excel(input_file, output_file)

if __name__ == "__main__":
    main()