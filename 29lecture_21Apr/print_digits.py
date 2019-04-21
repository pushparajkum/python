# wap to accept filename from user and print all digitts from it.

import re

def printNumbers(fd):
    data = fd.read()
    regexObj = re.compile(r"\d+") # r for raw
    for match in regexObj.finditer(data):
        print(match.group(0))

def main():
    filesrc = input("Enter filename : ")
    fd = open(filesrc)
    printNumbers(fd)

if __name__ == "__main__":
    main()