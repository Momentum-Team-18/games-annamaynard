import random

suits = ['♥️', '♠️', '♦️', '♣️']
ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


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
        return deck_string

    def shuffle(self):
        random.shuffle(self.cards)




class Dealer:
    def __init__(self):
        self.hand = []
    def __str__(self):
        return 'Dealer'
    def hit(self, card):
        self.hand.append(card)


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name
    
    def __str__(self):
        return self.name
    
    def hit(self, card):
        self.hand.append(card)
    
    def choice(self):
        choice = input('Would you like to (h)it or (s)tay?')
        return choice


class Game:
    def __init__(self, suits, ranks):
        self.player = Player(self.get_player_name())
        self.dealer = Dealer()
        self.deck = Deck(suits, ranks)
        self.deck.shuffle()
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.dealer)

    def get_player_name(self):
        name = input('What is your name?')
        return name
    
    def deal_card(self, person):
        card = self.deck.cards.pop()
        person.hand.append(card)

    def show_cards(self):
        print(f'{self.player} has')
        for card in self.player.hand:
            print(card)
        print('Dealer has: ')
        for card in self.dealer.hand:
            print(card)


new_game = Game(suits, ranks)






