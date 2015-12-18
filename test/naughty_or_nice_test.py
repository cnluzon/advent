
import unittest
import StringIO
import os
import sys
import logging

sys.path.append('../scripts/')
import naughty_or_nice as nn

class TestSantaStringEvaluator(unittest.TestCase):
    def setUp(self):
        self.default_santa = nn.SantaStringEvaluator()

    def tearDown(self):
        """Function to do cleaning up after the test."""
        pass

    def test_empty_string_raises_exception(self):
        with self.assertRaises(ValueError):
            self.default_santa.is_nice('')

    def test_valid_vowel_string(self):
        test = 'aei'
        is_nice = self.default_santa.is_vowel_valid(test)
        self.assertEquals(is_nice, True)

    def test_invalid_vowel_string(self):
        test = 'aa'
        self.assertFalse(self.default_santa.is_vowel_valid(test))

    def test_valid_double_string(self):
        test = 'aa'
        self.assertTrue(self.default_santa.is_double_letter_valid(test))

    def test_invalid_double_string(self):
        test = 'ab'
        self.assertFalse(self.default_santa.is_double_letter_valid(test))

    def test_invalid_blacklist_string(self):
        test = 'haegwjzuvuyypxyu'
        self.assertFalse(self.default_santa.is_blacklist_valid(test))

    def test_valid_blacklist_string(self):
        test = 'haegwjzuvuyypyu'
        self.assertTrue(self.default_santa.is_blacklist_valid(test))

    def test_all_nice_string(self):
        test = 'aeiixjk'
        self.assertTrue(self.default_santa.is_nice(test))

    def test_nice_examples_web(self):
        nice_examples = ['ugknbfddgicrmopn', 'aaa']
        for ex in nice_examples:
            self.assertTrue(self.default_santa.is_nice(ex))

    def test_naughty_examples_web(self):
        naughty_examples = ['jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
        for ex in naughty_examples:
            self.assertFalse(self.default_santa.is_nice(ex))

    def test_valid_paired_repeats(self):
        test = 'xyxy'
        self.assertTrue(self.default_santa.is_paired_repeats_valid(test))

    def test_invalid_paired_repeats(self):
        test = 'xyx'
        self.assertFalse(self.default_santa.is_paired_repeats_valid(test))

    def test_valid_gapped_repeats(self):
        test = 'xyx'
        self.assertTrue(self.default_santa.is_gapped_repeats_valid(test))

    def test_invalid_gapped_repeats(self):
        test = 'abcd'
        self.assertFalse(self.default_santa.is_gapped_repeats_valid(test))

    def test_nice_examples_second_model_web(self):
        nice_examples = ['qjhvhtzxzqqjkmpb', 'xxyxx']
        for ex in nice_examples:
            self.assertTrue(self.default_santa.is_nice_second_model(ex))

    def test_naughty_examples_second_model_web(self):
        naughty_examples = ['uurcxstgmygtbstg', 'ieodomkazucvgmuy']
        for ex in naughty_examples:
            self.assertFalse(self.default_santa.is_nice_second_model(ex))

if __name__ == '__main__':
    suites = []

    # Run the whole test using this function
    # unittest.main()
    # or you can have a more detailed test view with:
    # This will load all the tests methods that start with test_*
    suites.append(unittest.TestLoader().loadTestsFromTestCase(TestSantaStringEvaluator))

    for suite in suites:
        unittest.TextTestRunner(verbosity=2).run(suite)
