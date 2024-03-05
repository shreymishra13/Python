str1= "This is my first string"
str2= 'This is my second string'
str3= '''This is my third string'''

# print(str1)
# print(str2)
# print(str3)

# #concatenate operators
# print(str1+"\n" + str2)


## length of string 
# print(len(str1))
# print(len(str2))

# #indexing in python starts with 0
# char = str1[0]
# print(char)


#slicing in slicing the last index element is not included
str="shrey is the best"
# temp_str = str[1:5]
# print(temp_str)
# print(str[1:4])
# #if you want to go to last index, there are three ways you can do that

# print(str[0:5])
# print(str[0:len(str)])
# print(str[0:])

#also you can print something from backward but it will be negative

print(str[-3:-1 ])
print(str.endswith("st"))
print(str.endswith("ey"))

print(str.isupper())

s= "I am replacing a in this sentence"
print(s.replace("a", 'b'))
print(s)