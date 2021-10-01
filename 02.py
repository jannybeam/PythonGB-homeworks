fill_the_list = input('list: ')

input_list = fill_the_list.split()

len_list = len(input_list)

a = 0
if len_list > 1:
    while a < len_list - 1:
        input_list[a], input_list[a + 1] = input_list[a + 1], input_list[a]
        a += 2

print(input_list)