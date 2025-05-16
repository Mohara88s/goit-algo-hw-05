def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iter_number = 0
 
    while low <= high:
        iter_number +=1
 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
    if arr[mid] < x:
        mid+=1 
    return (iter_number, arr[mid])

arr = [1.2, 2.9, 3.5, 4.7, 5.8, 7.7, 10.8, 15.6, 20.8, 35.5, 40.2]
x = 5
result = binary_search(arr, x)
print(f"The required number of iterations is {result[0]}. The upper limit is {result[1]}")
