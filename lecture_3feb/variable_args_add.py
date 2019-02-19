
def add(*args):
	#print(type(args))
	#print(args)
	sum = 0
	for x in args:
		sum = sum + x
	print(sum)

def main():
	add(1,2)
	add(1,2,3)
	add(1,2,3,4)

if __name__ == '__main__':
	main()