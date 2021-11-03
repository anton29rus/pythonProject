from random import randint
my_list = [randint(100, 1001) for i in range(10)]
print(my_list)
from functools import reduce
def my_func(prev_el, el):
    return prev_el * el
print(reduce(my_func, my_list))