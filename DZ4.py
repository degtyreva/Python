# # Задание 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# # В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# # Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    result = time * salary + bonus
    print(f'Зарплата сотрудника равна:  {result}')
except ValueError:
    print('Вы ввели не числа')

# Задание 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

my_list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list2 = [el for i, el in enumerate(my_list1) if my_list1[i] > my_list1[i-1]]
print(new_list2)

# # Задание 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# # Подсказка: использовать функцию range() и генератор.
#
print([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0])

# # Задание 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# # Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
# # Для выполнения задания обязательно использовать генератор.
# # Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# # Результат: [23, 1, 3, 10, 4, 11]

my_list4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_my_list4 = [el for el in my_list4 if my_list4.count(el) < 2]
print("Старый список: ", my_list4)
print("Новый список: ", new_my_list4)

# # 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# # В список должны войти четные числа от 100 до 1000 (включая границы).
# # Необходимо получить результат вычисления произведения всех элементов списка.
# # Подсказка: использовать функцию reduce().
#
from functools import reduce
def my_func5(num1, num2):
    return num1 * num2

my_list5 = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list5)
print(reduce(my_func5, my_list5))

# # 6. Реализовать два небольших скрипта:
# # а) итератор, генерирующий целые числа, начиная с указанного,
#
# # б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# # Подсказка: использовать функцию count() и cycle() модуля itertools.
# # Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

from itertools import count
for el in count(10):
    print(el)
    if el > 29:
        break


from itertools import cycle
s = 1
for el in cycle(["A", "B", "C", "D"]):
    print(el)
    s = s + 1
    if s > 10:
        break

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from math import factorial
from itertools import count
n = int(input("Введите целое положительное число n: "))
print(n)
def fact_gen():
    for el in count(1):
        yield factorial(el)
generator = fact_gen()
x = 0
for i in generator:
    if x < n:
        print(i)
        x += 1
    else:
        break



