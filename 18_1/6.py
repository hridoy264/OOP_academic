input_dict = {"key1": "value1", "key2": "value2", "key3": "value1"}

inverted_dict = {}

for key, val in input_dict.items():
    if val not in inverted_dict:
        inverted_dict[val] = [key]
    else:
        inverted_dict[val].append(key)

print(inverted_dict)