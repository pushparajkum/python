'''
1 2
2 4 8
3 6 12 24
4 8 16 32 64

1 2
2 4 6
3 6 9 12
4 8 12 16 20
'''

def pattern_double(n):
	for i in  range(1,n+1):
		k=i
		for _ in range(1,i+2):
			print(k, " ", end="")
			k*=2
		print()
	print()

def pattern_table(n):
	for i in range(1,n+1):
		k = i
		for _ in range(1,i+2):
			print(k, " ", end='')
			k+= i
		print()
	print()

def main():
	n = eval(input("Enter the number of rows :: "))
	pattern_double(n)
	pattern_table(n)

if __name__ == '__main__':
	main()