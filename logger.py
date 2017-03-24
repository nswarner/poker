#!/usr/bin/python

from time import time


class Logger:

    f = None

    def __init__(self):
        pass

    def __del__(self):
        pass

    @staticmethod
    def initialize(directory="./poker.log"):
        Logger.f = open(directory, "a+")

    @staticmethod
    def log(msg):
        Logger.f.write("[" + str(time()) + "] " + str(msg) + "\n")

    @staticmethod
    def cleanup():
        Logger.f.close()