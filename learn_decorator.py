# -*- coding: utf-8 -*-


import functools

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print("%s begin call %s()" % (text, func.__name__))
#             ret = func(*args, **kw)
#             print("%s end call %s()" % (text, func.__name__))
#             return ret
#         return wrapper
#     if isinstance(text, str):
#         return decorator
#     else:
#         f = text
#         text = ''
#         return decorator(f)

# @log    #('excute')
# def f():
#     print("soso!")
# f()
# 

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s begin call %s()" % (text, func.__name__))
            ret = func(*args, **kw)
            print("%s end call %s()" % (text, func.__name__))
            return ret
        return wrapper
    if isinstance(text, str):
        return decorator
    else:
        f = text
        text = ''
        return decorator(f)

@log#('excute')
def f():
    print("soso!")
f()
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def abc():
#     print('2015-3-25')

# abc()