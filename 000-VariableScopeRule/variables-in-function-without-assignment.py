# 一个函数，读取一个局部变量和一个全局变量
# 变量未在函数的定义体中赋值

b = 6

def func(a):
    print(a)
    print(b)

func(3)


"""
如果 b = 6 被注释的话:
3
Traceback (most recent call last):
  File "/Users/tsw/Documents/CodeCampus/LearningPython/000-VariableScopeRule/variables-in-function.py", line 7, in <module>
    func(3)
  File "/Users/tsw/Documents/CodeCampus/LearningPython/000-VariableScopeRule/variables-in-function.py", line 5, in func
    print(b)
NameError: name 'b' is not defined
"""