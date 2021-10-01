users_list = input('Words: ')

words = users_list.split()
for num, word in enumerate(words):
    print(f'#{num} - {word[:10]}')