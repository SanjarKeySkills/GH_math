def find_after_index(arr, target, start_from = 0):
    for i, num in enumerate(arr):
        if i < start_from:
            continue
        if num == target:
            return 1
    return -1

arr = [10, 20, 30, 20, 40]
print(find_after_index(arr, 20, 2))

# ----O(log N)------------
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right)//2 #looking for middle
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1 # search in right side
        else:
            right = mid - 1 # search in the left side
        return - 1