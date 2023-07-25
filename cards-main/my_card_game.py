# Rename this file to the name of your game and delete this comment
# Names: 
# Date: 

# Import statements
from card import Card

# Program your game here!
# Rename this function to the name of your game and delete this comment
def my_card_game():
    deck = Card.new_deck()
    print(deck)

# Code that runs when script is called from terminal
# ex: python my_card_game.py
if __name__ == "__main__":
    my_card_game()
