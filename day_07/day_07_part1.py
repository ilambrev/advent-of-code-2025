def find_manifold_location(diagram, manifold):
    location = [-1, -1]

    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[i][j] == manifold:
                location[0] = i
                location[1] = j

                return location

    return location

def print_diagram(diagram):
    for row in diagram:
        print("".join(row))

file_path = "day_07_sample_data.txt"

file = open(file_path, "r")
diagram = [[col for col in row] for row in file.read().split("\n")]
file.close()

manifold = "S"
spliter = "^"
empty_space = "."
beam = "|"

manifold_location = find_manifold_location(diagram, manifold)
row = manifold_location[0]

split_counter = 0

for i in range(row + 1, len(diagram)):
    for j in range(len(diagram[i])):
        if diagram[i][j] == empty_space and (diagram[i - 1][j] == manifold or diagram[i - 1][j] == beam):
            diagram[i][j] = beam

        if diagram[i][j] == spliter and (diagram[i - 1][j] == manifold or diagram[i - 1][j] == beam):
            split_counter += 1

            if j > 0:
                diagram[i][j - 1] = beam

            if j < len(diagram[i]) - 1:
                diagram[i][j + 1] = beam

print_diagram(diagram)
print(split_counter)