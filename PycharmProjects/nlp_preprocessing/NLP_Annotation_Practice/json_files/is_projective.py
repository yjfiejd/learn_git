# -*- coding:utf8 -*-
# @TIME : 2018/9/3 下午2:36
# @Author : Allen
# @File : is_projective.py

def is_projective(sentence):
    roots = sentence[:]

    unassigned = defaultdict(int)
    for entry in sentence:
        for possible_child in sentence:
            if entry.id == possible_child.parent:
                unassigned[entry.id] += 1

    for _ in range(len(sentence)):
        for i in range(len(roots) - 1):
            if roots[i].parent == roots[i+1].id and unassigned[roots[i].id] == 0:
                unassigned[roots[i+1].id] -= 1
                del roots[i]
                break
            if roots[i+1].parent == roots[i].id and unassigned[roots[i+1].id] == 0:
                unassigned[roots[i].id] -= 1
                del roots[i+1]
                break
