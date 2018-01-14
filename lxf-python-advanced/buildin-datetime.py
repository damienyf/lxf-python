#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# datatime

from datetime import datetime
now = datetime.now()
# datetime.now()返回当前日期和时间，其类型是datetime。
print(type(now), now)

# 要指定某个日期和时间，我们直接用参数构造一个datetime
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
# 2015-04-19 12:20:00

# datetime转换为timestamp
# 我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），
# 当前时间就是相对于epoch time的秒数，称为timestamp。
# 你可以认为：
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间是：
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
# 任意时刻的timestamp都是完全相同的

from datetime import datetime
# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
t = 1429417200.0
print(datetime.fromtimestamp(t))
# timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的

print(datetime.utcfromtimestamp(t)) # UTC时间


# str转换为datetime
from datetime import datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# 注意转换后的datetime是没有时区信息的。

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))


# datetime加减
from datetime import datetime, timedelta
now = datetime.now()
now + timedelta(hours=10)
# datetime.datetime(2018, 1, 14, 8, 10, 10, 197190)
now - timedelta(days=1)
# datetime.datetime(2018, 1, 12, 22, 10, 10, 197190)
now + timedelta(days=2, hours=12)
# datetime.datetime(2018, 1, 16, 10, 10, 10, 197190)


# 本地时间转换为UTC时间
# 一个datetime类型有一个时区属性tzinfo，但是默认为None
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。

# utcnow()拿到当前的UTC时间
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)

# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))

# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))

print(utc_dt, bj_dt, tokyo_dt, tokyo_dt2)

# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

