import random

w = 10
h = 10
N = 5

# Create 2D array.
grid = []
for row in range(10):
    grid.append([])  # To store cells in the row
    for column in range(10):
        grid[row].append(random.randint(0, 1))  # Append cell

print(grid)
