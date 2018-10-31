"""
输入：
高层关系删除后的 json cluster （含有多个子json）
1）处理后 -> 目前json中的所有环（含多个文件）
2）处理后 -> 贴上标签，边的标签，节点的标签  -> 本程序到这里结束
------------------------------------------------------------
3）分情况处理：（需要在json cluster 中操作，注意）
    3.1）遇到2个节点：
    3.2）遇到3个节点：
    3.3）遇到4个节点：
    3.4）遇到5个节点：
------------------------------------------------------------
4）处理完成后，获得该json中（多个子json），无环，无高层关系的，子簇

输出：
处理完成剩下的环（处理2个节点、3个节点、4个节点、5个节点、的环）-> 输出不带环整个json cluster


"""
import re

import networkx as nx
import matplotlib.pyplot as plt
from NLP_Annotation_Stage_One.change_format_for_loop_nodes_find_cheklist import find_all_checklist_json
from NLP_Annotation_Stage_One.change_format_for_loop_nodes_in_json import get_export_file_category, \
    get_change_format_for_loop_nodes_in_json
from NLP_Annotation_Stage_One.del_high_level_relations_in_one_json import \
    find_new_paragrapher_cluster_without_label_in_all_json
from NLP_Annotation_Stage_One.find_all_loop_edges_category_text_in_one_jsonfile import get_json_file_relations, \
    get_relation_file_category_text


# 1) 对单独的single_json找环
def find_loop_edges_after_del_high_relations_in_single_json(new_paragrapher_cluster_without_label):
    """
    输入：,: 删除了高层关系后，剩下的簇，edges
    -> [[(6, 445), (446, 445), (723, 445)],
     [(10, 426), (424, 426), (425, 426)],
     [(12, 14), (13, 14)],

    输出：all_loop_edges_clean_in_para -> 这个簇中找到的环
    -> [[(165, 597), (560, 597), (559, 560), (561, 559), (561, 562), (562, 165)],
     [(283, 623), (282, 623), (282, 624), (283, 624)],
    """
    # 找到还存在的环
    all_loop_edges_in_each_cluster_edges = []
    for each_cluster_edges in new_paragrapher_cluster_without_label:
        G_sub_tree = nx.DiGraph()
        G_sub_tree.add_edges_from(each_cluster_edges)
        try:
            a = list(nx.find_cycle(G_sub_tree, orientation='ignore'))
            all_loop_edges_in_each_cluster_edges.append(a)
        except:
            pass
    # 去掉 'forward' & 'reverse' 表达路径方向
    all_loop_edges_clean_in_single_json = []
    for each_loop in all_loop_edges_in_each_cluster_edges:
        list_temp = []
        for each_eage in each_loop:
            list_temp.append((each_eage[0], each_eage[1]))
        all_loop_edges_clean_in_single_json.append(list_temp)
    return all_loop_edges_clean_in_single_json


# 2）获得输入：删除高层关系后的整一个json簇中，现在所有的环：
def find_all_loop_edges_clean_in_one_json(json_path, relation_path):
    """
    输入: json_path, relation_path  然后获得
    ->  处理过的json_簇（这里含62个子json） -> [[[(6, 445), (446, 445), (723, 445)], [(10, 426),

    输出: all_loop_edges_clean_in_one_json：目前每个子json中还剩下的环（一共62个）
    -> [[[(487, 735), (489, 735), (491, 489), (491, 487)],[(513, 516), (514, 516),
    """

    json_cluster_without_label_list, json_selected_del_edges_list = find_new_paragrapher_cluster_without_label_in_all_json(json_path, relation_path)

    all_loop_edges_clean_in_one_json = []
    for i in range(len(json_cluster_without_label_list)):
        # 取其中的一个子json的所有的簇，edges
        new_paragrapher_cluster_without_label = json_cluster_without_label_list[i]
        # 找到子json 其中的环
        all_loop_edges_clean_in_single_json = find_loop_edges_after_del_high_relations_in_single_json(new_paragrapher_cluster_without_label)
        all_loop_edges_clean_in_one_json.append(all_loop_edges_clean_in_single_json)
    return all_loop_edges_clean_in_one_json


