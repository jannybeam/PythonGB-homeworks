class Warehouse:

    def __init__(self, equipments=None):
        if not equipments:
            equipments = []
        self.equipments = equipments

    def add_equipment(self, equipment, office):
        if office.return_equipment(equipment):
            self.equipments.append(equipment)
        else:
            print('Equipment is not add')

    def get_equipment(self, equipment, office):
        if equipment in self.equipments:
            self.equipments.remove(equipment)
            office.add_equipment(equipment)
        else:
            print('Equipment is not found')


class Office:

    def __init__(self, name, equipments=None):
        if not equipments:
            equipments = []
        self.equipments = equipments
        self.name = name

    def add_equipment(self, equipment):
        self.equipments.append(equipment)

    def return_equipment(self, equipment):
        if equipment in self.equipments:
            self.equipments.remove(equipment)
            return True
        else:
            return False


class OfficeEquipment:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f'{self.name, self.quantity}'

    def add_equipment():
        try:
            name = input(f'Print name: ')
            quantity = int(input(f'Print quantity: '))
            return name, quantity
        except ValueError:
            print('Invalid Value')


class Printer(OfficeEquipment):
    def __init__(self, name, quantity):
        super(Printer, self).__init__(name, quantity)
        self.color = 'white'



class Scanner(OfficeEquipment):
    def __init__(self, name, quantity):
        super(Scanner, self).__init__(name, quantity)
        self.scan_resolution = 'high'


class Xerox(OfficeEquipment):
    def __init__(self, name, quantity):
        super(Xerox, self).__init__(name, quantity)
        self.wifi = True



printer_1 = Printer('Samsung', 1)
printer_2 = Printer('Cannon', 1)
printer_3 = Printer.add_equipment()
scanner_1 = Scanner('HP', 1)
scanner_2 = Scanner('Dell', 1)
xerox_1 = Xerox('Xerox', 1)

warehouse_1 = Warehouse([printer_1])
office_1 = Office('design', [scanner_2])
office_2 = Office('it', [xerox_1])

print(printer_3)

print(warehouse_1.equipments)
print(office_1.equipments)

print(office_2.equipments)
warehouse_1.get_equipment(printer_1, office_2)
print(warehouse_1.equipments)
print(office_2.equipments)