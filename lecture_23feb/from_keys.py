
def from_keys(input_dict, values=None):
	res = dict()
	keys = input_dict.keys()
	if type(values) == list:
		i=0
		for key in keys :
			if i < len(values):
				res[key] = values[i]
				i+=1
				continue
			res[key] = None
	else:
		res = dict.fromkeys(input_dict, values)
		return res

def main():
	dict1 = eval(input("Enter dictionary :: "))
	res = from_keys(dict1, {1,2,3})
	print("Palindrome")

if __name__ == '__main__':
	main()