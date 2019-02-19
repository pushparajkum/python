'''
1.
****
***
**
*

2.
****
 ***
  **
   *

3.
*******
*** ***
**   **
*     *

4.
  *
 ***
*****
 ***
  *
'''

def pattern1(n):
	while n:
		for _ in range(1,n+1):
			print("*", end='')
		print()
		n-=1

def pattern2(n):
	i = 0
	while n:
		for _ in range(1,i+1):
			print(" ", end='')

		for _ in range(1,n+1):
			print("*", end='')

		i+=1
		print()
		n-=1

def pattern3(n):
	i=0
	while n:
		for _ in range(1,n+1):
			print("*", end='')

		for _ in range(1,i+1):
			print(" ", end='')
			print(" ", end='')

		for _ in range(1,n+1):
			print("*", end='')

		i+=1
		n-=1
		print()

def pattern4(n):
	for i in range(1,n+1):
		for _ in range(1,n+1-i):
			print(" ", end='')

		for _ in range(1, i*2):
			print("*", end='')
		print()

	while n > 0:
		print(" ", end='')
		for j in range(1,n):
			for _ in range(1,n-j):
				print(" ", end='')
			
			for _ in range(1, j*2):
				print("*",end='')
			print()
		n-=1

def main():
	n = eval(input("Enter the number of lines : "))
	#pattern1(n)
	#pattern2(n)
	#pattern3(n)
	pattern4(n)

if __name__ == '__main__':
	main()