# 输入地址
from NLP_Annotation_Stage_One.change_format_for_loop_nodes_in_10_json import find_all_loop_nodes_labelled_list
from NLP_Annotation_Stage_One.find_all_loop_edges_in_one_json import find_all_loop_edges_in_one_json_list
from NLP_Annotation_Stage_One.find_all_node_id_category_name import find_all_node_id_category_name
from NLP_Annotation_Stage_One.find_all_node_parent_relation_para import find_all_node_parent_relations

# export_file_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/export.json"
# relation_path = "../python_test_data/relation.json"

# json_path = "../python_test_data/json_file/annotation38125-38225.json"

# json_path = "../python_test_data/json_file/annotation38225-38325.json" #空

# json_path = "../python_test_data/json_file/annotation38325-38424.json" # 空

# json_path = "../python_test_data/json_file/annotation38425-38525.json" # 部分

# json_path = "../python_test_data/json_file/annotation38525-38625.json" # 空

# json_path = "../python_test_data/json_file/annotation38625-38724.json" # 空

# json_path = "../python_test_data/json_file/annotation38725-38825.json" # 部分标注

# json_path = "../python_test_data/json_file/annotation38825-38925.json" #空

# json_path = "../python_test_data/json_file/annotation38925-39024.json" #空

# json_path = "../python_test_data/json_file/annotation39025-39054.json" # 部分标注

# json_path = "../python_test_data/json_file/annotation39055-39155.json"

# json_path = "../python_test_data/json_file/annotation39155-39255.json"

# json_path = "../python_test_data/json_file/annotation39255-39354.json"

# json_path = "../python_test_data/json_file/annotation39356-39367.json"

# json_path = "../python_test_data/json_file/annotation39368-39375.json"

# json_path = "../python_test_data/json_file/annotation39376-39382.json"

# json_path = "../python_test_data/json_file/annotation39601-39664.json"

# json_path = "../python_test_data/json_file/annotation39531-39600.json"


# 出现问题：-------- IndexError: list index out of range

# json_path = "../python_test_data/json_file/annotation39469-39530.json"

# # 已经修复，无问题

# # 画图所需的数据



# # 输出1：
# all_loop_edges_in_one_json_list = find_all_loop_edges_in_one_json_list(json_path)

# print('all_loop_edges_in_one_json_list = ', all_loop_edges_in_one_json_list)
# print('-------------------1--------------------')

# # 输出2：
# all_loop_nodes_labelled_list = find_all_loop_nodes_labelled_list(json_path, export_file_path)
# print('all_loop_nodes_labelled_list = ', all_loop_nodes_labelled_list)
# print('-------------------2--------------------')

# # 输出3：
# all_loop_nodes_and_parents, all_loop_nodes_and_parents_relation = find_all_node_parent_relations(json_path, relation_path)
# print('all_loop_nodes_and_parents_relation = ', all_loop_nodes_and_parents_relation)
# print('-------------------3--------------------')

# # 输出4：
# all_node_id_category_name = find_all_node_id_category_name(json_path, export_file_path)
# print('all_node_id_category_name =', all_node_id_category_name)
# print('-------------------4--------------------')
