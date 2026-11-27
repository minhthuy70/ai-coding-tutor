def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Test với mảng lớn
import random
large_array = [random.randint(1, 1000) for _ in range(20000)]
print('Bắt đầu sắp xếp...')
sorted_arr = bubble_sort(large_array)
print('Hoàn thành!')