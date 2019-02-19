# count of consonents

def count_consonents(str1):
	count = 0
	for x in str1:
		if x not in "aeiouAEIOU":
			count+=1
	return count

def main():
	str1 = input("Enter a string :: ")
	print("Count of consonents  is :: ",count_consonents(str1))

if __name__ == '__main__':
	main()