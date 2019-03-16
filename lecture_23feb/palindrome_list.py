# wap to accept a list from user and chk if it is paliindrome

def palindrome(list1):
	list2 = list1[::-1]
	if list1 == list2:
		return True
	else:
		return False

def main():
	list1 = eval(input("Enter list elements :: "))
	res = palindrome(list1)
	if res:
		print("Palindrome")
	else:
		print("Not Palindrome")

if __name__ == '__main__':
	main()