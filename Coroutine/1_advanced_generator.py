
# 0.生成器可以 yield 值
def gen_func_0():
    yield 1
    yield 2
    yield 3
    return 'tsw'

# 1.生成器不仅可以 yield 值，还可以接收值
def gen_func_1():
    # 1.
    html = yield "http://www.baidu.com"
    print(html)
    yield 1
    yield 2
    yield 3
    return 'tsw'



if __name__ == "__main__":
    
    # 启动生成器方式有两种：1.next() 2.send()

    # next()
    # gen = gen_func_0()
    # Gen 实现了迭代协议，可以使用 next()
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))

    # send()
    gen = gen_func_1()
    
    
    # 在调用 send 发送非 None 值之前，必须启动一次生成器
    # 方式有两种：
    
    # 第一种：发送 None 值url = gen.send(None)
    # 此处只能 send None
    # url = gen.send(None) 
    
    # 第二种：
    url = next(gen)
    
    # download url
    html = "<h1>Hello!</h1>"

    # send() 可以传递值进入生成器内部,next() 不行。并且重启生成器执行到下一个 yield
    gen.send(html)
    print(gen.send(html))

    # 有了 send 方法，生成器才可能成为一个协程

    # next()

    # send()

    # close()

    # throw()


    # GeneratorExit 继承 BaseException 而不是 Exception