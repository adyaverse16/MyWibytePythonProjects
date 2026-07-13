#Tennis Store
#Project 1 of Wibyte Level 3
#P.S: EXTEND TERMINAL TO FULL SCREEN FOR BEST VIEW

#PART 1 - SETTING UP

##Importing
import random
import pyfiglet
from colorama import init, Fore
init(autoreset = True)

##Function for master dictionary keys
def append_keys(name):
    return name + 's'

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

#PART 2 - CREATING STORE INVENTORY

##Specifying features
features = ['Brand', 'Model', 'Color', 'Weight', 'Length', 'Grip Size', 'String Pattern','Price']

##Creating master dictionary with keys
features_modified = list(map(append_keys, features))
master_dict = dict.fromkeys(features_modified)

##Populating master dictionary
master_dict['Brands'] = ['Babolat', 'HEAD', 'Wilson', 'Yonex']
master_dict['Models'] = ['AAA', 'BBB', 'CCC']
master_dict['Colors'] = ['Red', 'Blue', 'Yellow', 'Green']
master_dict['Weights'] = ['270g', '280g', '290g' , '300g', '310g', '320g']
master_dict['Lengths'] = ['21 in', '23 in', '25 in', '26 in' , '27 in']
master_dict['Grip Sizes'] = ['4.0 in', '4.25 in' , '4.5 in', '4.625 in']
master_dict['String Patterns'] = ['16x19', '18x20', '16x18', '16x20']
master_dict['Prices'] = ['INR 8000', 'INR 10,000', 'INR 12,000', 'INR 15,000', 'INR 20,000', 'INR 25,000']

##Creating final inventory of rackets
rackets_list = []
rackets_num = 60

for _ in range(rackets_num):
    new_racket = dict.fromkeys(features)
    ###Populating values for the specific laptop randomly
    for feature in new_racket:
        new_racket[feature] = random.choice(master_dict[feature + 's'])
    rackets_list.append(new_racket)

#PART 3  - DISPLAYING CUSTOMIZED CATALOGUE OF RACKETS

##Recieving user's choice
user_choices = dict.fromkeys(features)
for feature in features:
    user_choices[feature] = input(Fore.CYAN + "Any preference for " + feature + " (Enter none for no preference)\n" + Fore.RESET)

##Creating the query
query = ''

for choice in user_choices:
    if user_choices[choice].lower() == 'none':
        pass
    else:
        query = query + 'racket[' + '\'' + choice + '\'] == ' + '\'' + user_choices[choice] + '\' and '

##Removing the last 'and' from the query
query = query[0:-4:1]

##Using the query to pull out preferred rackets
if query == '':
    selected_rackets = [racket for racket in rackets_list]
else:
    selected_rackets = [racket for racket in rackets_list if eval(query)]

##Displaying the selected rackets in a formatted manner
characters = 0
print(len(selected_rackets), ' rackets met your preferences.')
print()
for kk in features:
  print(Fore.CYAN + kk, end = '')
  characters = len(kk)
  print((16 - characters)*' ', end = '')

print()

characters = 0

for racket in selected_rackets:
  for kk in racket:
    print(racket[kk],  end = '')
    characters = len(racket[kk])
    print((16- characters)*' ', end = '')
  print()

#BASIC DONE - BONUS TBD