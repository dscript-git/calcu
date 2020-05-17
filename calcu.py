#!/usr/bin/env python3

import os

# Function
def calcu():
    os.system('clear')
    #colors
    red = '\033[91m'
    yellow = '\033[93m'
    white = '\033[97m'
    green = '\033[92m'
    info = '\033[93m[!]\033[0m'
    good = '\033[92m[+]\033[0m'
    #Title
    print (red," ===>SIMPLE CALCU v1.0 by d-script-dev ;) <===")
    #Choices
    print (yellow," ==> CHOICES FOR OPERATION:[ +, -, *, OR /] <==")
    num1 = float(input(' ENTER 1st NUMBER: '))
    oper = input(' ENTER OPERATION TO USE: ')
    num2 = float(input(' ENTER 2nd NUMBER: '))

    if  oper == '+':
        print (green,"THE ANSWER IS: ")
        print (good,num1 + num2)
        ask = input('Do you want to continue? y/n: ')
    elif oper == '-':
        print (green,"THE ANSWER IS: ")
        print (good,num1 - num2)
        ask = input('Do you want to continue? y/n: ')
    elif oper == '*':
        print (green,"THE ANSWER IS: ")
        print (good,num1 * num2)
        ask = input('Do you want to continue? y/n: ')
    elif oper == '/':
        print (green,"THE ANSWER IS: ")
        print (good,num1 / num2)
        ask = input('Do you want to continue? y/n: ')
    elif oper == "":
        print (info,"NO OPERATOR")
        print (white,"Bye Bye ! ! !")
        exit()
    else:
        print (info,"UNKNOWN ERROR OCCURED!")
        print (white,"Bye Bye ! ! !")
        exit()

    if ask == 'y' or ask == 'Y' or ask == 'yes' or ask == 'Yes' or ask == 'YES':
        os.system('clear')
        calcu()
    else:
        print (white,"Bye Bye ! ! !")
        exit()
calcu()
