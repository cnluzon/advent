
import unittest
import StringIO
import os
import sys
import logging

sys.path.append('../scripts/')
import lights_decoration as ld

class TestLightsGrid(unittest.TestCase):
    def setUp(self):
        self.test_christmas_lights = ld.LightsGrid(dimensions=(1000, 1000))

    def tearDown(self):
        """Function to do cleaning up after the test."""
        pass

    def test_zero_dimensions_raise_exception(self):
        with self.assertRaises(ValueError):
            test_lights = ld.LightsGrid((0, 0))

    def test_negative_dimensions_raise_exception(self):
        with self.assertRaises(ValueError):
            test_lights = ld.LightsGrid((-1,20))

    def test_dimensions_grid_creation(self):
        test_lights = ld.LightsGrid((100,80))
        self.assertEquals(len(test_lights.grid[0]), 80)
        self.assertEquals(len(test_lights.grid), 100)

    def test_set_lights_out_of_bounds_coords(self):
        with self.assertRaises(IndexError):
            start = (20,40)
            end = (1005, 80)
            self.test_christmas_lights.set(start, end, value=1)

    def test_set_lights_valid_coords(self):
        test_lights = ld.LightsGrid(dimensions=(10,10))
        start = (3,6)
        end = (4,8)
        test_lights.set(start, end, value=1)

        self.assertEquals(test_lights.grid[3,6], 1)
        self.assertEquals(test_lights.grid[3,7], 1)
        self.assertEquals(test_lights.grid[3,8], 1)

        self.assertEquals(test_lights.grid[4,6], 1)
        self.assertEquals(test_lights.grid[4,7], 1)
        self.assertEquals(test_lights.grid[4,8], 1)

        self.assertEquals(test_lights.grid[2,6], 0)
        self.assertEquals(test_lights.grid[2,7], 0)
        self.assertEquals(test_lights.grid[2,8], 0)

        self.assertEquals(test_lights.grid[4,9], 0)
        self.assertEquals(test_lights.grid[5,7], 0)
        self.assertEquals(test_lights.grid[3,2], 0)

    def test_toggle_lights_valid_coords(self):
        test_lights = ld.LightsGrid(dimensions=(10,10))
        start = (3,6)
        end = (4,8)
        test_lights.toggle(start, end)

        self.assertEquals(test_lights.grid[3,6], 1)
        self.assertEquals(test_lights.grid[3,7], 1)
        self.assertEquals(test_lights.grid[3,8], 1)

        self.assertEquals(test_lights.grid[4,6], 1)
        self.assertEquals(test_lights.grid[4,7], 1)
        self.assertEquals(test_lights.grid[4,8], 1)

        test_lights.toggle(start, end)

        self.assertEquals(test_lights.grid[3,6], 0)
        self.assertEquals(test_lights.grid[3,7], 0)
        self.assertEquals(test_lights.grid[3,8], 0)

        self.assertEquals(test_lights.grid[4,6], 0)
        self.assertEquals(test_lights.grid[4,7], 0)
        self.assertEquals(test_lights.grid[4,8], 0)

    def test_turn_on_lights_valid(self):
        test_lights = ld.LightsGrid(dimensions=(10,10))
        start = (2,3)
        end = (3,4)
        test_lights.turn_on(start, end)

        self.assertEquals(test_lights.grid[2,3], 1)
        self.assertEquals(test_lights.grid[2,4], 1)
        self.assertEquals(test_lights.grid[3,3], 1)
        self.assertEquals(test_lights.grid[3,4], 1)

    def test_turn_off_lights_valid(self):
        test_lights = ld.LightsGrid(dimensions=(10,10))
        start = (2,3)
        end = (3,4)
        test_lights.turn_on(start, end)
        test_lights.turn_off(start, end)
        self.assertEquals(test_lights.grid[2,3], 0)
        self.assertEquals(test_lights.grid[2,4], 0)
        self.assertEquals(test_lights.grid[3,3], 0)
        self.assertEquals(test_lights.grid[3,4], 0)

    def test_count_lit_zero(self):
        test_lights = ld.LightsGrid(dimensions=(10,10))
        self.assertEquals(test_lights.count_lit(), 0)

    def test_count_lit_example(self):
        test_lights = ld.LightsGrid(dimensions=(10,10))
        start = (0,0)
        end = (9,9)
        test_lights.turn_on(start, end)
        self.assertEquals(test_lights.count_lit(), 100)


if __name__ == '__main__':
    suites = []

    # Run the whole test using this function
    # unittest.main()
    # or you can have a more detailed test view with:
    # This will load all the tests methods that start with test_*
    suites.append(unittest.TestLoader().loadTestsFromTestCase(TestLightsGrid))

    for suite in suites:
        unittest.TextTestRunner(verbosity=2).run(suite)
