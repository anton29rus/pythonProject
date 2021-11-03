def salary():
    try:
        work_time = float(input('Время работы, час: '))
        wage_rate = int(input('Ставка $/час: '))
        bonus = int(input('Премия в $: '))
        sal = work_time * wage_rate + bonus
        print(f'Выплата сотруднику:  {sal}')
    except ValueError:
        return print('Not a number')
salary()