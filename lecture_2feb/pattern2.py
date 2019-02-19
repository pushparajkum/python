'''
wap to print following pattern
   *
  ***
 *****
*******
wap to print following pattern
     1
   212
 32123
4321234
'''

def pattern(n):
	for i in range(1, n+1):
		for _ in range(1, n-i+1):
			print(" ", end='')
		
		for _ in range(1, i*2):
			print("*",end='')
		
		print()
		
def number_pattern(n):
	for i in range(1, n+1):
		x = i
		for _ in range(1, n-i+1):
			print(" ", end='')
		
		for j in range(1,i*2):
			print(x, end='')
			if j < i:
				x = x-1
			else:
				x = x+1
		
		print()
	
def main():
	n = eval(input("Enter number of rows :: "))
	pattern(n)
	number_pattern(n)

if __name__ == "__main__":
	main()