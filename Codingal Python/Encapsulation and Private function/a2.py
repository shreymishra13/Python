# Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.


class Computer:
    __maxPrice=0
    
    def __init__(self, defaultMaxPrice ):
        self.__maxPrice=defaultMaxPrice
    
    def sellPrice(self):
        print("The maximum selling price : $",self.__maxPrice)
        
    def setMaxPrice(self, updateValue):
        self.__maxPrice=updateValue


myComp = Computer(2300)
myComp.sellPrice()
myComp.setMaxPrice(2433)
myComp.sellPrice()