class SkladOperationError(Exception):
    def __init__(self, txt):
        self.txt=txt

class Sklad:
    def __init__(self):
        self.__list_prduction=[]
        self.__otdel_list=set()

    def __str__(self):
        result = 'На склае лежит: \n'
        for prod in self.__list_prduction:
            result=result+str(prod)+'\n'
        return result

    def add_orgtehnics(self, *orgtehics):
        for org in orgtehics:
            self.__list_prduction.append(org)

    def transfer_tehnic_to_otdel(self, orgtehnic, otdel):
        try:
            self.__list_prduction.remove(orgtehnic)
            otdel.push_tehnic(orgtehnic)
            self.__otdel_list.add(otdel)
        except SkladOperationError as e:
            print('нет такой техники на складе!')

    def recive_tehnic_from_otdel(self, orgtehnic, otdel):
        otdel.pull_tehnic(orgtehnic)
        self.__list_prduction.append(orgtehnic)

    def del_tehnic(self, orgtehnic):
        self.__list_prduction.remove(orgtehnic)

    def get_orgtehnics(self):
        return self.__list_prduction

    def print_report(self):
        result= str(self)
        for otdel in self.__otdel_list:
            result=result + f'Отдел: {otdel.name}: \n'
            for tehnic in otdel.list_tehinc():
                result=result+str(tehnic)+ '\n'
        return result

class Orgtehnic:
    def __init__(self, model, inv_number):
        self.model=model
        self.inv_number=inv_number
    def __str__(self):
        return self.name+ ' ' + self.model

class Printer(Orgtehnic):
    def __init__(self, model, inv_number, type):
        super().__init__(model, inv_number)
        self.type=type

    def __str__(self):
        return f'Принтер: {self.model}, инвентарный номер: {self.inv_number}, тип печати: {self.type} '

    def print(self, message):
        print(f'А вот тут я какбы печатаю: {message}')


class Scaner(Orgtehnic):
    def __init__(self, model, inv_number, type):
        super().__init__(model, inv_number)
        self.type = type

    def __str__(self):
        return f'Сканер: {self.model}, инвентарный номер: {self.inv_number}, тип устройства: {self.type} '

    def scan(self):
        print ('Сканируем....')


class Xserox(Orgtehnic):
    def __init__(self, model, inv_number):
        super().__init__(model, inv_number)


    def __str__(self):
        return f'Ксерокс: {self.model}, инвентарный номер: {self.inv_number}'

    def copy(self):
        print('Я ксерокс я не могу не ксеря!')

class Otdel:
    def __init__(self, name):
        self.name=name
        self.__tehnic_list=[]
    def pull_tehnic(self, tehnic):
        self.tehnic_list.remove(tehnic)
        return tehnic

    def push_tehnic(self, tehnic):
        self.__tehnic_list.append(tehnic)

    def list_tehinc(self):
        return self.__tehnic_list


class InputValueError(Exception):
    def __init__(self, txt):
        self.txt = txt


def check_correct_data(model, ser_num):
    if len(model)<3: return False
    if len(ser_num)<5: return False
    return True


#Демонстрация работы
scan1=Scaner('HP GP1270', 'qwer1', 'hand')
scan2=Scaner('HP FR1235', 'qweqw', 'dectop')
scan3=Scaner('Canon SR4680', 'qweqw', 'dectop')
printer1=Printer('HP LJ1250', 'dkdkccds32ds', 'Laser')
printer2=Printer('HP LJ3270', 'fsdfecd', 'Laser')
printer3=Printer('HP DJ1250', 'vdds', 'MFU')
xserox1=Xserox('xerox M638', 'SFKF75GT')
xserox2=Xserox('xerox M636', 'KLKJDOI')
xserox3=Xserox('xerox M635', 'FJKYD')


sklad=Sklad()
sklad.add_orgtehnics(scan1, scan2, scan3, printer1, printer2, printer3, xserox1, xserox2, xserox3)
print(sklad)
print(sklad.print_report())
otd_buh = Otdel('Бухгалтерия')
otd_it = Otdel('ИТ')
sklad.transfer_tehnic_to_otdel(scan1, otd_buh)
sklad.transfer_tehnic_to_otdel(printer2, otd_it)
print (f'отдали в бухгалтерию: {len(otd_buh.list_tehinc())}')
for org in otd_buh.list_tehinc():
    print(str(org))
print(sklad.print_report())

# С валидацией данных
try:
    type_org=int(input('Введите вид устройства: \n 1-сканер \n 2- принтер \n 3- сканер \n'))
    model_org=input('Введите модель устройства:')
    num_org=input('Введите серийный номер устройства:')
    if check_correct_data(model_org, num_org): InputValueError('Введены некорректные параметры устройства')
    if type_org==1 or type_org==2:
        num_org=input('Введите тип устройства:')
    obj_teh=None
    if type_org == 1:
        obj_teh = Scaner(model_org, model_org, num_org)
    elif type_org == 2:
        obj_teh = Printer(model_org, model_org, num_org)
    elif type_org == 3:
        obj_teh = Xserox(model_org, model_org)
    elif obj_teh==None: raise InputValueError('Устройство не создано')
    else:
        raise InputValueError('Введен некорректный тип устройства')
    print(f'Устройство {str(obj_teh)} добавлено на склад')
    sklad.add_orgtehnics(obj_teh)
except InputValueError as e:
    print(e)
except ValueError as e:
    print ('Вы ввели некорректный тип устройства!')
print(sklad.print_report())
