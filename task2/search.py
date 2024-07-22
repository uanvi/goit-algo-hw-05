def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == x:
            return (iterations, arr[mid])
        
        if arr[mid] < x:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
    
    return (iterations, upper_bound)

# Приклад використання:
sorted_array = [0.1, 1.2, 2.4, 4.1, 5.7, 6.2, 7.7, 7.9, 8.1]
search_value = 4.1

result = binary_search(sorted_array, search_value)
print(f"Ітерації: {result[0]}, Верхня межа: {result[1]}")
