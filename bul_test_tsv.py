#!/usr/bin/env python3

import csv
import unittest
import bulgarian_tn
from pynini.lib import rewrite


class NumTest(unittest.TestCase):
    def test_tsv(self):
        with open("bul_num_grammar_test.tsv", "r") as source:
            tsv_reader = csv.reader(source, delimiter="\t")
            for number_str, number_word in tsv_reader:
                self.assertEqual(number_word, rewrite.one_top_rewrite(number_str, bulgarian_tn.new_hundreds_and_tens))


if __name__ == "__main__":
    unittest.main()