def lychrel_number(num):
    for i in xrange(1,50):
        num = reverse_and_add(num)
        if is_palindromic(num):
            return False

    return True

def reverse_and_add(num):
    reversed_num = int((str(num))[::-1])
    return reversed_num + num

def is_palindromic(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

count = 0
for i in xrange(1,10000):
    if lychrel_number(i):
        count += 1
print count

