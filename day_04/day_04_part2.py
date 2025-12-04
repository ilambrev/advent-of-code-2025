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

def find_accessible_rows(grid, paper_roll):
    coordinates = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == paper_roll and is_accessible(grid, i, j, paper_roll):
                coordinates.append([i, j])

    return coordinates

def remove_accessible_rolls(grid, coordinates, empty_space):
    for coordinate in coordinates:
        i = coordinate[0]
        j = coordinate[1]
        grid[i][j] = empty_space


file_path = "day_04_sample_data.txt"

file = open(file_path, "r")
grid = [[e for e in row] for row in file.read().split("\n")]
file.close()

empty_space = "."
paper_roll = "@"
accessable_rolls = 0

coordinates = find_accessible_rows(grid, paper_roll)

while len(coordinates) > 0:
    accessable_rolls += len(coordinates)
    remove_accessible_rolls(grid, coordinates, empty_space)
    coordinates = find_accessible_rows(grid, paper_roll)

print(accessable_rolls)