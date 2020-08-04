# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
# светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}')

            if TrafficLight.__color[i] == 'Красный':
                sleep(7)
            elif TrafficLight.__color[i] == 'Желтый':
                sleep(5)
            elif TrafficLight.__color[i] == 'Зеленый':
                sleep(1)
            i += 1

traffic_l = TrafficLight()
traffic_l.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного
# полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, _length, _width):
        self._length = int(_length)
        self._width = int(_width)

    def count_road(self, param1=25, param2=5):
        self.param1 = int(param1)
        self.param2 = int(param2)
        result = int(self._length * self._width * self.param1 * self.param2/1000)
        print(f'Need {result} ton for the building')

road1 = Road(20, 5000)
road1.count_road()

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать
# методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income
    def method_worker(self):
        pass
class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)
    def get_full_name(self):
        print(f'Worker {self.name} {self.surname}')
        full_income = int(self._income['wage']) + int(self._income['bonus'])
        print(f'Full worker income: {full_income}')

worker_income = {"wage": 20000, "bonus": 10000}
worker_Position = Position('Ivan', 'Ivanov', 'manager', worker_income)
worker_Position.get_full_name()




# # 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# # speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# # которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# # Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# # Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# # Для классов TownCar и WorkCar переопределите метод show_speed.
# # При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
    def method_go(self):
        print(f'Car {self.name} go.')
    def method_stop(self):
        print(f'Car {self.name} stop.')
    def method_turn(self, direction):
        self.direction = direction
        print(f'Car {self.name} tern {direction}.')
    def show_speed(self):
        print(f'Speed {self.name} car {self.speed} km/hour.')

class TownCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'TownCar {self.name} speed {self.speed} km/hour. Over speed')
        else:
            print(f'Speed of {self.name} is normal for town car')

class SportCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
    def method_sportcar(self):
        print(f'Car {self.name} is SportCar.')

class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
    def show_speed(self):
        if self.speed > 40:
            print(f'WorkCar {self.name} speed {self.speed} km/hour. Over speed')
        else:
            print(f'Speed of {self.name} is normal for work car')

class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
    def method_policecar(self):
        if self.is_police == True:
            print(f'Car {self.name} is PoliceCar.')

base_car = Car(100, 'red', 'Nissan', False)
town_car = TownCar(80, 'black', 'Ford', False)
work_car = WorkCar(90, 'white', 'Toyota', False)
sport_car = SportCar(150, 'silver', 'Ferrari', False)
police_car = PoliceCar(110, 'white', 'Lada', True)

base_car.method_go()
base_car.method_stop()
base_car.method_turn('left')
base_car.show_speed()
town_car.show_speed()
work_car.show_speed()
sport_car.method_sportcar()
police_car.method_policecar()

# # # 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# # # title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# # # Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом
# # # из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# # # выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# # # метод для каждого экземпляра.
# #
class Stationery:

    def __init__(self, title):
        self.title = title

    def method_drow(self):
        return f'Start drow {self.title}.'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def method_drow(self):
        return f'Start drow {self.title}.'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def method_drow(self):
        return f'Start drow {self.title}.'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def method_drow(self):
        return f'Start drow {self.title}.'

stationery_st = Stationery('stationery')
pen_st = Pen('pen')
pencil_st = Pencil('pencil')
handle_st = Handle('handle')
print(stationery_st.method_drow())
print(pen_st.method_drow())
print(pencil_st.method_drow())
print(handle_st.method_drow())



