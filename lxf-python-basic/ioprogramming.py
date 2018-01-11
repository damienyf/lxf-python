#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文件读写

# 如果文件不存在，open()函数就会抛出一个IOError的错误
f = open('/test/mydict.py', r)

# read()方法可以一次读取文件的全部内容，
# Python把内容读到内存，用一个str对象表示：
f.read()

# 最后一步是调用close()方法关闭文件。
f.close()

# 由于文件读写时都有可能产生IOError，
# 一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，
# 我们可以使用try ... finally来实现

# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# Python引入了with语句来自动帮我们调用close()方法
with open('/test/mydict.py', 'r') as f:
    print(f.read())

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
# 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行


# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件
f = open('/Users/michael/test.jpg', 'rb') 
f.read()

# 非UTF-8编码的文本文件，需要给open()函数传入encoding参数
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
f.read()

# UnicodeDecodeError errors参数
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')


# 'w' write 文本文件
# 'wb' wite 二进制文件
# 'a'以追加（append）模式写入

# 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
with open('Users/michael/test.txt', 'a', encoding='gbk') as f:
    f.write('Hello, world!')

# StringIO
# 数据读写不一定是文件，也可以在内存中读写。
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
# write
from io import StringIO
f = StringIO()
f.write('hello')

f.write(' ')

f.write('world!')
# getvalue()方法用于获得写入后的str。
print(f.getvalue())

# read
from io import StringIO
f = StringIO('Hello!\nHi\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO for binary data
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
f.close()

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()

# set the stream position
from io import StringIO
f = StringIO()
f.write('Hello World')
# tell() method returns current streaming position
f.tell()
f.seek(0)