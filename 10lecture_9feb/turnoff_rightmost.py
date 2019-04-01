#  wap to accept  a number and turnoff rightmost one bit of it

def turnoff_rightmost(n):
	x = 1
	while (n&x == 0):
		x = x<<1
	return n&~x

def optimize_turnoff_rightmost(n):
	return (n & n-1)

def main():
	n = eval(input("Enter the number : "))
	res  = turnoff_rightmost(n)
	print("Result is :: ", res)
	
	res1  = optimize_turnoff_rightmost(n)
	print("Result is :: ", res1)

if __name__ == '__main__':
	main()