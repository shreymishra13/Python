# Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.

class Point:
    __x=0
    __y=0
    
    def __init__(self, x , y ):
        self.__x=x
        self.__y=y
        
    def setCoordinates(self , x , y ):
        self.__x=x
        self.__y=y
    
    def display(self):
        print("The coordinates are : (",self.__x,",",self.__y,")")
        


myPoint=Point(2,3)
myPoint.display()
myPoint.setCoordinates(4,1)
myPoint.display()