#!/usr/bin/env python
from common import get_divisors, get_divisors2

def abundant_numbers():
    numbers = []
    for i in xrange(12,28123):
        divisors = get_divisors(i)

        sum_of_divisors = sum(divisors)
        if sum_of_divisors > i:
            numbers.append(i)

    return numbers

dict = {}
numbers = abundant_numbers()
numbers.sort()
for i in numbers:
    for j in numbers:
        k = i + j
        if k <= 28123:
            dict[k] = 1
        else:
            break

sum = 0
for i in xrange(1,28124):
    if not dict.has_key(i):
        sum += i

print sum
