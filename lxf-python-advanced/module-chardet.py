#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# chardet
# 检测编码，简单易用。
# chardet支持检测中文、日文、韩文等多种语言。
import chardet

chardet.detect(b'Hello, world!')
# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。


data = '离离原上草，一岁一枯荣'.encode('gbk')
chardet.detect(data)
# {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}

data = '离离原上草，一岁一枯荣'.encode('utf-8')
chardet.detect(data)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}


data = '最新の主要ニュース'.encode('euc-jp')
chardet.detect(data)
{'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}