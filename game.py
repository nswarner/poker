#!/usr/bin/python3

from card import Card
from deck import Deck
from hand import Hand
from invalid_argument_exception import InvalidArgumentException
from logger import Logger
from util import Util


class Game:

    deck = None
    hands = None
    community_cards = None

    def __init__(self):
        self.deck = Deck()
        self.main()

    def __del__(self):
        pass

    def add_hand(self):
        o_hand = Hand(0)
        a_card = self.deck.get_card()
        b_card = self.deck.get_card()
        o_hand.add_card(a_card)
        o_hand.add_card(b_card)
        Logger.log("Hand: " + str(o_hand))
        self.hands.append(o_hand)

    def pull_community_cards(self):
        for i in range (0,5):
            self.community_cards.append(self.deck.get_card())

    def community_cards_to_string(self):
        results = ""
        for i in range (0,5):
            results += Card.to_string(self.community_cards[i]) + ", "
        return results[:-2]

    def all_hands_to_string(self):
        results = ""
        for i in range (0, len(self.hands)):
            results += "Player " + str(i + 1) + ": "
            results += self.hands[i].hand_to_string() + "\n"
        return results

    def main(self):

        acceptable_input = False
        num_hands = None
        self.hands = []
        self.community_cards = []

        Logger.log("Game: Initialized game. Running.")

        while(not acceptable_input):
            num_hands = input("How many players are there? ")
            try:
                if (1 < int(num_hands) < 10):
                    Logger.log("Game: num_hands == " + str(num_hands))
                    acceptable_input = True
                    num_hands = int(num_hands)
            except ValueError as e:
                Logger.log("Game: int(num_hands) threw ValueError; trying as String [" + str(num_hands) + "]")
                try:
                    num_hands = Util.convert_string_num(str(num_hands))
                    if (1 < num_hands < 10):
                        Logger.log("Game: convert_string_num(num_hands) succeeded.")
                        acceptable_input = True
                except InvalidArgumentException as ignore:
                    Logger.log("Game: num_hands failed as int() and str(). Retrying.")
            if (not acceptable_input):
                print("Invalid input. The number of players must be between 2 and 9.");

        Logger.log("Game: There are " + str(num_hands) + " playing.")

        for i in range(0, num_hands):
            Logger.log("Game: Adding hand for Player " + str(i))
            self.add_hand()

        self.pull_community_cards()
        print("Community cards are: " + self.community_cards_to_string())
        print(self.all_hands_to_string())

if (__name__ == '__main__'):
    Logger.log("Game: Launching game.")
    game = Game()