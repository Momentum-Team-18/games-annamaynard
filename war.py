import random
suits = [':hearts:', ':spades:', ':diamonds:', ':clubs:']
ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
class Card:
    def __init__ (self, suit, rank):
        self.suit = suit
        self.suit = rank
    def __str__(self):
        return f'{self.rank} of {self.suit}'
class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)
    def __str__(self):
        deck_string = ' '
        for card in self.cards:
            deck_string += ' ' + str(card)
        return deck_string
    def shuffle(self):
        random.shuffle(self.cards)
class Dealer:
    def __init__(self):
        self.hand = []
    def __str__(self):
        return 'Dealer'
    def flip(self, card):
        self.hand.append(card)
class Player:
    def __init__(self):
        self.hand = []
        self.name = name
    def __str__(self):
        return self.name
    def flip(self, card):
        self.hand.append(card)
def Score(card1, card2)
    if card1 == card2
        return 0
    elif card1 > card2
        return 1
    else:
        return 2
    # if card1 > card2
    #     append cards to holder of higher card.
class Game:
# Dealer shuffles and splits deck - dividing deck into two piles
    # player hand / dealer hand
# both FLIP at the same time
    # player flip by typing F
        # INPUT = F 
        # F = FLIP
    # If player card > computer card -> append card to player hand(list)
    # if computer card > player card --> append card to computer hand(list)
# when the game ends with either player or computer holds 52 cards = WINNER!