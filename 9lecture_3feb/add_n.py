# write a function to add 2,3,4,5 numbers

def add(a=0,b=0,c=0,d=0,e=0):
	print(a+b+c+d+e)

def multiply(a=1,b=1,c=1,d=1,e=1):
	print(a*b*c*d*e)

def main():
	add(1,2)
	add(2,4,6)
	add(1,2,3,4)
	add(1,2,3,4,5)
	
	multiply(2,3)
	multiply(2,3,4)
	multiply(2,3,4,5)
	multiply(2,3,4,5,6)

if __name__ == '__main__':
	main()