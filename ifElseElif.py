import time

t=time.localtime()


currentHour=int(time.strftime("%H",t))
print(currentHour)
currentHour=17


if(currentHour>=12 and currentHour<=16):
    print("Good afternoon !!")
elif(currentHour<=20):
    print("Good evening!!")
elif(currentHour<=24):
    print("Good Night!!")
else:
    print("Good Morning")
    
