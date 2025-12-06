def calculate_value_of_column(numbers, col, operation):
    value = 0

    if len(numbers) > 0:
        value = numbers[0][col]

    for i in range(1, len(numbers)):
        if operation == "+":
            value += numbers[i][col]

        if operation == "*":
            value *= numbers[i][col]

    return value

file_path = "day_06_sample_data.txt"

file = open(file_path, "r")
input_data = [row.strip() for row in file.read().split("\n")]
file.close()

numbers = [row.split() for row in input_data[:-1]]

for i in range(len(numbers)):
    numbers[i] = [int(n) for n in numbers[i]]

operations = [o for o in input_data[-1].split()]

grand_total = 0

for i in range(len(operations)):
    grand_total += calculate_value_of_column(numbers, i, operations[i])

print(grand_total)