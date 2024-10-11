def linear_search_recursive(arr, target, index=0):
    # Base case: If index reaches the end of the list
    if index == len(arr):
        return -1  # Target not found
    
    # If the target is found at the current index
    if arr[index] == target:
        return index  # Return the index of the target
    
    # Recursive call to check the next element
    return linear_search_recursive(arr, target, index + 1)

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30

result = linear_search_recursive(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
