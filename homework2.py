class Circle:

    def __init__(self, radius, pi):
        self.radius = None
        if not isinstance(radius, int):
            raise TypeError('Circle Radius sides , use be inteegers or floats')
        self.radius = radius
        self.pi = pi

    def area(self):
        return f'circle radus = {self.radius} pi = {self.pi}  area = pi*r^2 ={self.pi * pow(int(self.radius), 2)}'

    def perimeter(self):
        return f'circle radus = {self.radius} pi = {self.pi}  perimeter = 2 *pi*r ={int(2*self.pi * int(self.radius))}'


radius_1 = Circle(int(input('give Radius parameter')), 3.14)
print(radius_1.area())
print(radius_1.perimeter())

class Human:

    def __init__(self, name, lastname, age, height):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.height= height

    def hundrid_years(self):
        self.age = int(self.age)
        return f'your age {self.age} you be 100 yers from {(2022-self.age)+100}'

    def optimal_weight(self):
        self.age = int(self.age)
        self.height = int(self.height)
        return 'dzer tariqn e {} dzer boy {}  dzer optimal qashy klini {}'.format(self.age, self.height, int(50 + (self.height - 150) * 0.32 + (self.age - 21) / 5))

    def present(self):
        return f'your name {self.name}\nyour lastname {self.lastname}\nyour age{self.age}\nyour heighe{self.height}\nyour optimal weight{int(50 + (self.height - 150) * 0.32 + (self.age - 21) / 5)}\ndu kdrnas 100 tarekan{(2022-self.age)+100}'


human = Human(input('your name'), input('your lastname'), input('your age'), input('your height'))
print(human.hundrid_years())
print(human.optimal_weight())
print(human.present())
print('hello')