#!/usr/bin/env python
#<1>->1/2 = n/dn
#<2>->1/2+2 = 1/2+4/2=5/5=>n/dn + dn*2/dn = dn / (n+dn*2)
def fraction(n, dn):
    return (dn, n + dn * 2)

def fraction_list():
    n = 1
    dn = 2
    yield (n, dn)
    for i in xrange(1,1000):
        n , dn = fraction(n, dn)
        yield (n, dn)

count = 0
for (n, dn) in fraction_list():
    a, b = (n + dn, dn) #1 + n/dn
    if len(str(a)) > len(str(b)):
        count += 1

print count
