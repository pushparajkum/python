class Demo:
    @staticmethod
    def invokeStatic():
        print("Invoked static method")

def main():
    Demo.invokeStatic()

if __name__ == "__main__":
    main()