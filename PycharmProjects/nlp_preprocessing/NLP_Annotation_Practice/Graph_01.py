# -*- coding:utf8 -*-
# @TIME : 2018/8/30 下午8:00
# @Author : Allen
# @File : Graph_01.py


from collections import deque

GRAPH = {
    'A': ['B', 'C'],
    'B': ['D', 'E', ],
    'C': ['F'],
    'D': ['E'],
    'E': ['B', 'D', 'G'],
    'F': ['C', 'G'],
    'G': ['E', 'F'],
}


class Queue(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


def bfs(graph, start):
    search_queue = Queue()
    search_queue.push(start)
    searched = set()

    while search_queue:  # 当前队列不为空
        cur_node = search_queue.pop()
        if cur_node not in searched:
            print(cur_node)
            searched.add(cur_node)
            for node in graph[cur_node]:
                search_queue.push(node)


print("-------------")

print('bfs: ')
bfs(GRAPH, 'A')

print("-------------")

dfs_searched = set()


def dfs(graph, start):
    if start not in dfs_searched:
        print(start)
        dfs_searched.add(start)
    for node in graph[start]:
        if node not in dfs_searched:
            dfs(graph, node)


print('dfs: ')
dfs(GRAPH, 'A')
