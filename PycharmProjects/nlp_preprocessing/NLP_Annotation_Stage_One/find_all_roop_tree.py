"""
输入： 一个json文件中10段话的子图 -> 生成的所有树的集合

输出：长度大于1的元素(存在环),组成的list

"""

from NLP_Annotation_Stage_One.json_to_all_trees import *


# all_trees_in_json = json_to_all_trees(json_path)


def find_all_roop_tree(all_trees_in_json):
    all_loop_tree_extend = []
    all_loop_tree_append = []

    for sub_graph in all_trees_in_json:
        sub_graph_roop_tree = find_roop_tree(sub_graph)
        all_loop_tree_extend.extend(sub_graph_roop_tree)  # 注意这里不能使用append, 需要使用extend, 把10个图的结果作为list加入，不行
        all_loop_tree_append.append(sub_graph_roop_tree)  # 如果需要使用append，它可以用来单独计算每段话中，有多少个环。
    return all_loop_tree_append


def find_roop_tree(all_trees_in_json_01):
    roop_tree_list = []
    for i in all_trees_in_json_01:
        if len(i) > 1:
            roop_tree_list.append(i)
    return roop_tree_list


# all_loop_tree = find_all_roop_tree(all_trees_in_json)


# 汇总上面的步骤：
def find_all_roop_tree_total(json_path):
    all_trees_in_json = json_to_all_trees(json_path)
    all_loop_tree = find_all_roop_tree(all_trees_in_json)
    return all_loop_tree


# 【测试】：
# json_path = "../python_test_data/json_file/annotation37529-37538.json"

json_path = "../python_test_data/json_file/annotation37730-37739.json"

all_loop_tree = find_all_roop_tree_total(json_path)


print(all_loop_tree)
print(len(all_loop_tree))  # 使用extend时候结果len = 35， 说明一共10段话中，出现了35个环, 集合已打印出来， 使用append时，结果len=10， 因为一共add了10次，10段话中的结果
print('------------------\n')

# print(all_loop_tree[0])
# print(len(all_loop_tree[0]))  # 结果len = 3， 说明第一段话中，出现了3个环
# print('------------------\n')
#
# print(all_loop_tree[1])
# print(len(all_loop_tree[1]))  # 结果len = 3， 说明第一段话中，出现了3个环
# print('------------------\n')




# 找出10段话中，每段话中有几个环，
for i in range(len(all_loop_tree)):
    print('第', i, '段话中，所有带环的子图集合为： ', all_loop_tree[i])
    print('第', i, '段话中，出现环的子图个数为： ', len(all_loop_tree[i]))
    print('\n')
    for j in range(len(all_loop_tree[i])):
        print('第', j, '个子图为：', all_loop_tree[i][j])
        print('第', j, '个子图包含的边个数为： ', len(all_loop_tree[i][j]))

    print('-------------\n')

