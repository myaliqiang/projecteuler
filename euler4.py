#!/usr/bin/env python
def is_palindromic(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False

max_value = 0
for i in xrange(100, 999):
    for j in xrange(100, 999):
        value = i * j
        if is_palindromic(value):
            if value > max_value:
                max_value = value

print max_value