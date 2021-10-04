def data (name, surname, year, city, email, phone):
    print(f'{name} {surname} {year} {city} {email} {phone}')

n = input('Name: ')
s = input('Surname: ')
y = input('Year: ')
c = input('City: ')
e = input('Email: ')
p = input('Phone: ')

data(name=n, surname=s, year=y, city=c, email=e, phone=p)