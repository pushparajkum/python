'''WAP to accept  sentence from user and replace the 'not bad' construct if found with 'good'
eg. "Aus played not that bad still lose" ==> "Aus played good still lose"
hint : find not slice -- separate string after not and replace with good'''

string1 = input("Enter string containing not-bad construct in it : ")

not_index = string1.find('not')
if(not_index != -1):
	bad_index = string1.find('bad')
	if(bad_index != -1 and bad_index > not_index):
		result = string1[:not_index]
		result += 'good'
		result += string1[bad_index+3:]

		print(result)
	print("String does not contain not-bad construct.")