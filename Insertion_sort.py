def insertion_sort_decreasing(arr):
    """
    Sorts an array in monotonically decreasing order using the insertion sort algorithm.

    Parameters:
    arr (list): The list of elements to be sorted.
    """
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be inserted into the sorted portion
        j = i - 1
        
        # Move elements of arr[0..i-1] that are smaller than key to one position ahead
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key at its correct position
        arr[j + 1] = key

if __name__ == "__main__":
    # Example usage
    array = [12, 11, 13, 5, 6]
    print("Original array:", array)
    insertion_sort_decreasing(array)
    print("Sorted array in monotonically decreasing order:", array)
