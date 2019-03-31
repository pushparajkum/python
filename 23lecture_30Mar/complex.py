#!/usr/bin/python

class Complex:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
    def __del__(self):
        print("destructor invoked")
    def add(self, c2):
        '''
            c1 = Complex(10, 20)
            c2 = Complex(1, 2)
            c3 = c1.add(c2) --> Complex.add(c1, c2)
        '''
        return Complex(self.real+c2.real, self.imag+c2.imag)
    def mul(self, no):
        return Complex(self.real*no, self.imag*no)
    def __repr__(self):
        '''
            c1 = Complex(10, 20)
            print(c1) --> Complex.__repr__(c1)
        '''
        return str(self.real)+"+"+str(self.imag)+"i"
    
    
    def __add__(self, obj):
        '''
            c1 = Complex(10, 20)
            c2 = Complex(1, 2)
            c3 = c1 + c2
            c4 = c1 + 10
        '''
        temp = Complex(self.real, self.imag)
        if isinstance(obj, int):
            temp.real += obj
        else:
            temp.real += obj.real
            temp.imag += obj.imag
        return temp
    def __sub__(self, obj):
        temp = Complex(self.real, self.imag)
        if isinstance(obj, int):
            temp.real -= obj
        else:
            temp.real -= obj.real
            temp.imag -= obj.imag
        return temp
def main():
    c1 = Complex(10,10)
    print(c1)
    print("adding integer:",c1+10)
    c2 = Complex(1,3)
    print("addition:",c1+c2)
    print("subtraction:",c1-c2)
if __name__ == "__main__":
    main()
