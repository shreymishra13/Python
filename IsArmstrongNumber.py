
def isArmstrong(num):
    temp=num
    temp2=0
    while (temp>0):
        x = temp%10
        temp//=10
        temp2+=(x**3)
    
    if(num==temp2):
       print("Hurray, your number is armstrong number")
    else :
       print("Alas, it is not armstrong number")
       
       
isArmstrong(153)
isArmstrong(157)

    
