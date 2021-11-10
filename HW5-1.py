my_list = []
while True:
    line = input("Enter your phrase: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("test.txt", "w") as file_obj:
        file_obj.writelines(my_list)