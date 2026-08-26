original_dict = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

filtered_dict = {}

for key, values in original_dict.items():
    even_numbers = []
    for num in values:
        if num % 2 == 0:
            even_numbers.append(num)
    filtered_dict[key] = even_numbers

print("Filter even numbers from given dictionary values:")
print(filtered_dict)