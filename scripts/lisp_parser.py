#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
.. moduleauthor:: cnluzon
.. module:: lisp_parser.py
Script to solve advent code calendar problem 1.

"""

import os
import sys
import argparse

def compute_floor(lisp_string):
    current_floor = 0
    for char in lisp_string:
        if char == '(':
            current_floor += 1
        elif char == ')':
            current_floor -= 1

    return current_floor

def find_first_basement_floor(lisp_string):
    current_floor = 0
    lisp_str_values = {'(':1, ')':-1}

    for i in range(len(lisp_string)):
        current_floor += lisp_str_values[lisp_string[i]]
        if current_floor == -1:
            return i+1

    return -1

def read_lisp_file(in_file):
    fi = open(in_file)
    lisp_string = fi.readline().rstrip()
    fi.close()
    return lisp_string


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Reads the input from programming advent 01 and outputs the result')

    parser.add_argument('in_file', help='Input text file composed by ( and )')

    args = parser.parse_args()

    lisp_string = read_lisp_file(args.in_file)
    print "End floor:", compute_floor(lisp_string)
    print "First basement: ", find_first_basement_floor(lisp_string)
