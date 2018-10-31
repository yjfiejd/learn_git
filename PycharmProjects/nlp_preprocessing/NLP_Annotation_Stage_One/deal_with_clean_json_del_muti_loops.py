"""
本段程序处理
------------------------------------------------------------
3）分情况处理：（注意需要在clean_json_cluster中操作）
    3.1）遇到2个节点：
    3.2）遇到3个节点：
    3.3）遇到4个节点：
    3.4）遇到5个节点：
    3.5) 遇到6个节点：
------------------------------------------------------------

"""
import re
import networkx as nx
import matplotlib.pyplot as plt
from NLP_Annotation_Stage_One.deal_with_clean_json_get_new_loop_relations_and_tags import \
    find_all_loop_edges_clean_in_one_json, find_all_loop_edges_category_text_in_one_clean_json, \
    find_all_loop_nodes_tag_in_one_clean_json


relation_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/relation.json"
json_path = "../python_test_data/json_file/annotation39469-39530.json"
export_file_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/export.json"


# 1 ） 画图，可以看到整个clean_json的环图，带信息，方便分析 -> 在jupyter中实现
# 画图
def find_a_b_in_json_path(json_path):
    pattern = r'.*annotation(\d{5})-(\d{5})'
    match_a_b = re.match(pattern, json_path, re.I)
    a = int(match_a_b.group(1))
    b = int(match_a_b.group(2))
    return a, b

def draw_clean_json_loop_edges_and_tags(json_path, relation_path, export_file_path):

    # 获得输出：去除高层关系后的 - 环 edges (包含多个子json)
    all_loop_edges_clean_in_one_json = find_all_loop_edges_clean_in_one_json(json_path, relation_path)
    # 获得输出：去除高层关系后的 - 环 edges - 边的relations (包含多个子json)
    all_loop_edges_category_in_one_clean_json = find_all_loop_edges_category_text_in_one_clean_json(json_path, relation_path)
    # 获得输出：去除高层关系后的 - 环 edges - 环的节点tag表示 (包含多个子json)
    all_loop_nodes_tag_in_one_clean_json = find_all_loop_nodes_tag_in_one_clean_json(json_path, relation_path, export_file_path)

    a, b = find_a_b_in_json_path(json_path)
    num_1 = a
    for j in range(len(all_loop_edges_clean_in_one_json)):
        k = j
        p = j
        num_2 = 0
        for i, m, g in zip(all_loop_edges_clean_in_one_json[j], all_loop_nodes_tag_in_one_clean_json[k], all_loop_edges_category_in_one_clean_json[p]):  # 注意使用zip函数，好用
            G_test = nx.DiGraph()
            G_test.add_edges_from(i)
            print('出现环的节点为： ', G_test.nodes)
            print('出现环节点含义为：', m)
            print('出现环，边的含义为：', g)
            nx.draw_networkx(G_test)
            a = plt.show()
            num_2 = num_2 + 1
            print('****以上为第', num_1, '段话--中的第', num_2, '个环****')

        print('--------------------以上为第', num_1, '段话中出现的环----------------------\n')
        num_1 = num_1 + 1
    return


# 2) 处理4个节点：
# 在一个子json中，提取出4个节点的环
#

