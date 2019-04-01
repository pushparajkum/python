def palindrome(str1):
	str2 = str1[::-1]
	if str1 == str2:
		print("The string '",str2,"' palindrome")
	else:
		print("The string ",str1," is not palindrome")

def main():
	str1 = input("Enter string : ")
	palindrome(str1)

if __name__ == '__main__':
	main()