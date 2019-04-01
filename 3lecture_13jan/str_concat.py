string = input("Enter string : ")
print("the output is : ", string[0::2]+string[1::2])
print(string[-1::-2] + string[-2::-2])

string1 = input("Enter String to check if it starts with 'T' : ")
print(string1.startswith('T'))