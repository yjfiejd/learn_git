import json
import sys
import re
from collections import defaultdict


def remove_unlabel(annotation):
    data = sorted(annotation['labels'], key=lambda x: x['pos'][0])
    flag = 0
    unlabel = []
    for item in data:
        # if re.search('鉴别诊断',annotation['content'][item['pos'][0]:item['pos'][1] + 1]):
        #     print('*******',annotation['id'])

        if re.match(r'^鉴别诊断$', annotation['content'][item['pos'][0]:item['pos'][1] + 1]) or item['category'] == 44:
            # print('---------------', annotation['id'])
            # print(annotation['content'][item['pos'][0]:item['pos'][1] + 1])

            flag = 1
            unlabel.append(item['id'])
        elif flag == 1:
            # print(annotation['content'][item['pos'][0]:item['pos'][1] + 1], annotation['id'])
            if item['category'] == 28 or item['category'] == 44:
                flag = 0
            unlabel.append(item['id'])
        elif re.match(r'^\s+$', annotation['content'][item['pos'][0]:item['pos'][1] + 1]):
            unlabel.append(item['id'])

    rel = [i for i in annotation['relations'] if (i['src'] not in unlabel and i['dst'] not in unlabel)]
    lab = [i for i in annotation['labels'] if i['id'] not in unlabel]
    annotation['labels'] = lab
    annotation['relations'] = rel

    return annotation

def train2anno(train):
    result = {'concepts': []}
    train = remove_unlabel(train)
    sorted_label = sorted(train['labels'], key=lambda x: x['pos'][0])
    temp = {'id': 0, 'pos': [0, 0], 'relation': [], 'timestamps': 0}
    for j, item in enumerate(sorted_label):
        result['concepts'].append(
            {'id': item['id'], 'pos': [item['pos'][0], item['pos'][1] + 1], 'relations': [], 'timestamps': item['id'],
             'category':item['category'],'text':train['content'][item['pos'][0]:item['pos'][1] + 1]})

    for j, item in enumerate(train['relations']):
        src = item['src']
        dst = item['dst']
        for ii in result['concepts']:
            if ii['timestamps'] == dst:
                for jj in result['concepts']:
                    if jj['timestamps'] == src:
                        ii['relations'].append({"text": jj['text'], "src_id": jj['id'], 'type': item['category']})

    anno = {'NLPResult': result, 'rawText': train['content']}

    return anno

if __name__ == "__main__":
    anno_id = 37532

    path = '/Users/synyi/PycharmProjects/NLP_Annotation_Practice/NLP_Annotation_Practice/json_files/annotation37529-37538.json'

    # path = '../training_data/record_1712.json'

    # path = '/Users/Ludwig/Downloads/annotation23143-23143.json'

    import os
    def open_json(files):
        if files.endswith('.json'):
            with open(files, 'r', encoding='utf8') as f:
                return json.load(f)

        else:
            result = []
            PATH = os.listdir(files)
            for file in PATH:
                with open(files + file, 'r', encoding='utf8') as f:
                    result.extend(json.load(f))
            return result


    data = open_json(path)
    a=set()
    # result = []
    # for item in data:
    #     result.append(train2anno(item))
    # with open('../result/' + str(anno_id) + '.json', 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(train2anno(item), ensure_ascii=False, indent=4))

    # for item in data:
    #     with open('../result/cemr'+str(item['id'])+'.json', 'w', encoding='utf-8') as f:
    #         f.write(json.dumps(train2anno(item), ensure_ascii=False, indent=4))


    for item in data:
        if  item["id"] == anno_id:
            print('ok')
            print(item)
            with open('./'+str(anno_id)+'.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(train2anno(item), ensure_ascii=False, indent=4))

            # with open('test_content.txt','w',encoding='utf-8') as f:
            #     f.write(item['content'])
            # break
        # print(a)

    # if __name__ == '__main__':
    #     with open(sys.argv[1],'r',encoding='utf-8') as f:
    #         data = json.load(f)
    #         for i, emr in enumerate(data):
    #             with open (sys.argv[2]+str(i),'w',encoding='utf-8') as fp:
    #                 fp.write(json.dumps(train2anno(emr),ensure_ascii=False,indent=4))
    #         print(len(data))