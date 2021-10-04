def num_func(num_str, stop):
    nums = num_str.split(' ')
    sum_list = 0
    for i in nums:
        if i == stop:
            break
        sum_list += int(i)
    return sum_list

stop_word = '!'
finish = False
a = 0
while not finish:
    user_nums = input('Enter numbers separated by a space: ')
    a += num_func(user_nums, stop_word)
    finish = stop_word in user_nums
    print(f'Sum = {a}')