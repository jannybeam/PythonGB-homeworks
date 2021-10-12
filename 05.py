import random

with open('test_five.txt', 'w') as file:
    for _ in range(21):
        file.write(f'{random.randint(1, 11)}')

with open('test_five.txt') as file:
    nums = file.read().split()
    sum_nums = 0
    for num in nums:
        sum_nums += int(num)

print(sum_nums)