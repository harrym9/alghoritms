def find_biggest_number(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        temp = find_biggest_number(arr[1:])
        return arr[0] if arr[0] > temp else temp
    
arr = [4, 2, 24, 6, 1, 7, 45, 1, 6, 41]
print(find_biggest_number(arr))
