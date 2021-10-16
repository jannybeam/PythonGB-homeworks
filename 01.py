from time import sleep

class TrafficLight:
    color = ('red', 'yellow', 'green')
    timing = (4, 6, 8)

    def __init__(self):
        self.__color = 'red'

    def running(self):
        while True:
            for a in self.color:
                self.__color = a
                print(self.__color)
                sleep(self.timing[self.color.index(self.__color)])

traffic_light = TrafficLight()
traffic_light.running()