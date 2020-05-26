class InputDigitError(Exception):
    def __init__(self, txt):
        self.txt = txt
class DigiPrinter:
    def __init__(self):
        self.result_list=[]

    def print_result(self):
        print(f'Финальный список: {self.result_list}')

    def get_new_digit(self):
        try:
            digit = input('Веедите новое число или stop:')
            if digit == 'stop':
                self.print_result()
            elif digit.isdigit():
                self.result_list.append(digit)
                self.get_new_digit()
            else:
                raise InputDigitError('И никакая это не цифра!')
        except InputDigitError as e:
            print (e)
            self.get_new_digit()

dp=DigiPrinter()
dp.get_new_digit()