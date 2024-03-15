isMedicalCondition=input("Enter if you are medical conditioned with 'Y' or N' ")

if (isMedicalCondition=='Y'):
    print("You are allowed")
else:
    attendance=int(input("Kindly state your attendance."))
    if(attendance>75):
         print("You are allowed")
    else:
         print("You are not allowed")
        