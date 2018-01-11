#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# customize class
# 定制类 such as __slots___ attribute, __len__() method

# __str__

class Student(object):
    def __init__(self, name):
        self.name = name 
    # print method will call __str__() method
    def __str__(self):
        return "Student object (name: %s)" % self.name

    # __repr__() is used for calling oject directly
    __repr__ = __str__

print(Student('Michael'))
Student('Michael')

# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，
# 就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    
    # __iter___() method makes sure object is 'iterable'
    def __iter__(self):
        return self

    # __next__ method is called in the for loop
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

# __getitem__() enables the object to support index
# Fib()[5]

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    
    # __iter___() method makes sure object is 'iterable'
    def __iter__(self):
        return self

    # __next__ method is called in the for loop
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

#   __getitem__() enables the index
    def __getitem__(self, n):
        a, b = 1, 1

        for x in range(n):
            a, b = b, a + b
        return a

    # with slicing
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
f[0:4]
f[4:10]

# obviously our getitem function hasn't dealt with step parameter and negative indices
# 所以，要正确实现一个__getitem__()还是有很多工作要做的。
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，用于删除某个元素。
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
# 这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。


# __getattr__ to get value for NON-existent attributes
class Student(object):

    def __init__(self):
        self.name = 'Michael'
        
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        # getattr can return a lambda function(no parameter)
        if attr == 'age':
            return lambda: 25
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')
# 来尝试获得属性，这样，我们就有机会返回score的值：
s = Student()

# return a number or return a function:
s.score
s.age()

# default return is None w/ __getattr__ 
s.abc

# Now, adding limitation with raising an error:
class Student(object):
        
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        # getattr can return a lambda function(no parameter)
        if attr == 'age':
            return lambda: 25
        # if we don't want getattr to return None:
        raise AttributeError('Message from getattr: \'Student\' object has no attribute \'%s\'' % attr)

# 用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):

    def __init__(self, path = ''):
        self._path = path
    
    def __getattr__(self, path):
        print(self._path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

c = Chain().status.user.txt.subpath1.subpath2
# __getattr__ method is called three times 
# it's similar to call:
# Chain()
# Chain('/status')
# Chain('/status/user')
# and then return Chain('/status/user/txt') 
c._path

# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
# 还有些REST API会把参数放到URL中，比如GitHub的API：

class Chain(object):

    def log(func):
        def wrapper(*args, **kw):
            print('Called %s' % func.__name__, end='\n')
            return func(*args, **kw)
        return wrapper

    def __init__(self, path=''):
        self._path = path

    # Can EITHER use a condtion and lambda function inside the __getattr__
    # def __getattr__(self, path):
    #     if path == 'users':
    #         return lambda attr : Chain('%s/%s/%s' % (self._path, path, attr))
    #     else:
    #         return Chain('%s/%s' % (self._path, path))

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    # OR add a users method since users is always followed by username
    @log
    def users(self, name):
        return Chain('%s/%s/%s' % (self._path, 'users', name))

    # repr copies the str function
    __repr__ = __str__

Chain().users('damienyf').repos

# __call__
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Damien')
s()

# 那么，怎么判断一个变量是对象还是函数呢？
# 其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# True
callable(Student())
# False
callable(None)
# True
callable(max)
# False
callable([1, 2, 3])
# False
callable(['str'])
