import random as rd
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks=('Two', "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values ={"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
playing = True

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.decks = []
        for suit in suits:
            for rank in ranks:
                self.decks.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for cards in self.decks:
            deck_comp += "\n" + cards.__str__()
        return deck_comp

    def shuffle(self):
        rd.shuffle(self.decks)

    def deal(self):
        single_card = self.decks.pop()
        return single_card

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much bet would you like to stake: "))
        except ValueError:
            print("Your entry is invalid")
        else:
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips")
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal()) # dealer will give player a card
    hand.adjust_for_ace() # accounting for the occurrence of an ace

def hit_or_stand(deck,hand):
    global playing
    while True:
        prmpt = input("Would you like to hit or stand? (H/S): ")
        prmpt.title()
        if prmpt[0] == "H":
            hit(deck,hand)
        elif prmpt[0] == "S":
            print("Player stands. Dealer is playing")
            playing = False
        else:
            print("Invalid entry")
            break

def show_some(player,dealer):
    print("Dealer's hand: ")
    print("One card hidden")
    print(dealer.cards[1])
    print("\n")
    print("Player's hand: ")
    for card in player.cards:
        print(card)


def show_all(player,dealer):
    print("Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("Player's hand: ")
    for card in player.cards:
        print(card)

def player_busts(_player, _dealer, chips):
    print("PLAYER LOSES THE GAME")
    chips.lose_bet()

def player_wins(_player, _dealer, chips):
    print("PLAYER WINS THE GAME")
    chips.win_bet()

def dealer_busts(_player, _dealer, chips):
    print("PLAYER WINS THE GAME! DEALER BUSTED")
    chips.win_bet()

def dealer_wins(_player, _dealer, chips):
    print("DEALER WINS THE GAME! PLAYER BUSTED")
    chips.lose_bet()

def push():
    print("DEALER AND PLAYER AT TIE NO WINS")



while True:
    print("****************************************************************")
    print("*************************Black Jack Game************************")
    print("*********************Hosted by Eben's Casino********************")
    print("***********************Powered by OOPython**********************")
    print("****************************************************************")
    print("Welcome to Eben's casino!!\nThe most lucrative and trendy game here is Blackjack")
    print("Let me show you to the tables so you score some cash")
    print("****************************************************************")
    print("************************Black Jack Tables***********************")
    print("****************************************************************")
    quest = input("Would you like to continue? (Y/N): ")
    if quest[0].upper() == "Y":
        print("Let's begin")
    else:
        print("Cool. Do come back for more later")
        break

    #create and shuffle the deck
    my_deck=Deck()
    my_deck.shuffle()
    # dealing two cards to each player
    player_hand = Hand()
    player_hand.add_card(my_deck.deal())
    player_hand.add_card(my_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(my_deck.deal())
    dealer_hand.add_card(my_deck.deal())

    # set up the chips for the player
    player_chips=Chips()

    # informing the player for their bet
    take_bet(player_chips)

    # time to show cards of players. remember to show one card of dealer
    show_some(player_hand, dealer_hand)

    while playing:
        #prompt player to hit or stand
        hit_or_stand(my_deck, player_hand)
        #show cards of players(only one dealer hand is known)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
        #if player hasn't busted, play dealer's hand until dealer reaches 17(according to the sweet 17 rule)
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(my_deck, dealer_hand)
            #show all cards
            show_all(player_hand, dealer_hand)
            """
            run winning scenarios for the game
            if dealer has more than 21, he loses
            if dealer has less than player's total, he wins
            if dealer has equal to player's total, it's a tie
            if dealer has more than player's total, he loses
            """
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push()
        # inform players of total chips
        print(f"Player, your total chips are: {player_chips.total}")

        #ask if player wants to go again
        ask = input("Would you like to deal another hand (Y/N): ")
        if ask[0].capitalize() == "Y":
            playing = True
        else:
            print("Thanks for playing, goodbye")
            break