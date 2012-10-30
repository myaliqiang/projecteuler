def get_sequence_count(n):
    count = 1
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return count

max_count = 0
num = 0
for i in xrange(1, 1000000):
    count = get_sequence_count(i)
    if max_count < count:
        num = i
        max_count = count

print max_count
print num