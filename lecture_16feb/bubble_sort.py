
def bubble_sort(num_list):
	for i in range(0, len(num_list) - 1):
		already_sorted = True
		for j in range(0, len(num_list) - i - 1):
			if num_list[j] > num_list[j+1]:
				x = num_list[j]
				num_list[j] = num_list[j+1]
				num_list[j+1] = x
			else:
				already_sorted = False
		

def main():
	num_list = eval(input("Enter the list of numbers to sort : "))
	bubble_sort(num_list)

if __name__ == "__main__":
	main()