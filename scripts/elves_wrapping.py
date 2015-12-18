#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
.. moduleauthor:: cnluzon
.. module:: lisp_parser.py
Script to solve advent code calendar problem 2.

--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an
order for more. They have a list of the dimensions (length l, width w, and
height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which
makes calculating the required wrapping paper for each gift a little easier:
find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves
also need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet
    of wrapping paper plus 6 square feet of slack, for a total of 58 square
    feet.

    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square
    feet of wrapping paper plus 1 square foot of slack, for a total of 43
    square feet.

All numbers in the elves' list are in feet. How many total square feet of
wrapping paper should they order?

"""

import os
import sys
import argparse

class ElfBox:
    def __init__(self, dimensions):
        if len(dimensions) != 3:
            msg = "A box must have three dimensions"
            raise ValueError(msg)

        self.dims = dimensions

    def compute_surface(self):
        l = self.dims[0]
        w = self.dims[1]
        h = self.dims[2]

        surface = 2*l*w + 2*w*h + 2*h*l

        return surface

    def compute_extra_slack(self):
        sorted_dims = sorted(self.dims)[0:2]
        return sorted_dims[0]*sorted_dims[1]

    def compute_wrapping_surface(self):
        box_surface = self.compute_surface()
        extra_slack = self.compute_extra_slack()

        return box_surface+extra_slack

def read_input_file(in_file):
    result = []
    fi = open(in_file)
    for line in fi.readlines():
        dims = [int(i) for i in line.split('x')]
        result.append(dims)

    fi.close()
    return result

def compute_total_wrapping_paper(in_file):
    total_paper = 0
    box_dims_matrix = read_input_file(in_file)

    for box_dims in box_dims_matrix:
        gift_box = ElfBox(box_dims)
        wrapping_surface = gift_box.compute_wrapping_surface()
        total_paper += wrapping_surface

    return total_paper

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Reads the input from programming advent 02 and outputs the result')

    parser.add_argument('in_file', help='Input text file composed by dimensions')

    args = parser.parse_args()
    total_paper = compute_total_wrapping_paper(args.in_file)
    print total_paper
