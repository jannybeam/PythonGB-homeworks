earnings = int(input('Proceeds: '))
costs = int(input('Costs: '))

if earnings > costs:
    print('Profit')
    profitability = (earnings - costs) / earnings
    print (f'Profitability: {profitability}')
    num_of_employees = int(input('Number of employees: '))
    profit_per_employee = (earnings - costs) / num_of_employees
    print(f'Profit per employee: {profit_per_employee}')
elif earnings < costs:
    print(f'Waste.')