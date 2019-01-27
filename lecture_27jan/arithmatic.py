#wap add, sub, multiply, div

print("Free fall at starts")
def add(x,y,z):
	return x+y+z

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y
	
def div(x,y):
	return x/y
	
def main():
	x,y,z = eval(input("Please enter 3 numbers : "))
	res = add(x,y)
	print("addition is  : ",res)
	res1 = subtract(x,y)
	print("subtraction is  : ",res1)
	res2 = div(x,y)
	print("division is  : ",res2)
	res3 = multiply(x,y)
	print("multiplication is  : ",res3)

if __name__ == '__main__':
	main()
	
print("Free fall at end")