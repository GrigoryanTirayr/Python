
# class Car:
#     car_type = 'sport'
#     model = 'BMW'
#     prod_year = 1960


# print(Car.car_type, Car.model, Car.prod_year)
# # print(Car)


class Car:
    NAME = 'Class Car'

    def __init__(self, name, color, year):
        self.car_name = name
        self.color = color
        self.year = year

    def present(self):
        print(self.car_name, self.year, self.color)

    def change_year(self, new_year):
        if type(new_year) is int:
            self.year = new_year
        else:
            raise ValueError(f'{new_year} is not integer')


car_1 = Car('Bmw x5', 'white', 2022)
car_2 = Car('Mercedes', 'Red', 2021)
# print(car_1.car_name, car_1.color, car_1.year)
# print(car_2.car_name, car_2.color, car_2.year)
# print(car_1.__dict__)
# print(Car.NAME)
# print(car_2.NAME)
# print(car_1.NAME)
# car_2.year = 2011
# print(car_2.__dict__)

car_1.present()
car_2.present()
Car.present(car_1)
Car.present(car_2)
car_3 = Car('audi', 'black', 2013)
Car.present(car_3)
car_3.model = 'a6'
print(car_3.__dict__)

Car.type = 'sport'
print(car_1.type)
car_1.type = 'common'
print(car_2.type)
car_1.change_year(2012)
print(car_1.__dict__)