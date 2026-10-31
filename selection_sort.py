# selection sort: find the smallest element left and put it in place

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr


nums = [64, 25, 12, 22, 11]
print(selection_sort(nums))

nums2 = [5, 4, 3, 2, 1]
print(selection_sort(nums2))

nums3 = [3, 1, 4, 1, 5, 9]
print(selection_sort(nums3))
