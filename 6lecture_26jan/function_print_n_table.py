# wap to accept n from user and print tables from 2 to n using function.

def print_table(n):
	for x in range(2, n+1):
		print("Table for x :: ",x)
		for y in range(1, 11):
			print(x*y)

n = eval(input("Enter number : "))
print_table(n)