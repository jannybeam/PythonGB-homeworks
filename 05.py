class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Lets drrawing!')

class Pen(Stationery):

    def draw(self):
        print(f'Lets draw with a pen {self.title}')

class Pencil(Stationery):

    def draw(self):
        print(f'Lets draw with a pencil {self.title}')

class Handle(Stationery):

    def draw(self):
        print(f'Lets draw with a handle {self.title}')

pen = Pen('A')
pencil = Pencil('B')
handle = Handle('C')

for sth in (pen, pencil, handle):
    sth.draw()

