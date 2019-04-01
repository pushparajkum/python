# wap to accept 2 strings from user and swap their first 2 chars
# eg. Dog dinner ==> Dig donnor

str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

str11 = str2[0:2] + str1[2:]
str22 = str1[0:2] + str2[2:]

print(str11)
print(str22)