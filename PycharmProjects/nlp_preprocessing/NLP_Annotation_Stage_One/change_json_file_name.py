import os

def change_json_file_name(path):
    file_name = os.listdir(path)
    for temp in file_name:
        num = temp.find('.json')
        new_name = temp[:num+5]
        os.rename(path+temp, path+new_name)
    return



# 测试函数

# path3 = '/Users/synyi/Documents/2018.9/9_28_胸科/Archive/copy3/'
# change_json_file_name(path3)