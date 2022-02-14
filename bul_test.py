#!/usr/bin/env python3

"""Unit tests for Bulgarian cardinal numbers."""

import unittest
import csv
import bulgarian_tn


class NumTest(unittest.TestCase):
    def rewrites(self, istring: str, expected_ostring: str) -> None:


        ostring = bulgarian_tn.number(istring)
        self.assertEqual(ostring, expected_ostring)


    def test_9(self):
        self.rewrites("9", "девет")

    def test_10(self):
        self.rewrites("10", "десет")

    def test_15(self):
        self.rewrites("15", "петнадесет")

    def test_35(self):
        self.rewrites("35", "тридесет и пет")

    def test_300(self):
        self.rewrites("300", "триста")

    def test_719(self):
        self.rewrites("719", "седемстотин и деветнадесет")  

    def test_999(self):
        self.rewrites("999", "деветстотин деветдесет и девет")

if __name__ == "__main__":
    unittest.main()
