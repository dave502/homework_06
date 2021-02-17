
from time import sleep


class TrafficLight:
    __color = None

    # метод запускает один цикл смены цветов
    def running(self):

        pause_time = (7, 2, 6)
        colors = ('red', 'yellow', 'green')

        for i in range(3):
            # меняем цвет
            self.__color = colors[i]
            # выводим цвет
            print(f'\n color "{self.__color}"', end=' ')
            # для наглядости выводим время посекундно
            for second in range(pause_time[i]):
                print(f" {second + 1}", end=' ')
                sleep(1)


traffic_light = TrafficLight()
traffic_light.running()
