#WAP to accept a folder name from user and create zip file out of it.
#(hint: import shutil)

import shutil

def main():
    inputDirPath = input("Please enter directory name : ")
    shutil.make_archive("OutputZip", "zip", inputDirPath)
    print("Archived..")

if __name__ == "__main__":
    main()