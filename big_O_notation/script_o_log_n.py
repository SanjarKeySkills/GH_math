arr = [1, 2, 3, 4, 5, 6, 7]
dict_from_list = {i: val for i, val in enumerate(arr)}
# print(dict_from_list)

#-----------------------------------------

students =  ["Ann", "Boris", "Tanya", "Nathan"]
students_ids = {id: name for id, name in enumerate(students, start=13)}
# print(students_ids)

# ----------------------------------------
arr = [45, 98, 3, 24, 78, 56, 14, 97, 55, 1, 18, 73]

def separate(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
# ----recursion--------------------------
    left = separate(left)
    right = separate(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
#-------------------оставшиеся элементы----------
    result.extend(left[i:])
    result.extend(right[j:])
    return result

sorted_arr = separate(arr)
# print("not sorted arr", arr)
# print("sorted", sorted_arr)


# -------------separate---arrays----sorts------------

arr_zero = [7, 9, 8, 5, 10, 11]
arr_first = [23, 90, 87, 12, 34, 56, 98, 16, 8, 11, 55, 88, 96, 69]
arr_second = [33, 31, 45, 46, 80, 123, 304, 41, 111, 101, 97, 59, 15]

def sort_arrays(arr_first, arr_second):
    final_result = []
    e = o = 0
    while e < len(arr_first) and o < len(arr_second):
        if arr_first[e] <= arr_second[o]:
            final_result.append(arr_first[e])
            e += 1
        else:
            final_result.append(arr_second[o])
            o += 1
    final_result.extend(arr_first[e:])
    final_result.extend(arr_second[o:])
    return final_result
output = sort_arrays(arr_first, arr_second)
print(output)
