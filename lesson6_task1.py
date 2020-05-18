import time


class LightColor:
    def __init__(self, color: str, delay: int):
        self.color = color
        self.delay = delay
        self.next_color = self

    def set_next_color(self, color):
        self.next_color = color


class TrafficLight:
    def __init__(self):
        self.__red_color = LightColor('красный', 7)
        self.__yelow_color = LightColor('желтый', 2)
        self.__green_color = LightColor('зеленый', 5)
        self.__red_color.set_next_color(self.__yelow_color)
        self.__yelow_color.set_next_color(self.__green_color)
        self.__green_color.set_next_color(self.__yelow_color)
        self.__cur_color = self.__red_color

    def running(self):
        #print(f'Горит {self.__cur_collor.collor}')
        #print(f'{self.__cur_color.color}, следующий {self.__cur_color.next_color}' )
        for i in range(self.__cur_color.delay, 0, -1):
            print(f'\rГорит {self.__cur_color.color}  {i} sec ', end='')
            #sys.stdout.write(f'{i} sec \r')
            #sys.stdout.flush()
            time.sleep(1)
        if self.__cur_color is self.__green_color:
            self.__yelow_color.set_next_color(self.__red_color)
        elif self.__cur_color is self.__red_color:
           #print(f'###########{type(self.__yelow_color)}')
            self.__yelow_color.set_next_color(self.__green_color)
        self.__cur_color = self.__cur_color.next_color
        self.running()


traffic_light = TrafficLight()
traffic_light.running()
#задачу со звездочкой делать не буду ибо непонятно как тут вообще может что-то сбиться
#в теории кто-то может поменять значение приватной переменной, в этом случае мы не сможем гарантировать корректную логику проверяющей функции