from dictogram import Dictogram
from pprint import pprint
import random, sys


class MarkovNthOrder(object):

    def __init__(self, order):
        self.states = {}
        self.separator = " "

        if int(order) > 0:
            self.order = order
        else:
            raise Exception("")

    def 