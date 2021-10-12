nums = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре",
}

with open('test_four.txt') as file, open('new_04.txt', 'w') as new_04:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        rus_nums = nums.get(data[0])
        new_04.write(f'{line.replace(data[0], rus_nums)}')
