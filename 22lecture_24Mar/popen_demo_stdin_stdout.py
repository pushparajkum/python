#!/usr/bin/python
import subprocess

def main():
    proc = subprocess.Popen(['cat','-'], stdin = subprocess.PIPE, stdout=subprocess.PIPE)
    stdout_value = proc.communicate(b'through stdin to stdout')[0]
    print('\tpass through', repr(stdout_value))

if __name__ == "__main__":
    main()