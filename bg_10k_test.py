#!/usr/bin/env python3

import unittest
import bg_factor


class NumTest(unittest.TestCase):
    def test_num(self):
        for i in range(10001):
            self.assertNotEqual("", (str(i), bg_factor.number))
        

if __name__ == "__main__":
    unittest.main()

