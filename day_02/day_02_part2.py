file_path = "day_02_sample_data.txt"

file = open(file_path, "r")
id_ranges = file.read().split(",")
file.close()

def is_id_invalid(i):
    string_value = str(i)

    divisors = [d for d in range(1, len(string_value)) if len(string_value) % d == 0]

    if len(divisors) == 1:
        return string_value.count(string_value[0]) == len(string_value)

    for divisor in divisors:
        string_value_part = string_value[0:divisor]
        is_invalid = True

        for i in range(divisor, len(string_value), divisor):
            current_part = string_value[i:i+divisor]

            if not current_part == string_value_part:
                is_invalid = False
                break

        if is_invalid:
            return True

    return False

invalid_ids_sum = 0

for id_range in id_ranges:
    first_id, last_id = id_range.split("-")
    first_id = int(first_id)
    last_id = int(last_id)

    for i in range(first_id, last_id + 1):
        if is_id_invalid(i):
            invalid_ids_sum += i

print(invalid_ids_sum)