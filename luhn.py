from colorama import init,Fore, Back, Style
import os
#This is for colorama
init(convert=True)
version = "1.0"
#OS Specific clear mechanism
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#Input Function, put into function so we can restart it if user enters something invalid.
def input_num():
    print(Fore.GREEN,end='')
    print("    [Luhn]",end='')
    print(Fore.LIGHTGREEN_EX,end='')
    card_num = input(" Please enter a 10 digit number to check against the Luhn algorithim: ")
    #Make sure the input is an integer, because if its not, the luhn function will fail
    try:
        int(card_num)
        result = luhn(card_num)
        if (result == 1):
            print(Fore.GREEN,end='')
            print("    [Luhn]",end='')
            print(Fore.LIGHTGREEN_EX + " That card number is valid!")
            print()
        else:
            print(Fore.GREEN,end='')
            print("    [Luhn]",end='')
            print(Fore.LIGHTGREEN_EX + " That card number is NOT valid.")
            print()
    except:
        print(Fore.GREEN,end='')
        print("    [Luhn]",end='')
        print(Fore.LIGHTGREEN_EX,end='')
        card_num = input(" The number you inputted contained letters. Please enter a number!")
        input_num()

#Main Algorithim!
def luhn(card_num):
    digits = len(card_num)
    oddeven = digits & 1
    sum = 0
    for enumerate in range(0, digits):
        digit = int(card_num[enumerate])

        if not (( enumerate & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        sum += digit
    return ( (sum % 10) == 0 )
#ANSI Logo :D
cls()
print(Fore.GREEN + '''
    ██╗     ██╗   ██╗██╗  ██╗███╗   ██╗
    ██║     ██║   ██║██║  ██║████╗  ██║
    ██║     ██║   ██║███████║██╔██╗ ██║
    ██║     ██║   ██║██╔══██║██║╚██╗██║
    ███████╗╚██████╔╝██║  ██║██║ ╚████║
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
''')
print(Fore.LIGHTGREEN_EX + "    By Cade, Version: " + version)
print()
print()
input_num()
