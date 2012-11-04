#!/usr/bin/env python
max = 0
for a in xrange(2,100):
    for b in xrange(2,100):
        num = str(a**b)
        sum = 0
        for i in num:
            sum += int(i)

        if sum > max:
            max = sum

print max

