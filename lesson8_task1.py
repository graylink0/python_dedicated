class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def parse_to_int(cls, date):
        list_date=date.date.split('-')
        int_date = int(''.join(map(str.capitalize, list_date)))
        return int_date

    @staticmethod
    def check_date(date):
        list_date = date.date.split('-')
        if int(list_date[0])<0 or int(list_date[0])>59: return False
        elif int(list_date[1]) < 1 or int(list_date[1]) > 12: return False
        elif int(list_date[2]) < 1900 or int(list_date[2]) > 2099: return False
        else: return True

    def __str__(self):
        return str(self.date)

list_date= [Date('01-01-2020'), Date('01-13-2020'), Date('01-13-3020')]
for date in list_date:
    print(f'date: {date}', end='\t')
    print(f'type: {type(Date.parse_to_int(date))}  int_value:{Date.parse_to_int(date)}, check: {Date.check_date(date)}')
