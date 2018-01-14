#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 摘要算法简介
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
# 就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。


import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())



# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。


# 另一种常见的摘要算法是SHA1


import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# 2c76b57293ce30acef38d98f6046927161b46a44


由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
def calc_md5(password):
    return get_md5(password + 'the-Salt')

# 经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

# 但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，
# 这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？

# 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。