# Create a class reverse that consists of a constructor with a default value of string s. Then, create a method that will return the reversed string. The value of string s must be equal to the word taken as input from the user.


class Reverse:
    str = None
    
    def __init__(self, s):
        self.str = s
        
    def reverseString(self):
        return self.str[::-1]
        
    

string = Reverse("Shrey")
print(string.reverseString())