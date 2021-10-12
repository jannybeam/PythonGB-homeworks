with open('test_three.txt') as file:
    file_lines = file.readlines()
    employees = {}
    sum_salary = 0
    for line in file_lines:
        empl_data = line.split()
        employees.update({empl_data[0]: float(empl_data[1])})
        sum_salary += float(empl_data[1])
average_salary = sum_salary / len(employees)
print(f'Average = {average_salary}')

for a, b in employees.items():
    if b < 20000:
        print(f'{a}: {b}')

