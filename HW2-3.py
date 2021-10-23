month = int(input("Введите номер месяца: "))
if month <= 12 and month >= 1:
    month_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
                  7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == month - 1:
            print(f"Введенному номеру соответствует месяц: {month_list[i]}")
            break
else:
    print("Нет такого номера месяца!")