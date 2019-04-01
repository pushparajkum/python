# wap to accept 2 lists from user sort them and merge the 2 sorted lists element by element preserving the sort order.

def merge_list(res, res1):
	i = 0
	j = 0
	res2 = []
	while i < len(res) and j < len(res1):
		if res[i] > res1[j]:
			res2.append(res1[j])
			j+=1
		else : 
			res2.append(res[i])
			i+=1
	if i < len(res):
		res2.extend(res[i:])
	if j < len(res1):
		res2.extend(res1[j:])
	return res2

def sort_list(l):
	for i in range(0, len(l)):
		for j in range(0, len(l) - i - 1):
			if l[j] > l[j+1]:
				x = l[j]
				l[j] = l[j+1]
				l[j+1] = x
	return l

def main():
	l1 = eval(input("Enter first list : "))
	l2 = eval(input("Enter 2nd list : "))
	res = sort_list(l1)
	res1 = sort_list(l2)
	res2 = merge_list(res, res1)
	print(res)
	print(res1)
	print(res2)

if __name__ == '__main__':
	main()