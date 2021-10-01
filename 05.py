rating_list = [8, 4, 3, 3, 4, 2, 5, 5, 6, 7, 1]

rating = int(input('Enter number: '))
inserted = False
for index, number in enumerate(rating_list):
    if rating > number:
        rating_list.insert(index, rating)
        inserted = True
        break

if not inserted:
    rating_list.append(rating)

print(rating_list)