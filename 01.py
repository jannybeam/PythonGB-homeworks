with open('test_one.txt', 'w') as file:
    user_str = input('Text :\n')
    while user_str:
        file.write(f'{user_str}\n')
        user_str = input('Text :\n')