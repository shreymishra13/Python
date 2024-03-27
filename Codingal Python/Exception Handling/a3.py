while True: #using nested while loop
  try:
    n=int(input("Enter a number: "))
  #enter a even number
    while n%2==0:
      print("bye", n)
  except ValueError:
    print("Invalid")