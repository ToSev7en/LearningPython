# 检查某个类是否有某个方法
class Company:
    def __init__(self, employee_lst):
        self.employee = employee_lst
    
    def __len__(self):
        return len(self.employee)



com = Company(["Bob","Jack"])
print(hasattr(com, "__len__"))
print(len(com))

import collections.abc

