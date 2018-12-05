
# Python 3.3 新增 yield from 语法，是理解协程的基础

# 将迭代类型连接起来进行循环遍历
from itertools import chain
lst = [1,2,3]
dic = {
    "tsw":"www.tsw.com",
    "bob":"bob.com"
}
# 使用 chain 方法可以直接对三个进行 for 循环
for value in chain(lst,dic,range(5,10)):
    print(value)

# chain 的实现方法
# *args
# **kwargs 
def chainer(*args, **kwargs):
    for iterable in args:
        yield from iterable
        # 可以使用 yield from 代替以下语句
        # for value in iterable:
        #     yield value


# for value in chainer(lst,dic,range(5,10)):
#     print(value)



# yield from + iterable 对象


# yield from 和 yield 的区别
def g1(iterable):
    yield range(10)

def g2(iterable):
    yield from range(10)

for v in g1(range(10)):
    print(v)

for v in g2(range(10)):
    print(v)