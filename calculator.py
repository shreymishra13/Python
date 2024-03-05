print("Welcome to the Calculator : ")
print("Enter your first number : ")
a = int(input(""))
print("Enter your Second number : ")
b = int(input(""))
print("Choose from the below operation that you want to perform : ")
print("1. Addition  or +   ")
print("2. Subtraction or - ")
print("3. Multiplication or * ")
print("4. Division or / ")
print("5. Exponentation or ^ ")
print("6. Floor division or // ")
print("7. Remainder or % ")

var = input("Either enter the nmber or the symbol : ")

if(var=="*" or var=="3"):
    var="*"
    print(a,var,b,"=", a*b)
elif(var=="+" or var=="1"):
    var="+"
    print(a,var,b,"=", a+b)
elif(var=="-" or var=="2"):
    var="-"
    print(a,var,b,"=", a-b)
elif(var=="/" or var=="4"):
    var="/"
    print(a,var,b,"=", a/b)
elif(var=="^" or var=="5"):
    var="^"
    print(a,var,b,"=", a**b)
elif(var=="//" or var=="6"):
    var="//"
    print(a,var,b,"=", a//b)
else:
    var="%"
    print(a,var,b,"=", a%b)


