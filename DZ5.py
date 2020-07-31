# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
filename = input('Имя файла в текстовом формате: ')
my_list1 = []

while True:
    line = input('Введите информацию: ')
    if line == '':
        print(my_list1)
        exit()
    else:
        newline = line + '\n'
        my_list1.append(newline)
    with open(filename, 'w') as my_file1:
        my_file1.writelines(my_list1)


# # # 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# # # выполнить подсчет количества строк, количества слов в каждой строке.
with open('test2.txt', 'r') as my_file:
    text = my_file.read()
    print(text)
    my_file.seek(0)
    lines = my_file.readlines()
    print('Количество строк в файле:', len(lines))
    my_file.seek(0)
    worlds = 0
    i = 1

    for elem in my_file:
        worlds = elem.split()
        print(f'{len(worlds)} слова в {i} строке.')
        i = i + 1




# # 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# # Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# # Выполнить подсчет средней величины дохода сотрудников.

with open('test3.txt', 'r') as my_file3:
    sal = []
    workers = []
    my_list3 = my_file3.read().split('\n')
    print(my_list3)
    for elem in my_list3:
        elem = elem.split()
        if int(elem[1]) < 20000:
            workers.append(elem[0])
        sal.append(int(elem[1]))
print(f'Оклад меньше 20000 руб: {workers}')
kol_workers = len(workers)
sum_workers = sum(sal)
print(f'Средний оклад: {sum_workers/kol_workers}')


# # 4. Создать (не программно) текстовый файл со следующим содержимым:
# # One — 1
# # Two — 2
# # Three — 3
# # Four — 4
# # Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# # При этом английские числительные должны заменяться на русские.
# # Новый блок строк должен записываться в новый текстовый файл.
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []

with open('test4.txt', 'r', encoding='utf-8') as my_file4:
    for i in my_file4:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('test4-2.txt', 'w', encoding='utf-8') as my_file4_2:
    my_file4_2.writelines(new_file)

# # 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# # Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
filename = input('Имя файла в текстовом формате: ')
with open(filename, 'w', encoding='utf-8') as my_file5:
    line = input('Введите набор чисел разделенных пробелами: ')
    my_file5.write('Вы ввели: ' + line + '\n')
    line = map(int, line.split())
    sum_line = sum(line)
    my_file5.write('Сумма чисел равна: '+ str(sum_line))
    print('Сумма чисел равна: ', sum_line)

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#
subj = {}
with open('test6.txt', 'r', encoding='utf-8') as my_file6:
    for line in my_file6:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')
