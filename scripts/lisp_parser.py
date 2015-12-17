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

def read_lisp_file(in_file):
    fi = open(in_file)
    lisp_string = fi.readline()
    fi.close()
    return lisp_string


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Reads the input from programming advent 01 and outputs the result')

    parser.add_argument('in_file', help='Input text file composed by ( and )')

    args = parser.parse_args()

    lisp_string = read_lisp_file(args.in_file)
    print compute_floor(lisp_string)
