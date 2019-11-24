'''
Создать класс ​ TrafficLight ​ (светофор) и определить у него один атрибут ​ color ​ (цвет) и метод
running ​ (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) ​ — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод
'''

from time import sleep


class TrafficLight():
    __color_arr = ['Red', 'Yellow', 'Green']
    _color = ''

    def running(self):
        for _ in range(0, 5):
            for el in self.__color_arr:
                self._color = el
                print(self._color)
                if self._color == 'Red':
                    sleep(7)
                elif self._color == 'Yellow':
                    sleep(2)
                else:
                    sleep(5)


t1 = TrafficLight()
t1.running()