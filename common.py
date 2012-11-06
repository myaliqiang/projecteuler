import math 
def Cnr(n, r):
    n_factorial = math.factorial(n)
    r_factorial = math.factorial(r)
    n_minus_r_factorial = math.factorial(n-r)
    return n_factorial/r_factorial / n_minus_r_factorial

def get_divisors(n, exclude_n = False):
    divisors = []
    for i in xrange(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n/i)
    if exclude_n:
        divisors.remove(n)
    return list(set(divisors))

def get_divisors_pair(n):
    divisors = []
    for i in xrange(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append((i, n/i))
    return divisors

def get_divisors_pair_generator(n):
    for i in xrange(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield (i, n/i)

    


def get_primes(n):
    primes = []
    for i in xrange(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            primes.append(n)

    return primes

def get_divisors_count(n):
    i = 2
    count = {}
    num = n
    divisors = {}
    while n != 1 and i < num:
        if n % i == 0:
            if i in count: 
                count[i] += 1
            else: 
                count[i] = 1

            n /= i
        else:
            i += 1
    total = 1
    for k in count.keys():
        total *= count[k] + 1

    return total


if __name__ == '__main__':
    
    for i in xrange(12, 50000):
        result1 = get_divisors(i)
        

    # print get_divisors_pair(34)