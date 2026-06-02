# Filtering Lists with Conditional Logic

num_list = [10, 12, 15, 20, 25, 23, 56, 65]
new_list = []
def divisible_by_five(number_list):
    for i in range(0, len(number_list)):
        if number_list[i]%5==0:
            new_list.append(number_list[i])
    return new_list

print(divisible_by_five(num_list))