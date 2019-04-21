# wap print all words starting with T and ending with E ignoring case 

import re

def matchRegExp(fd):
    data = fd.read()
    regexObj = re.compile(r"\bT\w+e\b", re.IGNORECASE) # r for raw
    for match in regexObj.finditer(data):
        print(match)

def main():
    fileSrc = input("Please enter filepath : ")
    fd = open(fileSrc)
    matchRegExp(fd)

if __name__ == "__main__":
    main()