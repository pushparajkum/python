# wap to aacept a paragraph from user and retrn dictionary of count of words in the given paragraph

def count_words(str1):
	res = dict()
	for x in str1.split():
		if res.get(x) == None:
			res[x] = 1
		else:
			res[x] += 1
	return res

def main():
	str1 = input("Enter a string :: ")
	res = count_words(str1)
	print(res)

if __name__ == '__main__':
	main()