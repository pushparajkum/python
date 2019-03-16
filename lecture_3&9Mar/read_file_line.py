# wap prog to accept a filename from user and print line by line

def readFile(filename):
    fd = open(filename)
    if fd != None:
        line = fd.readline()
        while line != '':
            print(line)
            line = fd.readline()
    else:
        print("File is empty.")

def main():
    filename = input("Enter filename to open :: ")
    readFile(filename)

if __name__ == "__main__":
    main()