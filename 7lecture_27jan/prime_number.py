#! /usr/local/bin/python3

def prime(n, flag):
	if n%2 == 0:
		return False

	for x in range(3, n//2+1, 2):
		if n%x == 0:
			flag = 0
			print("The number is not prime..")
			return False

	if flag == 1:
		print("The number is prime..")

def main():
	flag = 1
	n = eval(input("Enter a number :: "))
	prime(n, flag)

if __name__ == '__main__':
	main()
