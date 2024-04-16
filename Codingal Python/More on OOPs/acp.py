class Circle:
    def __init__(self, r):
        self.radius = r
        
    def area(self):
        print("The area of the circle is ", (3.14 * self.radius *self.radius))
    
    def perimeter(self):
         print("The perimeter of the circle is ", (2*3.14 * self.radius))

rad = float(input("Enter the radius : "))
firstCircle = Circle(rad)  

firstCircle.area()     
firstCircle.perimeter()     