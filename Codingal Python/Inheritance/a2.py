class Person: 
    def __init__(self , name , id  , mobileNo):
        self.name=name
        self.id=id
        self.mobileNo=mobileNo
        
    def display(self):
        print("The name of the person is : ", self.name)
        print("The id of the person is : ", self.id)
        print("The Mobile Number of the person is : ", self.mobileNo)
        
class Employee(Person):
    def __init__(self , name , id , mobileNo , post , salaryInUSD):
        super().__init__(name , id , mobileNo)
        self.post=post
        self.salaryInUSD=salaryInUSD
        super().display()
        print("The post of the person is : ", self.post)
        print("The salary of the person is : ", self.salaryInUSD)
        
Shrey=Employee("Shrey Mishra" , 123312 , 8957183030 , "SDE at Google","$120,052")
        