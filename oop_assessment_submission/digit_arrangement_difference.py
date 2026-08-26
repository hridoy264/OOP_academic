
def max_min(num):
    num = str(num)
    li = list(num)
    low_sort = sorted(li)
    low = int("".join(low_sort))
    high_sort = sorted(li, reverse=True)
    high = int("".join(high_sort))

    print(high-low)

max_min(418)