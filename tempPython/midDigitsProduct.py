num = int(input("Enter your number : "))

def countDigits(n):
    count=0
    while(n>0):
        count+=1
        n//=10
    
    return count


digits= countDigits(num)

midPoint=math.ceil(digits)
#needs to work