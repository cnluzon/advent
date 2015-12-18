#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
.. moduleauthor:: cnluzon
.. module:: advent_coins.py
Script to solve advent code calendar problem 4.

--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at
least five zeroes. The input to the MD5 hash is some secret key (your puzzle
input, given below) followed by a number in decimal. To mine AdventCoins,
you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3,...)
that produces such a hash.

For example:

    If your secret key is abcdef, the answer is 609043, because the MD5 hash of
    abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest
    such number to do so.

    If your secret key is pqrstuv, the lowest number it combines with to make
    an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash
    of pqrstuv1048970 looks like 000006136ef....


"""

import os
import sys
import argparse
import operator
import hashlib

class AdventCoinMiner:
    def __init__(self, key):
        if not key:
            msg = "A key must be provided."
            raise ValueError(msg)

        self.key = key

    def compute_md5_hexadecimal_hash(self, string):
        md5_calculator = hashlib.md5()
        md5_calculator.update(string)

        return md5_calculator.hexdigest()

    def validate_md5_value(self, hash_value):
        for hexval in hash_value[0:5]:
            if hexval != '0':
                return False
        return True

    def is_advent_coin(self, coin_value):
        composed_value = '{}{}'.format(self.key, str(coin_value))
        md5_hash = self.compute_md5_hexadecimal_hash(composed_value)
        return self.validate_md5_value(md5_hash)

    def mine_advent_coin_value(self):
        last_hashed_value = 0
        found = False

        while not found:
            if self.is_advent_coin(last_hashed_value):
                found = True
            else:
                last_hashed_value += 1

        return last_hashed_value

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Reads the input from programming advent 04 and outputs the result')

    parser.add_argument('key', help='Input key')

    args = parser.parse_args()

    miner = AdventCoinMiner(args.key)
    advent_coin = miner.mine_advent_coin_value()

    print advent_coin
