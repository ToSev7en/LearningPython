import numbers
class Group:

    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    """
    Sequence 协议需要实现的魔法函数
    """

    def __reversed__(self):
        self.staffs.reverse()
    
    # 实现切片功能的关键
    # item 可以是索引数值，也可以是 Slice 对象
    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(company_name=self.company_name, group_name=self.group_name, staffs=self.staffs[item])
        if isinstance(item, numbers.Integral):
            return cls(company_name=self.company_name, group_name=self.group_name, staffs=[self.staffs[item]])
    
    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


group = Group(company_name="ecnu", group_name="stu", staffs=['bob','jack','tom'])

# print(group[:2])
# print(group[0])

# if 'bob' in group:
#     print('yes')

# for user in group:
#     print(user)

res = reversed(group)

print(group[:2])
print(group[0])

        