# 3) 为目前所有的环，边关系 贴标签，
def find_all_loop_edges_category_text_in_one_clean_json(json_path, relation_path):
    """
    输入：
    json_path: json文件
    relation_path: relation文件

    输出：
    返回（去除高层关系后）-> json_path中所有的环，边的关系
    [[[{(487, 735): {91: '发起_动作'}}, {(489, 735): {91: '发起_动作'}},

    # 该函数与之前find_all_loop_edges_category_text_in_one_jsonfile.py中的函数的区别：
    # 第一个是通过json ->  获得所有环 -> 打标签
    # 在这里是通过json -> “剔除高层次关系后”  -> 获得所有环 - > 打标签

    """

    # 获得输入一： 删除完高层关系后，整个json获得的环，(含有多个) ：[[[(487, 735), (489, 735), (491, 489), (491, 487)], [(513, 516), (514, 516), (512, 514), (512, 513)],
    all_loop_edges_clean_in_one_json = find_all_loop_edges_clean_in_one_json(json_path, relation_path)
    # 获得输入二， 可以通过"dst"& "src"找到每个环对应的文章中的 'category' 关系数值:
    # [[{'dst': 426, 'id': 0, 'category': 135, 'src': 425}, {'dst': 426, 'id': 1, 'category': 92, 'src': 424},...
    json_file_relations = get_json_file_relations(json_path)
    # 获得输入三，找到relation的匹配关系， 由category -> text 文本:
    # {1: '作用于_（失效）', 2: '是_的治疗', 3: '是_的发展趋势', ...
    relation_file_name = get_relation_file_category_text(relation_path)
    # 获得整个json中的结果
    all_loop_edges_category_in_one_clean_json = []
    for i in range(len(json_file_relations)):
        loop_edges_just_in_one_json_i = all_loop_edges_clean_in_one_json[i]
        relations_just_in_one_json_i = json_file_relations[i]
        # for each_loop in all_loop_edges_in_one_json_list:
        list_1 = []
        for single_loop in loop_edges_just_in_one_json_i:
            #     print(single_loop)
            list_0 = []
            for edges in single_loop:
                src, dst = edges[0], edges[1]
                edges_category_dict = {}
                for j in relations_just_in_one_json_i:
                    if j['dst'] == dst and j['src'] == src:
                        category_text = {}
                        for i in relation_file_name.items():
                            if j['category'] == i[0]:
                                category_text[j['category']] = i[1]
                        edges_category_dict[(src, dst)] = category_text
                        list_0.append(edges_category_dict)
            #                     print(edges_category_dict)
            #         print('***')
            #     print(list_0)
            list_1.append(list_0)
        #     print(list_1)
        all_loop_edges_category_in_one_clean_json.append(list_1)
    #     print('------------------')
    return all_loop_edges_category_in_one_clean_json


# 4） 为目前所有的环，节点，贴标签

# 4.1 new 处理 all_loop_edges_clean_in_one_json，（删除高层关系后）-> 产生的环 -> 生成节点 -> 为了获得下方输入一
def get_all_loop_node_in_clean_json(json_path, relation_path):
    """
    :param json_path: 一个json文件的地址
    :return: 一整个json中存在的所有的环（子json），节点表示
    """
    # 1) 找到了处理后的json_cluster, 中找到的环：[[[(487, 735), (489, 735), (491, 489),
    all_loop_edges_clean_in_one_json = find_all_loop_edges_clean_in_one_json(json_path, relation_path)

    all_loop_node_in_clean_json = []
    for paragraph_loop in all_loop_edges_clean_in_one_json:
        #     print(paragraph_loop) # 获得每一段中出现的环，边表示
        all_loop_node_in_para = []
        for i in paragraph_loop:
            #         print(i) # 获得每段话中的每一个环
            G_loop_in_para = nx.DiGraph()
            G_loop_in_para.add_edges_from(i)
            # 注意获得nodes_list，需要格式转换为list
            loop_node_in_para = list(G_loop_in_para.nodes())
            all_loop_node_in_para.append(loop_node_in_para)
        all_loop_node_in_clean_json.append(all_loop_node_in_para)
    return all_loop_node_in_clean_json


