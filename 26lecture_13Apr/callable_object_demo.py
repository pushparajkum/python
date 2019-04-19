# callable object demo

class Simple:
    def __call__(self):
        print("inside call")

def main():
    s = Simple()
    s()

if __name__ == "__main__":
    main()    