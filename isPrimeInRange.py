lowerRange=int(input("Enter the lower number : "))
upperRange=int(input("Enter the upper number : "))

def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    
    return True

for i in range(lowerRange,upperRange+1):
    if(isPrime(i)):
        print(i,end=" ")
    

