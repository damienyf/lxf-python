#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# 如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。
# 但实际上，把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，根据不通口令计算出不同的哈希。
# 要验证哈希值，必须同时提供正确的口令。
# 这实际上就是Hmac算法：Keyed-Hashing for Message Authentication。
# 它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。


# Python自带的hmac模块实现了标准的Hmac算法。
# 我们来看看如何使用hmac实现带key的哈希。

import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
h.hexdigest()