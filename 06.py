from itertools import cycle, count
a = 50
num_list = [b for b in range(5)]
count = count()
cycle = cycle(num_list)
print([next(count) for b in range(a)])
print([next(cycle) for b in range(a)])