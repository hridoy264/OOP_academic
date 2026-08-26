def sort_and_print(list, list_name):
    list.sort(reverse=True)
    print(f"{list_name} is sorted: {list}")

L1 = [ 1, 2, 3, 4, 5, 6]
L2 = [3, 2, 7, 4, 0, 1]

sort_and_print(L1, "L1")
sort_and_print(L2, "L2")