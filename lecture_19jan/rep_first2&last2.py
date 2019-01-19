''' WAP to accept a string from user and return a string having first 2 and last 2 chars in string
eg. string ==> stng'''

string1 = input("Enter a string : ")
strlen = len(string1)
str1 = string1[0:2]
str2 = string1[strlen-2:strlen]

print("result is : ", str1+str2)