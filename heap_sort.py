# heap sort - sort a list by building a max heap and pulling the biggest
# element to the end, one at a time.

def heapify(arr, n, i):
    biggest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[biggest]:
        biggest = left
    if right < n and arr[right] > arr[biggest]:
        biggest = right

    if biggest != i:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        heapify(arr, n, biggest)


def heap_sort(arr):
    n = len(arr)

    # turn the list into a max heap, starting from the last parent
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # pull the biggest element to the end and fix the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


nums = [12, 11, 13, 5, 6, 7]
print(heap_sort(nums))

nums2 = [4, 10, 3, 5, 1]
print(heap_sort(nums2))

print(heap_sort([]))
print(heap_sort([42]))
