
def VariableArgsDictionary(a, b, *args, **kwargs):
	print(a,b)
	print(type(args), type(kwargs))
	
	for x in args:
		print(x)
	
	for x in kwargs:
		print(x, kwargs[x])

def main():
	VariableArgsDictionary(10,20,30,40,50,60,70,name = "Raj", hobby="Coding")

if __name__ == '__main__':
	main()