#!/usr/bin/env python
#the problem is nearly same to euler34
import math
fac = []
for i in xrange(0,10):
    fac.append(i**5)

def fac_sum(num):
    global fac
    try:
        nums = sum([ fac[int(i)] for i in str(num)])
    except:
        print i
        return 0
    return nums

items = []
for i in xrange(10, fac[9] * 7):
    if i == fac_sum(i):
        items.append(i)

# print items

print sum(items)