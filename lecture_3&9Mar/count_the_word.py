# wap to accept a filename from user and print those lines which have 'the' word more than once (hint : dictionary split ) (make generic)

def lines_the_word(filename, word):
    fd = open(filename)
    if fd != None:
        line = fd.readline()
        while line != '':
            if line.count(word) > 1:
                print(line)
            line = fd.readline()            

def main():
    filename = input("Enter filename : ")
    word = input("Enter word to search : ")
    lines_the_word(filename, word)

if __name__ == "__main__":
    main()