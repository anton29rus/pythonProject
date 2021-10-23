my_str = "Обычная строка"
my_list = ['x', '5']
my_tuple = ('y', '10')
my_dict = {'city': 'Санкт-Петербург', 'country': 'Россия'}
big_list = [my_str, my_list, my_tuple, my_dict]
for i in big_list:
    print(f'{i} is {type(i)}')
