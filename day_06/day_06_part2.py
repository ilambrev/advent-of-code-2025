def calculate_numbers_lengths(operations_string):
    number_lengths = []
    count = 0

    for i in range(1, len(operations_string)):
        if operations_string[i] == " ":
            count += 1
        else:
            number_lengths.append(count)
            count = 0

    number_lengths.append(count + 1)

    return number_lengths

def separate_numbers(number_strings, number_lengths):
    numbers = []

    for string in number_strings:
        row = []
        i = 0

        for number_length in number_lengths:
            number = string[i:i+number_length]
            row.append(number)
            i += number_length + 1

        numbers.append(row)

    return numbers

def calculate_value_of_column(numbers, col, operation):
    value = 0

    col_strings = []

    for i in range(len(numbers)):
        col_strings.append(numbers[i][col])

    col_numbers = []

    for i in range(len(col_strings[0]) - 1, -1, -1):
        digits = []

        for j in range(len(col_strings)):
            if not col_strings[j][i] == " ":
                digits.append(col_strings[j][i])

        col_numbers.append(int("".join(digits)))

    if len(col_numbers) > 0:
        value = col_numbers[0]

    for i in range(1, len(col_numbers)):
        if operation == "+":
            value += col_numbers[i]

        if operation == "*":
            value *= col_numbers[i]

    return value

file_path = "day_06_sample_data.txt"

file = open(file_path, "r")
input_data = file.read().split("\n")
file.close()

number_strings = [row for row in input_data[:-1]]
operations_string = input_data[-1]
operations = [o for o in operations_string.split()]

number_lengths = calculate_numbers_lengths(operations_string)

numbers = separate_numbers(number_strings, number_lengths)

grand_total = 0

for i in range(len(operations) - 1, -1, -1):
    grand_total += calculate_value_of_column(numbers, i, operations[i])

print(grand_total)