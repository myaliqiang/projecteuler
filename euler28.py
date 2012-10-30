def disgonals_value(num):
    base_value = []
    for i in xrange(3, num + 1, 2):
        base_value.append(i * i)

    base = 2
    sum = 0
    for i in base_value:
        sum += i - base
        sum += i #added the numbers in the base_value
        base += 2

    base = 6 
    for i in base_value:
        sum += i - base
        base += 6

    base = 4
    for i in base_value:
        sum += i - base
        base += 4

    return sum

print 1 + disgonals_value(1001)
#print 1 + disgonals_value(5)