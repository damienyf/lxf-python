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