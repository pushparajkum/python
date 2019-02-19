#wap to accpet a list from user and print in reverse order element by element using recursion.

def reverse_list(num_list):
	if len(num_list) == 0:
		return num_list
	x = reverse_list(num_list[1:])
	x.append(num_list[0])
	return x

def main():
	x = []
	num_list = eval(input("Enter list : "))
	res = reverse_list(num_list)
	print(res)

if __name__ == "__main__":
	main()

'''
def reverse_container(l1):
	if len(l1) == 0
		if type(l1) == str:
			return l1
		return list()
	
'''