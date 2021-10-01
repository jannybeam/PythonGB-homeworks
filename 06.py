goods = []
counter = 1
command = ''

while command != 'stop':
    product = input('product: ')
    prise = input('pries: ')
    amount = input('amount: ')
    units = input('units: ')
    goods.append(
        (counter, {'product': product, 'prise': prise, 'amount': amount, 'units': units})
    )
    counter += 1
    command = input("Write 'stop' to stop inputing: ")

final_list = {}
for numb, good_dict in goods:
    for key, value in good_dict.items():
        if not final_list.get(key):
            final_list[key] = [value]
        else:
          final_list[key].append(value)

for key, value in final_list.items():
    final_list[key] = list(set(value))

print(final_list)

