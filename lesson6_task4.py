from enum import Enum


class Car:
    colors = Enum('Color', 'red green yelow orange black blue')
    directions = Enum('Directions', 'лево право')

    def __init__(self, color: colors, name: str, is_police: bool = False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0

    def go(self, speed: int):
        self.speed = speed
        print(f'Машина двигается ао скростью {speed} км/час')

    def stop(self):
        self.speed = 0
        print(f'Ваш {self.name} остановился')

    def turn(self, direction: directions):
        print(f'Ваш {self.name} повернул на {direction.name}')

    def show_speed(self):
        print(f'текущая скорость вашего {self.name}: {self.speed} км/час')


class TownCar(Car):
    def __init__(self, color: Car.colors, name: str, is_police: bool = False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Внимание ваша скорость слишком высокая!')
            super().show_speed()


class SportCar(Car):
    def __init__(self, color: Car.colors, name: str, is_police: bool = False):
        super().__init__(color, name, is_police)


class WorkCar(Car):
    def __init__(self, color: Car.colors, name: str, is_police: bool = False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Внимание ваша скорость слишком высокая!')
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, color: Car.colors, name: str, is_police: bool = False):
        super().__init__(color, name, is_police)


town_car = TownCar(Car.colors.black, 'Пыжо')
sport_car = SportCar(Car.colors.red, 'Ferarri')
work_car = WorkCar(Car.colors.black, 'Рыно')
police_car = PoliceCar(Car.colors.blue, 'Ваз', True)
list_car = [town_car, sport_car, work_car, police_car]
for car in list_car:
    car.go(30)
    car.turn(Car.directions.лево)
    car.go(41)
    car.show_speed()
    car.turn(Car.directions.право)
    car.go(61)
    car.show_speed()
    car.stop()
