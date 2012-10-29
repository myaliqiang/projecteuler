from multiprocessing import Process, Lock, Queue

import math
def is_prime(num):
    for i in xrange(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


"""method 1, may die on Windows"""
q = Queue()

class Foo(Process):

    def __init__(self, begin, end):
        Process.__init__(self)
        self.begin = begin
        self.end = end


    def run(self):
        local_total = 0
        self.begin = self.begin - 1
        while self.begin <= self.end:
            self.begin += 1
            if self.begin % 2 == 0 or self.begin % 3 == 0:
                continue
            if is_prime(self.begin):
                local_total += self.begin
        q.put(local_total)

p1 = Foo(4, 1000000)
p2 = Foo(1000001, 1600000)
p3 = Foo(1600001, 2000000)

p1.start()
p2.start()
p3.start()
p1.join()
p2.join()
p3.join()

total = 5
for i in xrange(0,3):
    total += q.get()


"""method 2"""
# i = 1
# total = 2 + 3
# while True:
#     i += 1
#     if i >= 2000000:
#         break
#     if i % 2 == 0 or i % 3 == 0:
#         continue

#     if is_prime(i):
#         total += i

print total
