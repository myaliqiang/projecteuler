#from bottom to top algorithm

nums = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
nums = nums.split('\n')
new_nums = []
rows = 0
cols = 0
for n in nums:
    if n:
        rows += 1
        new_n = [int(i) for i in n.split(' ')]
        cols = len(new_n)
        new_nums.append(new_n)

for i in reversed(xrange(0,14)):
    for j in xrange(0, len(new_nums[i])):
        if new_nums[i+1][j] > new_nums[i+1][j+1]:
            new_nums[i][j] += new_nums[i+1][j]
        else:
            new_nums[i][j] += new_nums[i+1][j+1]

print new_nums[0][0]