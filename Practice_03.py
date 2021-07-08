# Solve a quadratic equation with real solutions. Like x^2-5x+6 = 0 where x = 2,3
# ax^2+bx+c = 0. X = Solution?

import math
print('Enter the coefficients : ')
astr = input()
bstr = input()
cstr = input()

a = int(astr)
b = int(bstr)
c = int(cstr)

D = math.sqrt(b*b-4*a*c)
x1 = (-b+D)/(2*a)
x2 = (-b-D)/(2*a)
print(x1)
print(x2)
