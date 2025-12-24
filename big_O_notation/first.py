def find_pairs_optimal(arr, target):
    """Решение за O(N) с использованием хэш-таблицы"""
    result = []
    seen = {}
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            for j in seen[complement]:
                result.append((j, i))
        
        if num not in seen:
            seen[num] = []
        seen[num].append(i)
    
    return result