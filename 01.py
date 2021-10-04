def my_function(k_1, k_2):
    if k_2 == 0:
        return "Impossible"
    else:
        return k_1 / k_2

k_1 = int(input('k_1: '))
k_2 = int(input('k_2: '))
print(my_function(k_1, k_2))
