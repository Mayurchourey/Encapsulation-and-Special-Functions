class creator
      def __init__(self):
            self._newprice_ = 900

      def sell(self):
            print(self.__maxprice)

      def setPrice(self,price):
            self.__maxprice = price

c = creator()
c.sell()

c.__maxprice = 1000
c.sell()

c.__maxprice(1000)
c.sell()
