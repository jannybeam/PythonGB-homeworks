def my_func(x, y):
    if x < 0:
        return '(x) must be greater then 0'
    if y > 0:
        return '(y) must be less then 0'
    a = 1
    for i in range (y * -1):
        a *= x
    return 1/z

x = int(input('Enter a positive number (x): '))
y = int(input('Enter a negative number (y): '))
print(my_func(x, y))