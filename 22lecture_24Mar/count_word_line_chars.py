# wap to accept input filename, output filename and error filename from user 
# using subprocess.Popen() ensure that wordcount, line count and character count are returned to output file. 

#!/usr/bin/python
import subprocess

def count_words_lines_count(input_file, output_file, error_file):
    inputFile = open(input_file)
    outputFile = open(output_file,'w')
    errorFile = open(error_file,'w')
    subprocess.Popen(['wc', '-m', '-l', '-w'], stdin=inputFile, stdout=outputFile, stderr=errorFile)
    inputFile.close()
    outputFile.close()
    errorFile.close()

def main():
    input_file = input("Enter input filename : ")
    output_file = input("Enter output filename : ")
    error_file = input("Enter error filename : ")
    count_words_lines_count(input_file,output_file, error_file)

if __name__ == "__main__":
    main()