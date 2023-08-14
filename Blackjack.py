# Names: Victor, Jiebin, Keven, Jamal
# Date: 7/27/23

# Import statements
from card import Card

# Create the player class
class Player():
    def __init__(self, name, hand, points):
        self.name = name
        self.hand = hand
        self.points = points

# Return the next card in the deck and remove it from the deck
def next_card(deck):
    deck.pop(0)
    return deck[0]

# Deal a card
def deal(player, deck):
    player.hand.append(next_card(deck))

# State the player's hand
def displayCards(player):
    print(f"{player.name}, your current hand is {player.hand}")

# Return the total of a player's hand, this is where we also set all the face cards to 10 and aces to 1 or 11
def handTotal(player):
    total = 0
    for card in player.hand:
        faceFix(card)
        total = total + card.value
    aceFix(player)
    return total

# Check if total hand is greater than 21
def over_21(player):
    return (handTotal(player) > 21) # If the total hand is greater than 21, function will return True

# Check if a card is a face card, and thus reduce it's value to 10
def faceFix(card):
    if card.value > 10:
        card.value = 10

# Check if any cards in a player's hand is an ace, and figure out whether it should be treated as a 1 or 11
def aceFix(player):
    for card in player.hand:
        if card.value == 1:
            card.value = 11
            if over_21(player):
                card.value = 1

# If a player is over 21, show that they bust
def checkBust(player):
    if over_21(player):
        print(f"{player.name} busts!")
    return(over_21(player))

# Ask whether a player wants to hit or stand, and act accordingly
def hit_or_stand(player, deck):
    while True:
        user = input(f"{player.name}, do you want to hit or stand? ")
        if user.lower() == "hit" or user == "h":
            deal(player,deck)
            return
        elif user.lower() == "stand" or user == "s":
            print("You stand")
            return "stand" # If the user stands, the function will return stand
        else:
            print("Invalid input, please try again")

# Ask the player how much they want to gamble and continue accordingly
def bet(player, deck):
    while True:
        previous = player.points
        raw = input(f"{player.name}, how much do you want to bet? ")
        user = int(raw)
        if type(user) == int and user > 0 and user <= player.points:
            player.points = previous - user
            return user
        else:
            print("Invalid input, please try again")

# Program your game here!
def blackjack():
    # Initialize the player and dealer
    p1name = input("Enter you name: ") 
    p1 = Player(p1name, [], 1000)
    dealer = Player("Dealer", [], 99999999)

    # Deal to cards to the dealer and player
    while True:
        deck = Card.new_deck()
        p1.hand = []
        dealer.hand = []

        # Ask player for their bet
        print(f"You have ${p1.points}")
        wager = bet(p1, deck)
        print(f"You are betting ${wager} in this game")
        print(f"You have ${p1.points} left, good luck")

        deal(dealer, deck)
        displayCards(dealer)
        deal(p1, deck)
        deal(p1, deck)
        displayCards(p1)
        

        while True:
            user = hit_or_stand(p1, deck)
            displayCards(p1)
            if checkBust(p1) == True:
                break

            if user == "stand": # If the user returns stand, compare it to the dealer
                while handTotal(dealer) <= 16: # If the dealer has a total less than 16, they draw
                    deal(dealer, deck)
                displayCards(dealer)
                if checkBust(dealer) == True:
                    print(f"{p1.name} wins!")
                    p1.points += wager * 2
                    break

                if handTotal(dealer) > handTotal(p1):
                    print("Dealer wins!")
                    break
                elif handTotal(dealer) == handTotal(p1):
                    numberDealer = 0
                    for card in dealer.hand:
                        numberDealer += 1
                    numberP1 = 0
                    for card in p1.hand:
                        numberP1 += 1
                    if numberDealer < numberP1:
                        print(f"Dealer wins!")
                        break
                else:
                    print(f"{p1.name} wins!")
                    p1.points += wager * 2
                    break
            
        if p1.points > 0:
            user = input(f"{p1.name}, do you wish to continue (Y/N)? ")
            if user.lower == "y" or "yes":
                continue
            if user.lower == "n" or "no":
                print(f"{p1.name}, you left the table with {p1.points}")
                exit()
        else:
            print()
            print("Damn, you broke as hell")
            print("You don't have enough money to play again")
            exit()

# Code that runs when script is called from terminal
# ex: python my_card_game.py
if __name__ == "__main__":
    blackjack()