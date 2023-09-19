import os

# 获取当前目录
current_dir = os.getcwd()

# 遍历当前目录下的所有文件和文件夹
all_items = os.listdir(current_dir)

# 筛选出文件夹路径
folder_paths = [item for item in all_items if os.path.isdir(os.path.join(current_dir, item))]

# 将文件夹路径写入train.txt文件
with open('train.txt', 'w') as file:
    for folder_path in folder_paths:
        file.write(os.path.join(current_dir, folder_path) + '\n')