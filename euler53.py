def Cn_r(n, r):
    a = 1
    b = 1
    for i in xrange(1, r+1):
        a *= n 
        n -= 1
        b *= i
    return a/b

count = 0
for n in xrange(1,101):
    for r in xrange(n-1, 0, -1):
        result = Cn_r(n, r)
        if result > 1000000:
            count += 1
       

print count
