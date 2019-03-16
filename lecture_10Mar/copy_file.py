# WAP to accept a filename from user and no of lines to be copied to another file..
# Accept inputs in command line parameters.

import sys

def copyLines(srcFilePath, destFilePath, countOfLines):
    srcFile = open(srcFilePath)
    destFile = open(destFilePath, 'w')
    line = srcFile.readline()
    count = 0

    while line != "":
        if count > countOfLines:
            break
        destFile.write(line)
        line = srcFile.readline()
        count+=1
    else:
        print("All lines copied")

    destFile.close()
    srcFile.close()

def main():
    sysArgv = sys.argv
    if len(sysArgv) != 4:
        print("Invalid number of arguments : ")
    else:
        copyLines(str(sysArgv[1]), str(sysArgv[2]), int(sysArgv[3]))

if __name__ == "__main__":
    main()