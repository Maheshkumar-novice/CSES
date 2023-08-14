n = input()

previous_value = ''
max_value_counter = 0
current_value_counter = 0
for i in n:
    if previous_value != i:
        max_value_counter = max(max_value_counter, current_value_counter)
        current_value_counter = 0

    current_value_counter += 1
    previous_value = i


print(max(max_value_counter, current_value_counter))
