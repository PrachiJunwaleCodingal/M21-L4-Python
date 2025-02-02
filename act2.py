#Computer Price
class Computer:
    def __init__(self):
        self.__Mprice = 50000

    def sell(self):
        print( "Price:", self.__Mprice)

    def setMprice(self, price):
        self.__Mprice = price

comp = Computer()
comp.sell()
comp.__Mprice = 70000 #private var can't update outside
comp.sell()
comp.setMprice(70000)
comp.sell()