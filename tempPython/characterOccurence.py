word = input("Enter your word : ")
char = input("Enter your char : ")

count=0
for c in word:
    if(char==c):
        count+=1
    
print(count)
        
    