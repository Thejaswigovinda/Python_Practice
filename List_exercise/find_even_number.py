def even_num(list):
  new_list = []
  for num in list:
    if num%2==0:
      new_list.append(num)
  print(new_list)

my_list = [2,5,3,6,7,8]
even_list(my_list)
