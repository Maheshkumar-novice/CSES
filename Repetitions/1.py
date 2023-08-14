n = input()
current_count_map = {}

previous_value = ''
max_value = 0
for i in n:
    if previous_value != i:
        if i in current_count_map:
            max_value = max(current_count_map[i], max_value)
        current_count_map[i] = 0

    if i in current_count_map:
        current_count_map[i] += 1
    else:
        current_count_map[i] = 1 

    previous_value = i

print(max(max_value, max(current_count_map.values())))
