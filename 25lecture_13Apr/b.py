from a import A

class B(A):
    def __init__(self):
        A.__init__(self)
        print("B in initiated")

    def l(self):
        print("Inside B(l)")