
def palindrome(n):
	n1 = n[::-1]
	if n == n1:
		print("The number is palindrome..")
	else:
		print("The number is not palindrome..")

def main():
	n = input("Enter number :: ")
	palindrome(n)

if __name__ == '__main__':
	main()