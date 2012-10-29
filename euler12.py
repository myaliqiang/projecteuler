import math

def number():
    i = 1
    num = 1
    while True:
        yield num
        i += 1
        num += i

def get_count(i):
    count = 0
    for num in xrange(1, int(math.sqrt(i)) + 1):
        if i % num == 0:
            count += 2
    return count

for i in number():
    count = get_count(i)
    if count > 500:
        print i
        break
