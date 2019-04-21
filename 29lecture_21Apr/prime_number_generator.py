''' WAP to accept a list of numbers from user and 
write a generator to return prime numbers from given list '''

def IsPrime(n, flag):
	if n%2 == 0:
		return False

	for x in range(3, n//2+1, 2):
		if n%x == 0:
			flag = 0
			print("The number is not prime..")
			return False

def getPrimes(inputList):
    for number in inputList:
        if IsPrime(number):
            yield number

def main():
    x = getPrimes(range(1,100))
    for y in x:
        print(y)