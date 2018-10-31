"""

【输入】：
输入一；loop_node_in_json -> 10个json中，每一个json中所有的环，节点表示
[[139, 41, 138, 140], [45, 44, 47, 46], [57, 56, 59, 58]]

输入二：text_category_checklist_in_json -> 10个json中，每一个json对应的查找字典，id - text - category
[{'id': 106, 'pos': [1, 18], 'relations': [], 'timestamps': 106, 'category': 28, 'text': 'ClinicalDiagnosis'}, ...]

输入三：export_file_category -> 查找字典 category - name
[{'id': 16, 'name': '概率'}, {'id': 45, 'name': '时间点'},{'id': 1, 'name': '症状表现'},...]


【输出】： 这个json中，所有的环节点，list新格式
[[{139: ('内', {13: '方位'}), 41: ('胆管', {7: '身体结构'}), 138: ('肝', {7: '身体结构'}), 140: ('外', {13: '方位'})}], [{45: ('大小', {54: '属性或性状的名称'}), 44: ('脾脏', {7: '身体结构'}), 47: ('如常', {92: '描述'}), 46: ('形态', {54: '属性或性状的名称'})}], [{57: ('大小', {54: '属性或性状的名称'}), 56: ('胰腺', {7: '身体结构'}), 59: ('正常', {92: '描述'}), 58: ('形态', {54: '属性或性状的名称'})}]]


"""


import json
import networkx as nx
import matplotlib.pyplot as plt

from NLP_Annotation_Stage_One.find_all_loop_edges_in_one_json import find_all_loop_edges_in_one_json_list


# 1) 通过json_path 获得包含了10个json文件中所有的环的节点表达形式
def get_all_loop_node_in_json(json_path):
    """
    :param json_path:  一个json文件的地址
    :return: 十段话中，每段话中存在的所有环，的节点表示, list
    all_loop_node_in_json:  [[[139, 41, 138, 140], [45, 44, 47, 46], [57, 56, 59, 58]],...]
    """
    # 1） 先找到json文件中十段话中所有的环，的边表示(包括多个子json文件): [[[(139, 41), (138, 139), (138, 140), (140, 41)] ...
    all_loop_edges_in_one_json_list = find_all_loop_edges_in_one_json_list(json_path)

    all_loop_node_in_json = []
    for paragraph_loop in all_loop_edges_in_one_json_list:
        #     print(paragraph_loop) # 获得每一段中出现的环，边表示
        all_loop_node_in_para = []
        for i in paragraph_loop:
            #         print(i) # 获得每段话中的每一个环
            G_loop_in_para = nx.DiGraph()
            G_loop_in_para.add_edges_from(i)
            # 注意获得nodes_list，需要格式转换为list
            loop_node_in_para = list(G_loop_in_para.nodes())
            all_loop_node_in_para.append(loop_node_in_para)
        all_loop_node_in_json.append(all_loop_node_in_para)
    return all_loop_node_in_json



# 2） 某一个json文件中，提取出查找字典， 注意一个json带环图对应一个查找字典， 注意id不同
def get_single_json_id_text_category_list(single_json_path):
    """
    :param single_json_path: 一个json文件的地址
    :return: 获得这个json文件中的信息字典，用于查询
    single_json_id_text_category_list:  [{'id': 106, 'pos': [1, 18], 'relations': [], 'timestamps': 106, 'category': 28, 'text': 'ClinicalDiagnosis'}, ...]
    """
    with open(single_json_path, "r") as f:
        single_json = json.load(f)  # 注意json.load() 与 json.loads()的区别
    single_json_id_text_category_list = single_json['NLPResult']['concepts']
    return single_json_id_text_category_list


# 2.5 ) 获取 export文件中的category -> 这个是某个词的tag
def get_export_file_category(export_file_path):
    with open(export_file_path, "r") as f:
        export_file = json.load(f)
    export_file_category = export_file['categories']
    return export_file_category


# 3）修改格式一：


# 后期用这个函数，作为map, lambda, list(zip) 使用
def change_format_1(loop_node_in_json, text_category_checklist_in_json):
    """
    :param loop_node_in_json: 单个的json文件中出现的所有的环
    :param text_category_checklist_in_json: 单个json文件中的对应的查找字典
    :return: 增加格式 ‘text’， ‘category’
    # 输出：[139, 41, 138, 140] —> [[{139: ('内', 13)}, {41: ('胆管', 7)}, {138: ('肝', 7)}, {140: ('外', 13)}]
    """
    new_nodes_list = []
    for para_loop_list in loop_node_in_json:
        #     print(para_loop_list)
        # 进入环中的node
        sub_list = []
        for node in para_loop_list:
            new_node_dict = dict()
            # 进入查找
            for item in text_category_checklist_in_json:
                if node == item['id']:
                    new_node_dict[node] = item['text'], item['category']
            sub_list.append(new_node_dict)
        new_nodes_list.append(sub_list)
    return new_nodes_list


