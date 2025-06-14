import os
import chardet

def read_data_file(file_path):
    """
    读取数据文件并自动检测编码
    """
    try:
        # 首先以二进制模式读取文件
        with open(file_path, 'rb') as f:
            raw_data = f.read()
        
        # 使用chardet检测编码
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        confidence = result['confidence']
        
        print(f"检测到的编码: {encoding}，置信度: {confidence:.2f}")
        
        # 尝试使用检测到的编码解码
        try:
            content = raw_data.decode(encoding)
            print(f"成功使用 {encoding} 编码读取文件")
            print("\n文件内容预览（前10行）:")
            print("\n".join(content.split('\n')[:10]))
            
            # 询问是否显示全部内容
            show_all = input("\n是否显示全部内容？(y/n): ").lower() == 'y'
            if show_all:
                print("\n完整文件内容:")
                print(content)
                
        except UnicodeDecodeError:
            print(f"使用检测到的编码 {encoding} 解码失败")
            
            # 尝试常用的中文编码
            for enc in ['gbk', 'gb2312', 'gb18030', 'utf-8', 'big5']:
                try:
                    content = raw_data.decode(enc)
                    print(f"成功使用 {enc} 编码读取文件")
                    print("\n文件内容预览（前10行）:")
                    print("\n".join(content.split('\n')[:10]))
                    
                    # 询问是否显示全部内容
                    show_all = input("\n是否显示全部内容？(y/n): ").lower() == 'y'
                    if show_all:
                        print("\n完整文件内容:")
                        print(content)
                    break
                except UnicodeDecodeError:
                    continue
            else:
                print("所有尝试的编码都失败，显示二进制内容的十六进制表示")
                print(raw_data.hex())
    except Exception as e:
        print(f"读取文件时出错: {e}")

if __name__ == "__main__":
    # 获取当前目录下的所有txt文件
    txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    
    if not txt_files:
        print("当前目录下没有找到txt文件")
    else:
        print(f"找到以下txt文件: {txt_files}")
        # 如果有多个文件，让用户选择一个
        if len(txt_files) > 1:
            print("请选择要读取的文件编号:")
            for i, file in enumerate(txt_files):
                print(f"{i+1}. {file}")
            try:
                choice = int(input("请输入文件编号: "))
                if 1 <= choice <= len(txt_files):
                    file_path = txt_files[choice-1]
                else:
                    print("无效的选择，使用第一个文件")
                    file_path = txt_files[0]
            except:
                print("输入错误，使用第一个文件")
                file_path = txt_files[0]
        else:
            file_path = txt_files[0]
        
        print(f"\n正在读取文件: {file_path}")
        read_data_file(file_path) 