## wap to print string in reverse order

def reverse_string(str1):
	if len(str1) == 0:
		return str1
	x = reverse_string(str1[1:])
	return x + str1[0]

def main():
	str1 = input("Enter string : ")
	res = reverse_string(str1)
	print(res)

if __name__ == "__main__":
	main()