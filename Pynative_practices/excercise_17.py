# Merging Lists with Parity Filtering

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8, 9, 0]
merge=[]
def parity_filter(list_1, list_2):
    for i in range(len(list_1)):
        if list_1[i]%2 == 1:
            merge.append(list_1[i])
    for i in range(len(list_2)):
        if list_2[i]%2 == 0:
            merge.append(list_2[i])
    print(merge)

parity_filter(list_1, list_2)