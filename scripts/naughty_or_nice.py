#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
.. moduleauthor:: cnluzon
.. module:: naughty_or_nice.py
Script to solve advent code calendar problem 5.

--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or
nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or
    aeiouaeiouaeiou.

    It contains at least one letter that appears twice in a row, like xx,
    abcdde (dd), or aabbccdd (aa, bb, cc, or dd).

    It does not contain the strings ab, cd, pq, or xy, even if they are part of
    one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because
        it has at least three vowels (u...i...o...),
        a double letter (...dd...),
        and none of the disallowed substrings.

    aaa is nice because it has at least three vowels and a double letter, even
    though the letters used by different rules overlap.

    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of
determining whether a string is naughty or nice. None of the old rules apply,
as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the
    string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like
    aaa (aa, but it overlaps).

    It contains at least one letter which repeats with exactly one letter
    between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj)
        and a letter that repeats with exactly one letter between them (zxz).
    xxyxx is nice because it has a pair that appears twice and a letter that
        repeats with one between, even though the letters used by each rule
        overlap.

    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with
        a single letter between them.
    ieodomkazucvgmuy is naughty because it has a repeating letter with one
        between (odo), but no pair that appears twice.

How many strings are nice under these new rules?


"""

import os
import sys
import argparse
import operator

class SantaStringEvaluator:
    def __init__(self, min_vowels=3,
                       min_double_letters=1,
                       disallowed=['ab', 'cd', 'pq', 'xy']):

        if min_vowels < 0:
            msg = 'Minimum vowels value should be greater or equal to 0'
            raise ValueError(msg)

        self.min_vowels = min_vowels

        if min_double_letters < 0:
            msg = 'Minimum double letters value should be greater or equal to 0'
            raise ValueError(msg)

        self.min_double_letters = min_double_letters
        self.disallowed = disallowed

    def is_nice(self, string):
        if not string:
            msg = 'A non-empty string must be provided'
            raise ValueError(msg)

        is_vowel_valid = self.is_vowel_valid(string)
        is_double_letter_valid = self.is_double_letter_valid(string)
        is_blacklist_valid = self.is_blacklist_valid(string)

        return (is_vowel_valid and is_double_letter_valid and is_blacklist_valid)


    def is_vowel_valid(self, string):
        return self.contains_minimum_vowels(string, self.min_vowels)

    def contains_minimum_vowels(self, string, minimum):
        count = self._count_vowels(string)
        result = (count >= minimum)
        return result

    def _count_vowels(self, string):
        vowels = 'aeiou'
        count = 0
        for s in string:
            if s in vowels:
                count += 1

        return count

    def is_double_letter_valid(self, string):
        return self.contains_minimum_double_letters(string, self.min_double_letters)

    def contains_minimum_double_letters(self, string, minimum):
        count = self._count_double_letters(string)
        return (count >= minimum)

    def _count_double_letters(self, string):
        count = 0
        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                count += 1
        return count

    def is_blacklist_valid(self, string):
        return not(self.contains_disallowed_substrings(string, self.disallowed))

    def contains_disallowed_substrings(self, string, disallowed):
        for s in disallowed:
            if string.find(s) != -1:
                return True

        return False


    def is_nice_second_model(self, string):
        if not string:
            msg = 'A non-empty string must be provided'
            raise ValueError(msg)

        is_paired_repeats_valid = self.is_paired_repeats_valid(string)
        is_gapped_repeats_valid = self.is_gapped_repeats_valid(string)

        return (is_paired_repeats_valid and is_gapped_repeats_valid)

    def is_paired_repeats_valid(self, string):
        min_repeats = 2
        count = self._count_paired_nonoverlapping_repeats(string)
        return (count >= min_repeats)

    def _count_paired_nonoverlapping_repeats(self, string):
        max_paired = 0
        processed_pairs = set()
        for i in range(len(string)-2):
            cur_pair = string[i:i+2]
            cur_count = self._count_nonoverlapping_repeats(string, cur_pair)
            if cur_count > max_paired:
                max_paired  = cur_count

        return max_paired

    def _count_nonoverlapping_repeats(self, string, substr):
        return string.count(substr)

    def is_gapped_repeats_valid(self, string):
        for i in range(len(string)-2):
            if string[i] == string[i+2]:
                return True

        return False



def read_santa_strings(in_file):
    fi = open(in_file)
    santa_strings = []
    for line in fi.readlines():
        santa_strings.append(line.rstrip())
    fi.close()
    return santa_strings

def count_nice_strings(santa_strings):
    count = 0
    default_santa = SantaStringEvaluator()
    for st in santa_strings:
        if default_santa.is_nice(st):
            count += 1

    return count

def count_nice_strings_second_model(santa_strings):
    count = 0
    default_santa = SantaStringEvaluator()
    for st in santa_strings:
        if default_santa.is_nice_second_model(st):
            count += 1

    return count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Reads the input from programming advent 05 and outputs the result')

    parser.add_argument('in_file', help='Input file')

    args = parser.parse_args()

    santa_strings = read_santa_strings(args.in_file)
    nice_strings = count_nice_strings(santa_strings)
    print "From {} there were {} nice strings.".format(str(len(santa_strings)),
                                                       str(nice_strings))

    nice_strings = count_nice_strings_second_model(santa_strings)
    print "From {} there were {} nice strings (2nd).".format(str(len(santa_strings)),
                                                       str(nice_strings))
