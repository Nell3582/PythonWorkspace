def print_log(func):
    def wrapper(*args,**kwargs):
        print(f'call {func.__name__}()')
        return func(*args, **kwargs)
    return wrapper


@print_log
def foo(*args):
    lt = []
    for data in args:
        print(f'My Name is {data}')
    #     lt.append(f'my name is {data}')
    # return lt

lt = ['xiaoyu','xiaohui','xiaohei','honghong','fangfang']

f = foo(*lt)
print(f)


