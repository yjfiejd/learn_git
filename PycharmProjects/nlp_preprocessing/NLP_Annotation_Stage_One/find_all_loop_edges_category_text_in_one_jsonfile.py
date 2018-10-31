import json

from NLP_Annotation_Stage_One.find_all_loop_edges_in_one_json import find_all_loop_edges_in_one_json_list, \
    find_all_right_input_by_edges


def get_json_file_relations(json_path):
    """
    :param json_path: 一个json文件
    :return: 获得每篇json的查找字典list
    [[{'dst': 426, 'id': 0, 'category': 135, 'src': 425},
      {'dst': 426, 'id': 1, 'category': 92, 'src': 424},
      {'dst': 426, 'id': 2, 'category': 86, 'src': 10},
    """
    with open(json_path, "r") as f:
        one_json = json.load(f)
    one_json_relations = []
    for i in one_json:
        one_json_relations.append(i['relations'])
    return one_json_relations


def get_relation_file_category_text(relation_path):
    """
    :param relation_path:  一个 relation文件路径
    :return:  category -> 对应的文本，
    {1: '作用于_（失效）',
     2: '是_的治疗',
     3: '是_的发展趋势',
     4: '导致了_（失效）',
    """
    with open(relation_path, "r") as f:
        export_file = json.load(f)
    # 返回一个只含有 category : text 的字典
    list_id_text = {}
    for item in export_file:
        list_id_text[item['id']] = item['text']

    return list_id_text


def find_all_loop_edges_category_text_in_one_json(json_path, relation_path):
    """
    :param json_path: json文件
    :param relation_path: relation文件
    :return: 返回json_path中所有的【带环边：边的relation】的一个字典
    [[[{(487, 735): {91: '发起_动作'}}, {(735, 490): {92: '作用于_'}}, {(487, 490): {119: '(不借助知识等信息无法具体化)有相关'}}],....

    """

    # 获得输入一，找到json（含有多个single_json文件）中所有环：[[[(487, 735), (735, 490), (487, 490)], [(513, 516), (514, 516), (512, 514), (512, 513)], ...
    all_loop_edges_in_one_json_list = find_all_loop_edges_in_one_json_list(json_path)

    # 获得输入二， 可以通过"dst"& "src"找到每个环对应的文章中的 'category' 关系数值: [[{'dst': 426, 'id': 0, 'category': 135, 'src': 425},....
    json_file_relations = get_json_file_relations(json_path)

    # 获得输入三，找到relation的匹配关系， 由category -> text 文本
    relation_file_name = get_relation_file_category_text(relation_path)

    # 获得整个json中的结果
    all_loop_edges_category_list = []
    for i in range(len(json_file_relations)):
        loop_edges_just_in_one_json_i = all_loop_edges_in_one_json_list[i]
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
        all_loop_edges_category_list.append(list_1)
    #     print('------------------')
    return all_loop_edges_category_list


# new 【新建一个函数】-> 让每篇文章中的子簇(edges)表达出边的信息(就是带含义)，
def find_all_right_input_by_edges_list_category(json_path, relation_path):
    """
    :param json_path: 文件
    :param relation_path: 文件
    :return:
    为了获得 all_right_input_by_edges_list 边的集合
    [[[{(6, 445): {86: '是_的限定'}}, {(446, 445): {121: '是_的描述/值'}},

    """
    # 获得输入一：这里不同于上面的函数，上面的边是带环边的合集，这里是所有子簇的合集(edges).
    all_right_input_by_edges_list = find_all_right_input_by_edges(json_path)

    # 下面是一样的处理过程 ->  注意第i个，名字修改 all_right_input_by_edges_list[i]

    # 获得输入二， 可以通过"dst"& "src"找到每个环对应的文章中的 'category' 关系数值: [[{'dst': 426, 'id': 0, 'category': 135, 'src': 425},....
    json_file_relations = get_json_file_relations(json_path)

    # 获得输入三，找到relation的匹配关系， 由category -> text 文本
    relation_file_name = get_relation_file_category_text(relation_path)

    # 获得整个json中的结果
    all_right_input_by_edges_list_with_category = []
    for i in range(len(json_file_relations)):
        loop_edges_just_in_one_json_i = all_right_input_by_edges_list[i]
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
        all_right_input_by_edges_list_with_category.append(list_1)
    #     print('------------------')
    return all_right_input_by_edges_list_with_category







# 测试一下：

# relation_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/relation.json"
# json_path = "../python_test_data/json_file/annotation39469-39530.json"
# json_path = "../python_test_data/json_file/annotation39469-39530.json"
#
#
# all_loop_edges_category_list = find_all_loop_edges_category_text_in_one_json(json_path, relation_path)
# print("all_loop_edges_category_list = ", all_loop_edges_category_list)


# new test 10.15 -> 子簇所有的边的标记


# json_path = "../python_test_data/json_file/annotation39469-39530.json"
# relation_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/relation.json"
# all_right_input_by_edges_list_with_category = find_all_right_input_by_edges_list_category(json_path, relation_path)
# print("all_right_input_by_edges_list_with_category = ", all_right_input_by_edges_list_with_category)





