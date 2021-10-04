def my_func(a, s, d):
    sum_nums = a + s + d
    return sum_nums - min((a, s, d))

a = int(input('a: '))
s = int(input('s: '))
d = int(input('d: '))
print(my_func(a, s, d))