# wap to accept a filename from user and print it in reverse order. 
#(no lines to be repeated, no readlines, read functions, no list,) (hint: recursive)

def reverse_file(fd):
    line = fd.readline()
    if line == "":
        return
    reverse_file(fd)
    print(line)        

def main():
    filename = input("Enter filename : ")
    fd = open(filename)
    reverse_file(fd)

if __name__ == "__main__":
    main()