a_set = []
for i in xrange(2,101):
    for j in xrange(2,101):
        a_set.append(i**j)

print len(set(a_set))