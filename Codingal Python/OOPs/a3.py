class Parrot:
    species="bird"
    
    def __init__(self, name , age):
        self.name=name
        self.age=age
    
    def printInfo(self):
        print("The name is ", self.name, "and the age is : ",self.age)
        

first=Parrot("Shrey",10)
first.printInfo()