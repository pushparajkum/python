# WAP to accept a filename from user and no of lines to be copied to another file..
# Accept inputs in command line parameters.
# Hint - parse the arguments -using OPTION PARSER

import sys
import optparse

def copyLines(srcFilePath, destFilePath, countOfLines):
    srcFile = open(srcFilePath)
    destFile = open(destFilePath, 'w')
    line = srcFile.readline()
    count = 0

    # not optimized logic - copy file line by line
    while line != "":
        if count > countOfLines and countOfLines != 0:
            break
        destFile.write(line)
        line = srcFile.readline()
        count+=1
    else:
        print("All lines copied")

    # optimized logic - using shutil to copy complete file at a time 
    if countOfLines == 0:
        shutil.copyfileobj(srcFile, destFile)
        print("Complete file copied successfully")
    else:
        while line != "":
            if count > countOfLines and countOfLines != 0:
                break
            destFile.write(line)
            line = srcFile.readline()
            count+=1
        else:
            print("All lines copied")

    destFile.close()
    srcFile.close()

def main():
    print(sys.argv)
    parser = optparse.OptionParser()
    parser.add_option('-i', type = str, help = "Input/Source file name")
    parser.add_option('-d', type = str, help = "Destination file name")
    parser.add_option('-n', type = int, help = "Number of lines to be copied, default=0", default=0)
    (options, args) = parser.parse_args()
    copyLines(args.i, args.d, args.n)
    print("File copy successful")

if __name__ == "__main__":
    main()