
def same_values(lst1, lst2):
  new_arr = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      new_arr.append(i)
  return new_arr

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))