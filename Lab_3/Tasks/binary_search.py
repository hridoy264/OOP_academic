def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    # If we reach here, the element was not present
    return -1

# Example usage
numbers = [2, 3, 4, 10, 40]
target = 10
result = binary_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not present in array")
