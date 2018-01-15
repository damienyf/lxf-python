#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
r = requests.get('https://www.douban.com/') # douban front page
r.status_code
r.text


r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
r.url # 实际请求的URL
# 'https://www.douban.com/search?q=python&cat=1001'

# requests自动检测编码，可以使用encoding属性查看：
r.encoding

# content属性获得bytes对象：
r.content

# 对于特定类型的响应，例如JSON，可以直接获取：
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
r.json()r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
r.json()

# 需要传入HTTP Header时，我们传入一个dict作为headers参数：
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
r.headers

# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r = requests.post(url, json=params) # 内部自动序列化为JSON

# 注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)

# requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
r.cookies['ts']

# 要在请求中传入Cookie，只需准备一个dict传入cookies参数：
cs = {'token': '12345', 'status': 'working')
r = requests.get(url, cookies=cs)

# 最后，要指定超时，传入以秒为单位的timeout参数：
r = requests.get(url, timeout=2.5) 