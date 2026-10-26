def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # already sorted, no need to go again
        if not swapped:
            break
    return arr


nums = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(nums))

print(bubble_sort([5, 2, 9, 1, 7]))
print(bubble_sort([1, 2, 3, 4]))
print(bubble_sort([]))
