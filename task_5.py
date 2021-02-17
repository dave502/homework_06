class Stationery:
    title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print('Пишет.')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print('Рисует.')


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print('Выделяет.')


stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

stationery_list = [stationery, pen, pencil, handle]
for obj in stationery_list:
    print(f'draw by {obj.title}: ')
    obj.draw()
