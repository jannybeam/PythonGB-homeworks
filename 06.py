def int_func(text):
    word = text[0].upper() + text[1:].lower()
    return word

string = input('Enter a few words separated by a spase: ')
for word in string.split(' '):
    print(f'{int_func(word)} ', end = ' ')