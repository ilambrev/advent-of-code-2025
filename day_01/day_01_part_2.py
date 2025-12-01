file_path = "day_01_sample_data.txt"

file = open(file_path, "r")
turns = file.read().split("\n")
file.close()

min_position = 0
max_position = 99
positions = 100
dial_position = 50
dial_points_zero = 0

for turn in turns:
    direction = turn[0]
    value = int(turn[1:]) % positions
    rotations = int(int(turn[1:]) / positions)
    is_zero_passed = False

    if direction == "L":
        if value > dial_position:
            is_zero_passed = not dial_position == 0
            dial_position = positions - (value - dial_position)
        else:
            dial_position -= value
    elif direction == "R":
        if dial_position + value > max_position:
            is_zero_passed = not dial_position == 0
            dial_position = value - (positions - dial_position)
        else:
            dial_position += value

    if dial_position == min_position or is_zero_passed:
        dial_points_zero += 1

    dial_points_zero += rotations

print(dial_points_zero)