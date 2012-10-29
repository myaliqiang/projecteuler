#!/usr/bin/env python
import math

def is_prime(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

num = 600851475143 
max_prime = 0

for i in xrange(3, int(math.sqrt(num))):
    if is_prime(num, i):
        max_prime = i
        num = num / i
        
print max_prime