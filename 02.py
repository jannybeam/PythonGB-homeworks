class ZeroExeption(Exception):

    def __init__(self, txt):
        self.txt = txt

def divide_nums():
    try:
        num_1 = int(input('num_1: '))
        num_2 = int(input('num_2: '))
        if num_2 == 0:
            raise ZeroExeption('Cannot be divided by zero! Try again!')
        else:
            return num_1 / num_2
    except ZeroExeption as error:
        return error

print(divide_nums())