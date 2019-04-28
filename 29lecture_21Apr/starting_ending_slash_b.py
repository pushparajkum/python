#!/usr/bin/python
import re

def PrintWordsStartingTEndingE(file_name):
    fd = open(file_name)
    data = fd.read()
    regex_obj = re.compile(r"\bT\w+e\b", re.IGNORECASE)
    for match in regex_obj.finditer(data):
        print(match)

def main():
    file_name = input("enter filename:")
    PrintWordsStartingTEndingE(file_name)

if __name__ == '__main__':
    main()
