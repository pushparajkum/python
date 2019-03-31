#WAP to implement a complex number on your own. FOllwoing operation should be supported
#1.Add complex number,
#2.substract complex number,
#3.multiply complex number by an integer
class Complex:
    def __init__(self,r=0,i=0):
        self.real=r
        self.imaginary=i
    def __del__(self):
        print("Stack destructed")
        del self.real
        del self.imaginary
    def add(self,complex2):
        return Complex(self.real+complex2.real,self.imaginary+complex2.imaginary)
    def sub(self,complex2):
        return Complex(self.real-complex2.real,self.imaginary-complex2.imaginary)
    def mult(self,complex2):
        return Complex(self.real*complex2.real,self.imaginary*complex2.imaginary)
    def __repr__(self):
        return str(self.real)+"+"+str(self.imaginary)+"i"

def main():
    cn=Complex(10,20)
    print(cn.add(Complex(2,3)))
    print(cn.sub(Complex(1,2)))
    print(cn.mult(Complex(1,2)))
    
    '''while 1:
        print("Enter you choice : \n1.Add\n2. Substract\n 3.Mupltiply")
        ch=input("Enter your choice")
        while(ch):
            if (ch==1):
                complex2=input("Enter complex number to add")
                print(cn.add(cn,Complex(complex2)))
                break
            elif (ch==2):
                complex2=input("Enter data to substract")
                print(cn.sub(cn,Complex(complex2)))
                break'''
            
if __name__=='__main__':
    main()
