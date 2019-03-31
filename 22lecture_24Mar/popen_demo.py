#!/usr/bin/python
import subprocess

def foo():
    print("Executed..")

def main():
    subprocess.Popen(['echo', '"to stdout"'], preexec_fn=foo)

if __name__ == "__main__":
    main()