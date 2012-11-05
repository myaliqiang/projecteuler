import math 
def Cnr(n, r):
    n_factorial = math.factorial(n)
    r_factorial = math.factorial(r)
    n_minus_r_factorial = math.factorial(n-r)
    return n_factorial/r_factorial / n_minus_r_factorial
    
def get_divisors(n):
    divisors = []
    for i in xrange(1,(n+1)/2+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def get_divisors2(n):
    #the function has problem, don't use it until I find a solution
    i = 2
    arr1 = {}
    original_n = n
    divisors = {}
    while n != 1 and i < original_n:
        if n % i == 0:
            if i in arr1: 
                arr1[i] += 1
            else: 
                arr1[i] = 1

            n /= i
        else:
            i += 1

    arr2 = []
    # print arr1
    for num in arr1.keys():
        tmp_arr = []
        for i in xrange(1, arr1[num]+1):
            tmp_arr.append(num**i)
        arr2.append(tmp_arr)

    count = len(arr2)
    arr3 = {}
    print arr2

    for i in xrange(0, count-1):
        for j in xrange(i+1, count):
            for item1 in arr2[i]:
                for item2 in arr2[j]:
                    result = item1 * item2
                    arr3[result] = 1
                    arr3[item1] = 1
                    arr3[item2] = 1

    arr3 = arr3.keys()
    arr3 += [1]
    if count == 1:
        arr3 += arr2[0]
    if original_n in arr3:
         arr3.remove(original_n)
    
    return arr3
    


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
    # result = get_divisors(2342)
    # result.sort()
    # print result
    # result2 = get_divisors2(2342)
    # result2.sort()
    # print result2
    for i in xrange(12, 28123):
        result1 = get_divisors(i)
        result2 = get_divisors2(i)
        result1.sort()
        result2.sort()
        if result1 != result2:
            print i
            print result1
            print result2
            print 
            import sys
            sys.exit(1)