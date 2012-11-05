#!/usr/bin/env python
def get_divisors(num):
    divisors = []
    for i in xrange(1, num / 2 + 2):
        if num % i == 0:
            divisors.append(i)

    return divisors

divisors = get_divisors(220)
d1 = sum(divisors)
d2_vidisors = get_divisors(d1)
d2 = sum(d2_vidisors)

count = 0
numbers = []
for i in xrange(1, 10000):
    divisors = get_divisors(i)
    d1 = sum(divisors)
    d2_vidisors = get_divisors(d1)
    d2 = sum(d2_vidisors)
    if d2 == i and d2 != d1:
        numbers.append(d1)
        numbers.append(d2)

numbers = set(numbers) #去除重复的数字(delete those redundant numbers)
for item in numbers:
    count += item

print count