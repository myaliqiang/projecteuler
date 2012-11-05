#!/usr/bin/env python
import datetime
count = 0
for i in xrange(1901, 2001):
    for k in xrange(1, 13):
        date_string = str(i) + str(k) + str(1)
        date = datetime.datetime.strptime(date_string, "%Y%m%d")
        weekday = date.strftime("%w")
        if weekday == '0':
            count += 1
print count
