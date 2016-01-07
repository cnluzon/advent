#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
.. moduleauthor:: cnluzon
.. module:: lights_decoration.py
Script to solve advent code calendar problem 6.

--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating
contest year after year, you've decided to deploy one million lights in a
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed
you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at
each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include
whether to turn on, turn off, or toggle various inclusive ranges given as
coordinate pairs. Each coordinate pair represents opposite corners of a
rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers
to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by
doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
        turning off the ones that were on, and turning on the ones that were
        off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle
        four lights.

After following the instructions, how many lights are lit?

"""

import os
import sys
import argparse
import operator
import numpy

class LightsGrid:
    def __init__(self, dimensions=(1000, 1000), regulable=False):
        self._validate_dimensions(dimensions)
        self.dimensions = dimensions

        self.grid = self._build_matrix(dimensions)
        self.regulable = regulable

    def _validate_dimensions(self, dims):
        if dims[0] <= 0 or dims[1] <= 0:
            msg = "Invalid dimensions {}: must be positive numbers.".format(str(dims))
            raise ValueError(msg)

    def _build_matrix(self, dims):
        matrix = numpy.zeros(dims, dtype=numpy.int)
        return matrix

    def turn_on(self, start, end):
        self.set(start, end, value=1)

    def turn_off(self, start, end):
        self.set(start, end, value=0)

    def set(self, start, end, value=1):
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                self.grid[i,j] = value

    def increase(self, start, end, value=1):
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                self.grid[i,j] += value

    def decrease(self, start, end, value=1):
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                self.grid[i,j] -= value

                if self.grid[i,j] < 0:
                    self.grid[i,j] = 0

    def toggle_brightness(self, start, end):
        self.increase(start, end, 2)

    def toggle(self, start, end):
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                self.grid[i,j] = 1 - self.grid[i,j]

    def count_lit(self):
        count = 0
        for i in range(len(self.grid[0])):
            for j in range(len(self.grid)):
                count += self.grid[i,j]

        return count

    def perform_instruction(self, light_instruction):
        function, start, end = self._process_instruction(light_instruction, processing_method=self._extract_function)
        function(start, end)

    def _process_instruction(self, instruction, processing_method):
        words = instruction.split(' ')
        function = processing_method(instruction)
        start, end = self._extract_coords(instruction)
        return function, start, end

    def _extract_coords(self, instruction):
        words = instruction.split(' ')
        through_index = words.index('through')
        start_string = words[through_index-1].split(',')
        end_string = words[through_index+1].split(',')

        start = (int(start_string[0]), int(start_string[1]))
        end = (int(end_string[0]), int(end_string[1]))

        return start, end

    def perform_instruction_brightness_meaning(self, light_instruction):
        function, start, end = self._process_instruction(light_instruction,
                                                         processing_method=self._extract_function_brightness_meaning)
        function(start, end)

    def _extract_function_brightness_meaning(self, instruction):
        words = instruction.split(' ')
        function = None
        if words[0] == 'turn':
            if words[1] == 'on':
                function = self.increase
            elif words[1] == 'off':
                function = self.decrease
            else:
                self._raise_unknown_function_error(instruction)

        elif words[0] == 'toggle':
            function = self.toggle_brightness
        else:
            self._raise_unknown_function_error(instruction)

        return function

    def _extract_function(self, instruction):
        words = instruction.split(' ')
        function = None
        if words[0] == 'turn':
            if words[1] == 'on':
                function = self.turn_on
            elif words[1] == 'off':
                function = self.turn_off
            else:
                self._raise_unknown_function_error(instruction)

        elif words[0] == 'toggle':
            function = self.toggle
        else:
            self._raise_unknown_function_error(instruction)

        return function

    def _raise_unknown_function_error(self, instruction):
        msg = 'instruction not known: {}'.format(instruction)
        raise ValueError(msg)

def read_instructions(in_file):
    result = []
    fi = open(in_file)
    for line in fi.readlines():
        result.append(line.rstrip())
    fi.close()
    return result

def perform_all_light_instructions(lights, instructions_list):
    for item in instructions_list:
        lights.perform_instruction(item)

def perform_all_light_instructions_brightness(lights, instructions_list):
    for item in instructions_list:
        lights.perform_instruction_brightness_meaning(item)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Reads the input from programming advent 06 and outputs the result')

    parser.add_argument('in_file', help='Input file')

    args = parser.parse_args()

    santa_lights = LightsGrid((1000,1000))
    instructions = read_instructions(args.in_file)
    perform_all_light_instructions_brightness(santa_lights, instructions)

    print santa_lights.count_lit()
