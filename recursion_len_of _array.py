def len_of_array(lst):
    if not lst:
        return 0
    else:
        return 1 + len_of_array(lst[1:])

lst = ["Gayrat", "Dowran", "Hoşgeldi", "Murat", "Didar", "Maryam"]
print(len_of_array(lst))