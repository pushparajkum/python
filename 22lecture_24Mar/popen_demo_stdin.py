#!/usr/bin/python
import subprocess

def main():
    proc = subprocess.Popen(['cat','-'], stdin = subprocess.PIPE)
    proc.communicate(b'\tJay jay ram krishna hari to stdin\n')

if __name__ == "__main__":
    main()