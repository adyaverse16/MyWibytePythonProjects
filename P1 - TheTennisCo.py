#Tennis Store
#Project 1 of Wibyte Level 3
#P.S: EXTEND TERMINAL TO FULL SCREEN FOR BEST VIEW

#SETTING UP

##Importing
import random
import pyfiglet
from colorama import init, Fore
init(autoreset = True)

##Introducing
print()
print("Welcome to....")
print()
intro = ("The Tennis Co.")
introPyfiglet = pyfiglet.figlet_format( intro, font = "smslant" )
print(Fore.CYAN + "-----------------------------------------------------------")
print()
print(Fore.CYAN + introPyfiglet)
print(Fore.CYAN + "-----------------------------------------------------------")
print()
print("Your one stop shop for all tennis equipment!")
print("All you have to do is enter your preferences")
print("We will recommend the best rackets for you, along with prices and specifications!")
print("Let's get started!")
print()
print(Fore.CYAN + "-----------------------------------------------------------")
print()