#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# try except finally

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)

# add second except
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
# if NO error else will be excuted
else:
    print('no error!')
# finally will be excuted ALWAYS
finally:
    print('finally...')
print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，
# 这时，只要main()捕获到了，就可以处理
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

# 调用栈
# Traceback (most recent call last):
#   File "err.py", line 11, in <module>
#     main()
#   File "err.py", line 9, in main
#     bar('0')
#   File "err.py", line 6, in bar
#     return foo(s) * 2
#   File "err.py", line 3, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
#  出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。

# err_logging.py

# log will record the error and keep excution
# 程序打印完错误信息后会继续执行，并正常退出
import logging
# debug，info，warning，error
# logging.basicConfig(level=logging.INFO)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')


# raise 
# 抛出错误

# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
# 捕获错误目的只是记录一下，便于后续追踪。
# 但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。

# raise语句如果不带参数，就会把当前错误原样抛出。
# 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')

# DEBUGGING
# 调试

# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
# 如果断言失败，assert语句本身就会抛出AssertionError

# 启动Python解释器时可以用-O参数来关闭assert
# python -O err.py

import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                     datefmt='%m-%d %H:%M',
#                     filename='/temp/myapp.log',
#                     filemode='w')
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# Python的调试器pdb
import pdb
pdb.set_trace()

import numpy as np
y = np.random.random(10**5).astype(np.float32)

def clip(y, a, b):
    if y < a:
        return a
    if y > b:
        return b
    return y