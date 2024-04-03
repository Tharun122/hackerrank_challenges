# Quick Sort
def partition(arr: list[int], low: int, high: int):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr: list[int], low: int, high: int):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)

print("\nQuick Sort")
inp_arr = [110, 2, 45, 23, 3, 45, 9, 4, 64, 4, 78, 34]
print(inp_arr)
quick_sort(inp_arr, 0, len(inp_arr)-1)
print(inp_arr)

# Merge Sort
def merge_sort_merge(left: list[int], right: list[int]):
    merged_arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
    merged_arr += left[i:]
    merged_arr += right[j:]
    return merged_arr

def merge_sort(arr: list[int]):
    n = len(arr)
    if n == 1:
        return arr
    break_point = int(n/2)
    left = merge_sort(arr[:break_point])
    right = merge_sort(arr[break_point:])
    return merge_sort_merge(left, right)

print("\nMerge Sort")
inp_arr = [110, 2, 45, 23, 3, 45, 9, 4, 64, 4, 78, 34]
print(inp_arr)
print(merge_sort(inp_arr))

# Bubble Sort
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
                swapped = True
        if not swapped:
            break
    return arr

print("\nBubble Sort")
inp_arr = [110, 2, 45, 23, 3, 45, 9, 4, 64, 4, 78, 34]
print(inp_arr)
print(bubble_sort(inp_arr))

# Selection Sort
def selection_sort(arr: list[int]):
    n = len(arr)
    for i in range(n):
        minElementIndex = i
        for j in range(i, n):
            if arr[j] < arr[minElementIndex]:
                minElementIndex = j
        arr[i],arr[minElementIndex] = arr[minElementIndex],arr[i]
    return arr

print("\nSelection Sort")
inp_arr = [110, 2, 45, 23, 3, 45, 9, 4, 64, 4, 78, 34]
print(inp_arr)
print(selection_sort(inp_arr))

# Insertion Sort
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

print("\nInsertion Sort")
inp_arr = [110, 2, 45, 23, 3, 45, 9, 4, 64, 4, 78, 34]
print(inp_arr)
print(insertion_sort(inp_arr))
