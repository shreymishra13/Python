class Vehicle:
    # mileage, name , maxspeed
    def __init__(self, name, mileage, maxSpeed):
        self.name=name
        self.mileage=mileage
        self.maxSpeed=maxSpeed
    
    def display(self):
        print("The name of the bus is : ", self.name)
        print("The Mileage of the bus is : ", self.mileage)
        print("The Max speed of the bus is : ", self.maxSpeed)
        
class Bus(Vehicle):
    def __init__(self, name , mileage , maxSpeed):
        super().__init__(name, mileage , maxSpeed)
        super().display()
        
VolveBus = Bus("Volvo School Bus", 10 , 40)