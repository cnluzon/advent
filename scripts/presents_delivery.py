#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
.. moduleauthor:: cnluzon
.. module:: present_delivery.py
Script to solve advent code calendar problem 3.

--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location,
and then an elf at the North Pole calls him via radio and tells him where to
move next. Moves are always exactly one house to the north (^), south (v),
east (>), or west (<). After each move, he delivers another present to the
house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and
so his directions are a little off, and Santa ends up visiting some houses more
 than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location,
    and one to the east.

    ^>v< delivers presents to 4 houses in a square, including twice to the
    house at his starting/ending location.

    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only
    2 houses.

"""

import os
import sys
import argparse
import operator

class PresentDelivery:
    def __init__(self, directions):
        if not directions:
            msg = "Directions must be provided."
            raise ValueError(msg)

        self._validate_directions(directions)
        self.directions = directions
        self._init_delivery()

    def _init_delivery(self):
        self.current_position = (0,0)
        self.visited_houses = set([(self.current_position)])
        self.delivered_presents = 1

    def _validate_directions(self, directions):
        accepted_chars = '^v><'
        for d in directions:
            if d not in accepted_chars:
                msg = "Invalid char found {}".format(d)
                raise ValueError(msg)

    def move_to_direction(self, d):
        two_dim_directions = {'^':(0,1), 'v':(0,-1), '>':(1,0), '<':(-1,0)}
        self.current_position = tuple(map(operator.add,
                                          self.current_position,
                                          two_dim_directions[d]))

    def deliver_current_position(self):
        self.visited_houses.add(self.current_position)
        self.delivered_presents += 1

    def deliver(self):
        for d in self.directions:
            self.move_to_direction(d)
            self.deliver_current_position()

def read_directions(in_file):
    fi = open(in_file)
    result = fi.readline().rstrip()
    fi.close()
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Reads the input from programming advent 03 and outputs the result')

    parser.add_argument('in_file', help='Input text file composed by dimensions')

    args = parser.parse_args()

    directions = read_directions(args.in_file)
    santa_delivery = PresentDelivery(directions)
    santa_delivery.deliver()
    print len(santa_delivery.visited_houses)
