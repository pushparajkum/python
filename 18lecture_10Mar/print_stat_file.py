#WAP to accept file name from user and print its statistical information like type of file,
# size of file, permissions. (use stat/fstat system call)

import os

def main():
    inputFilePath = input("Please enter filename : ")
    print("The file details are: ", os.stat(inputFilePath)) 

if __name__ == "__main__":
    main()