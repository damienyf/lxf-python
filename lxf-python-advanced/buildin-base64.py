#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# base64
# Base64是一种用64个字符来表示任意二进制数据的方法。

# Base64是一种最常见的二进制编码方法。首先，准备一个包含64个字符的数组：
# ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
# 然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit：
# 这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。

# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
# Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节
import base64
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

# 有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_

base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
# b'abcd++//'
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
# b'abcd--__'
base64.urlsafe_b64decode('abcd--__')
# b'i\xb7\x1d\xfb\xef\xff'


# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
# 因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。