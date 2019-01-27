
def swap_first2chars(str1, str2):
	str11 = str2[0:2] + str1[2:]
	str22 = str1[0:2] + str2[2:]
	
	print(str11)
	print(str22)

str1 = input("Enter first string : ")
str2 = input("Enter second string : ")
swap_first2chars(str1, str2)