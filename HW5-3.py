comp = {'Ivanov': 120, 'Petrov': 140, 'Sidorov': 160, 'Vasechkin': 275}
try:
    file_obj = open("test.txt", 'w')
    for last_name, salary in comp.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"persons: {persons}")
print(f"average value: {result}")
