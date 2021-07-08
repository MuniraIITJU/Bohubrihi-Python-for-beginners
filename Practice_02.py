# 1. Swapping two variables.
# Two numbers will be taken as input and then they will be kept in a variable and displayed.Then the numbers will be swapped and then the changed layout will be displayed.

print("Enter two variables : ")
a = input()
b = input()

temp = 0
temp = a
a = b
b = temp
print('a= ', a)
print('b= ', b)

