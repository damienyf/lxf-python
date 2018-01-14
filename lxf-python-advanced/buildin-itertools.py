#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# count
import itertools
natuals = itertools.count(1)
for n in natuals:
    print(n)


# cycle
import itertools
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
for c in cs:
    print(c)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

# 通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
list(ns)

# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
    print(c)


# groupby()
# 把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBCWCA'):
    print(key, list(group))
# 相邻, 重复


# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
import itertools
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

# A ['A', 'a', 'a']
# B ['B', 'B', 'b']
# C ['c', 'C']
# A ['A', 'A', 'a']



import itertools
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    nature = itertools.count(1,2)

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x: x <= (2*N-1), nature)

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    incre = 1
    result = 0
    for n in ns:
        if incre % 2 == 1:
            result = result + (4*1.0/n)
        else:
            result = result - (4*1.0/n)
        incre += 1
    # step 4: 求和:
    return result

def pi(N):
    c = itertools.cycle([4, -4])
    s = sum([next(c)/(2*x-1) for x in range(1, N+1)])
    return s