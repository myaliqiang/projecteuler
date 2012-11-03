#!/usr/bin/env python
def same_digit(num):
    x2 = str(num * 2)
    x3 = str(num * 3 )
    x4 = str(num * 4)
    x5 = str(num * 5 )
    x6 = str(num * 6 )

    length = len(str(x2))
    if len(x3) == length and \
        len(x4) == length and \
        len(x5) == length and \
        len(x6) == length:
        pass
    else:
        return False

    x2 = sorted(x2)
    x3 = sorted(x3)
    if x2 != x3:
        return False
    x4 = sorted(x4)
    if x2 != x4:
        return False
    x5 = sorted(x5)
    if x2 != x5:
        return False
    x6 = sorted(x6)
    if x2 != x6:
        return False

    return True

min_length = 5
founded = False
for num_length in xrange(min_length, 20):
    if founded:
        break
    num = 10 ** (num_length - 1)
    max_num = int(str(num).replace('0','6')) + 1
    
    for i in xrange(num, max_num):
        if same_digit(i):
            print i
            founded = True
            break
