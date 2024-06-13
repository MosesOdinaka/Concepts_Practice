def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A sorted list of elements
    target (int): The value to search for

    Returns:
    int: The index of the array if found, else -1
    """
    left, right = 0, len(arr) -1

    while left <= right:
        # Calculate the midpoint of the current interval
        mid = (left + right) // 2
        # Check if target is at the midepoint
        if arr[mid] == target:
            return mid # Target found in index mid
        elif arr[mid] < target:
            left = mid + 1 # Narrow the search to the right half
        else:
            right = mid - 1 # Narrow thd search to the left half

    return -1 # Target not found in the array

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
index = binary_search(arr, target)
print(f"Target {target} found at index {index}") # Output: Target 7 found at index 6
