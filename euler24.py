#!/usr/bin/env python
#reference:http://dongxicheng.org/structure/permutation-combination/

num = '0123456789'
count = 1
length = len(num)
while True:
    #find the first number which is less than it's right
    founded = False
    # print 'start num', num
    for i in reversed(xrange(0, length - 1)):
        if founded:
            break
        for j in xrange(i + 1, length):
            if num[i] < num[j]:
                # print num[i], num[j], i, j
                num1 = num[i]
                pos1 = i
                founded = True
                break

    if not founded:
        break

    founded = False
    # print 'pos1', pos1, 'num1', num1
    for i in reversed(xrange(pos1+1, length)):
        if num[i] > num1:
            pos2 = i 
            num2 = num[i]
            founded = True
            break
    # print num2

    num = list(num)
    tmp = num[pos1]
    num[pos1] = num[pos2]
    num[pos2] = tmp
    num = ''.join(num)
    #print num

    num3 = ''
    for i in reversed(xrange(pos1+1, length)):
        num3 += num[i]
    num = num[:pos1+1] + num3
    
    
    count += 1
    # print num
    # if count < 10:
    #     pass
    #     print num
    # else:
    #     import sys
    #     sys.exit(1)
    if count == 1000000:
        print num
        break


