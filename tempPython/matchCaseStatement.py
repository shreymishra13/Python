x = int(input("Enter your age : "))

match x:
    case 17:
        print("Wait for one more year !!")
    
    case 19:
        prin("Hurray you are eligible for it!!")
        
    case _:
        print("This is our default case!!")
        