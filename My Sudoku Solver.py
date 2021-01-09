'''
The program takes nine lines of nine integers to construct the puzzle needing
to be solved. Uses 0's to represent unknown values. 
'''

import numpy as np
def input_grid():
  grid = []
  print("Enter each line without spaces, using 0 for unknown values")
  for i in range(1,10):
    print(f"Enter line {i}: ", end="")
    line = list(input())
    for number in range(0, len(line)):
      line[number] = int(line[number])
    grid.append(line)
  return grid

grid = input_grid()

def possible(y,x,n):
  global grid
  for i in range(0,9):
    if grid[y][i] == n:
      return False
  for i in range(0,9):
    if grid[i][x] == n:
      return False
  x0 = (x//3)*3
  y0 = (y//3)*3
  for i in range (0,3):
    for j in range(0,3):
      if grid[y0+i][x0+j] == n:
        return False
  return True

def solve():
  global grid
  for y in range (9): 
    for x in range(9):
      if grid[y][x] == 0:
        for n in range(1,10):
          if possible(y,x,n):
            grid[y][x] = n 
            solve()
            grid[y][x] = 0
        return 
  print(np.matrix(grid))
  input('Additional Solutions?')

solve()
