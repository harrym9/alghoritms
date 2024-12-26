def quicksort(array):
    if len(array) < 2:
        
        return array
    
    else:
        pivot = array[0]
        
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)
    
my_array = [4,6,1,8,3,7,2,9,5]
print(quicksort(my_array))