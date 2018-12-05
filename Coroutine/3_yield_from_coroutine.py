"""

def func_yield_from(iterable):
    yield from iterable


def main():
    g = func_yield_from(range(10))
    g.send(None)


# 1.main 调用方，g1 委托生成器， gen 子生成器
# 2.yield from 会在调用方和子生成器直接建立一个通道,双向通道，可以互相通信

"""

final_result = {}

# 子生成器
def sum_sales(product_name):
    total = 0
    nums = []
    while True:
        x = yield

        if x:
            print(product_name + "销量：", x)

        # 当 send None 的时候，跳出 while 循环
        if not x:
            break
        
        total += x
        nums.append(x)

    return total, nums


# 委托生成器
def middle(key):
    while True:
        final_result[key] = yield from sum_sales(key)
        print("Complete!",final_result[key])


# 调用方
def main():
    dataset = {
        'apple': [1200, 1330, 500],
        'orange': [400, 600, 1000],
        'banana': [100, 500, 50]
    }

    for key,dataset in dataset.items():
        
        print('key:', key)
        print('dataset:',dataset)
        
        m = middle(key)
        
        # 预激 middle 协程
        m.send(None)

        # 给协程传递每一组的值
        for value in dataset:
            m.send(value)
        
        # 传递 None 终止 while 循环
        m.send(None)
    
    print(final_result)

if __name__ == "__main__":
    main()