file_path = "day_03_sample_data.txt"

file = open(file_path, "r")
banks = file.read().split("\n")
file.close()

total_joltage = 0

for bank in banks:
    batteries_joltages = [int(battery) for battery in bank]
    max_joltage = max(batteries_joltages)
    max_joltage_index = batteries_joltages.index(max_joltage)

    if max_joltage_index == len(batteries_joltages) - 1:
        second_joltage = max(batteries_joltages[:len(batteries_joltages)-1])
        total_joltage += int(str(second_joltage) + str(max_joltage))
    else:
        second_joltage = max(batteries_joltages[max_joltage_index+1:])
        total_joltage += int(str(max_joltage) + str(second_joltage))

print(total_joltage)