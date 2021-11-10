from random import randint
my_list = [randint(1, 20) for i in range(10)]
new = [el for el in my_list if my_list.count(el) == 1]
print(my_list)
print(new)