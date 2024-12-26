def look_for(my_arr, target):
    if not my_arr:
        return False
    if my_arr[0] == target:
        return True
    return look_for(my_arr[1:], target)

my_arr = [2,3,1,4,12,2,6,3,5,6,7,1,2]
print(look_for(my_arr, 5))