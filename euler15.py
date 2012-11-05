#!/usr/bin/env python
# the problem is try to find the Cn(r)
from common import Cnr
rows = 20
cols = 20

"""method one"""
#so the n = 20 * 2, the r = 20
#so our problem is find C40(20)
#Cn(r) equals to n!/r!(n-r)!

print Cnr(rows * 2, rows)


# """method two"""
# # # using dynamic programming to solve the problem 
# pre_list = {}

# count = 0
# pre_list = {}
# for i in xrange(0, rows + 1):
#     for j in xrange(0, rows + 1):
#         pre_list[(i,j)] = []

# for i in xrange(0, rows + 1):
#     for j in xrange(0, rows + 1):
#         if i > 0:
#             pre_list[(i,j)].append((i-1, j))
#         if j > 0:
#             pre_list[(i,j)].append((i, j-1))

# route = {(rows,cols):1}
# keys = route.keys()
# while True:
#     if not keys:
#         break

#     new_route = {}
#     for key in keys:
#         pre = pre_list[key]
#         if not pre:
#             continue
#         for item in pre:
#             new_route[item] = 1
#             if item in route:
#                 route[item] += route[key]
#             else:
#                 route[item] = route[key]
#         route[key] = 0
#     keys = new_route.keys()

# print route[(0,0)]
