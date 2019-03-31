# wap which runs periodically and displays the status of currently running processes

#!/usr/bin/python
import subprocess
import time

def main():
    while 1:
        print("The processess currently running are : ")
        proc = subprocess.Popen(['ps'])
        time.sleep(10)
        cont_exit = input("Do you want to continue y/n : ")
        if cont_exit == 'n':
            break
        else:
            continue

if __name__ == "__main__":
    main()