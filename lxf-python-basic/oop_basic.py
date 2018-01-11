#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa', 99)

# 和静态语言不同，Python允许对实例变量绑定任何数据，
# 也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

bart = Student('Bart', 59)
bart.age = 8
bart.age

lisa.age

# access control through private variables

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(slef, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# 双下划线开头的实例变量是不是一定不能从外部访问呢？
# 其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量

# inheritance polymorphism:
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    
class Cat(Animal):
    
    def run(self):
        print('Cat is running...')

a = list()
b = Animal()
c = Dog()

# True
isinstance(a, list)
# True
isinstance(b, Animal)
# True
isinstance(c, Dog)
# True
isinstance(c, Animal)
# False
isinstance(b, Dog)


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

# polymorphism
run_twice(Tortoise())


class Timer(object):
    def run(self):
        print('Start...')
# duck type
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
# 一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
run_twice(Timer())

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
# 子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

# types for functions

import types
def fn():
    pass

type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType

# True
isinstance(b, Animal)
# True
isinstance(c, Animal)
# True
isinstance(c, Dog)

# dir() to get all methods and attributes 
dir('ABC')

len('ABC')
ABC.__len__()

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
len(dog)

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x 


obj = MyObject()
hasattr(obj, 'y')
setattr(obj, 'y', 19)
getattr(obj, 'y')
obj.y
# get default 
getattr(obj, 'z', 404)
# can also check method
hasattr(obj, 'power')
fn = getattr(obj, 'power')
# fn() is equavilent to obj.power()
fn()

# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
# 如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None


# 实例绑定属性
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 类属性!!!
# 千万不要对实例属性和类属性使用相同的名字
class Student(object):
    name = 'Student'


s = Student()
# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(s.name)
# 打印类的name属性
print(Student.name)
#  给实例绑定name属性
s.name = 'Damien'
print(s.name)
# Student
print(student.name)

del s.name
# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
print(s.name)