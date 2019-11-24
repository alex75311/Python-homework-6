'''
Реализуйте базовый класс ​ Car​ . У данного класса должны быть следующие атрибуты: ​ speed​ ,
color​ , ​ name​ , ​ is_police ​ (булево). А также методы: ​ go​ , ​ stop​ , ​ turn(direction)​ , которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: ​ TownCar​ , ​ SportCar​ , ​ WorkCar​ , ​ PoliceCar​ . Добавьте в базовый класс метод
show_speed​ , который должен показывать текущую скорость автомобиля. Для классов
TownCar ​ и ​ WorkCar ​ переопределите метод ​ show_speed​ . При значении скорости свыше 60
(​ TownCar​ ) и 40 (​ WorkCar​ ) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат
'''


class Car:
    def __init__(self, speed=0, color='red', name='car-car'):
        self.speed = speed
        self.my_speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Машина поехала')
        self.my_speed = self.speed

    def stop(self):
        print(f'Машина остановилась')
        self.my_speed = 0

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.my_speed}')

    def show_police(self):
        print(f'Это{" не" if not self.is_police else ""} полицейская машина')


class TownCar(Car):
    def show_speed(self):
        if self.my_speed > 60:
            print(f'Скорость машины {self.my_speed}, что превышает 60км\ч')
        else:
            print(f'Скорость машины {self.my_speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.my_speed > 40:
            print(f'Скорость машины {self.my_speed}, что превышает 40км\ч')
        else:
            print(f'Скорость машины {self.my_speed}')


class PoliceCar(Car):
    def __init__(self, speed=0, color='red', name='police-car'):
        super().__init__(speed, color, name)
        self.is_police = True


a = TownCar(40, 'black', 'Town1')
print(a.name)
a.go()
a.show_speed()
a.stop()
a.show_speed()

b = TownCar(70, 'blue', 'Town2')
print(b.name)
b.go()
b.show_speed()
b.stop()
b.show_police()

c = PoliceCar(90, 'blue')
print(c.name)
c.show_police()
c.show_speed()
c.turn('налево')
