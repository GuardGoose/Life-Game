import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

def random_grid(n):
    """returns grid of n*n values"""
    return np.random.choice(vals, n*n, p=[0.2, 0.8]).reshape(n,n)

def add_glider(i, j, grid):
    """adds a glider with top-left cell at (i, j)"""
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(frameNum, img, grid, n):
    # copy grid since we require 8 neighbours for calculation
    # and we can go line by line
    newGrid = grid.copy()
    for i in range(n):
        for j in range(n):
            # compute 8-neighbour sum using toroidal boundary conditions
            # x and y wrap around so that the simulation
            # takes place on a torodial surface
            total = int((grid[i, (j-1) % n] + grid[i, (j+1) % n] +
                         grid[(i-1) % n, j] + grid[(i-1) % n, j] +
                         grid[(i-1) % n, (j-1) % n] + grid[(i-1) % n, (j+1) % n] +
                         grid[(i+1) % n, (j-1) % n] + grid[(i+1) % n, (j+1) % n]) / 255)
            # apply Conway's Rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life")
    # add arguments
    parser.add_argument('--grid-size', dest='n', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', dest='store_true', required=False)
    parser.add_argument('--gosper', dest='store_true', required=False)
    args = parser.parse_args()
    # set grid size
    n = 100
    if args.n and int(args.n) > 8:
        n = int(args.n)

    # setup animation interval update
    update_interval = 50
    if args.interval:
        update_interval = int(args.interval)

    