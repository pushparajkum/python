
def add(x,y):
	return x+y
	
def subtract(x,y):
	return x - y

def multiply(x,y):
	return x*y
	
def divide(x,y):
	return x/y
	
def main():
	while 1 :
		print("1. Addition")
		print("2. Subtraction")
		print("3. Multiplication")
		print("4. Division")
		print("5. Exit")
		choice = eval(input("Enter Your choice :: "))
		if choice == 1 :
			x,y = eval(input("Enter 2 numbers for addition :: "))
			print("Addition is :: ",add(x,y))

		if choice == 2 :
			x,y = eval(input("Enter 2 numbers for subtraction :: "))
			print("Subtraction is :: ",subtract(x,y))
			
		if choice == 3 :
			x,y = eval(input("Enter 2 numbers for multiplication :: "))
			print("Multiplication is :: ",multiply(x,y))
			
		if choice == 4 :
			x,y = eval(input("Enter 2 numbers for division :: "))
			print("Division is :: ",divide(x,y))
		
		if choice == 5 :
			break
	
if __name__ == '__main__':
	main()
