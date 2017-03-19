#!/usr/bin/python


class Logger:

    def __init__(self):
        pass

    def __del__(self):
        pass

    @staticmethod
    def log(message, directory="./poker.log"):
        with open(directory, "a+") as f:
            f.write(str(message) + "\n")