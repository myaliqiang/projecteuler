#!/usr/bin/env python
num_dict = {1:'one',2:'two',3:'three',4:'four',5:'five', \
            6:'six',7:'seven',8:'eight',9:'nine',10:'ten', \
            11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen', \
            16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty', \
            40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'onehundred',1000:'onethousand'}
def generate(i):
    total_len = 0
    if i <=20 and i >=1:
        total_len = len(num_dict[i])
        s = num_dict[i]
    elif i > 20 and i < 100:
        i1 = int(i / 10) * 10
        i2 = i % 10
        if i2 > 0:
            total_len += len(num_dict[i1]) + len(num_dict[i2])
            s = num_dict[i1] + num_dict[i2]
        else:
            total_len += len(num_dict[i1])
            s = num_dict[i1]
    elif i >= 100 and i < 1000 and i % 100 == 0 :
        i1 = i / 100
        total_len = len(num_dict[i1]) + len('hundred')
        s = num_dict[i1] + 'hundred'
    elif (i >= 101 and i < 120) or (i >= 201 and i < 220) or \
         (i >= 301 and i < 320) or (i >= 401 and i < 420) or \
         (i >= 501 and i < 520) or (i >= 601 and i < 620) or \
         (i >= 701 and i < 720) or (i >= 801 and i < 820) or \
         (i >= 901 and i < 920):

        i1 = i / 100
        i2 = i % 100
        total_len += len(num_dict[i1]) + len('hundredand')
        s = num_dict[i1] + 'hundredand'
        total_len += len(num_dict[i2])
        s += num_dict[i2]
    elif i > 100 and i < 1000:
        i1 = i / 100
        i2 = i / 10 % 10 * 10
        i3 = i % 10
        total_len += len(num_dict[i1]) + len('hundredand')
        s = num_dict[i1] + 'hundredand'
        if i2 > 0:
            total_len += len(num_dict[i2])
            s += num_dict[i2]
        if i3 > 0:
            total_len += len(num_dict[i3])
            s += num_dict[i3]
            
    elif i == 1000:
        total_len += len(num_dict[1000])
        s = num_dict[1000]

    # print i, s, total_len
    return total_len

count = 0
for i in xrange(1, 1001):
    # print i, total_len
    count += generate(i)

print count