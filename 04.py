num = int(input('Enter positive integer: '))
max = 0
while num > 0:
    if max < num % 10:
        max = num % 10
    num = num // 10
print(f"Max integer:{max}")