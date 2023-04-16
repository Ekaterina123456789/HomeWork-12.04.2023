# Задание 1.
# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.
import re

employees = {}
with open('employees.txt', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()
    for line in lines:
        key, value = line.split(': ', 1)
        employees.update({key: value})
    print(employees)
    keys = ['position', 'age', 'email', 'phone']
while True:
    command = input('1. Ввести данные сотрудника\n'
                    '2. Редактировать данные сотрудника\n'
                    '3. Найти сотрудника по фамилии\n'
                    '4. Удалить сотрудника\n'
                    '5. Вывести информацию обо всех сотрудниках\n'
                    '6. Вывести информацию обо всех сотрудниках указанного возраста\n'
                    '7. Вывести информацию обо всех сотрудниках, фамилии которых начинаются на указанную букву\n'
                    '8. Вывести информацию обо всех сотрудниках указанной должности\n'
                    '9. Сохранить информацию в файл\n'
                    '0. Выйти\n'
                    'Введите команду: ')
    if command == '1' or command == '2':
        fio = str(input('Введите ФИО сотрудника через пробел: '))
        if command == '2' and fio not in employees:
            print('Такого сотрудника не существует!')
            continue
        employees[fio] = {}
        for key in keys:
            value = input(f'Введите {key} сотрудника: ')
            employees[fio][key] = value
        if command == '1':
            print('Новый сотрудник успешно добавлен!')
        else:
            print('Данные о сотруднике успешно изменены!')
    elif command == '4':
        fio = input('Введите ФИО сотрудника через пробел: ')
        del employees[fio]
        print(f'Сотрудник {fio} удален!')
    elif command == '3':
        surname = str(input('Введите фамилию сотрудника: '))
        for key, value in employees.items():
            if surname in key:
                print(key, value)
        else:
            print('Такой сотрудник не зарегистрирован!')
    elif command == '5':
        for i in range(0, len(employees)):
            print('{:20}'.format(*list(employees)[i:i + 3]) + '{:35}'.format(*list(employees.values())[i:i + 3]))
    elif command == '6':
        age = input('Введите возраст сотрудника для поиска: ')
        for key, value in employees.items():
            if age in value:
                print(key, value)
    elif command == '7':
        first_letter_surname = str(input('Введите первую букву фамилии сотрудника для поиска: '))
        for key, value in employees.items():
            name = key.split(' ')
            if first_letter_surname == name[1][0]:
                print(key, value)
    elif command == '8':
        position = str(input('Введите должность сотрудника для поиска: '))
        for key, value in employees.items():
            if position in value:
                print(key, value)
    elif command == '9':
        with open('employees.txt', 'w') as file:
            new_text = str(employees).replace('}', '}\n')
            file.writelines(new_text)
            print('Изменения сохранены')
    elif command == '0':
        save = input('Сохранить изменения? да (1), нет (0): ')
        if save == '1':
            with open('employees.txt', 'w', encoding='utf-8') as file:
                file.writelines(employees)
                print('Завершение работы')
                break
        else:
            print('Завершение работы без сохранения...')
            break
    else:
        print('Такой команды нет!')
        continue