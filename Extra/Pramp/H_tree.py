# O(4^depth)
# O(depth)
def drawHTree(x, y, length, depth):
  if depth == 0:
    return
  
  x0 = x - length / 2.0
  x1 = x + length / 2.0
  y0 = y - length / 2.0
  y1 = y + length / 2.0
  
  # Draw 3 line segments of the H-tree
  drawLine(x0, y0, x0, y1)    # left segment
  drawLine(x1, y0, x1, y1)    # right segment
  drawLine(x0,  y, x1,  y)    # connecting segment
  
  # The length decreases at each depth
  new_length = length / (2 ** (1/2))
  
  # Decrement depth by 1 and draw an H-tree
  # at each of the tips of the current H
  drawHTree(x0, y0, new_length, depth - 1)     # lower left  H-tree
  drawHTree(x0, y1, new_length, depth - 1)     # upper left  H-tree
  drawHTree(x1, y0, new_length, depth - 1)     # lower right H-tree
  drawHTree(x1, y1, new_length, depth - 1)     # upper right H-tree  
  
def drawLine(x1, y1, x2, y2):
  print([x1, y1], [x2, y2])


