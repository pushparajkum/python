# wap to accept sentence from user and return a dictionary with count of each character occuring in it.

def count_chars(str1):
	res = dict()
	for x in str1:
		if res.get(x) == None:
			res[x] = 1
		else:
			res[x] += 1
	return res

def main():
	str1 = input("Enter a string :: ")
	res = count_chars(str1)
	print(res)

if __name__ == '__main__':
	main()