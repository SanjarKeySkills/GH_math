def find_after_index(arr, target, start_from = 0):
    for i, num in enumerate(arr):
        if i <= start_from and num == target:
            return 1
    return -1

arr = [10, 20, 30, 20, 40]
print(find_after_index(arr, 20, 2))