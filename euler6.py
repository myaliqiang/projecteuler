#!/usr/bin/env python
def get_sum(num):
    sum = 0
    for i in xrange(1, num+1):
        sum += i * i
    return sum

def get_square(num):
    sum = 0
    for i in xrange(1, num + 1):
        sum += i

    return sum * sum

print get_square(100) - get_sum(100)