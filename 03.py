class Cell:

    def __init__(self, nums):
        self.nums = nums

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        diff = self.nums - other.nums
        if diff >= 0:
            return Cell(diff)
        else:
            print('DiffError')

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __truediv__(self, other):
        return Cell(self.nums // other.nums)

    def make_order(self, number):
        a = ''
        for b in range(self.nums // number):
            a += '*' * number + '\n'
        a += '*' * (self.nums % number) + '\n'
        return  a

    def __str__(self):
        return f'{self.nums}'

cell = Cell(18)
print(cell.make_order(10))
cell_2 = Cell(11)
print(cell_2.make_order(7))

print(cell + cell_2)
print(cell - cell_2)
print(cell * cell_2)
print(cell / cell_2)
print(cell_2 - cell)
