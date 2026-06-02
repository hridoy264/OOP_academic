list_a = [1, 2, 3, 4, 5]
list_b = [2, 4, 3, 5, 6]

set_a = set(list_a)
set_b = set(list_b)

common = set_a & set_b

print(f"Common list is {common}")