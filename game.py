#!/usr/bin/python3

from .deck import Deck
from .hand import Hand
from .invalid_argument_exception import InvalidArgumentException
from .logger import Logger
from .util import Util


class Game:

    deck = None
    hands = None

    def __init__(self):
        deck = Deck()
        self.main()

    def __del__(self):
        pass

    def add_hand(self):
        o_hand = Hand()
        a_card = self.deck.get_card()
        b_card = self.deck.get_card()
        o_hand.add_card(a_card)
        o_hand.add_card(b_card)
        self.hands.append(o_hand)

    def main(self):

        acceptable_input = False
        num_hands = None

        Logger.log("Game: Initialized game. Running.")

        while(not acceptable_input):
            num_hands = input("How many players are there? ")
            if (type(num_hands) is int and 1 < num_hands < 10):
                acceptable_input = True
            elif (type(num_hands) is ''):
                try:
                    num_hands = Util.convert_string_num(num_hands)
                    if (1 < num_hands < 10):
                        acceptable_input = True
                except InvalidArgumentException as ignore:
                    pass
            if (not acceptable_input):
                print("Invalid input. The number of players must be between 2 and 9.");

        Logger.log("Game: There are " + str(num_hands) + " playing.")

        for i in range(1, num_hands):
            game.add_hand()

            g_hand = Hand()
            g_hand.add_card(self.deck.rand_card())
            self.hands.append(Hand())


if (__name__ == '__main__'):
    Logger.log("Game: Launching game.")
    game = Game()