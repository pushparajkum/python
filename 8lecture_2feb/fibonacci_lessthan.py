def fibonacci(n):
	sum = 0
	n1 = 1
	n2 = 1
	print(n1,n2,end=""),
	while sum <= n :
		sum = n1 + n2
		print(" ",sum,end="")
		n1 = n2
		n2 = sum
	print()

def main():
	n = eval(input("Enter the maximum number till the series to be displayed :: "))
	fibonacci(n)

if __name__ == '__main__':
	main()