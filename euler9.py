#a<b<c=>3a < 3b < 3c=>3a < a+b+c = 1000 => a < 333, 
#3c > a + b + c => c > 333


flag = False
for a in xrange(1,333):
    if flag:
        break
    if a + 1 > 333:
        larger = a+1
    else:
        larger = 333
    for b in xrange(larger,1001-a):
        if flag:
            break
        if b + 1 < 333:
            larger = 333
        else:
            larger = b + 1
        for c in xrange(b+1, 1001-a-b):
            if a + b + c == 1000 and a * a + b * b == c * c:
                #print a, b, c
                print a * b * c
                flag = True
                break
