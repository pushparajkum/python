'''
wap to print following pattern (hint :: print stmt bydefault takes to newline -- print('*', end=''))
*
* *
* * * 
* * * *
'''

def pattern(n):
	for x in range(1, n+1):
		while x != 0:
			x -= 1
			print('*'),
		print("")

def main():
	n = input("Enter the number of lines to be printed :: ")
	pattern(n)

if __name__ == '__main__':
	main()