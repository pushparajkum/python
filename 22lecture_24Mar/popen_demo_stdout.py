#!/usr/bin/python
import subprocess

def main():
    proc = subprocess.Popen(['echo', '"to stdout"'], stdout= subprocess.PIPE)
    stdout_value = proc.communicate()[0]
    print('\tstdout: ', repr(stdout_value))

if __name__ == "__main__":
    main()