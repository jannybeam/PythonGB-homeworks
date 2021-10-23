class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_str_to_int(cls, date):
        day, month, year = [int(i) for i in date.split('.')]
        return f'{day}\n{month}\n{year}'

    @staticmethod
    def test_date(date):
        day, month, year = [int(i) for i in date.split('.')]
        if 0 < month < 13:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if 0 < day < 32:
                    return True
            elif month == 2:
                if 0 < day < 29:
                    return True
            else:
                if 0 < day < 31:
                    return True
        return False

print(Date.date_str_to_int('21.10.2021'))
print(Date.test_date('30.04.2021'))