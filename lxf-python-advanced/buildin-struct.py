#!/usr/bin/env python3
# -*- coding: utf-8 -*-

准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。
在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：

n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
bs
# b'\x00\x9c@c'


# struct的pack函数把任意数据类型变成bytes：
import struct
struct.pack('>I', 10240099)
# b'\x00\x9c@c'
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。


# unpack把bytes变成相应的数据类型：
struct.unpack('>I', b'\x00\x9c@c')

# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
# (4042322160, 32896)


s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。

# 所以，组合起来用unpack读取：
struct.unpack('<ccIIIIIIHH', s)