string1 = input("Enter string1 : ")
string2 = input("Enter string2 : ")
'''
str_len = len(string1)
print("str_len : ", str_len/2)

first_half = string1[0 : str_len//2+1]
second_half = string1[str_len//2+1:]

string3 = second_half + first_half

print(string3 == string2)
print(string2+" is rotation of "+ string1 )
'''
print(string2 in string1+string1)
