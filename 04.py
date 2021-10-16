class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go!')

    def stop(self):
        print('Stop!')

    def turn(self, direction):
        print(f'The car turned to {direction}')

    def show_speed(self):
        print(f'Current speed is {self.speed}')

class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Over speed!')

class SportCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Over speed!')

class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Over speed!')

class PoliceCar(Car):

     def __init__(self, speed, color, name):
         super().__init__(speed, color, name, True)

town = TownCar(80, 'black', 'Town')
sport = SportCar(120, 'red', 'Sport')
work = WorkCar(40, 'white', 'Work')
police = PoliceCar(110, 'blue', 'Police')

town.show_speed()
work.show_speed()

town.speed = 70
town.turn('right')

work.speed = 20
work.turn('left')
work.stop()

police.turn('on the Main street')