# WAP rewrite validation of rotation of string with if-else

string1 = input("Enter first string : ")
string2 = input("Enter second string : ")

if(string2 in (string1 + string1)):
	print("second string is rotation of first string")
else:
	print("second sting is not rotation of first string")
	
if((string1 + string1).__contains__(string2)):
	print("second string is rotation of first string")
else:
	print("second sting is not rotation of first string")