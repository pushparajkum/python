'''num1 = eval(input("Enter first number : "))
num2 = eval(input("Enter second number : "))
'''
num1, num2 = eval(input("Enter two numbers : "))
if(num1>num2):
	sub = num1 - num2
else:
	sub = num2 - num1
	
print(sub)