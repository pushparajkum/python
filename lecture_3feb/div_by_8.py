
def divby8(n):
	return ((n & 7) == 0)

def main():
	n = eval(input("Enter number: "))
	res = divby8(n)
	if res:
		print("Number is divisible by 8..", res)
	else:
		print("Number not divisible by 8..", res)

if __name__ == '__main__':
	main()