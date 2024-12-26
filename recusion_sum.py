def sum(arr, i):
    if i <= -1:
        return 0
    else:
        return arr[i] + sum(arr, i-1)

arr = [3, 4, 5, 2, 6, 1]
print(sum(arr, len(arr)-1))