def get_url():
    pass
    # 耗IO，希望此处暂停，立马切换到另一个函数去执行
    # html = get_html(url)

    # urls = parse_url(html)

# 耗 CPU 



# 传统的函数调用是基于栈的，A->B->C
# 需要一个可以暂停的函数，并且可以在适当的时候恢复并继续执行
# 这样就可以用 同步的方式写代码 以及 使用单线程切换任务


# 为解决这个问题，出现了 Coroutine 的概念。
# Coroutine -> 多个入口的函数，可以暂停的函数（可以往里面传入值）

# Generator 就是一个可以暂停的函数罗

