import math
def is_prime(num):
    for i in xrange(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

count = 0
i = 1
while True:
    i += 1
    if is_prime(i):
        count += 1
        if count == 10001:
            print i
            break

