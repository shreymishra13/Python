# Write a program to overload the less than (<) and equal to (==) operators. For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively. You can additionally create more objects to try different values.


class overloadingOperators: 
    def __init__(self, num):
        self.num = num 
        
    def __lt__(self,obj2):
        if(self.num<obj2.num):
            return (str(self.num)+" is less than "+str(obj2.num))
        else:
            return (str(self.num)+" is greater than "+str(obj2.num))
        
    def __eq__(self,obj2):
        if(self.num==obj2.num):
            return (str(self.num)+" is equal to "+str(obj2.num))
        else:
            return (str(self.num)+" is not equal to "+str(obj2.num))
        
        

obj1 = overloadingOperators(4+1+7)
obj2 = overloadingOperators(5)
print(obj1==obj2)

            