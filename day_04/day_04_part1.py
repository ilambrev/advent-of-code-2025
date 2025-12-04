def is_accessible(grid, i, j, paper_roll):
    adjacent_rolls = 0

    if i - 1 >= 0 and grid[i - 1][j] == paper_roll:
        adjacent_rolls += 1

    if i - 1 >= 0 and j + 1 < len(grid[i - 1]) and grid[i - 1][j + 1] == paper_roll:
        adjacent_rolls += 1

    if j + 1 < len(grid[i]) and grid[i][j + 1] == paper_roll:
        adjacent_rolls += 1

    if i + 1 < len(grid) and j + 1 < len(grid[i + 1]) and grid[i + 1][j + 1] == paper_roll:
        adjacent_rolls += 1

    if i + 1 < len(grid) and grid[i + 1][j] == paper_roll:
        adjacent_rolls += 1

    if i + 1 < len(grid) and j - 1 >= 0 and grid[i + 1][j - 1] == paper_roll:
        adjacent_rolls += 1

    if j - 1 >= 0 and grid[i][j - 1] == paper_roll:
        adjacent_rolls += 1

    if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] == paper_roll:
        adjacent_rolls += 1

    return adjacent_rolls < 4

file_path = "day_04_sample_data.txt"

file = open(file_path, "r")
grid = file.read().split("\n")
file.close()

paper_roll = "@"
accessable_rolls = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == paper_roll and is_accessible(grid, i, j, paper_roll):
            accessable_rolls += 1

print(accessable_rolls)