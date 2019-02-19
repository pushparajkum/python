# wap to count number of 1 bits in a given number ( input 64 - o/p -> 1, i/p 63 -  o/p -> 6)

def count_numberof1(n):
	count = 0
	while n != 0:
		count+=1
		n = n & (n-1)
	return count

def main():
	n = eval(input("Enter the number :: "))
	res = count_numberof1(n)
	print("Number of 1 in number is : ", res)

if __name__ == '__main__':
	main()