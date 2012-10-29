#!/usr/bin/env python

i = 1 
j = 2
sum = 2
while True:
    k = i + j
    i = j
    j = k
    if k > 4 * 10**6:
        break
    if k % 2 == 0:
        sum += k

print sum