#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# multiple process & thread processing

# native fork() on mac & linux

# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
# 普通的函数调用，调用一次，返回一次，但是fork()调用一次，
# 返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

# 子进程永远返回0，而父进程返回子进程的ID。
# 这样做的理由是，一个父进程可以fork出很多子进程，
# 所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

# import os

# print('Process (%s) start ...' % os.getpid())

# pid = os.fork()

# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getpid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# multiprocessing

from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
# you will need to run it in command line mode...
if __name__ == '__main__':
    print('Parent process %s. ' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')


# Pool 
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
# 

# 子进程
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

# 下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，
# 这和命令行直接运行的效果是一样的：

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


# 如果子进程还需要输入，则可以通过communicate()方法输入

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)


# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：

# set q=mx
# python.org
# exit

# 进程间通信

# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。



# 多任务可以由多进程完成，也可以由一个进程内的多线程完成。
# 我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。

# 于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，
# Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，
# threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块。


# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import time, threading

def loop():
    # current_thread()函数，它永远返回当前线程的实例。
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1

        print('thread %s >>> %s' % (threading.current_thread().name, n))

        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

# 主线程实例的名字叫MainThread
print('thread %s is running...' % threading.current_thread().name)
# 子线程的名字在创建时指定，名字仅仅在打印时用来显示，完全没有其他意义
t = threading.Thread(target=loop, name='LoopThread')
# start()开始执行
t.start()
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
t.join()
print('thread %s ended.' % threading.current_thread().name)


# Lock
# 来看看多个线程同时操作一个变量怎么把内容给改乱了
import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：
# 初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8

t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2   # balance = -8

# 结果 balance = -8



# 要确保balance计算正确，就要给change_it()上一把锁
# 锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁
# 通过threading.Lock()来实现

balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
# 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将成为死线程。
# 所以我们用try...finally来确保锁一定会被释放。

# 包含锁的某段代码实际上只能以单线程模式执行
# 其次，由于可以存在多个锁，不同的线程持有不同的锁，
# 并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起



# 多核CPU
# 试试用Python写个死循环：

import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
# 启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。
# 但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？


# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
# 任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

# Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。