class IOstring:
    
    def __init__(self):
        self.str1  = "default Value"
        
    def takeInput(self):
        self.str1 = input("Enter your string to change the default string : ")
        
    def toUpper(self):
        print(self.str1.upper())
        

a = IOstring()
print(a.str1)
a.takeInput()
a.toUpper()