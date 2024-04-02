class Person:
    name ="harry"
    occupation = "Software Developer"
    netWorth = 10
    
    def printInfo(self):
        print("The name is : "+ self.name)
        print("The occupation is : "+ self.occupation)
    
    
a=Person()
a.printInfo()


a.name="Shrey"
a.occupation="Software Developer"

a.printInfo()
