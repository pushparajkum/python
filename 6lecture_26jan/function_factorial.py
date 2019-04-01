def factorial(n):
	res = 1
	for x in range(2, n+1):
		res = res*x
	return res

n = eval(input("Enter number : "))
print(factorial(n))
