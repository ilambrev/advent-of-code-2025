file_path = "day_02_sample_data.txt"

file = open(file_path, "r")
id_ranges = file.read().split(",")
file.close()

def is_id_invalid(i):
    string_value = str(i)
    half = int(len(string_value) / 2)

    return len(string_value) % 2 == 0 and string_value[0:half] == string_value[half:]

invalid_ids_sum = 0

for id_range in id_ranges:
    first_id, last_id = id_range.split("-")
    first_id = int(first_id)
    last_id = int(last_id)

    for i in range(first_id, last_id + 1):
        if is_id_invalid(i):
            invalid_ids_sum += i

print(invalid_ids_sum)