import random
from art import logo

class Card:
    suite = ""
    picture = None
    value = 0
    revealed = False

    symbols = {
        "Hearts": "♥",
        "Diamonds": "♦",
        "Spades": "♠",
        "Clubs": "♣"
    }

    def __init__(self, suite, value, picture=None):
        self.suite = suite
        self.value = value
        self.picture = picture
        self.revealed = False

    def display_string(self):
        if self.revealed == False:
            return("?")
        elif self.picture:
            return(self.symbols[self.suite] + self.picture[0])
        elif self.value == 11 or self.value == 1:
            return(self.symbols[self.suite] + "A")
        else:
            return(self.symbols[self.suite] + str(self.value))



class CardDeck:

    def __init__(self):
        self.cards = [
            Card("Spades", 11), Card("Spades", 2), Card("Spades", 3), Card("Spades", 4), Card("Spades", 5), Card("Spades", 6), Card("Spades", 7), Card("Spades", 8), Card("Spades", 9), Card("Spades", 10), Card("Spades", 10, "Jack"), Card("Spades", 10, "Queen"), Card("Spades", 10, "King"),
            Card("Clubs", 11), Card("Clubs", 2), Card("Clubs", 3), Card("Clubs", 4), Card("Clubs", 5), Card("Clubs", 6), Card("Clubs", 7), Card("Clubs", 8), Card("Clubs", 9), Card("Clubs", 10), Card("Clubs", 10, "Jack"), Card("Clubs", 10, "Queen"), Card("Clubs", 10, "King"),
            Card("Hearts", 11), Card("Hearts", 2), Card("Hearts", 3), Card("Hearts", 4), Card("Hearts", 5), Card("Hearts", 6), Card("Hearts", 7), Card("Hearts", 8), Card("Hearts", 9), Card("Hearts", 10), Card("Hearts", 10, "Jack"), Card("Hearts", 10, "Queen"), Card("Hearts", 10, "King"),
            Card("Diamonds", 11), Card("Diamonds", 2), Card("Diamonds", 3), Card("Diamonds", 4), Card("Diamonds", 5), Card("Diamonds", 6), Card("Diamonds", 7), Card("Diamonds", 8), Card("Diamonds", 9), Card("Diamonds", 10), Card("Diamonds", 10, "Jack"), Card("Diamonds", 10, "Queen"), Card("Diamonds", 10, "King")
            ]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def count(self):
        return len(self.cards)

    def deal(self):
        return self.cards.pop(0)

class BlackjackGame:
    deck = None
    player_hand = []
    dealer_hand = []

    def __init__(self):
        self.deck = CardDeck()
        self.player_hand = []
        self.dealer_hand = []

    def play(self):
        print(logo)
        self._initial_deal()
        self._print_cards()
        hold = False
        if self._get_player_score() == 21:
            print("\nBLACKJACK!\n")
            input("Press any key to continue")
            hold = True
        while not hold:
            valid_input = False
            while not valid_input:
                choice = input(f"'hold' or 'call'? Please type your choice: ").lower()
                if choice in ["hold", "h", "call", "c"]:
                    valid_input = True
                else:
                    continue
                if choice[0] == "h":
                    hold = True
                elif choice[0] == "c":
                    self._call()
                    self._print_cards()
                    if self._get_player_score() > 21:
                        self._lose()
                        return
        self._dealer_turn()

    def _initial_deal(self):
        self.player_hand.append(self.deck.deal())
        self.dealer_hand.append(self.deck.deal())
        self.player_hand.append(self.deck.deal())
        self.dealer_hand.append(self.deck.deal())
        self.dealer_hand[0].revealed = True
        for card in self.player_hand:
            card.revealed = True

    def _get_score(self, hand):
        cards = hand.copy()
        total_score = 0
        cards.sort(key=lambda x: x.value, reverse=True)

        for card in cards:
            if card.revealed:
                total_score += card.value

        index_of_next_ace = 0
        while total_score > 21 and any(card.value == 11 for card in cards):
            cards[index_of_next_ace].value = 1
            index_of_next_ace += 1
            total_score = 0
            for card in cards:
                if card.revealed:
                    total_score += card.value

        return total_score

    def _get_player_score(self):
        return self._get_score(self.player_hand)

    def _get_dealer_score(self):
        return self._get_score(self.dealer_hand)

    def _call(self):
        card = self.deck.deal()
        card.revealed = True
        self.player_hand.append(card)

    def _dealer_turn(self):
        self.dealer_hand[1].revealed = True
        self._print_cards()
        dealer_score = self._get_dealer_score()
        player_score = self._get_player_score()
        if dealer_score > player_score:
            self._lose()
            return
        elif dealer_score == 21 and dealer_score == player_score:
            self._draw()
            return
        elif dealer_score >= 17 and dealer_score == player_score:
            self._draw()
            return
        else:
            input("Press any key to continue")
            while dealer_score < player_score:
                self.dealer_hand.append(self.deck.deal())
                self.dealer_hand[-1].revealed = True
                dealer_score = self._get_dealer_score()
                self._print_cards()
                if dealer_score > 21:
                    self._win()
                    return
                elif dealer_score > player_score:
                    self._lose()
                    return
                elif dealer_score >= 17 and dealer_score == player_score:
                    self._draw()
                    return
                else:
                    input("Press any key to continue")

    def _lose(self):
        print("You Lose!")

    def _draw(self):
        print("Draw.")

    def _win(self):
        print("You Win!")

    def _print_cards(self):
        output = ""
        output += "\nDealer cards: "
        for card in self.dealer_hand:
            output += card.display_string() + " "
        output += f"\tTOTAL: {self._get_dealer_score()}"
        output += "\nPlayer cards: "
        for card in self.player_hand:
            output += card.display_string() + " "
        output += f"\tTOTAL: {self._get_player_score()}"
        output += "\n"
        print(output)

keep_playing = True
while keep_playing:
    blackjack = BlackjackGame()
    blackjack.play()
    player_choice = input(f"\nType 'y' or press enter to play again: ").lower()
    if player_choice == "" or player_choice[0] == "y":
        pass
    else:
        keep_playing = False
