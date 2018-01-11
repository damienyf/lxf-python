#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pickling

import pickle

d = dict(name='Bob', age=20, score=88)

# dumps method return bytes file
pickle.dumps(d)

# dump() method write object to bytes file directly
# using with, no need to close()
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)

d

# pickle is not compatible across python versions
# check the compression parameter

# json is better to support web
# JSON
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)

# open as 'w' not 'wb'
with open('dump.txt', 'w') as f:
    json.dump(d, f)

# loads and load
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)


# class序列化为JSON的{}
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        self.__test__ = score
        self.__test = score # this one will be renamed
        self._test = score
s = Student('Bob', 20, 88)

# return parameters to dict first
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

# default takes the function from class to dict
print(json.dumps(s, default=student2dict))

# 把任意class的实例变为dict:
# 因为通常class的实例都有一个__dict__属性，它就是一个dict
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 把dict转换为Student实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

# object_hook to convert dict to class
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))