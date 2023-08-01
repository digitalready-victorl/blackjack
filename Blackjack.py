# Names: Victor, Jiebin, Keven, Jamal
# Date: 7/27/23

# Import statements
from card import Card

# Program your game here!
def blackjack():
    p1 = Player(input("What is your name?", [], 1000))
    deck = Card.new_deck()
    hit_or_stand(p1, deck)
    over_21(p1)
    


# Create the player class
class Player():
    def __init__(self, name, hand, score):
        self.name = name
        self.hand = hand
        self.score = score

# Return the next card in the deck and remove it from the deck
def next_card(deck):
    deck.pop(0)
    return deck[0]

# Deal a card
def deal(player, deck):
    player.hand.append(next_card(deck))

# Check if total hand is greater than 21
def over_21(player):
    total = 0
    for card in player.hand:
        total = total + card.value
    return (total > 21)

# Ask whether a player wants to hit or stand, and act accordingly
def hit_or_stand(player, deck):
    while True:
        input = input(player.name + ", do you want to hit or stand?")
        if input.lower() == "hit" or "h":
            deal(player,deck)
            return
        elif input.lower() == "stand" or "s":
            return
        else:
            print("Invalid input, please try again")

# Code that runs when script is called from terminal
# ex: python my_card_game.py
if __name__ == "__main__":
    blackjack()

