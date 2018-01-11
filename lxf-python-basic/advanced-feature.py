# list slicing
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[0:3]
# 0 can be ignored
L[:3]

# L['Bob', 'Jack']
L[-2:]

# Check iterable or not

from collections import Iterable
# True
isinstance('abc', Iterable)
# True
isinstance([1, 2, 3], Iterable)
# False
isinstance(123, Iterable)


# index loop
for index, value in enumerate(L):
    print(index, value)

for x, y in zip(X, Y):
    pass

# list comprehensions
list(range(1, 11))

[x * x for x in range(1, 11)]
# with codition
[x * x for x in range(1, 11) if x % 2 == 0]

# nested loop
[m + n for m in 'ABC' for n in 'XYZ']

# show all file and folders in current path
import os
[d for d in os.listdir('.')]

# multiple variables for same for loop
d = {'x': 'A', 'y': 'B', 'z': 'C'}
[k + '=' + v for k, v in d.items()]

L = ['Hello', 'World', 18, 'Apple', None]

# use if only in list comprehension
L2 = [s.lower() for s in L if isinstance(s, str)]
print(L2)
# use if - else statement in the list comprehension!!! syntax change
L2 = [s.lower() if isinstance(s, str) else s for s in L]


#  GENERATOR
L = [x * x for x in range(10)]
L
g = (x * x for x in range(10))
g

for n in g:
    print(n)

# using next on generator
next(g)

# using generator for complex list

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'
f = fib(6)

# you CAN'T get the return value from a generator
for n in fib(6):
    print(n)

# instead, you should catch the StopIteration exception;
# the return value is in the StopIteration values

g = fib(6)
while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as e:
        print('Generator returns value:', e.value)
        break

# iterable vs. iterator


from collections import Iterable
isinstance([], Iterable)
# True
isinstance({}, Iterable)
# True
isinstance('abc', Iterable)
# True
isinstance((x for x in range(10)), Iterable)
# True
isinstance(100, Iterable)
# False


from collections import Iterator
isinstance([], Iterator)
# False
isinstance({}, Iterator)
# False
isinstance('abc', Iterator)
# False
isinstance((x for x in range(10)), Iterator)
# True

isinstance(iter([]), Iterator)


# for loop is equivalent to next()

for x in [1,2,3,4]:
    pass

it = iter([1,2,3,4])

while True:
    try:
        x = next(it)
    except StopIteration:
        break

# iterator takes only iterables
# you can build an iterator with two method iter: return itself/ next: return next value until
# raising StopIteration exception


