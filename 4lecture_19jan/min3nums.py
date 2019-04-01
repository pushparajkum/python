# WAP to accept 3 numbers from user and print minimum of them

num1, num2, num3 = eval(input("Enter 3 numbers : "))

if(num1 < num2 and num1 < num3):
	print(num1," is lowest.")
elif(num2 < num3):
	print(num2," is lowest.")
else:
	print(num3," is lowest.")