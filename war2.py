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
        deck_string = ''
        for card in self.cards:
            deck_string += str(card) + ' '
        return deck_string.strip()

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

    def play_game(self):
        print("Press 'F' to flip the cards.")
        while True:
            key = input()
            if key.lower() == 'f':
                break
        while len(self.player.hand) < 52 and len(self.dealer.hand) < 52:
            player_card = self.player.hand.pop(0)
            dealer_card = self.dealer.hand.pop(0)
            print(f"\n{self.player.name}'s card: {player_card}")
            print(f"Dealer's card: {dealer_card}")

            if player_card.rank > dealer_card.rank:
                self.player.flip(player_card)
                self.player.flip(dealer_card)
                print(f"\n{self.player.name} wins the round!")
            elif dealer_card.rank > player_card.rank:
                self.dealer.flip(dealer_card)
                self.dealer.flip(player_card)
                print("\nDealer wins the round!")
            else:
                print("\nIt's a tie!")
                tie_cards = [player_card, dealer_card]
                for _ in range(3):
                    if len(self.player.hand) > 0 and len(self.dealer.hand) > 0:
                        player_tie_card = self.player.hand.pop(0)
                        dealer_tie_card = self.dealer.hand.pop(0)
                        tie_cards.extend([player_tie_card, dealer_tie_card])
                        print(f"\n{self.player.name}'s tie card: {player_tie_card}")
                        print(f"Dealer's tie card: {dealer_tie_card}")
                if len(self.player.hand) > 0 and len(self.dealer.hand) > 0:
                    player_final_card = self.player.hand.pop(0)
                    dealer_final_card = self.dealer.hand.pop(0)
                    tie_cards.extend([player_final_card, dealer_final_card])


        # Append the cards to the hand of the higher-ranking player
                if player_card.rank > dealer_card.rank:
                    self.player.hand.extend([player_card, dealer_card])
                elif dealer_card.rank > player_card.rank:
                    self.dealer.hand.extend([dealer_card, player_card])

        # Print the length of each player's hand
                print(f"\n{self.player.name}'s hand length: {len(self.player.hand)}")
                print(f"Dealer's hand length: {len(self.dealer.hand)}")


new_game = Game(SUITS, RANKS)
new_game.split_deck()
new_game.play_game()


# when the game ends with either player or computer holds 52 cards = WINNER!
# adding a loop to keep the game going
#

# TIE --> IF same card is telt then deal three cards
# then the winner takes all.
