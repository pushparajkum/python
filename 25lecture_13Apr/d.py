from b import B
from c import C
import inspect

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print("D in initiated")

#    def m(self):
#        C.m(self)

def main():
    d1 = D()
    d1.m()
    print(inspect.getmro(D))

if __name__ == "__main__":
    main()