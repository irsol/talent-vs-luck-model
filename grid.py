import random

# Create 2D array.
grid = []
for row in range(10):
    grid.append([])  # To store cells in the row
    for column in range(10):
        grid[row].append(random.randint(0, 1))  # Append cell

print(grid)
