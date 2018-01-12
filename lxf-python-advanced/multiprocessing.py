#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 分布式进程

# 在Thread和Process中，应当优选Process，因为Process更稳定，
# 而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
# 一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。
# 由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

# 举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，
# 希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？

# 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。

# 我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：




# 请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
# 但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，
# 那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。

# 然后，在另一台机器上启动任务进程（本机上启动也可以）：



# 任务进程要通过网络连接到服务进程，所以要指定服务进程的IP。

# 现在，可以试试分布式进程的工作效果了。先启动task_master.py服务进程：

# $ python3 task_master.py 
# Put task 3411...
# Put task 1605...
# Put task 1398...
# Put task 4729...
# Put task 5300...
# Put task 7471...
# Put task 68...
# Put task 4219...
# Put task 339...
# Put task 7866...
# Try get results...
# task_master.py进程发送完任务后，开始等待result队列的结果。现在启动task_worker.py进程：

# $ python3 task_worker.py
# Connect to server 127.0.0.1...
# run task 3411 * 3411...
# run task 1605 * 1605...
# run task 1398 * 1398...
# run task 4729 * 4729...
# run task 5300 * 5300...
# run task 7471 * 7471...
# run task 68 * 68...
# run task 4219 * 4219...
# run task 339 * 339...
# run task 7866 * 7866...
# worker exit.
# task_worker.py进程结束，在task_master.py进程中会继续打印出结果：

# Result: 3411 * 3411 = 11634921
# Result: 1605 * 1605 = 2576025
# Result: 1398 * 1398 = 1954404
# Result: 4729 * 4729 = 22363441
# Result: 5300 * 5300 = 28090000
# Result: 7471 * 7471 = 55815841
# Result: 68 * 68 = 4624
# Result: 4219 * 4219 = 17799961
# Result: 339 * 339 = 114921
# Result: 7866 * 7866 = 61873956
# 这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，
# 就可以把任务分布到几台甚至几十台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。

# Queue对象存储在哪？注意到task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中：

#                                              │
# ┌─────────────────────────────────────────┐     ┌──────────────────────────────────────┐
# │task_master.py                           │  │  │task_worker.py                        │
# │                                         │     │                                      │
# │  task = manager.get_task_queue()        │  │  │  task = manager.get_task_queue()     │
# │  result = manager.get_result_queue()    │     │  result = manager.get_result_queue() │
# │              │                          │  │  │              │                       │
# │              │                          │     │              │                       │
# │              ▼                          │  │  │              │                       │
# │  ┌─────────────────────────────────┐    │     │              │                       │
# │  │QueueManager                     │    │  │  │              │                       │
# │  │ ┌────────────┐ ┌──────────────┐ │    │     │              │                       │
# │  │ │ task_queue │ │ result_queue │ │<───┼──┼──┼──────────────┘                       │
# │  │ └────────────┘ └──────────────┘ │    │     │                                      │
# │  └─────────────────────────────────┘    │  │  │                                      │
# └─────────────────────────────────────────┘     └──────────────────────────────────────┘
#                                              │

#                                           Network
# 而Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。

# authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果task_worker.py的authkey和task_master.py的authkey不一致，肯定连接不上。


#############################################################################################################################
# 小结
# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。

# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。
# 比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。