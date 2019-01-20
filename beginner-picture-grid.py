#Author : Muhammad Handry Wahyudi
#Date : 14-07-2016
#Filename : beginner-picture-grid.py

#!/usr/bin/python

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def picture(grid):
    n = 0
    while n < (len(grid[0])):
        for i in range(len(grid)):
            print grid[i][n],
        print ""
        n += 1

picture(grid)

    

