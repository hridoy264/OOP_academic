
catalog = [
    {"id": 1245, "title": "Artificial Intelligence", "author": "Sophia White", "copies": 3, "year": 2021},
    {"id": 1001, "title": "Python Basics", "author": "John Smith", "copies": 4, "year": 2018},
    {"id": 1450, "title": "Cyber Security", "author": "Daniel Clark", "copies": 2, "year": 2022},
    {"id": 1078, "title": "Algorithms Made Easy", "author": "David Lee", "copies": 0, "year": 2019},
    {"id": 1525, "title": "Cloud Computing", "author": "Olivia Martin", "copies": 4, "year": 2023},
    {"id": 1120, "title": "Database Systems", "author": "Maria Green", "copies": 5, "year": 2017},
    {"id": 1300, "title": "Machine Learning", "author": "James Wilson", "copies": 0, "year": 2020},
    {"id": 1035, "title": "Data Structures", "author": "Alice Brown", "copies": 2, "year": 2016},
    {"id": 1375, "title": "Operating Systems", "author": "Emma Davis", "copies": 6, "year": 2015},
    {"id": 1189, "title": "Computer Networks", "author": "Robert King", "copies": 1, "year": 2014}
]


comparisons = 0
shifts = 0

def quick_sort(arr, key):
    global comparisons, shifts
    
    if len(arr) <= 1:
        return arr
    

    pivot = arr[0]
    lower = []
    middle = []
    upper = []
    
    for book in arr:
        comparisons += 1
        if book[key] < pivot[key]:
            lower.append(book)
            shifts += 1 
        elif book[key] > pivot[key]:
            upper.append(book)
            shifts += 1 
        else:
            middle.append(book)
            

    return quick_sort(lower, key) + middle + quick_sort(upper, key)



comparisons = 0
shifts = 0

def merge_sort(arr, key):
    global comparisons, shifts
    
    # Base case: A list of 1 or 0 is already sorted
    if len(arr) <= 1:
        return arr

    # Split the catalog into two halves 
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], key)
    right_half = merge_sort(arr[mid:], key)

    return merge(left_half, right_half, key)

def merge(left, right, key):
    global comparisons, shifts
    result = []
    i = j = 0


    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        shifts += 1


    while i < len(left):
        result.append(left[i])
        i += 1
        shifts += 1
        
    while j < len(right):
        result.append(right[j])
        j += 1
        shifts += 1

    return result


def display_results(sorted_catalog, sort_type):
    print(f"\nSorted Catalog by {sort_type}:")
    for book in sorted_catalog:
        copies_text = book["copies"] if book["copies"] > 0 else "Currently Not Available"
        
        print(f"Book ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Copies: {copies_text}")
        print(f"Year: {book['year']}")

    
    print(f"Number of Comparisons: {comparisons}") 
    print(f"Number of Swaps/Shifts: {shifts}")     

def main():
    global comparisons, shifts
    
    while True:
        comparisons = 0
        shifts = 0
        
        print("\nChoose sorting option:")
        print("1. Sort by Book ID")       
        print("2. Sort by Year of Publication") 
        print("3. Sort by Available Copies")    
        
        choice = input("Enter your choice (or 'no' to exit): ").strip().lower()
        
        if choice == 'no':
            print("Exiting program.")
            break
        

        options = {"1": ("id", "Book ID"), 
                   "2": ("year", "Year of Publication"), 
                   "3": ("copies", "Available Copies")}
        
        if choice in options:
            key, label = options[choice]
            sorted_data_for_id = quick_sort(catalog, key)
            display_results(sorted_data_for_id, label)
        else:
            print("Invalid choice, please select 1, 2, 3, or 'no'.")

if __name__ == "__main__":
    main()