# quick sort - pick a pivot, split into smaller and bigger parts, sort each part

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)

    return quick_sort(left) + middle + quick_sort(right)


nums = [8, 3, 1, 7, 0, 10, 2]
print(quick_sort(nums))

print(quick_sort([5, 2, 9, 1, 5, 6]))
print(quick_sort([]))
print(quick_sort([4]))
