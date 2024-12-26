
def main():
    arr = [5,2,4,2,1,5,1,5,3,5,7,8,9,6,5,213,4,3,1]
    print(selection_sort(arr))
    print(arr)

def find_smallest(arr):
    smallest = arr[0]
    ind_smallest = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            ind_smallest = i
    return ind_smallest

def selection_sort(arr):
    new_sorted_array = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_sorted_array.append(arr.pop(smallest))
    return new_sorted_array
main()
