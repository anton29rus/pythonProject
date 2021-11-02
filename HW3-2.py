def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])

print(my_func(surname='Ivanov', name='Ivan', year='1980', city='S-Pb', email='work@mail.ru',
              telephone='+7-123-456-78-90'))