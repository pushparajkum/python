# write a pytgon prog toaccept name from user and greet user with GM and name

#! /usr/bin/python

name = input("Enter your name : ")
# if we use eval(str(input("Enter your name : "))) -> string input must be in quotes
# if we use str(input("Enter your name : ")) -> no restriction on quotes
print("Good Morning "+ name)
