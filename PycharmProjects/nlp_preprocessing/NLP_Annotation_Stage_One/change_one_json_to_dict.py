"""
输入：json_path

输出：all_graph:  [{106: {}, 1: {109: 135}, 108: {109: 134}, 109: {}, 107: {}, 4: {5: 135}, 5: {110: 135}, 6: {110: 134}, 111: {8: 138},

"""


import json
import emoji


# print(emoji.emojize("Python is fun :thumbs_up:"))
# print(emoji.emojize("Python is fun :thumbs_down:"))


# 1) 把其中一个json文件中的所有段落，拆出
def get_paragraph_of_json(json_path):
    with open(json_path, "r") as f:
        load_dict = json.load(f)
    json_paragraph_list = []

    for paragraph in load_dict:
        json_paragraph_list.append(paragraph)
    return json_paragraph_list


# 2）把每个段落，进行处理， one json file -> one paragraph -> one dict
def change_one_paragraph_to_dict(json_paragraph):
    # 对每个json文件中的每一段话，进行处理
    graph_in = dict()
    for node in json_paragraph['labels']:
        graph_in[node['id']] = {'type': node['category']}

    for item in json_paragraph['relations']:
        dst = item['dst']
        src = item['src']
        category = item['category']
        graph_in[src][dst] = category

    for node in graph_in:
        graph_in[node].__delitem__('type')
    # graph_in_all_dict.append(graph_in)
    return graph_in

# 3) 把整个json文件，转好的dict，统一到list
def all_graph_in_json(json_path):
    all_graph_in_json = []
    json_paragraph_list = get_paragraph_of_json(json_path)
    for paragraph_i in json_paragraph_list:
        one_paragraph_to_dict = change_one_paragraph_to_dict(paragraph_i)
        all_graph_in_json.append(one_paragraph_to_dict)
    return all_graph_in_json

# [测试]：
# json_path = "../python_test_data/json_file/annotation37730-37739.json"
# json_path = "../python_test_data/json_file/annotation37529-37538.json"


# 举例
# json_path = "../python_test_data/json_file/annotation39469-39530.json"


# all_graph = all_graph_in_json(json_path)
# print('all_graph: ', all_graph)
# print(emoji.emojize("Program passed :thumbs_up:"))
