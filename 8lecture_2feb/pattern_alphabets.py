'''
(hint -- print(chr(x+64))) replace in 4 above
      A
    BAB
  CBABC
DCBABCD
'''

def print_pattern(n):
	for i in range(1, n+1):
		x = i
		for _ in range(1, n-i+1):
			print(" ", end='')
		
		for j in range(1,i*2):
			print(chr(x+64), end='')
			if j < i:
				x = x-1
			else:
				x = x+1

		print()

def main():
	n = eval(input("Enter the number of rows :: "))
	print_pattern(n)

if __name__ == '__main__':
	main()