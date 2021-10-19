from random import randint

class Matrix:

    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        a = ''
        for b in range(len(self.nums)):
            for c in range (len(self.nums[b])):
                a += f'{self.nums[b][c]:2} '
            a += '\n'
        return a

    def __add__(self, other):
        nums = [
            [self.nums[b][c] + other.nums[b][c] for c in range(len(self.nums[b]))]
                for b in range(len(self.nums))]
        return Matrix(nums)

e = Matrix([[randint(0, 6) for _ in range(8)] for _ in range(6)])
f = Matrix([[randint(0, 6) for _ in range(8)] for _ in range(6)])

print(e)
print(f)
print(e + f)