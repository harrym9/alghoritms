
def binary_search(my_list, target, sayac = 0):
    low = 0
    high = len(my_list) - 1

    while low >= high:
        sayac += 1
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == target:
            print(sayac)
            print(mid)
            return
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1 
    
    return None

my_list = [i+1 for i in range(400000)]

binary_search(my_list, 4000)