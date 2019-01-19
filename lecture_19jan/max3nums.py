num1, num2, num3 = eval(input("enter 3 numbers : "))

if(num1 > num2 and num1>num3):
	print("Greater number is : ", num1)
elif(num2>num3):
	print("Greater number is : ", num2)
else:
	print("Greater number is : ", num3)