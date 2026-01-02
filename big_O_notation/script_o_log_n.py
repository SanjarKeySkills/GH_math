arr = [1, 2, 3, 4, 5, 6, 7]
dict_from_list = {i: val for i, val in enumerate(arr)}
print(dict_from_list)

#-------------------

students =  ["Ann", "Boris", "Tanya", "Nathan"]
students_ids = {id: name for id, name in enumerate(students, start=13)}
print(students_ids)

# ---------
arr = [45, 98, 3, 24, 78, 56, 14, 97, 55, 1, 18, 73]

def separate(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
# ----recursion
    left = separate(left)
    right = separate(right)
    return separate(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    while i < arr(left) and j < arr(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        result.extend(left[i:])
        result.extend(right[j:])
    return result