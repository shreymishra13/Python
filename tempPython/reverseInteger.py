# program to reverse a integer

def reverse_Int(x:int):
    rev=0
    flag=1
    
    if (x<0):
        flag=-1
        x=x*(-1)
    
    while(x>0):
        if rev> (2**31-1):
            return 0
        
        rev=(rev*10)+(x%10)
        x=x//10
    
    if (flag==-1):
        rev=rev*flag
    return rev
    
print(reverse_Int(-2781))
        
    
     