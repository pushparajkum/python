# WAP to accpet a number from user and a bit position to turn-off from the given number.. print number after turning off the bit in decimal.. (eg. 16 (bit pos : 5) ==> 0)

def turn_off_bit(num,pos):
	x = 1
	x = x << (pos - 1)
	x = ~x
	return num & x

def turn_off_bits(num, pos, noOfBits):
	x = 1
	x = x << 

def main():
	num, pos = eval(input("Enter the number and position to turn off ::  "))
	num1 = turn_off_bit(num,pos)
	print("number is :: ",num1)
	
	num2, pos1, no_Bits = eval(input("Enter the number, position and number of bits to turn off ::  "))
	num3 = turn_off_bits(num2, pos1, no_Bits)
	print("number is :: ",num3)

if __name__ == '__main__':
	main()