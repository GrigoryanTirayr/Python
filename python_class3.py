from __future__ import print_function


class Vehicle(object):

    def __init__(self, name, max_speed, *args, **kwargs):
        self.name = name
        self.max_speed = max_speed
        super().__init__(*args, **kwargs)
    
    def present(self):
        return 'Vehicle {} end speed {}'.format(self.name, self.max_speed)


class SportCar(Vehicle):

    # def __init__(self, name, max_speed, competition_type):
    def __init__(self, competition_type, *args, **kwargs):
        # Vehicle.__init__(self, name, max_speed)
        print('in class Sport Car', args, kwargs)
        self.competition_type = competition_type
        super().__init__(*args, **kwargs)
        # self.competition_type = competition_type


class Bus(Vehicle):
    # def __init__(self, name, max_speed, seats_amount):
    def __init__(self, seats_amount, *args, **kwargs):
        # Vehicle.__init__(self, name, max_speed)
        # self.name = "Bus"
        # super().__init__(name, max_speed)
        # super(Bus,self).__init__(name, max_speed)
        self.seats_amount = seats_amount
        print('in class Sport Car', args, kwargs)
        super(Bus, self).__init__(*args, **kwargs)
        # self.seats_amount = seats_amount

    def present(self):
        return f'{super().present()} and seats amount is {self.seats_amount}'


class Largebus(Bus):
    pass


class SporteBus(Bus, SportCar):
    def __init__(self, sb_name, *args, **kwargs):
        self.sb_name = sb_name
        print('sportbus', args, kwargs)
        super().__init__(*args, **kwargs)


sport_car = SportCar("ferrari", 300, "F1")
bus_1 = Bus('Volvo', 140, 12)
sb_1 = SporteBus('FerrariBus', 18, 'Bus camp', "Bus", 160)


# print(sport_car.present())
# print(bus_1.present())
# print(Largebus.__mro__)
# print(SporteBus.__mro__)


# tuple_1 = (1,2,3)
# kwargs = dict(
#     sep='-----', 
#     end ='fsafasfasf\n'
#     )
# print(tuple_1, sep='\n')
# print(*tuple_1, sep='\n')
# print(*tuple_1, kwargs)
# print(*tuple_1, **kwargs)
# print('hello')