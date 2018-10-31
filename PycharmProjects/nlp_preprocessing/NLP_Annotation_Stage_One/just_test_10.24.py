# import tsunagi
# print(tsunagi.get_disease_concept_id("肺癌"))
# print(tsunagi.get_disease_concept_id("肺恶性肿瘤"))

# basic
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
#     def print_score(self):
#         print('name:{} \nscore:{}'.format(self.name, self.score))
#
#
#     def get_grade(self):
#         if self.score >= 90:
#             return "A"
#         elif self.score >= 60:
#             return "B"
#         else:
#             return "C"
#     i = 12345

# bart = Student('bart', 50)
# bart_2 = Student('bart_2', 98)
#
# bart.print_score()
# bart_grade = bart.get_grade()
#
# print(bart_grade)
# print(bart_2.get_grade())
# print(bart.i)


# class Employee:
#     pass
#
# john = Employee()
#
# john.name = 'Jonh Doe'
# john.dep = 'computer lab'
#
# print(john.name)


# class Account(object):
#
#     num_accounts = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.num_accounts += 1
#
#     def del_account(self):
#         Account.num_accounts -= 1
#
#     def add_account(self):
#         Account.num_accounts += 10
#
#     def __getattr__(self, item):
#         return "Hey, i don't see any attribute called {}".format(item)
#
#
# x = Account('obj', 0)
#
# a = x.number
#
# print(a)


# CustomList是个真实列表的简单包装器
# class A(object):
#
#     def __init__(self, container = None):
#         if container is None:
#             self.container = []
#         else:
#             self.container = container
#
#     # classmethod & staticmethod 的区别
#     def foo(self, x):
#         print(" executing foo {}, {}".format(self, x))
#
#     @classmethod
#     def class_foo(cls, x):
#         print(" executing class_foo {}, {}".format(cls, x))
#
#     @staticmethod
#     def static_foo(x):
#         print(" executing static_foo {}".format(x))
#
#     # 自己定义的特殊方法会优先调用
#     def __len__(self):
#         return len(self.container)
#
#     def __getitem__(self, index):
#         return self.container[index]
#
#     def __setitem__(self, key, value):
#         self.container[key] = value
#
#     def append(self, value):
#         self.container.append(value)
#
#     def __add__(self, other):
#         return A(self.container + other.container)
#
#     def __repr__(self):
#         return str(self.container)
#
#     # 加2杠变为私有方法
#     def __kanbujian(self):
#         return 2


# 测试
# a = A()
#
# a1 = a.foo(1)
# a2 = a.class_foo(1)
# a3 = a.static_foo(1)
#
# print("a1: ", a1)
# print("a2: ", a2)
# print("a3: ", a3)
# print(a.class_foo(1))
# a = 1


# 类中最常见的方法是实例方法 ： 类与实例的交互
# class Kls(object):
#
#     def __init__(self, data):
#         self.data = data
#
#     def printd(self):
#         print(self.data)
#
# ik1 = Kls('arun')
#
# ik1.printd()


# 类与类之间的交互，我们要写一个只在类中运行而不在实例中运行的方法 -》 @classmethod
# class Kls(object):
#
#     no_inst = 0
#
#     def __init__(self):
#         Kls.no_inst += 1
#
#     @classmethod
#     def get_no_of_instance(cls_obj):
#         return cls_obj.no_inst
#
# ik1 = Kls()
#
# print(ik1.get_no_of_instance())


# @staticmethod
# 经常有一些跟类有关系的功能但在运行时又不需要实例和类参与的情况下需要用到静态方法
#
# __metaclass__ = type
#
# class Bird(object):
#     def __init__(self):
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry == True:
#             print("eat,eat,eat...")
#             self.hungry = False
#         else:
#             print('No, thanks')
#
#
# # a = Bird()
# # a.eat()
#
# class SongBird(Bird):
#
#     #
#     # 子类的方法，注意别重写构造方法，会提示，song_bird没有eat的方法
#     def __init__(self):
#         super(SongBird, self).__init__()
#         self.sound = "la~la~la~la~la~~"
#
#     def sing(self):
#         print(self.sound)
#         # print('la~la~la~la~la~~')
#
#
# print('------下面调用sing方法------')
#
# song_bird = SongBird()
# song_bird.sing()
#
# print('------下面调用eat方法------')
#
# song_bird.eat()


# -----------------------------------------------------------

# 绑定属性@property
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
# 这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：


# class Student(object):
#
#     @property
#     def get_score(self):
#         return self._score
#
#     # def __repr__(self):
#     #     return str(self.get_score())
#
#
#     # Python内置的@property装饰器就是负责把一个方法变成属性调用的：
#     @property
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100')
#         self._score = value
#
#     # def print_s_data(self):
#     #     print(self._score)
#
# s = Student()
#
# # s.set_score(9999)
#
# s.set_score = 50
# a = 1


#
# class Student(object):
#
#
#     def set_score(self):
#
#     pass
#
# def set_age(self, age):
#     self.age = age
#
#
#
#
# s = Student()
# s.name = "michael"
#
# print(s.name)


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
#     __repr__ = __str__
#
# a  = Student( ' xiaoming')
#



# continue 与 pass
# a = ['a', 'b', 'c', 'd']
# i = 2
#
# for element in a:
#     if element == 'd':
#         # continue # 表示跳过后面的程序，重新循环
#         pass   # 就是个占位
#         print('哈哈')
#     else:
#         print(element)
#         print('lalala')

