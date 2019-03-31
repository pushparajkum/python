#!/usr/bin/python

class Stack:
    def __init__(self, size):
        print("Stack Constructed of size %d"%size)
        self.__stack = []
        self.__size = size

    def __del__(self):
        print("Stack Destructed")
        del self.__stack

    def isFull(self):
        return len(self.__stack) == self.__size

    def isEmpty(self):
        return self.__stack == []

    def push(self, data):
        status = "FAILED"
        if not self.isFull():
            self.__stack.append(data)
            status = "SUCCESS"
        return status

    def pop(self):
        status = "FAILED"
        data = -1
        if not self.isEmpty():
            data = self.__stack.pop()
            status = "SUCCESS"
        return data, status
    def PrintInteresting(self):
        try:
            print("Interesting:",self.interesting)
        except:
            print("interesting attribute not found.")
def main():
    st = Stack(10)
    st1 = Stack(20)
    #st.__stack.append(1)
    print(st._Stack__size)
    print("object dictionary:",st.__dict__)
    print("class dictionary:",Stack.__dict__)
    st.interesting = True
    print("object dictionary:",st.__dict__)
    print("object dictionary:",st1.__dict__)
    st.PrintInteresting()
    st1.PrintInteresting()

    '''
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    '''
if __name__ == "__main__":
    main()
