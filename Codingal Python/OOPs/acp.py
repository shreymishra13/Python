class Dog:
    def __init__(self,breed, color):
        self.breed=breed
        self.color=color
        
    def printInfo(self):
        print("The dog breed is "+ self.breed + "and the color is "+ self.color)
        


Bruzo = Dog("German Shepherd","Brown")
Moti = Dog("Desi Breed","Black")

Bruzo.printInfo()
Moti.printInfo()