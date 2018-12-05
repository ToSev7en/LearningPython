
class Company(object):
    
    # 初始化
    def __init__(self, employee_list):
        self._emplyee = employee_list
    
    # def __getitem__(self, pos):
    #     return self._emplyee[pos]

    def __len__(self):
        return len(self._emplyee)


company = Company(['tom', 'bob', 'jack'])


# employee = company._emplyee

# for em in company:
#     print(em)


print(len(company))