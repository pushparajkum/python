class Demo:
    @classmethod
    def invokeClassMethod(cls):
        print("Invoke class method - ", type(cls), id(cls))

def main():
    Demo.invokeClassMethod()

if __name__ == "__main__":
    main()