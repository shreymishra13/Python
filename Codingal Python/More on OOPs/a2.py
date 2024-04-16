class Employee:
    
    def __init__(self):
        self.name="Not Assigned"
        self.id = "N/A"
        
    def __del__(self):
        print("Employee deleted successfully")
        
def toCreateEmployee():
    tempObj = Employee()
    print(tempObj.name)
    print(tempObj.id)
    
    return tempObj


realObj = toCreateEmployee()
print(realObj.name)
print(realObj.id)
          