from abc import ABC, abstractmethod

class Clotches(ABC):

    @abstractmethod
    def get_loss_material(self):
        pass

class Coat(Clotches):
    def __init__(self, size: int):
        self.size = size
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size=size

    def get_loss_material(self):
        return self.size/0.5+0.5

class Costume(Clotches):
    def __init__(self, high):
        self.high = high
    @property
    def high(self):
        return self.__high

    @high.setter
    def high(self, high):
        self.__high = high

    def get_loss_material(self):
        return self.high*2+0.3


coat1=Coat(10)
coat2=Coat(20)
costume1=Costume(10)
costume2=Costume(20)
list_cloath=[coat1, coat2, costume1, costume2]
summ_loss_materials=0
for cloatch in list_cloath:
    summ_loss_materials = summ_loss_materials+cloatch.get_loss_material()
print(f'Всего ушло: {summ_loss_materials}')

