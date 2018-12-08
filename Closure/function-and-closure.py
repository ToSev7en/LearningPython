# 只有在涉及嵌套函数的时候，才会有闭包问题
# 闭包指的是延伸了作用域的函数，其中包含了函数定义体中的引用、但是不在定义体中定义的非全局变量
# 函数是不是匿名的没有关系，关键是它能够访问定义体之外定义的非全局变量


# 计算移动平均值的类
class Averager():
    def __init__(self):
        self.series = []

    # 一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()
    def __call__(self,new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

cls_avg = Averager()
print(cls_avg(10))
print(cls_avg(11))
print(cls_avg(12))
print(cls_avg(13))


# 计算移动平均值的高阶函数
def make_averager():

    # 函数 averager 的闭包范围延伸到那个函数的作用域之外，包含自由变量 seris 的绑定
    '<closure name="函数 averager 的闭包范围">'

    # 在 make_averager 函数定义体中初始化，是该函数的局部变量
    series = []

    # 所有的函数都是可调用对象
    def averager(new_value):
        # 在 averager 函数中， series 是自由变量（free variable）
        # 指的是未在本地作用域中绑定的变量
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    '</closure>'

    return averager


fun_avg = make_averager()
print(fun_avg(10))
print(fun_avg(11))
print(fun_avg(12))
print(fun_avg(13))

"""
综上，闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，
这样调用函数时，虽然定义作用域不可用了，但是仍然能够使用那些绑定。
"""