def change_format_2(new_nodes_list, export_file_category):
    a = []
    for sub_graph_nodes in new_nodes_list:
        all_node_dict_1 = dict()

        # 进入某个node中
        #     print(sub_graph_nodes)
        sub_list = []
        node_dict_1 = dict()

        for node in sub_graph_nodes:
            node_dict = dict()
            # 进入node中的 取出category，取出text， 取id
            node_id = list(node.keys())

            # try: #有时候第一个为[]空，无法进行list【0】操作，会报错，需要pass掉这些
            #     node_category = list(node.values())[0][1]
            #     node_text = list(node.values())[0][0]
            # except:
            #     pass
            try:
                node_category = list(node.values())[0][1]
                node_text = list(node.values())[0][0]
            except:
                pass

            # 进入export_file文中，去匹配
            try: # UnboundLocalError: local variable 'node_category' referenced before assignment
                for item in export_file_category:
                    if node_category == item['id']:
                        node_dict[node_category] = item['name']
                        node_dict_1 = node_text, node_dict
                    all_node_dict_1[node_id[0]] = node_dict_1
            except:
                pass
        sub_list.append(all_node_dict_1)
        a.append(sub_list)

    return a


# 设置；主函数1) ：
def get_change_format_for_loop_nodes_in_json(loop_node_in_json, text_category_checklist_in_json, export_file_category):
    """
    :param loop_node_in_json: 输入一；[[139, 41, 138, 140], [45, 44, 47, 46], [57, 56, 59, 58]]
    :param text_category_checklist_in_json: 输入二：[{'id': 106, 'pos': [1, 18], 'relations': [], 'timestamps': 106, 'category': 28, 'text': 'ClinicalDiagnosis'}, ...]
    :param export_file_category 输入三：[{'id': 16, 'name': '概率'}, {'id': 45, 'name': '时间点'},{'id': 1, 'name': '症状表现'},...]
    :return: 输出一：[[{139: ('内', {13: '方位'}), 41: ('胆管', {7: '身体结构'}), 138: ('肝', {7: '身体结构'}), 140: ('外', {13: '方位'})}], [{45: ('大小', {54: '属性或性状的名称'}), 44: ('脾脏', {7: '身体结构'}), 47: ('如常', {92: '描述'}), 46: ('形态', {54: '属性或性状的名称'})}], [{57: ('大小', {54: '属性或性状的名称'}), 56: ('胰腺', {7: '身体结构'}), 59: ('正常', {92: '描述'}), 58: ('形态', {54: '属性或性状的名称'})}]]

    """
    new_nodes_list = change_format_1(loop_node_in_json, text_category_checklist_in_json)
    # print("new_nodes_list: ", new_nodes_list )
    new_nodes_list_2 = change_format_2(new_nodes_list, export_file_category)
    return new_nodes_list_2


# 测试如下：

# json_path = "../python_test_data/json_file/annotation37529-37538.json"
# json_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/json_file/annotation39531-39600.json"

# single_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/json_file/39533.json"
# single_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/json_file/39501.json"
# single_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/json_file/39502.json"
#
# json_path = "../python_test_data/json_file/annotation39469-39530.json"
#

# export_file_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/export.json"
#
# # # 获得输入【0】: 10个json中所有的环，的节点表达形式。
# json_path = "../python_test_data/json_file/annotation39469-39530.json"
# all_loop_node_in_json = get_all_loop_node_in_json(json_path)
# print("all_loop_node_in_json:  ", all_loop_node_in_json)
#
# # # 获得输入【1】: 一个json处理后的环
# loop_node_in_json = all_loop_node_in_json[32]
# # print("loop_node_in_json[32]:  ", loop_node_in_json)
# print("loop_node_in_json[32]:  ", loop_node_in_json)
# #
# # # loop_node_in_json = all_loop_node_in_json[1]  #  -> 注意不能直接修改这个参数，因为找不到匹配的id:category，不同的json环id，对应不同的查找字典！
# #
# # # 获得输入【2】: 一个json处理后的,查找字典 -> 增加'text', 'category'
# text_category_checklist_in_json = get_single_json_id_text_category_list(single_path)
# print("text_category_checklist_in_json: ", text_category_checklist_in_json)
# #
# # # 获得输入【3】： 一个category:name 查找字典  -> 增加category 对应的中文-'身体结构'
# export_file_category = get_export_file_category(export_file_path)
# print("export_file_category:  ",export_file_category )
# print('---------------------------------------------')
#
# # 获得输出：
# new_nodes_list_2 = get_change_format_for_loop_nodes_in_json(loop_node_in_json, text_category_checklist_in_json, export_file_category)
#
# print('new_nodes_list_2: ', new_nodes_list_2)
# print('new_nodes_list_2[0]: ', new_nodes_list_2[0])



#test


