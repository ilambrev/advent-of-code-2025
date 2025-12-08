from math import sqrt, pow, prod

def calculate_distance(p, q):
    return sqrt(pow(p[0] - q[0], 2) + pow(p[1] - q[1], 2) + pow(p[2] - q[2], 2))

file_path = "day_08_sample_data.txt"

file = open(file_path, "r")
junction_boxes = [[int(col) for col in row.split(",")] for row in file.read().split("\n")]
file.close()

distances = []

for i in range(len(junction_boxes) - 1):
    for j in range(i + 1, len(junction_boxes)):
        distance = calculate_distance(junction_boxes[i], junction_boxes[j])
        distances.append([distance, str(junction_boxes[i]), str(junction_boxes[j])])

distances.sort()

circuits = []

for i in range(len(distances)):
    distance = distances[i]
    connected_circuits = []

    is_not_in_circuit = True

    for j in range(len(circuits)):
        is_first_box_in_circuit = distance[1] in circuits[j]
        is_second_box_in_circuit = distance[2] in circuits[j]

        if is_first_box_in_circuit and is_second_box_in_circuit:
            is_not_in_circuit = False
            break

        if is_first_box_in_circuit:
            circuits[j].add(distance[2])
            connected_circuits.append(j)
            is_not_in_circuit = False

        if is_second_box_in_circuit:
            circuits[j].add(distance[1])
            connected_circuits.append(j)
            is_not_in_circuit = False

    if is_not_in_circuit:
        circuits.append({distance[1], distance[2]})

    if len(connected_circuits) > 1:
        if connected_circuits[0] < connected_circuits[1]:
            circuits[connected_circuits[0]].update(circuits[connected_circuits[1]])
            del circuits[connected_circuits[1]]
        else:
            circuits[connected_circuits[1]].update(circuits[connected_circuits[0]])
            del circuits[connected_circuits[0]]
    
    if len(circuits) == 1 and len(circuits[0]) == len(junction_boxes):
        first_box_x = int(distance[1].replace("[", "").split(", ")[0])
        second_box_x = int(distance[2].replace("[", "").split(", ")[0])

        print(first_box_x * second_box_x)
        
        break