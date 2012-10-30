
def get_recurring_cycle(b):
    # a / b = c, remains d
    len_b = len(str(b))
    a = 1 
    distinct_arr = []
    while True:
        a = a * 10 ** len_b
        c = int(a / b)
        d = a % b
        if d == 0:
            return len(distinct_arr)
        else:
            if c in distinct_arr:
                return len(distinct_arr)
            else:
                a = d
                distinct_arr.append(c)

max_length = 0
max_val = 0
for i in xrange(1, 1000):
    count = get_recurring_cycle(i)
    if count > max_length:
        max_length = count
        max_val = i

print max_val