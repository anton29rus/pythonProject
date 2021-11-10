result_1day = float(input("Enter your result of the first day: "))
result_f_day = float(input("Enter your desirable result: "))
day = 1
if result_1day > result_f_day:
    print(day)
while result_1day < result_f_day:
    result_1day = result_1day + result_1day*0.1
    day += 1
    print(day, round(result_1day, 2))
print('до достижения результата', day, 'дней')
