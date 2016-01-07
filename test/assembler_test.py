
import unittest
import StringIO
import os
import sys
import logging

sys.path.append('../scripts/')
import advent_coins as ac

class TestAssembler(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        """Function to do cleaning up after the test."""
        pass

    def test_empty_key_raises_exception(self):
        with self.assertRaises(ValueError):
            ac.AdventCoinMiner('')

    def test_example_one(self):
        miner = ac.AdventCoinMiner('abcdef')
        advent_coin = miner.mine_advent_coin_value()
        self.assertEquals(advent_coin, 609043)

    def test_example_two(self):
        miner = ac.AdventCoinMiner('pqrstuv')
        advent_coin = miner.mine_advent_coin_value()
        self.assertEquals(advent_coin, 1048970)

if __name__ == '__main__':
    suites = []

    # Run the whole test using this function
    # unittest.main()
    # or you can have a more detailed test view with:
    # This will load all the tests methods that start with test_*
    suites.append(unittest.TestLoader().loadTestsFromTestCase(TestAdventCoinMiner))

    for suite in suites:
        unittest.TextTestRunner(verbosity=2).run(suite)
