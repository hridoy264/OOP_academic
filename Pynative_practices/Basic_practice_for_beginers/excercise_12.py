# List Comparison and Boolean Logic

numbers_1 = [ 1, 2, 3, 4, 5, 1]
numbers_2 = [2, 3, 4, 5, 6, 7]

def first_last_same(numbers):
    if numbers[0] == numbers[-1]:
        return True
    else: 
        return False

print(first_last_same(numbers_1))
print(first_last_same(numbers_2))