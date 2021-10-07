from functools import reduce
num_list = [c for c in range(100, 1001) if c % 2 == 0]
print(reduce(lambda d, e: d * e, num_list))