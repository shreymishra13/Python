str = input("Enter your string to be reversed : ")
str1=""
for i in range(len(str)-1,-1,-1):
    str1+=str[i]

print(str1)
    
    