#Tennis Store
#Project 1 of Wibyte Level 3

#SETTING UP
##Importing
import random
import pyfiglet
from colorama import init, Fore
init(autoreset = True)

##Introducing

print()
print("Welcome to....")
intro = ("The Tennis Co.")
introPyfiglet = pyfiglet.figlet_format( intro, font = "smslant" )
print(Fore.CYAN + introPyfiglet)
print(Fore.BLUE + "Your one-stop shop for all tennis equipment!")


print()