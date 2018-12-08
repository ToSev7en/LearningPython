# 变量在函数的定义体中进行了赋值操作
# Python 编译函数的定义体时，会将假定该变量为局部变量
# 这不是缺陷，而是一种设计策略
# 如果在函数中赋值的时候，想让解释器把变量b当成全局变量，要使用 global 关键字声明

b = 6

def func(a):
    global b
    print(a)
    print(b)
    b = 9

func(3)

"""
3
Traceback (most recent call last):
  File "/Users/tsw/Documents/CodeCampus/LearningPython/000-VariableScopeRule/variables-with-assignment-in-function.py", line 11, in <module>
    func(3)
  File "/Users/tsw/Documents/CodeCampus/LearningPython/000-VariableScopeRule/variables-with-assignment-in-function.py", line 8, in func
    print(b)
UnboundLocalError: local variable 'b' referenced before assignment
"""