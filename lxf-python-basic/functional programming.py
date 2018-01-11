# map and reduce


def f(x):
    return x * x


# map function takes two input: function, Iterable
# and return an Iterator
r = map(f, [1, 2, 3, 4, 5, 6])
list(r)

list(map(str, [1, 2, 3, 4, 5, 6, 7]))


# reduce
from functools import reduce


def add(x, y):
    return x + y


reduce(add, [1, 3, 5, 7, 9])
# reduce calculates the cumulative sum
# the function in the reduce needs to have two input

# write a function to convert str2int
from functools import reduce


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        # notice how dictionary is used here!
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

# use lambda function:
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x*10 + y, map(char2num, s)) 


# filter applies a function on the iterable and return a iterator (boolean values)
# for items funtion(item) is True
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1,2,3,4,5,6,7]))

# return a and b is equal to return (a and b); i.e. x = a and b; return x.
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', 'B', None, 'C', ' ']))


# Sieve of Eratosthenes
def _odd_iter():
    n = 1
    while True:
        n =  n + 2
        yield n

# use of lambda function to remove the multiples of the first number 
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()  # initialize the series
    while True:
        n = next(it)  # return and remove the first number in the series
        yield n
        it = filter(_not_divisible(n), it)  # then use filter to create new series


for n in primes():
    if n < 1000:
        print(n)
    else break


# check for palindrome:

def is_palindrome(n):
    s = str(n)
    return s[:] == s[::-1]

output = filter(is_palindrome, range(1, 1000))

# sort
# sorted function can take key function
# such as abs, str.lower 

sorted([36, 5, -12, 9, -21], key=abs)

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

# sort a list of tuple 

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]

sorted(L, key=by_name)


def by_score(t):
    return t[1]

sorted(L, key=by_score, reverse=True)
