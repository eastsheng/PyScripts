#!/usr/bin/python
import os
import re

def combine_files(directory_path,rewrite_file):
    # 打开目标文件以写入内容
    with open(rewrite_file, 'w') as merged_file:
        # 列出要合并的文件列表
        file_list = os.listdir(directory_path)
        numbers = re.findall(r'\d+', file_list[0])
        index = numbers[-1]
        # 循环遍历每个文件并将其内容写入合并后的文件
        files_dict = {}
        for file_name in file_list:
            numbers = re.findall(r'\d+', file_name)
            index = int(numbers[-1])
            files_dict[index] = file_name
        # print(files_dict)
        sorted_keys = sorted(files_dict.keys())
        for key in sorted_keys:
            print(key, files_dict[key])
            with open(directory_path+files_dict[key], 'r') as file:
                merged_file.write(file.read())

if __name__ == '__main__':
    import sys
    try:
        directory_path = sys.argv[1]
    except:
        directory_path = './temp/'

    try:
        rewrite_file = sys.argv[2]
    except:
       rewrite_file = 'traj_npt_dissociation_330_1.lammpstrj'

    print("Files (sorted) that need to be merged:")
    combine_files(directory_path,rewrite_file)
    print("Combined files Successfully!")