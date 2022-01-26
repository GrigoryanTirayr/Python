# 1
class Country(object):
    def __init__(self, country_name, continent, *args, **kwargs):
        self.country_name = country_name
        self.continent = continent
        print('Country', args, kwargs)
        super().__init__(*args, **kwargs)

    def count_ret(self):
        return f'This is a continent {self.continent} and Country {self.country_name}'


class Brand(object):
    def __init__(self, bra_name, busin_start_dat, *args, **kwargs):
        self.bra_name = bra_name
        self.busin_start_dat = busin_start_dat
        print('Brand', args, kwargs)

        super().__init__(*args, **kwargs)
    
    def bran_present(self):
        return f'Brand name is a {self.bra_name} prsentation Date {self.busin_start_dat}'
        

class Season(object):
    def __init__(self, sea_name, ave_temperature, *args, **kwargs):
        self.sea_name = sea_name
        self.ave_temperature = ave_temperature
        print('Season', args, kwargs)

        super().__init__(*args, **kwargs)
    
    def season_pres(self):
        return f'this presentation is a {self.sea_name} and temperature is a {self.ave_temperature}'


class Product(Country, Brand, Season):
    def __init__(self, pro_name, pro_type, pro_price, pro_quatity, *args, **kwargs):
        self.pro_name = pro_name
        self.pro_type = pro_type
        self.pro_price = pro_price
        self.pro_quatity = pro_quatity
        super().__init__(*args, **kwargs)
        print(args, kwargs)
        print(f'Product name {self.pro_name} Product Type {self.pro_type} product price '
              f'{self.pro_price} product qutity{self.pro_quatity}')

    def price_precent(self):
        price = int(input('ichqan eq  uzum ijecnel'))
        return f'your product price {self.pro_price} product precente {price} product price now ' \
               f'{self.pro_price-self.pro_price * (price/100)}'

    def increas_quantity(self):
        quat = int(input('how quatity increas?'))
        self.quat = quat
        self.quat = quat + self.pro_quatity
        return f'your quatity {self.pro_quatity} you add quatity {quat} all quatity {self.quat}'

    def discount_quantity(self):
        qanak = int(input('how quatity discount ?'))
        return f'your quatity {self.quat} you add quatity {qanak} all quatity {self.quat -qanak}'


print(Product.__mro__)
pro_1 = Product("Compyuter", "Gaming", 1200000, 50, "Armenia", "Evrasia", "Dell", "26.01.2022", "Dzmer", "-25 C")
print(pro_1.count_ret())
print(pro_1.bran_present())
print(pro_1.season_pres())
print(pro_1.price_precent())
print(pro_1.increas_quantity())
print(pro_1.discount_quantity())
# 2

# class Hotel:
#     def __init__(self, hotel_name, hotel_place, *args, **kwargs):
#         self.hotel_name = hotel_name
#         self.hotel_place = hotel_place

# class Taxi:
#     def __init__(self, taxi_name, taxi_type, price_for_tour, *args, **kwargs):
#         self.taxi_name = taxi_name
#         self.taxi_type = taxi_type
#         self.price_for_tour = price_for_tour

# class Tour(Hotel, Taxi):
#     def __init__(self, tour_name, *args, **kwargs):
#         pass
