# def find_pairs_optimal(arr, target):
#     """Решение за O(N) с использованием хэш-таблицы"""
#     result = []
#     seen = {}
    
#     for i, num in enumerate(arr):
#         complement = target - num
#         if complement in seen:
#             for j in seen[complement]:
#                 result.append((j, i))
        
#         if num not in seen:
#             seen[num] = []
#         seen[num].append(i)
    
#     return result

 # O(1) when the index is known
 
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
first_element = my_list[0]
middle_element = my_list[5]
last_element = my_list[-1]
# print(first_element)
# print(middle_element)
# print(last_element)

# insert and delete O(N)

my_list1 = []
my_list1.append(1)
my_list1.append(2)
a = my_list1.append(3)
# print(my_list1)

last_element1 = my_list1.pop()
# print(last_element1)

my_list1.insert(0, 0)
# print(my_list1)

# hash-tag table workout (dictionary/multiplicity)
# average_case

my_dict = {'apple':5, 'banana':10, 'orange':7}
my_set = {1, 2, 3, 4, 5}
# O(1) in average case
my_dict['grape'] = 15 #insert
# print(my_dict)
value = my_dict['apple'] #receiving
exists = 'banana' in my_dict
# print(value)
# print(exists)

my_set.add(6)
exists = 3 in my_set
# print(exists)
# check out for the key and the element presence (key in dict, element in set)
# insert (dict[key] = value, set.add(element))
# dict[key] receives according to the key

# O(1) the constant complexity
def is_even(num):
    return num % 2 == 0 # O(1) - just one unit
result = is_even(101)
print(result)


#---------------------
#class Node:

def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def searchInBST(root, target):
    current = root
    while current:
        if current.value == target:
            return True #if we found
        elif target < current.value:
            current = current.left # we are going to the left sub-tree
        else:
            current = current.right # we are going to the right sub-tree
        return False # if not found
print()

#--------------------------

# (log N)
import bisect

arr = [1, 2, 4, 5, 7, 9]
index = bisect.bisect_left(arr, 5)
print(index)  # 3 (индекс, где находится 5)
#---------------------

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half
    else:
        return x * power(x, n - 1)

print(power(2, 10))  # 1024

# --------------

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Пример использования
arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))  # 3
print(binary_search(arr, 10)) # -1

#-----------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_in_bst(root, target):
    if root is None or root.value == target:
        return root
    if target < root.value:
        return search_in_bst(root.left, target)
    return search_in_bst(root.right, target)

# Пример использования
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.right = Node(7)
root.right.left = Node(15)

result = search_in_bst(root, 7)
print(result.value if result else "Не найдено")  # 7