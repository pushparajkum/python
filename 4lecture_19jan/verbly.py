'''WAP to accept a string from user and perform verbing operations on it. 
(rules : 1. len shld be gt or eq 3
	2. add ing to its end
	3. if ending in ing replace with ly
	4. if len lt 3 then string unchanged)'''
	
	
string1 = input("Enter a string : ")
if(len(string1) >= 3):
	if(string1.find('ing')):
		string1= string1[:-3]+'ly'
	else:
		string1 += 'ing'

print(string1)