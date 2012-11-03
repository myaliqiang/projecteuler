import math
def is_prime(num):
    for i in xrange(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True

def get_primes(num):
    arr = []
    arr_dict = {}
    
    for i in xrange(2, num):
        arr_dict[i] = 0
        if is_prime(i):
            arr.append(i)
            arr_dict[i] = 1
    return arr, arr_dict

def all_kinds(num):
    num = str(num)
    length = len(num)
    all = [int(num)]
    for i in xrange(0, length - 1):
        num = num[1:] + num[0]
        all.append(int(num))

    return all

primes, primes_dict = get_primes(1000000)
count = 0 
for item in primes:
    all_kinds_of_item = all_kinds(item)
    flag = True
    for i in all_kinds_of_item:
        if primes_dict[i] == 1: #ok, founded
            pass
        else:
            flag = False
            break
    if flag:
        count += 1
print count 