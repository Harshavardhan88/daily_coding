# selection sort - keep picking the smallest remaining element
# and move it to the front

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

print(selection_sort([5, 4, 3, 2, 1]))
print(selection_sort([1, 2, 3]))
print(selection_sort([]))
