# wap to accept number from user and and return a dictionary of squares from 1 to that number.

def square_dict(n):
	res = dict()
	for i in range(1, n+1):
		res[i] = i*i
	return res

def main():
	n = eval(input("enter number :: "))
	res = square_dict(n)
	print(res)

if __name__ == '__main__':
	main()