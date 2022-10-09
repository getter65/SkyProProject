# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, name, x_coord, y_coord):
        self.speed = 1
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord

    def speedway(self):
        if self.name == 'is_fly':
            self.speed *= 1.2
        if self.name == 'crawl':
            self.speed *= 0.5

    def move(self, field,  direction):
        if direction == 'UP':
            new_y = self.y_coord + self.speedway()
            new_x = self.x_coord
        elif direction == 'DOWN':
            new_y = self.y_coord - self.speedway()
            new_x = self.x_coord
        elif direction == 'LEFT':
            new_y = self.y_coord
            new_x = self.x_coord - self.speedway()
        elif direction == 'RIGTH':
            new_y = self.y_coord
            new_x = self.x_coord + self.speedway()


        field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
