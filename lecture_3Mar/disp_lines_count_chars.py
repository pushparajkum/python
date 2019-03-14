# wap to accept a filename from user and print those lines who have less than or equal to 80 chars also print line numbers which have more than 80 chars stating that lines having more than standard count of chars..

def disp_lt80chars(filename):
    fd = open(filename)
    line_num = 0
    line_numbers = []
    if fd != None:
        line = fd.readline()
        while line != '':
            line_num += 1
            if len(line) <= 80:
                print(line)
            else:
                line_numbers.append(line_num)
            line = fd.readline()
        print("Line numbers having more than standard count of chars are ", line_numbers)

def main():
    filename = input("Enter Filename :: ")
    disp_lt80chars(filename)

if __name__ == "__main__":
    main()