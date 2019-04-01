# wap to accpet a filename from user and print it line by line

def read_file(name):
	fd = open(name)
	#fd.readlines()
	#print(fd)
	for x in fd.readlines():
		print(x)

def main():
	name = input("Enter file name :: ")
	read_file(name)

if __name__ == '__main__':
	main()