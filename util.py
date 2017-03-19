#!usr/bin/python

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

    @staticmethod
    def convert_string_num(num):
        assert (isinstance(num, str)), "convert_string_num requires a String as argument"

        num = num.lower()

        if (num in Util.TRANSLATE.keys()):
            return Util.TRANSLATE[num]
        else:
            raise InvalidArgumentException("Argument num is not within range (0,12)")