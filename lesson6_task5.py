class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Корявенький такой рисунок, как курица лапой. Ктож ручкой рисует?')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Ни штриха больше! Это шедевр!')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Засох 0_о')

list = [Pen('ручка'), Pencil('Карандаш'), Handle('Маркер')]
for peace in list:
    peace.draw()

