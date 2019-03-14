'''wap to accept a filename from user and print alternate 10 chars from it (hint: use read, seek functions)
    (seek accept 2 params - 0 start, 1 current, 2 end--reverse)
    (first read then)
    (
        >>> fd  = open("read_file_line.py")
        >>> fd.seek(10,0)
        10
        >>> fd.read(10)
        ' to accept'
    )
    ( for opening file in 3.x :::: import io ----then----  io.FileIO(filename))
'''

def print_alternate(filename):
    

def main():
    filename = input("Enter filename : ")
    print_alternate(filename)

if __name__ == "__main__":
    main()