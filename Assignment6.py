n = int(input("enter number="))
a = 0
b = 1
for i in range(n):
    a, b = b, a+b
print("The",n,"the fibonacci number is=",a)
