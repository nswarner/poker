#!usr/bin/python

import os

from invalid_argument_exception import InvalidArgumentException


class Util:

    TRANSLATE = {"twelve":12,
                 "eleven":11,
                 "ten":10,
                 "nine":9,
                 "eight":8,
                 "seven":7,
                 "six":6,
                 "five":5,
                 "four":4,
                 "three":3,
                 "two":2,
                 "one":1,
                 "zero":0}

    def __init__(self):
        raise RuntimeError("Cannot instantiate Util class.")
        os._exit(0)

    @staticmethod
    def convert_string_num(self, num):
        if (num < 0 or num > 12):
            raise InvalidArgumentException("Argument num is not within range (0,12)")
        return (Util.TRANSLATE[num])