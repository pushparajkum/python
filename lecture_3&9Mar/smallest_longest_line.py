# wap to accepta file name from user and print smallest and longest line from it

def readLines(filename):
    fd = open(filename)
    if fd != None:
        line = fd.readline()
        minline = line
        maxline = line

        while line != '':
            line = fd.readline()
            if line == '\n' or line == '':
                continue
            if len(line) < len(minline):
                minline = line
            if len(line) > len(maxline):
                maxline = line

        print("smallest line :::: ",minline)
        print("Longest line :::: ", maxline)

def main():
    filename = input("Enter filename :: ")
    readLines(filename)

if __name__ == "__main__":
    main()