#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
# show os name, 'nt' if windows, and posix is linux kernel
os.name

# os.environ 环境变量
os.environ
os.environ.get('PATH')


# 查看当前目录的绝对路径:
os.path.abspath('.')

os.getcwd()

# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
new_dir = os.path.join(os.path.abspath('.'), 'testdir')

# make a directory
os.mkdir(new_dir)

# remove a directory
os.rmdir(new_dir) 

# 把两个路径合成一个时，不要直接拼字符串，
# 而要通过os.path.join()函数正确处理不同操作系统的路径分隔符

# 通过os.path.split()函数get文件名 (path + file.extension)
os.path.split(r'C:\Users\Yunfei\algo-ds\lxf\testdir\file.txt')

# os.path.splitext()得到文件扩展名 ( , .extension)
os.path.splitext(r'C:\Users\Yunfei\algo-ds\lxf\testdir\file.txt')
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在

# 对文件重命名:
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')

# shutil模块提供了copyfile()的函数

# list comprehension
# 列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]

# 要列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']