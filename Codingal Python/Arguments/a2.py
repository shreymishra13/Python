def cube(number):
  return number**3

def by_three(number):
  if number%3==0:
    print("It is divisible by 3")
    return cube(number)
  else:
    print("number not divisible by 3")

print(by_three(3))
print(by_three(4))