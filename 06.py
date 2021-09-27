distance = float(input("The first day distance: "))
goal = float(input("Goal: "))
days = 1
while distance < goal:
    distance *= 1.1
    days += 1
print(f'Days: {days}')