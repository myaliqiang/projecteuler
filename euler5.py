#!/usr/bin/env python
def even_divisble(num):
    for i in reversed(xrange(2, 21)):
        if num % i != 0:
            return False

    return True

start = 2520
while True:
    if even_divisble(start):
        print start
        break
    else:
        start += 1
