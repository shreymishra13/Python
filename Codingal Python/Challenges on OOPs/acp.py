class IntToRoman:

    def __init__(self,num):
        self.num = num
        
   
        
    def intToRomanMethod(self):
        temp=self.num
        answer=""
        
        while(temp!=0):
            if(temp>=1000):
                answer+="M"
                temp-=1000
                continue
            if(temp>=900 and temp<1000):
                answer+="CM"
                temp-=900
                continue
            if(temp>=500):
                answer+="D"
                temp-=500
                continue
            if(temp<500 and temp>=400):
                answer+="CD"
                temp-=400
                continue
            if(temp>=100):
                answer+="C"
                temp-=100
                continue
            if(temp<100 and temp>=90):
                answer+="XC"
                temp-=90
                continue
            if(temp>=50):
                answer+="L"
                temp-=50
                continue
            if(temp<50 and temp>=40):
                answer+="XL"
                temp-=40
                continue
            if(temp>=10):
                answer+="X"
                temp-=10
                continue
            if(temp==9):
                answer+="IX"
                temp-=9
                continue
            if(temp>=5 ):
                answer+="V"
                temp-=5
                continue
            if(temp==4):
                answer+="IV"
                temp-=4
                continue
            if(temp>=1 ):
                answer+="I"
                temp-=1
                continue
            
        return answer
    
num = IntToRoman(57)

print(num.intToRomanMethod())            
                
        
print("How are you doniing??")
        
    