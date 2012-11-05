#!/usr/bin/env python
rows = 15
cols = 15
start_row = 0
start_col = 0
count = 0

def trace(row, col):
    if row == rows and col == cols:
        global count
        count += 1
        return 
    if col < cols:
        # print row, col
        trace(row, col + 1)

    if row < rows:
        # print row, col
        trace(row + 1, col)

trace(start_row, start_col)
print count