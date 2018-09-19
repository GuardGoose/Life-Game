import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]])
plt.imshow(x, interpolation='nearest')
plt.show()

np.random.choice([0, 255], 4*4, p=[0.1, 0.9]).reshape(4, 4)

def add_glider(i, j, grid):
    """adds glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 255],  # Defines glider
                       [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider  # numpy slice operation copies the pattern
                                 # to two-dimensional array

grid = np.zeros(N*N).reshape(N, N)
add_glider(1, 1, grid)

# Boundary Conditions

if j == N-1:
    right = grid[i][0]
else:
    right = grid[i][j+1]

# Apply Conway's rules

if grid[i, j] == ON:
    if (total <2 ) or (total > 3):
        newGrid[i, j] = OFF
    else:
        if total == 3:
            newGrid[i, j] = ON