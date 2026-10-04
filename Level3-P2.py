#Top Trumps Card Game
print()
import csv
import random
from colorama import init, Fore
init(autoreset=True)
#DEFINING FUNCTIONS

##Function to display player's cards
def display_card(card):
    
    max_chars = 0
    for keys in card:
        if len(keys) > max_chars:
            max_chars = len(keys)
    for keys in card:
        key = Fore.CYAN + keys
        print(key,(max_chars - len(keys))*' ',':',card[keys])

#SETTING UP

## Reading the file and creating list of all cards
with open('TopTrumpsData.csv', mode ='r') as file:
    csvFile = csv.DictReader(file)
    all_cards = list(csvFile)
## Filtering out keys that we are NOT playing with
imp_keys = list(all_cards[0].keys())
imp_keys = imp_keys[1::]
## Shuffling and distributing cards
random.shuffle(all_cards)
player_cards = all_cards[0::2]
computer_cards = all_cards[1::2]
table_cards = []
## Creating a few important variables for gameplay
chance = 'player'
game_over = False
## Creating a mapping dictionary to enhance UI
key_mapper = {}
for key in imp_keys:
    key_mapper[key[0]] = key

#CORE GAMEPLAY

while not game_over:
    ## Giving basic information
    print(Fore.CYAN + 'Player Cards: ', len(player_cards))
    print(Fore.CYAN + 'Computer Cards: ', len(computer_cards))
    print(Fore.CYAN + 'Table Cards: ', len(table_cards))
    ## Picking up the top card for both participants
    player = player_cards.pop(0)
    computer = computer_cards.pop(0)
    ## Appending both picked cards to 'table_cards' as a DEFAULT setting
    table_cards.append(player)
    table_cards.append(computer)
    ## Displaying the player's card, by calling the function
    print()
    print('It is the', chance + '\'s', 'chance now')
    print("Your card (player's card) is...")
    display_card(player)
    ## Determining who gets to pick, and letting them choose
    print()
    if chance == 'player':
        chosen_key = input('Which category would you like to compare?')
        chance = 'computer'
    elif chance == 'computer':
        chosen_key = random.choice(list(key_mapper.keys()))
        chance = 'player'
    ## Finding the corresponding category
    key_requested = key_mapper[chosen_key]
    value_player = player[key_requested]
    value_computer = computer[key_requested]
    ## Displaying everybody's values for the category
    print()
    print("The chosen category is", key_requested)
    print("In the player's card,", key_requested, 'is', value_player)
    print("In the computer's card,", key_requested, 'is', value_computer)

    game_over = True