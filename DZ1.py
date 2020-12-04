# Задание 1. Работа с переменными.
a = int(input("Введите целое число: "))
print("Целое число: ", a)
print(type(a))
b = float(input("Введите дробное число: "))
print("Дробное число: ", b)
print(type(b))
с = (input("Введите слово: "))
print("Слово: ", с)
print(type(с))

# Задание 2. Пользователь вводит время в секундах. Перевести время в часы, минуты, секунды.
sec = int(input("Введите время в секундах: "))
print(sec)
hour = sec//3600
sec_for_minute = sec % 3600
minute = sec_for_minute//60
seconds = sec_for_minute % 60
print("Время в секундах: ", sec)
print(hour)
print(minute)
print(seconds)
print("Время(часы: минуты: секунды): %d : %d : %d" % (hour, minute, seconds))


# Задание 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
n = input("Введите целое число n: ")
nn = n + n
nnn = n + n + n
n = int(n)
nn = int(nn)
nnn = int(nnn)
sum = n + nn + nnn
print ("Вы ввели число: ", n)
print ("Сумма чисел n + nn + nnn равна: ", sum)


# Задание 4 первый вариант. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
number = input('Введите целое положительное число: ')
print("Вы ввели число: ", number)
print("Максимальная цифра: ", max(number))

# Задание 4 второй вариант. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
number1 = input("Введите целое положительное число: ")
repit = len(number1)-1
i = 0
a = int(number1[i])
while i < repit:
    b = int(number1[i+1])
    i += 1
    if a <= b:
        a = b
print("Ваше число:", number1)
print("Количество элементов в числе", len(number1))
print("Максимальное число:", a)

# Задание 5.
viruchka = int(input("Введите выручку: "))
izderzki = int(input("Введите издержки: "))
if viruchka > izderzki:
    print("Фирма работает с прибылью.")
    pribil = viruchka - izderzki
    rent = pribil/viruchka
    print("Рентабельность выручки: ", rent)
    chisl = int(input("Введите численность сотрудников: "))
    prib_s = pribil / chisl
    print("Прибыль фирмы в расчете на одного сотрудника: ", prib_s)
else:
    print("Фирма работает с убытками.")


