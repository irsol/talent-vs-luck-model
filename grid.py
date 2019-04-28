from pprint import pprint
import random

# Create 2D array.
grid = []
width = 5
height = 5
talents = {}
capital = {}


def create_grid(width, height):
    for row in range(height):
        grid.append([])  # To store cells in the row
        for column in range(width):
            # 0 - empty cell, 1 - individual, 2 - lucky_event, 3 - unlucky_event
            grid[row].append(random.choice([0, 1, 2, 3]))
            if grid[row][column] == 1:
                capital[(row, column)] = 10
                talents[(row, column)] = random.random()


def make_move(l_event, u_event, steps, ypos, xpos):
    # 4 - up, 5 - down, 6 - left, 7 -right
    direction = random.choice([4, 5, 6, 7])

    for step in steps:
        if direction == 4:
            ypos = ypos + 1
        elif direction == 5:
            ypos = ypos - 1
        elif direction == 6:
            xpos = xpos - 1
        elif direction == 7:
            xpos = xpos + 1
        return xpos, ypos


pprint(grid)
pprint(talents)
pprint(capital)

