"""
输入：
输入一：1）json_path, 2) export_file_path
-> 为了获得 all_loop_nodes_labelled_list：
->
[[[{4: ('后', {61: '时间副词（前时后）'}),
    251: ('PET', {3: '检查'}),
    2: ('显像剂', {38: '药品'}),
    473: ('CT', {3: '检查'})}],
  [{279: ('未见', {15: '否定'}),
    283: ('增宽', {10: '趋势和变化'}),
    518: ('沟回', {7: '身体结构'}),
    282: ('加深', {10: '趋势和变化'})}],...]

输入二：1)json_path,
-> 为了获得all_loop_edges_in_100_json_list
->
[[[(4, 251), (2, 251), (2, 473), (4, 473)],
  [(279, 283), (518, 283), (518, 282), (279, 282)],
  [(378, 380), (377, 378), (377, 379), (379, 380)],
  [(151, 385), (385, 149), (491, 149), (151, 491)],
  [(166, 392), (159, 166), (159, 167), (167, 392)]],
 [[(4, 198), (2, 198), (2, 9), (4, 9)],
  [(220, 223), (397, 223), (397, 222), (220, 222)],
  [(264, 265), (77, 265), (77, 396), (264, 396)],
  [(84, 271), (85, 271), (85, 269), (84, 269)],
  [(292, 294), (291, 292), (291, 293), (293, 294)],
  [(133, 299), (299, 131), (378, 131), (133, 378)],
  [(150, 307), (141, 150), (141, 151), (151, 307)]],


输出：所有json中，带环节点&含义
-> 结果如下：
出现环的节点为：  [4, 251, 2, 473]
出现环节点含义为： [{4: ('后', {61: '时间副词（前时后）'}), 251: ('PET', {3: '检查'}), 2: ('显像剂', {38: '药品'}), 473: ('CT', {3: '检查'})}]

"""


import networkx as nx
import matplotlib.pyplot as plt

from NLP_Annotation_Stage_One.change_format_for_loop_nodes_find_cheklist import find_a_b_in_json_path
from NLP_Annotation_Stage_One.change_format_for_loop_nodes_in_10_json import find_all_loop_nodes_labelled_list
from NLP_Annotation_Stage_One.find_all_loop_edges_in_one_json import find_all_loop_edges_in_one_json_list


def draw_changed_format_loop_nodes_in_all_json(json_path, export_file_path):
    """
    输入：
    输入一：1）json_path, 2) export_file_path ->为了获得 all_loop_nodes_labelled_list：
    输入二：1）json_path -> 为了获得all_loop_edges_in_100_json_list\

    输出：
    绘制图形 + 带环环节点含义

    """
    all_loop_edges_in_100_json_list = find_all_loop_edges_in_one_json_list(json_path)
    all_loop_nodes_labelled_list = find_all_loop_nodes_labelled_list(json_path, export_file_path)
    # 这里需要定义出现的段落id
    a, b = find_a_b_in_json_path(json_path)
    num_1 = a
    for j in range(len(all_loop_edges_in_100_json_list)):
        k = j
        num_2 = 0
        for i, m in zip(all_loop_edges_in_100_json_list[j], all_loop_nodes_labelled_list[k]):  # 注意使用zip函数，好用
            G_test = nx.DiGraph()
            G_test.add_edges_from(i)
            print('出现环的节点为： ', G_test.nodes)
            print('出现环节点含义为：', m)
            nx.draw_networkx(G_test)
            a = plt.show()
            num_2 = num_2 + 1
            print('****以上为第', num_1, '段话--中的第', num_2, '个环****')

        print('--------------------以上为第', num_1, '段话中出现的环----------------------\n')
        num_1 = num_1 + 1

    return a




# 测试开始

# json_path = "../python_test_data/json_file/annotation37529-37538.json"  # 10个json文件

# json_path = "../python_test_data/json_file/annotation37730-37739.json"  # 10个json文件
# export_file_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/export.json"
# changed_format_loop_nodes_in_all_json = draw_changed_format_loop_nodes_in_all_json(json_path, export_file_path)



