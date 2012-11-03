from __future__ import division

import math

def is_square(num):
    if num == 0:
        return False
    temp = int(math.sqrt(num))
    
    if temp * temp == num :
        return temp
    else:
        return False

def get_D():
    
    arr = []
    for i in xrange(2, 1001):
        if not is_square(i):
            arr.append(i)
    return arr

max_x = 0
for d in get_D():
    y = 0
    while True:
        y += 1
        x = 1 + d * y * y 
        x = is_square(x)
        if x:
            print x, y, d
            if x > max_x: 
                max_x = x
            break    

print max_x