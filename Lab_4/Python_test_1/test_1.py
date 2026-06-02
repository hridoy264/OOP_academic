catalog = [
    {"id":1245, "title":"Artificial Intelligence", "author": "Sophia White", "copies":3, "year": 2021},
    {"id":1001, "title":"Python Basics", "author": "John Smith", "copies":4, "year": 2018},
    {"id":1450, "title":"Artificial Intelligence", "author": "Sophia White", "copies":3, "year": 2021},
    {"id":1078, "title":"Artificial Intelligence", "author": "Sophia White", "copies":3, "year": 2021},
    {"id":1525, "title":"Artificial Intelligence", "author": "Sophia White", "copies":3, "year": 2021},
    {"id":1120, "title":"Artificial Intelligence", "author": "Sophia White", "copies":3, "year": 2021},
    {"id":1300, "title":"Artificial Intelligence", "author": "Sophia White", "copies":3, "year": 2021},
    {"id":1035, "title":"Artificial Intelligence", "author": "Sophia White", "copies":3, "year": 2021},
    {"id":1375, "title":"Artificial Intelligence", "author": "Sophia White", "copies":3, "year": 2021},
    {"id":1189, "title":"Artificial Intelligence", "author": "Sophia White", "copies":3, "year": 2021},

]

ids_catalog = [book["id"] for book in catalog]

# Sorting using quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    greater_values = []
    lower_values = []

    for i in arr:
        if pivot < i:
            greater_values.append(i)
        else:
            lower_values.append(i)
    return quick_sort(lower_values) + [pivot] + quick_sort(greater_values)

sorted_id = quick_sort(ids_catalog)
print([book["id"] for book in catalog])

# def get_book_attribute(catalog, book_id, attribute):
#     for book in catalog:
#         if book["id"] == book_id:
#             return book.get(attribute, "Attribute not found")
#     return "ID not found"

for book in catalog:
    print(book["id"], book["title"], book["author"], book["copies"], book["year"])

for i in range(len())





