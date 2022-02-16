#!/usr/bin/env python3

import unittest
import bg_factor
from pynini.lib import rewrite


class NumTest(unittest.TestCase):
    def test_num(self):
        for i in range(10001):
            self.assertNotEqual("", rewrite.one_top_rewrite(str(i), bg_factor.number))

        
if __name__ == "__main__":
    unittest.main()

