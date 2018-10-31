# -*- coding:utf8 -*-
# @TIME : 2018/8/29 上午9:50
# @Author : Allen
# @File : annotation_01_test.py

# 学习python的collections, python内建的一个集合模块
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431953239820157155d21c494e5786fce303f3018c86000


# nametuple
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(isinstance(p, Point))

Circle = namedtuple('circle', ['x', 'y', 'z'])
a = Circle(1, 2, 4)
print(a.z)

# deque: 双向列表，适合用于队列和栈
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
q.popleft()
print(q)

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict

from collections import defaultdict
dd = defaultdict(lambda : 'N/A')


dd['key1'] = 'abc'

print(dd['key1'])
print(dd['key2'])

#Counter
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
    print(c[ch])

print(c)

