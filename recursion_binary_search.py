#Write your function here
def exponents(bases, powers):
  new_list = []
  for i in bases:
    for j in powers:
      new_list.append(i**j)
  return new_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))