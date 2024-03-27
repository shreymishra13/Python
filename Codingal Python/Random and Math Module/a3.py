import math  # Importing math module

# Using ceil and floor function of math module
#print('The Floor and Ceiling value of 23.56 are: \n' + str(math.ceil(23.56)) + ' \n' + str(math.floor(23.56)))
print('The Ceiling value of 23.56 are: ' + str(math.ceil(23.56)))
print('The Floor  value of 23.56 are: ' + str(math.floor(23.56)))
X = 10
y = -15

# Using copysign function
print('The value of X after copying the sign from y is: ' + str(math.copysign(X, y)))

# Using fabs and gcd function
print('Absolute value of -96 and 56 are: ' + str(math.fabs(-96)) + ' ' + str(math.fabs(56)))
print('The GCD of 24 and 56: ' + str(math.gcd(24, 56)))

import math  #importing math module

x = float('nan')
if math.isnan(x): #to check whether the given value is number or not
    print('It is not a number')
x = float('inf')
y = 45
if math.isinf(x): #to check whether the given number is infinite or not
    print('It is Infinity')
print(math.isfinite(x)) #x is not a finite number
print(math.isfinite(y)) #y is a finite number

print(math.sin(45))
print(math.cos(45))
print(math.tan(45))