# 没有 yield 的情况
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


if __name__ == "__main__":
    gen = sum_sales('apple')
    gen.send(None)
    gen.send(1200)
    gen.send(1000)
    gen.send(800)
    try:
        gen.send(None)
    except StopIteration as e:
        result = e.value
        print(result)

