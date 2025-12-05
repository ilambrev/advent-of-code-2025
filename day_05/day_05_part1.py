def is_ingredient_fresh(id_ranges, id):
    for id_range in id_ranges:
        if id_range[0] <= id <= id_range[1]:
            return True

    return False

file_path = "day_05_sample_data.txt"

file = open(file_path, "r")
input_data = file.read().split("\n")
file.close()

empty_line_index = input_data.index("")

id_ranges = [[int(id) for id in r.split("-")]
             for r in input_data[:empty_line_index]]
ingredient_ids = [int(id) for id in input_data[empty_line_index+1:]]

fresh_ingredients_count = 0

for id in ingredient_ids:
    if is_ingredient_fresh(id_ranges, id):
        fresh_ingredients_count += 1

print(fresh_ingredients_count)