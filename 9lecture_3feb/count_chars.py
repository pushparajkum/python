'''
wap to accept a string which has repetative characters consecutively and optimize the storage space for the same..
 eg.  aaabbcccccddddddaaa =>> o/p -> a3b2c5d6a3
'''

def count_chars(str1):
	cntr = 0
	str11 = str1[0:1]
	cntr = str1.count(str11)
	return cntr

def main():
	str1 = input("Enter the string :: ")
	res = count_chars(str1)
	print(res)

if __name__ == '__main__':
	main()