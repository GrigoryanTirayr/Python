class Anun:
    def __init__(self, name, lastname):

        self.name = name
        self.lastname = lastname

    def las_nam(self):
        return f'your name {self.name}  and lastname {self.lastname}'


nam = Anun('Tirayr', 'Grigoryan')
print(nam.las_nam())


# class Erankyun:
#     def __init__(self,x,y,z,x_1,y_1,z_1):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.x_1 = x_1
#         self.y_1 = y_1
#         self.z_1 = z_1
    
#     def paragic_1(self):
#         return f'yerankyan x koxmy = {self.x} \nyerankyan x koxmy = {self.y} \nyerankyan x koxmy = {self.z} \ne
#         rankyan pragicy havasr e = {int(self.x) +int(self.y)+int(self.z)}'

#     def paragic_2(self):
#         return f'yerankyan x koxmy = {self.x_1} \nyerankyan x koxmy = {self.y_1} \nyerankyan x koxmy = {self.z_1} \n
#         erankyan pragicy havasr e = {int(self.x_1) +int(self.y_1)+int(self.z_1)}'

#     def Hamematutyun(self):
#         arjeq=0
#         arajin=[self.x,self.y,self.z]
#         erkrord=[self.x_1,self.y_1,self.z_1]
#         for i in arajin:
#             for j in erkrord:
#                 if i == j:
#                     arajin.remove(i)
#                     arjeq += 1
#         if arjeq == 3: 
#             return f'duq uneq hamynknum{arjeq} erankyunnery nman en '
#         else:
#             return f'erankyunnery nman chen'


# erank_1 = Erankyun(input('x'), input('y'), input('z'), input('2- i x'), input('2 - iy'), input('2-i z'))
# print(erank_1.paragic_1())
# print(erank_1.paragic_2())
# print(erank_1.Hamematutyun())


class Erankyun(object):

    def __init__(self, x, y, z):
        self.set_height = None
        if not isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
            raise TypeError('Erankyuny sides ,ust be inteegers or floats')

        self.x = x
        self.y = y
        self.z = z

    def to_list(self):
        return sorted((self.x, self.y, self.z))

    def is_alike(self, other_erankyun):
        # if type(other_erankyun) is not Erankyun:
        if not isinstance(other_erankyun, Erankyun):
            raise TypeError(f'{other_erankyun}is  not ')
        first_list = self.to_list()
        second_list = other_erankyun.to_list()
        return first_list[0]/second_list[0] == first_list[1]/second_list[1] == first_list[2]/second_list[2]

    def hamematel(self, other_erankyun):
        first_list = self.to_list()
        second_list = other_erankyun.to_list()
        if first_list[0] <= second_list[0]:
            if first_list[1] <= second_list[1]:
                if first_list[2] <= second_list[2]:
                    return 'hnaravor e '
                else:
                    return 'hnaravor che'
            else:
                return 'hnaravor che'
        else:
            return 'hnaravor che'

    def set_height(self, height):
        if not isinstance(height, (int,float)):
            raise TypeError(f'{height} is not an instnce ingers or float')
        self.set_height = height


    # def Hamematutyun(self):
    #     arjeq=0
    #     arajin=[self.x,self.y,self.z]
    #     erkrord=[self.x_1,self.y_1,self.z_1]
    #     for i in arajin:
    #         for j in erkrord:
    #             if i == j:
    #                 arajin.remove(i)
    #                 arjeq += 1
    #     if arjeq == 3: 
    #         return f'duq uneq hamynknum{arjeq} erankyunnery nman en '
    #     else:
    #         return f'erankyunnery nman chen'


erank_1 = Erankyun(5, 6, 7)
erank_2 = Erankyun(5, 6, 7)

# print(erank_1.Hamematutyun())
print(erank_1.to_list(), erank_2.to_list())
print(erank_1.is_alike(erank_2))
print(erank_1.hamematel(erank_2))

class RectTriangle(Erankyun):
    pass