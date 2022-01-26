class Dicit1:

    def __init__(self, name):

        self.name = name

    def stacox(self):

        dictonary_1 = {}
        dic_sarq = self.name
        for i in self.name:
            dictonary_1[i] = dictonary_1.get(i, 0) + 1

        print(f'my dictonary is a {dictonary_1}')
        
    def returns(self):

        dictonary_1 = {}
        dic_sarq = self.name
        for i in self.name:
            dictonary_1[i] = dictonary_1.get(i, 0) + 1

        temp = []
        res = dict()
        for key, val in dictonary_1.items():
            if val not in temp:
                temp.append(val)
                res[key] = val

        print(f'my dictonaryi is a {dictonary_1}\nmy dictonary  not duplicates is a{res}')

    def present_3(self):
        dictonary_1 = {}
        dic_sarq = self.name
        for i in self.name:
            dictonary_1[i] = dictonary_1.get(i, 0) + 1

        for key, val in dictonary_1.items():
            if val <= 3:
                dictonary_1 = dictonary_1.pop[val]
        print(dictonary_1)


stanal = Dicit1(input('your text \t'))
stanal.stacox()
stanal.returns()
stanal.present_3()