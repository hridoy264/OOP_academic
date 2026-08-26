numbers = []
unique_numbers = []

while True:
    user_input = input("Enter Number: ")
    
    if user_input.upper() == "SHESH":
        break

    num = int(user_input)
    numbers.append(num)

    if num not in unique_numbers:
        unique_numbers.append(num)

print("\nSample Output:")

for num in unique_numbers:
    count = numbers.count(num)
    print(f"{num} - {count} times")

