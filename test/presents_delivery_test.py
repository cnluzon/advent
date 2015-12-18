
import unittest
import StringIO
import os
import sys
import logging

sys.path.append('../scripts/')
import presents_delivery as pd

class TestPresentDelivery(unittest.TestCase):
    def setUp(self):
        """Function to create any data needed for the test and any configuration previous to it."""


    def tearDown(self):
        """Function to do cleaning up after the test."""
        pass

    def test_empty_directions_raise_exception(self):
        with self.assertRaises(ValueError):
            pd.PresentDelivery('')

    def test_invalid_directions_raise_exception(self):
        with self.assertRaises(ValueError):
            pd.PresentDelivery('>Av^')
        with self.assertRaises(ValueError):
            pd.PresentDelivery('%')

    def test_delivery_initialization(self):
        test = pd.PresentDelivery('>')
        self.assertEquals(test.current_position, (0,0))
        self.assertEquals(test.delivered_presents, 1)
        self.assertEquals(test.visited_houses, set([(0,0)]))

    def test_delivery_non_repeated_positions(self):
        test = pd.PresentDelivery('>')
        test.deliver()
        self.assertEquals(test.delivered_presents, 2)
        self.assertEquals(test.visited_houses, set([(0,0), (1,0)]))

    def test_delivery_repeated_positions(self):
        test = pd.PresentDelivery('><')
        test.deliver()
        self.assertEquals(test.delivered_presents, 3)
        self.assertEquals(test.visited_houses, set([(0,0), (1,0)]))

    def test_delivery_negative_non_repeated_positions(self):
        test = pd.PresentDelivery('<<v')
        test.deliver()
        self.assertEquals(test.delivered_presents, 4)
        self.assertEquals(test.visited_houses, set([(0,0), (-1,0), (-2,0), (-2,-1)]))

    def test_delivery_negative_repeated_positions(self):
        test = pd.PresentDelivery('<><>')
        test.deliver()
        self.assertEquals(test.delivered_presents, 5)
        self.assertEquals(test.visited_houses, set([(0,0), (-1,0)]))

    # Examples from the web
    def test_delivery_example_one(self):
        test = pd.PresentDelivery('>')
        test.deliver()
        self.assertEquals(test.delivered_presents, 2)
        self.assertEquals(test.visited_houses, set([(0,0), (1,0)]))
        self.assertEquals(len(test.visited_houses), 2)

    def test_delivery_example_two(self):
        test = pd.PresentDelivery('^>v<')
        test.deliver()
        self.assertEquals(test.delivered_presents, 5)
        self.assertEquals(test.visited_houses, set([(0,0), (0,1), (1,1), (1,0)]))
        self.assertEquals(len(test.visited_houses), 4)

    def test_delivery_example_three(self):
        test = pd.PresentDelivery('^v^v^v^v^v')
        test.deliver()
        self.assertEquals(test.delivered_presents, 11)
        self.assertEquals(test.visited_houses, set([(0,0), (0,1)]))
        self.assertEquals(len(test.visited_houses), 2)

if __name__ == '__main__':
    suites = []

    # Run the whole test using this function
    # unittest.main()
    # or you can have a more detailed test view with:
    # This will load all the tests methods that start with test_*
    suites.append(unittest.TestLoader().loadTestsFromTestCase(TestPresentDelivery))

    for suite in suites:
        unittest.TextTestRunner(verbosity=2).run(suite)
