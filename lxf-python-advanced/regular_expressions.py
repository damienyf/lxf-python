#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Basic
# ##################

# 在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字

# 可以匹配'007'，但无法匹配'00A'；
'00\d'

# 可以匹配'010'；
'\d\d\d'

# 可以匹配'py3'；
'\w\w\d'

# 可以匹配'pyc'、'pyo'、'py!'等等
'py.'

# 要匹配变长的字符，在正则表达式中，
# 用*表示任意个字符（包括0个），
# 用+表示至少一个字符，
# 用?表示0个或1个字符，
# 用{n}表示n个字符，
# 用{n,m}表示n-m个字符：

'\d{3}\s+\d{3,8}'


# \d{3}表示匹配3个数字，例如'010'；
# \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
# \d{3,8}表示3-8个数字，例如'1234567'。


# Advanced
# 要做更精确地匹配，可以用[]表示范围，比如：

'[0-9a-zA-Z\_]' # 可以匹配一个数字、字母或者下划线；

'[0-9a-zA-Z\_]+' # 可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

'[a-zA-Z\_][0-9a-zA-Z\_]*' # 可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

# not working..
'[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}' # 更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

'A|B' # 可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。

'^' # 表示行的开头，
'^\d' # 表示必须以数字开头。

'$' # 表示行的结束，
'\d$' # 表示必须以数字结束。

# 你可能注意到了，'py'也可以匹配'python'，但是加上'^py$'就变成了整行匹配，就只能匹配'py'了。

# re module

# 由于Python的字符串本身也用\转义，所以要特别注意：

s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'

# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
s = r'ABC\-001' # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'

import re
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

# 正常的切分代码
'a b   c'.split(' ')
# ['a', 'b', '', '', 'c']

# regular exp can split string more robust
re.split(r'\s+', 'a b   c')
# ['a', 'b', 'c']

re.split(r'[\s\,\;]+', 'a,b;; c  d')
# ['a', 'b', 'c', 'd']

# ^ means "beginning" if it comes at the start of the regex. 
# As the first character inside [], ^ has a different meaning: it means "not".

# 分组 提取子串
# 用()表示的就是要提取的分组（Group）
'^(\d{3})-(\d{3,8})$' # 分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
m.group(0)
# '010-12345'
m.group(1)
# '010'
m.group(2)
# '12345'

t = '19:05:30'
# first group match 0+0~9, 1+0~9, 2+0~3, 0~9
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|\
                4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
m.groups()

# 贪婪匹配
# 由于\d+采用贪婪匹配，匹配尽可能多的字符
# 直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
re.match(r'^(\d+)(0*)$', '102300').groups()

# 加个?就可以让\d+采用非贪婪匹配
re.match(r'^(\d+?)(0*)$', '102300').groups()


# 编译

# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 1. 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 2. 用编译后的正则表达式去匹配字符串。

# 预编译该正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

# 使用：
re_telephone.match('010-12345').groups()
# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。


# 第一题：
def is_valid_email(addr):
    if re.match(r'[a-zA-Z_.]*@([\w-]+\.)+[\w-]{2,4}', addr):
        return True
    else:
        return False

is_valid_email('ds@gmail.com')

# 第二题：
# \w matches any alphanumeric character and underscores, equivalent to the set [a-zA-Z0-9_]
# So [\w\.-] will appropriately match numbers as well as characters.
def name_of_email(addr):
    r = re.compile(r'^(<?)([\w\s]*)(>?)([\w\s]*)@([\w.]*)$')
    if not r.match(addr):
        return None
    else:
        m = r.match(addr)
        return m.group(2)

test = re.compile(r'[\w-]{2,4}')
# '-' matches the '-' character literally
test.match('d0000')
# <_sre.SRE_Match object; span=(0, 4), match='d000'>