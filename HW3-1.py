def my_funk(a, b):
    try:
        print('Результат деления: ')
        return a / b
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "На ноль делить нельзя!5"

print(my_funk(int(input('Введите первое число: ')), int(input('Введите второе число: '))))