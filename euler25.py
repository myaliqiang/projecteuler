i = 1 
j = 1
term = 2
while True:
    k = i + j
    term += 1
    str_k = str(k)
    if len(str_k) == 1000:
        print term
        break
    i = j 
    j = k

