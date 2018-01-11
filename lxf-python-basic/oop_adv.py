#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# add a method to an instance
class Student(object):
    pass

s = Student()

def set_age(self, age):
    self.age = age

# MethodType
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age


# 动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
# 为了给所有实例都绑定方法，可以给class绑定方法：

s2 = Student()
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s2.set_score

# 使用__slots__ 限制实例的属性
class Student(object):
    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age') 

s = Student()
s.name = 'Yunfei'
s.score = 99

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。


# @property
# @property装饰器就是负责把一个方法变成属性调用
# get & set methods are not easy to use..
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
s.score
s.score = 999

# @property doesn't limit the attributes
s.age = 10


class Student(object):

    # adding slots to limit the attributes
    __slots__ = ('name', '_birth') 

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
    # there's no age.setter so age is readonly


s1 = Student()
s1.birth = 1992

# @property广泛应用在类的定义中，可以让调用者写出简短的代码，
# 同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。



# MixIn 多重继承
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
class Animal(object):
    pass
# 大类:
class Mammal(Animal):
    pass
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class CarnivorousMixIn(object):
    def eat(self):
        print('Eating meat...')
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass


# 多进程模式的TCP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

# 多线程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass

# 协程模型
class MyTCPServer(TCPServer, CoroutineMixIn):
    pass

    
#生父
class Father():

    def func(self):
        print('生父打儿子')

#隔壁老王
class LaoWang():

    def func(self):
        print('老王打儿子')
    def func1(self):
        print('跟你妈说明天下午我会来')
#继父
class StepFather():

    def func(self):
        print('继父打儿子')
    def func1(self):
        print('我还会打你妈')

#神秘人
class Mysterious(Father,LaoWang,StepFather):
    pass

##让我们看看到底谁打了儿子
s=Mysterious()
s.func()
s.func1()