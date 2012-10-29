#from bottom to top algorithm
with open('triangle.txt', 'r') as f:
    nums = f.readlines()
new_nums = []
rows = 0
cols = 0
for n in nums:
    if n:
        rows += 1
        new_n = [int(i) for i in n.split(' ')]
        cols = len(new_n)
        new_nums.append(new_n)

for i in reversed(xrange(0,rows - 1)):
    for j in xrange(0, len(new_nums[i])):
        if new_nums[i+1][j] > new_nums[i+1][j+1]:
            new_nums[i][j] += new_nums[i+1][j]
        else:
            new_nums[i][j] += new_nums[i+1][j+1]

print new_nums[0][0]