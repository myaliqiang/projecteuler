#!/usr/bin/env python
#encoding=utf-8
#a，b的10分位的数字等于b的个位的数字
#a，b的取值范围在10，99之间
#a，b有公约数
#a，b里面去掉一个digit以后剩下的数字c,b组合起来的分数和a，b一样
#将找到的4个分数想乘，对于结果找到分子，分母的最大公约数，将分母除以最大公约数得到结果
from fractions import * 

def is_curious(a, b):
    f = Fraction(a,b)
    if f >= 1:
        return False

    a_digit = [int(i) for i in str(a)]
    b_digit = [int (i) for i in str(b)]

    if a_digit[1] == b_digit[0]:
        if b_digit[1] == 0:
            return False

        f2 = Fraction(a_digit[0], b_digit[1])
        try:
            if f == f2:
                return True
        except:
            return False

    return False

curious = []
a = 1
b = 1
for i in xrange(10, 99):
    for j in xrange(i+1, 100):
        if is_curious(i,j):
            curious.append((i,j))
            a *= i 
            b *= j


gcd = gcd(a,b)
print b/gcd