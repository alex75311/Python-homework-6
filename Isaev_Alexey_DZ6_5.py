'''
Реализовать класс ​ Stationery ​ (канцелярская принадлежность). Определить в нем атрибут ​ title
(название) и метод ​ draw ​ (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса ​ Pen ​ (ручка), ​ Pencil ​ (карандаш), ​ Handle ​ (маркер). В каждом из классов
реализовать переопределение метода ​ draw​ . Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра
'''


class Stationery:
    def __init__(self, title=''):
        self.title = title

    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw():
        print('Запуск отрисовки ручки')


class Pencil(Stationery):
    def draw():
        print('Запуск отрисовки карандаша')


class Handle(Stationery):
    def draw():
        print('Запуск отрисовки маркера')


a = Stationery
a.draw()
b = Pen
b.draw()
c = Pencil
c.draw()
d = Handle
d.draw()
