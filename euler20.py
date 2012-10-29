
def n(num):
    sum = 1
    for i in xrange(1, num + 1):
        sum *= i
    return str(sum)

total = 0
for i in n(100):
    total += int(i)
print total