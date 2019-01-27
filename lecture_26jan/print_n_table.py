#wap to accept n from user and print tables from 2 to n.

n = int(input("Enter an  integer  : "))

for x in range(2,n+1):
	print("Table for x is : : ", x)
	for y in range(1, 11):
		print(x * y)