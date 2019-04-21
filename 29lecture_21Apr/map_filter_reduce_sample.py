import functools

def Square(x):
    return x*x

def IsEven(x):
    return (x&1)==0

def Multiply(x, y):
    return x*y

def main():
    x = map(Square, range(1,30,2))
    for z in x:
        print(z)

    x = map(lambda x:x*x, range(1,30,2))
    for y in x:
        print(y)
    
    x = filter(IsEven, range(1,30,1))
    for y in x:
        print(y)

    x = functools.reduce(Multiply, range(1,10))
    print(x)

if __name__ == "__main__":
    main()

