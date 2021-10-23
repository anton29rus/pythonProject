a = int(input('введите число'))
b = int(input('введите число'))
c = int(input('введите число'))
d = int(input('введите число'))
e = int(input('введите число'))
f = int(input('введите число'))
my_list = [a, b, c, d, e, f]
print(my_list)
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)
