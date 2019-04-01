# WAP to accept entered number even or odd without using arithmetic operator.

def odd_even(n):
	if n & 1 == 0:
		return True
	else:
		return False

def main():
	n = eval(input("Enter the number :: "))
	res = odd_even(n)
	if(res):
		print("number is even")
	else:
		print("number is odd")

if __name__ == '__main__':
	main()