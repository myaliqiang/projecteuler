#!/usr/bin/env python
#9!=362880
#7*9! < 9999999, so if the number is bigger than 9999999, \
#then we couldn't get the sum of factorials equals to the num\
#itself, in fact you could still find some ways to get rid of some numbers

import math
fac = []
for i in xrange(0,10):
    fac.append(math.factorial(i))

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

print items

print sum(items)