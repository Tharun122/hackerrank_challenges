def selection_sort(arr: list[int]):
    n = len(arr)
    for i in range(n):
        minElementIndex = i
        for j in range(i, n):
            if arr[j] < arr[minElementIndex]:
                minElementIndex = j
        arr[i],arr[minElementIndex] = arr[minElementIndex],arr[i]
    return arr

def bubble_sort(arr: list[int]):
    n = len(arr)
    # Repeatedly iterate through the array
    for i in range(n-1):
        # Flag to check if any swaps occurred
        swapped = False
        for j in range(0, n-i-1):
            # Compare adjacent elements and swap if necessary
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(True, i, j, arr)
                swapped = True
            else:
                print(False, i, j, arr)
            # If no swaps occurred in the inner loop, the array is already sorted
        if not swapped:
            break
    return arr

def bubble_sort_recursive_delete(arr: list[int]):
    no_of_swaps = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            no_of_swaps += 1
        i += 1
    if no_of_swaps == 0:
        return arr
    return bubble_sort(arr)

print(selection_sort([110, 2, 45, 23, 3, 45, 9, 4, 64, 4, 78, 34]))
