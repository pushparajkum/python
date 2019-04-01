# wap to accept a number, bit position and number of bits to toggle from bit position.

def toggle_bits(n, pos, bits):
	x = 1 << bits
	x = x << (pos - bits)
	return n ^ x

def main():
	n, pos, bits = eval(input("Enter number, bit position and number of bits to toggle :: "))
	res = toggle_bits(n, pos, bits)
	print("Result is : ", res)

if __name__ == '__main__':
	main()