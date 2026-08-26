# Task 2: Binary Search for Library
# Data taken from the assignment 
books = [102, 118, 135, 149, 160, 175, 189, 201, 225, 240, 258, 274, 290, 315, 330, 348, 360, 379, 395, 410]

search_val = int(input("Enter the Book ID you want to find: "))

low = 0
high = len(books) - 1
comparisons = 0
found_index = -1

while low <= high:
    comparisons += 1
    mid = (low + high) // 2
    
    if books[mid] == search_val:
        found_index = mid
        break
    elif books[mid] < search_val:
        low = mid + 1
    else:
        high = mid - 1

print("Number of comparisons made:", comparisons)

if found_index != -1:
    print("Book ID found at index:", found_index)
else:
    print("Book is not available")
    
    # Finding closest smaller and larger
    # After the loop, 'high' is the smaller neighbor and 'low' is the larger one
    if high >= 0:
        print("Closest smaller Book ID:", books[high])
    else:
        print("Closest smaller Book ID: None")
        
    if low < len(books):
        print("Closest larger Book ID:", books[low])
    else:
        print("Closest larger Book ID: None")