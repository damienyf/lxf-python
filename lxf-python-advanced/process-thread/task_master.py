#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 绑定端口5000, 设置验证码'abc':
# manager = QueueManager(address=('', 5000), authkey=b'abc')

# 启动Queue:
# manager.start()

# "在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。"

# 序列化不支持匿名函数
def get_task():
    return task_queue

def get_result():
    return result_queue

def start_server():
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)
    manager = QueueManager(address=('127.0.0.1', 34512), authkey=b'abc')

    manager.start() 
    # ###########################
    # 获得通过网络访问的Queue对象:#
    # ###########################
    # 请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
    # 但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，
    # 那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 1000)
        print('Put task %d ...' % n)
        # put() in the task to task quque
        task.put(n)

    # 从result队列读取结果:
    print('Now, try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    # 关闭: queue manager
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    start_server()