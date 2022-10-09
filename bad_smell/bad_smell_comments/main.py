# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def unit_movement(self, field, x, y, direction, is_unit_fly, is_unit_creep, unit_speed = 1):

        if is_unit_fly and is_unit_creep:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_unit_fly:
            unit_speed *= 1.2
            if direction == 'UP':
                new_y = y + unit_speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - unit_speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - unit_speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + unit_speed
        if is_unit_creep:
            unit_speed *= 0.5
            if direction == 'UP':
                new_y = y + unit_speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - unit_speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - unit_speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + unit_speed

            field.set_unit(x=new_x, y=new_y, unit=self)

