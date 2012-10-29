#!/usr/bin/env python
# 其实就是求这些数字的最小公倍数
import math

def gcd(num1, num2):
    if num1 < num2:
        t = num1
        num1 = num2
        num2 = t

    remainder = num1 % num2
    if remainder == 0:
        return num2
    else:
        num1 = num2
        num2 = remainder
        return gcd(num1, num2)

def lcm(num1, num2):
    return num1 * num2 / gcd(num1, num2)

i = 1
for j in xrange(2, 21):
    num = lcm(i,j)
    i = num

print i

    