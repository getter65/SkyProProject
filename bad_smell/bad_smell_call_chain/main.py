# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, room, population):
        self.room = room
        self.population = population

    def get_person_room(self):
        return self.room

    def get_city_population(self):
        return self.population


jack = Person(25, 1000000)
print(jack.get_person_room())
print(jack.get_city_population())

# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.