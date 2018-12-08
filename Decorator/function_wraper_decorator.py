

def cache(func):
    data = {}

    def wrapper(*args, **kwargs):
        # 从Python 3.6开始，f-string是格式化字符串的一种很好的新方法。
        # 与其他格式化方式相比，它们不仅更易读，更简洁，不易出错，而且速度更快！
        key = f'{func.__name__}-{str(args)}-{str(kwargs)})'

        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')
        return result

    return wrapper
    


@cache
def rectangle_area(length, width):
    return length * width

rectangle_area(2, 3)
# calculated
# 6

rectangle_area(2, 3)
# cached
# 6