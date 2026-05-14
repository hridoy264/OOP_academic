# Task 1: Library Sorting Program
# Name: Shahnewaj Hridoy
# Roll: 18

# Book IDs from the question paper
book_ids = [258, 102, 395, 175, 330, 118, 410, 240, 149, 315, 189, 360, 135, 274, 201, 348, 160, 290, 225, 379]

# 1. Checking if the list is already sorted first
is_sorted = True
for i in range(len(book_ids) - 1):
    if book_ids[i] > book_ids[i+1]:
        is_sorted = False
        break

if is_sorted == True:
    print("Catalog is already sorted.")
else:
    # 2. Manual Selection Sort
    count_comp = 0
    count_swap = 0
    n = len(book_ids)

    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            count_comp += 1
            if book_ids[j] < book_ids[min_pos]:
                min_pos = j
        
        # Swapping values
        if min_pos != i:
            temp = book_ids[i]
            book_ids[i] = book_ids[min_pos]
            book_ids[min_pos] = temp
            count_swap += 1

    # 4, 5, 6. Displaying results
    print("Sorted Book IDs:", book_ids)
    print("Total Comparisons:", count_comp)
    print("Total Swaps:", count_swap)

# 9. Search part
find_id = int(input("\nEnter Book ID to search: "))
found = False
for item in book_ids:
    if item == find_id:
        found = True
        break

if found:
    print("Book is available in the catalog.")
else:
    print("Book is not available in the catalog.")