
def reverse_number(n):
	rem = 0
	rev = 0
	while n != 0:	
		rem = n%10
		rev = rev * 10 + rem
		n = int(n//10)
	return rev

def palindrome(n, rev_num):
	if n == rev_num:
		print("The number is palindrome..",rev_num)
	else:
		print("The number is not palindrome..",rev_num)

def main():
	n = eval(input("Enter number :: "))
	rev_num = reverse_number(n)
	palindrome(n, rev_num)

if __name__ == '__main__':
	main()