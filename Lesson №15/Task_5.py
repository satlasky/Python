import time


class TrafficLight:
    def __init__(self):
        self.__color = 'red'

    def running(self):
        while True:
            if self.__color == 'red':
                print('Red')
                time.sleep(1)
                self.__color = 'green'
            elif self.__color == 'green':
                print('Green')
                time.sleep(2)
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                print('Yellow')
                time.sleep(0.5)
                self.__color = 'red'


traffic_light = TrafficLight()
traffic_light.running()