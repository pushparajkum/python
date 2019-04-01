# wap to accept an integer from user and print its table.

def print_table(n):
	for x in range(1, 11):
		print(n*x)

n = eval(input("Enter the number :: "))
print_table(n)