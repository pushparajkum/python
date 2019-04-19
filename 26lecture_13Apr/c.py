from a import A

class C(A):
    def __init__(self):
        A.__init__(self)
        print("C in initiated")

    def m(self):
        A.m(self)
        #print("Inside C(m)")

    def n(self):
        print("Inside C(n)")