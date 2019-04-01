# wap to accept an integer from user and print its table.

n  = int(input("Enter number : "))

for x in range(1,11):
	print(n*x)
else:
	print("Executed else of while")