#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# returning function

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax =ax + n
        return ax
    return sum

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。

f = lazy_sum(1,4,5,6,7,9)
f()

# every time we call lazy_sum(), it will return a new function:
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
# False
f1 == f2


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
# thiso will return a list of 3 functions..
f = count()
# f1 , f2 and f3 have same result
f1, f2, f3 = count()
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
# f1, f2 and f3 are actually function g
# when f(i) is called, i's current value is passed into g 
f1, f2, f3 = count()

# anonymous function:
# this will return a function that takes NO input parameter
def build(x, y):
    return lambda: x * x + y * y

# this will return a function that takes x as input paramter 
def build2(y):
    return lambda x: x * x + y * y
x = build2(2)


# Decorator
def now():
    print('2017-11-18')

f = now
f()

# function has a __name__ property 
now.__name__
f.__name__

# now we want to enhance the function 'now()' however keeping the definition
def log(func):
    def wrapper(*args, **kw):
        # print a log
        print('call %s():' % func.__name__)
        # return the function
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

# keep the function property such as __name__
# functools.wraps(func)
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*agrs, **kw)
    return wrapper


# 针对带参数的decorator
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-03-25')


# partial function can fix parameter to create new function
# like setting default paramter
import functools
int2 = functools.partial(int, base=2)

int2('100')

# but you can always reset it
int2('10000', base=10)

# functools.partial can take three parameters: function, *args, **kw
# e.g. int2 = functools.partial(int, base=2)
# int2('100') is equivalent to kw = { 'base': 2 }
# int('100', **kw)

# add *args
max2 = functools.partial(max, 10)

max2(2, 4, 6)
# is equivalent to args = (10,2,4,6)
# max(*args)
