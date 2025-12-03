file_path = "day_03_sample_data.txt"

file = open(file_path, "r")
banks = file.read().split("\n")
file.close()

total_joltage = 0

for bank in banks:
    batteries_joltages = [int(battery) for battery in bank]
    joltages = []
    start_index = 0

    for i in range(12, 0, -1):
        max_joltage = max(batteries_joltages[start_index:len(batteries_joltages)+1-i])
        start_index = batteries_joltages.index(max_joltage, start_index) + 1
        joltages.append(max_joltage)
    
    max_bank_joltage = int("".join(map(str, joltages)))
    
    total_joltage += max_bank_joltage

print(total_joltage)