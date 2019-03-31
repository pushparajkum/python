class Stack:
    def __init__(self,size):
        print("Stack Constructed of size %d"%size)
        self.stack=[]
        self.size=size
        self.__arg=7887
    def __del__(self):
        print("Stack destructed")
        del self.stack
                
    def isempty(self):
        return self.stack == []
        
    def isfull(self):
        return self.stack==self.size
    
    def push(self,data):
        status="FAILED"
        if not self.isfull():
            self.stack.append(data)
            status="SUCCESS"
        return status

    def pop(self):
        status="FAILED"
        data=-1
        if not self.isempty():
            data=self.stack.pop()
            status="SUCCESS"
        return data,status
    def printinteresting(self):
        try:
            print("Interesting present",self.interesting)
        except:
            print("Interesting not found")
        
def main():
    st=Stack(10)
    st1=Stack(10)
    print st._Stack__arg
    st.interesting=True
    st.printinteresting()
    st1.printinteresting()
    print("object dictionary",st.__dict__)
    print("object dictionary",st1.__dict__)
    #print("Class dictionary",Stack.__dict__)
    #st.stack.append(25)
    #data=input("Enter data to push")
    while 1:
        print("Enter you choice : \n1.Push\n2. Pop\n 3.Exit")
        ch=input("Enter your choice")
        while(ch):
            if (ch==1):
                data=input("Enter data to push")
                print(st.push(data))
                break
            elif (ch==2):
                print(st.pop())
                break

if __name__=='__main__':
    main()
