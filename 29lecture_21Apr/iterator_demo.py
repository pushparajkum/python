def YieldDemo():
    i = 0
    for i in range(10):
        yield(i)

def iter_demo(x):
    i = iter(range(x))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))

def main():
    iter_demo(5)
    b = YieldDemo()
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))

if __name__ == "__main__":
    main()