# 4.2 new 新的函数，用在deal_with_high_relation_deleted_json_cluster.py
def find_all_loop_nodes_tag_in_one_clean_json(json_path, relation_path, export_file_path):
    """
    输入：json_path（含有多个json），export_file_path

    输出：找到所有json中，带环节点，标出他们的 id - text - category
    [[{139: ('内', {13: '方位'}), 41: ('胆管', {7: '身体结构'})...
    """

    # 获得输入一： 10个json中，每一个json中所有的环，节点表示 -> list
    # all_loop_node_in_json = get_all_loop_node_in_json(json_path)

    # 新的loop_edges (去除了高层关系)
    all_loop_node_in_json = get_all_loop_node_in_clean_json(json_path, relation_path)
    # print("all_loop_node_in_json: ", all_loop_node_in_json)

    # 获得输入二：多个json中，每一个json对应的查找字典, -> list
    all_checklist_json_list = find_all_checklist_json(json_path)
    # print("all_checklist_json_list: ", all_checklist_json_list)

    # 获得输入三： category - 'name' 查找字典 --> 查找dict
    export_file_category = get_export_file_category(export_file_path)
    # print("export_file_category: " , export_file_category)

    # print('------------------')

    all_loop_nodes_tag_in_one_clean_json = []
    for i in range(len(all_loop_node_in_json)):
        loop_node_in_json = all_loop_node_in_json[i]
        text_category_checklist_in_json = all_checklist_json_list[i]

        # 把输入一，输入二，输入三，填入，获得结果。
        new_nodes_list_2 = get_change_format_for_loop_nodes_in_json(loop_node_in_json, text_category_checklist_in_json, export_file_category)

        all_loop_nodes_tag_in_one_clean_json.append(new_nodes_list_2)

    return all_loop_nodes_tag_in_one_clean_json


# 5）画个图看一波效果 -> 只能看单个子json中的图，不带信息
def draw_directed_tree(right_input_by_edges):
    """
    :param right_input_by_edges: [[(6, 445), (446, 445), (723, 445)],
    :return: 有向图
    """
    for i in right_input_by_edges:
        print(i)
        G = nx.DiGraph()  # 定义有向图，图形
        G.add_edges_from(i)  # 添加边
        plt.figure()
        nx.draw_networkx(G, with_labels=True)
        sub_picture = plt.show()
    return sub_picture


# 测试

relation_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/relation.json"
json_path = "../python_test_data/json_file/annotation39469-39530.json"
# json_path = "../python_test_data/json_file/annotation38125-38225.json"
# json_path = "../python_test_data/json_file/annotation39601-39664.json"
export_file_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/export.json"

# 获得输出：删除高层关系后的簇
json_cluster_without_label_list, json_selected_del_edges_list = find_new_paragrapher_cluster_without_label_in_all_json(json_path, relation_path)
print('json_cluster_without_label_list = ', json_cluster_without_label_list)
print('--------------------------------------------')

# 获得输出：去除高层关系后的 - 环 edges (包含多个子json)
all_loop_edges_clean_in_one_json = find_all_loop_edges_clean_in_one_json(json_path, relation_path)
print("all_loop_edges_clean_in_one_json = ", all_loop_edges_clean_in_one_json)
print('--------------------------------------------')

# 获得输出：去除高层关系后的 - 环 edges - 边的relations(包含多个子json)
all_loop_edges_category_in_one_clean_json = find_all_loop_edges_category_text_in_one_clean_json(json_path, relation_path)
print("all_loop_edges_category_in_one_clean_json = ", all_loop_edges_category_in_one_clean_json)
print('--------------------------------------------')

# 获得输出：去除高层关系后的 - 环 edges - 环的节点tag表示 (包含多个子json)
all_loop_nodes_tag_in_one_clean_json = find_all_loop_nodes_tag_in_one_clean_json(json_path, relation_path, export_file_path)
print("all_loop_nodes_tag_in_one_clean_json = ", all_loop_nodes_tag_in_one_clean_json)
print('--------------------------------------------')

# 接下来进行环的分类处理！
