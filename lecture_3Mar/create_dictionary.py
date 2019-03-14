# wap to accept a configuration file from user and create a dictionary of configurations defined in it. 
# (if line starting with comment ignore the line or if line contains comment in between then also ignore)

#!/usr/bin/python
import configparser as cfp

def parseConfigFile(filename):
    parser = cfp.ConfigParser()
    parser.read(filename)
    print(parser.sections())
    print(parser.options("General"))
    print(parser.get('General', 'master'))
    print(parser.options("Headset"))
    print(parser.options("A2DP"))

def create_dictionary(filename):
    res = dict()
    fd = open(filename)
    category = ''
    if fd != None:
        line = fd.readline()
        while line != '':
            if not line.startswith('#') and line != '\n':
                line = line[:-1]
                if line.startswith('['):
                    res[line] = dict()
                    category = line
                elif ('=' in line or ':' in line):
                    if ':' in line:
                        lst = line.split(':')
                    if '=' in line:
                        lst = line.split('=')

                    if '#' in lst[1]:
                        res[category][lst[0]] = lst[1].split('#')[0]
                    else:
                        res[category][lst[0]] = lst[1]
            line = fd.readline()
    return res

def main():
    filename = input("Enter configuration filename : ")
    res = create_dictionary(filename)
    print(res)
    parseConfigFile(filename)

if __name__ == "__main__":
    main()