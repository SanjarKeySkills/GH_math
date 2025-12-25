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
print(first_element)
print(middle_element)
print(last_element)

# insert and delete O(N)

my_list1 = []
my_list1.append(1)
my_list1.append(2)
a = my_list1.append(3)
print(my_list1)

last_element1 = my_list1.pop()
print(last_element1)

my_list1.insert(0, 0)
print(my_list1)

# hash-tag table workout (dictionary/multiplicity)
# average_case

my_dict = {'apple':5, 'banana':10, 'orange':7}
my_set = {1, 2, 3, 4, 5}
# O(1) in average case