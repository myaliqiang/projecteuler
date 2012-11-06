#!/usr/bin/env python
from common import get_divisors_pair_generator

def is_pandigital(a, b, c):
    nums = []
    while a > 0:
        i = a % 10
        a = a / 10
        nums.append(i)

    while b > 0:
        i = b % 10
        b = b / 10
        nums.append(i)

    while c > 0:
        i = c % 10
        c = c / 10
        nums.append(i)

    if len(nums) != 9:
        return False
    nums = set(nums)
    if len(nums) == 9 and nums == set([1,2,3,4,5,6,7,8,9]):
        # print nums
        return True
    else:
        return False 

numbers = []
for i in xrange(1000, 10000):
    divisors = get_divisors_pair_generator(i)
    for divisor in divisors:
        # print divisor
        a, b = divisor
        if is_pandigital(a,b,i):
            numbers.append(i)
            break

# print numbers

print sum(numbers)