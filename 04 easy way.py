def my_func(x, y):
    """Fourth case easy way"""
    if x < 0:
        return '(x) must be greater then 0'
    if y > 0:
        return '(y) must be less then 0'
    else:
        return x ** y

x = int(input('Enter a positive number (x): '))
y = int(input('Enter a negative number (y): '))
print(my_func(x, y))