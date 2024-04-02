
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

def selection_sort(arr: list[int]):
    n = len(arr)
    for i in range(n):
        minElementIndex = i
        for j in range(i, n):
            if arr[j] < arr[minElementIndex]:
                minElementIndex = j
        arr[i],arr[minElementIndex] = arr[minElementIndex],arr[i]
    return arr

def insertion_sort(arr: list[int]):
    n = len(arr)
    for i in range(n):
        for j in range(i):
            if arr[j] > arr[i]:
                temp = arr[i]
                k = i
                while k > j:
                    arr[k] = arr[k-1]
                    k -= 1
                arr[j] = temp
                # break
    return arr
