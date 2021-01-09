'''
The program takes nine lines of nine integers to construct the puzzle needing
to be solved. Uses 0's to represent unknown values. 
'''

import numpy as np

def input_grid():
  """ 
  Saves a user entered sodoku grid of 9x9 integers, 
  one line at a time, and returns a soduku grid 
  """
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
  """ 
  Returns if a given value and grid position is a legal entry 
  """
  global grid
  for i in range(0,9):
    if grid[x][i] == n:
      return False
  for i in range(0,9):
    if grid[i][y] == n:
      return False
  x0 = (x//3)*3
  y0 = (y//3)*3
  for i in range (0,3):
    for j in range(0,3):
      if grid[x0+j][y0+i] == n:
        return False
  return True

def solve():
  """ 
  Recursively iterates over soduko grid until a completely legal completed board is achieved. 
  """
  global grid
  for x in range (9): 
    for y in range(9):
      if grid[x][y] == 0:
        for n in range(1,10):
          if possible(x,y,n):
            grid[x][y] = n 
            solve()
            grid[x][y] = 0
        return 
  print(np.matrix(grid))
  input('Additional Solutions?')

solve()
