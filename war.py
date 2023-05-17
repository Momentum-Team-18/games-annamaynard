import random

SUITS = ['♥️', '♠️', '♦️', '♣️']
RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
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
            full_deck = deck_string
        return full_deck
    
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
    def __init__(self, name):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name
    
    def flip(self, card):
        self.hand.append(card)


class Game:
    def __init__(self, suits, ranks):
        self.player = Player(self.get_player_name())
        self.dealer = Dealer()
        self.deck = Deck(suits, ranks)
        self.deck.shuffle()

    def get_player_name(self):
        name = input('What is your name? ')
        return name

    def split_deck(self):
        half = len(self.deck.cards) // 2
        self.player.hand = self.deck.cards[:half]
        self.dealer.hand = self.deck.cards[half:]


new_game = Game(SUITS, RANKS)
new_game.deck.shuffle()
new_game.split_deck()

print("Player's hand:")
for card in new_game.player.hand:
    print(card)

print("\nDealer's hand:")
for card in new_game.dealer.hand:
    print(card)






    # if card1 > card2
    #     append cards to holder of higher card.

# Dealer shuffles and splits deck - dividing deck into two piles
    # player hand / dealer hand (lists)
# both FLIP at the same time
    # player flip by typing F
        # INPUT = F 
        # F = FLIP
        # list(pop)

    # If player card > computer card -> append card to player hand(list)
    # if computer card > player card --> append card to computer hand(list)
# when the game ends with either player or computer holds 52 cards = WINNER!