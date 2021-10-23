class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

def append_number():
    stop = True
    number_list = []
    while stop == True:
        num = input('Wright a number excluding another symbols: ')
        if num == 'stop':
            return number_list
            break

        else:
            try:
                number_list.append(float(num))
            except:
                print(f'You print sth not a number')

print(append_number())