class strtest:

    def __init__(self):
        print("init: print")

    def __str__(self):
        return "str: print"


class person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        # 可以指定位置位置
        return "{1} : {0} - {1}".format(self.name, self.gender)


class Mynumber(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "正在调用__str__方法，转为普通字符串{}".format(self.value)

    def __repr__(self):
        return "正在调用__repr__方法，转为普通字符串{}".format(self.value)


# import sys
# python 获取当前运行的 class 的名字
class testsqaws(object):

    def hello(self):
        # print("the name of method is {}".format(sys._getframe().f_code.co_name))
        print('the name of class is ## {} ##'.format(self.__class__.__name__))


if __name__ == "__main__":
    a = strtest()
    print(a)
    print("----------")

    b = person('male', 30)
    print(b)

    print('----------')

    c = Mynumber(100)
    print(c)
    print(str(c))  # 上面2个结果一样
    print(repr(c))  # 下面结果不同了

    print('-----------')
    d = testsqaws()
    d.hello()



# >> > "{} {}".format("hello", "world")  # 不设置指定位置，按默认顺序
# 'hello world'
#
# >> > "{0} {1}".format("hello", "world")  # 设置指定位置
# 'hello world'
#
# >> > "{1} {0} {1}".format("hello", "world")  # 设置指定位置
# 'world hello world'


# print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
#
# # 通过字典设置参数
# site = {"name": "菜鸟教程", "url": "www.runoob.com"}
# print("网站名：{name}, 地址 {url}".format(**site))
#
# # 通过列表索引设置参数
# my_list = ['菜鸟教程', 'www.runoob.com']
# print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
