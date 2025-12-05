file_path = "day_05_sample_data.txt"

file = open(file_path, "r")
input_data = file.read().split("\n")
file.close()

empty_line_index = input_data.index("")

id_ranges = sorted([[int(id) for id in r.split("-")]
                    for r in input_data[:empty_line_index]])

new_ranges = []
begin = id_ranges[0][0]
end = id_ranges[0][1]

for i in range(1, len(id_ranges)):
    if id_ranges[i][0] <= end and id_ranges[i][1] > end:
        end = id_ranges[i][1]
    elif id_ranges[i][0] > end:
        new_ranges.append([begin, end])
        begin = id_ranges[i][0]
        end = id_ranges[i][1]

new_ranges.append([begin, end])

fresh_ingredients_ids = 0

for id_range in new_ranges:
    fresh_ingredients_ids += id_range[1] - id_range[0] + 1

print(fresh_ingredients_ids)