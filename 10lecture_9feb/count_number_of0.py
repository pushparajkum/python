
def countof0(n):
	count = 0
	while n != 0:
		count+=1
		n = n & (n-1)
	return count

def main():
	n = eval(input("Enter number : "))
	res = countof0(n)
	print("The number of 0's is : ", res)

if __name__ == '__main__':
	main()