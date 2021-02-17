from random import randint


# родительский класс
class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print(f'машина повернула {direction}')

    def show_speed(self):
        print(f'текущая скорость машины: {self.speed} км/ч')


# дочерние классы
class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'превышение скорости на  {self.speed - 60} км/ч!')


class SportCar(Car):
    team = None

    def set_team(self, team):
        self.team = team

    def get_team(self, team):
        return self.team


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'превышение скорости на  {self.speed - 40} км/ч!')


class PoliceCar(Car):
    # переопределяем конструктор, чтобы is_police всегда = True
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


# создаём объекты классов
town_car = TownCar(80, 'white', 'Lada')
sport_car = SportCar(290, 'red', 'Ferrari')
work_car = WorkCar(30, 'yellow', 'Bobcat')
police_car = PoliceCar(180, 'blue', 'Chevrolet')

# добавляем объекты в список и вызываем методы каждого элемента списка
cars = [town_car, sport_car, work_car, police_car]
directions = ('прямо', 'налево', 'направо')

for car in cars:
    print(f'машина {car.name} цвета {car.color}'
          f' ({" не " if not car.is_police else " "}полицейская )')
    car.go()
    car.show_speed()
    # поворачиваем в случайном направлении
    car.turn(directions[randint(0, len(directions)-1)])
    print('\n')
