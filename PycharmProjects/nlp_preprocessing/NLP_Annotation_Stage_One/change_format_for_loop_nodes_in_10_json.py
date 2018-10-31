
import json
import emoji

# 获得输入一：找到10个json的中环节点 list集合
import re

from NLP_Annotation_Stage_One.change_format_for_loop_nodes_find_cheklist import find_all_checklist_json
from NLP_Annotation_Stage_One.change_format_for_loop_nodes_in_json import get_all_loop_node_in_json, \
    get_export_file_category, get_change_format_for_loop_nodes_in_json
from NLP_Annotation_Stage_One.deal_with_clean_json_get_new_loop_relations_and_tags import get_all_loop_node_in_clean_json


def find_all_loop_nodes_labelled_list(json_path, export_file_path):
    """
    输入：json_path（含有多个json），export_file_path

    输出：找到所有json中，带环节点，标出他们的 id - text - category
    """

    # 获得输入一： 10个json中，每一个json中所有的环，节点表示 -> list
    all_loop_node_in_json = get_all_loop_node_in_json(json_path)
    # print("all_loop_node_in_json: ", all_loop_node_in_json)

    # 获得输入二：10个json中，每一个json对应的查找字典, -> list
    all_checklist_json_list = find_all_checklist_json(json_path)
    # print("all_checklist_json_list: ", all_checklist_json_list)

    # 获得输入三： category - 'name' 查找字典 --> 查找dict
    export_file_category = get_export_file_category(export_file_path)
    # print("export_file_category: " , export_file_category)
    # print('------------------')

    all_loop_nodes_labelled_list = []
    for i in range(len(all_loop_node_in_json)):
        loop_node_in_json = all_loop_node_in_json[i]
        text_category_checklist_in_json = all_checklist_json_list[i]

        # 把输入一，输入二，输入三，填入，获得结果。
        new_nodes_list_2 = get_change_format_for_loop_nodes_in_json(loop_node_in_json, text_category_checklist_in_json, export_file_category)

        all_loop_nodes_labelled_list.append(new_nodes_list_2)

    return all_loop_nodes_labelled_list








# 【测试如下：】
# 多个json_path ok (对格式有要求，pattern = r'.*annotation(\d{5})-(\d{5})'）
# json_path = "../python_test_data/json_file/annotation37529-37538.json"  # 10个json文件
# json_path = "../python_test_data/json_file/annotation37730-37739.json" # 10 个json文件
# json_path = "../python_test_data/json_file/annotation38125-38225.json" # 100个json文件

# relation_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/relation.json"
# json_path = "../python_test_data/json_file/annotation39469-39530.json"
# json_path = "../python_test_data/json_file/annotation39255-39354.json"

# export_file_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/export.json"

# all_loop_nodes_labelled_list = find_all_loop_nodes_labelled_list(json_path, export_file_path)
# print('all_loop_nodes_labelled_list: ', all_loop_nodes_labelled_list)
# print(emoji.emojize("program pass :thumbs_up:"))
