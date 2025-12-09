file_path = "day_09_sample_data.txt"

file = open(file_path, "r")
red_tiles = [[int(col) for col in row.split(",")][::-1] for row in file.read().split("\n")]
file.close()

max_area = 0

for i in range(len(red_tiles) - 1):
    for j in range(i + 1, len(red_tiles)):
        a = abs(red_tiles[i][1] - red_tiles[j][1]) + 1
        b = abs(red_tiles[i][0] - red_tiles[j][0])
        
        area = a * (1 + b)

        if area > max_area:
            max_area = area

print(max_area)