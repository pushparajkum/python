
def lambda_sample():
    x = lambda x : x*x
    print(x(3))

    x = lambda y,z: y*z
    print(x(3,4))

    x = lambda y, z : [y*y, z*z]
    print(x(3,4))

def generator(x):
    return lambda n:n+x

def main():
    lambda_sample()

    generator_of_5 = generator(5)
    print("generator of 5 : ", generator_of_5(10))

    generator_of_10 = generator(10)
    print("generator of 5 : ", generator_of_10(10))

if __name__ == "__main__":
    main()