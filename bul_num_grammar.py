#!/usr/bin/env python3

"""Bulgarian cardinal number rules."""

import pynini

from pynini.lib import pynutil


def apply_fst(num, fst):
    try:
        print(pynini.shortestpath(num @ fst).string())
    except pynini.FstOpError:
        print(f"Error: No valid output with given input: '{num}'")

zero = pynini.string_map([("нула", "0")])

digits = pynini.string_map([
    ("едно", "1"),
    ("две", "2"),
    ("три", "3"),
    ("четири", "4"),
    ("пет", "5"),
    ("шест", "6"),
    ("седем", "7"),
    ("осем", "8"),
    ("девет", "9")
])

tens = pynini.string_map([
    ("десет", "1"),
    ("двадесет", "2"),
    ("тридесет", "3"),
    ("четиридесет", "4"),
    ("петдесет", "5"),
    ("шестдесет", "6"),
    ("седемдесет", "7"),
    ("осемдесет", "8"),
    ("деветдесет", "9")
])

teens = pynini.string_map([
    ("единадесет", "11"),
    ("дванадесет", "12"),
    ("тринадесет", "13"),
    ("четиринадесет", "14"),
    ("петнадесет", "15"),
    ("шестнадесет", "16"),
    ("седемнадесет", "17"),
    ("осемнадесет", "18"),
    ("деветнадесет", "19")
])

hundreds = pynini.string_map([
    ("сто", "1"),
    ("двеста", "2"),
    ("триста", "3"),
    ("четиристотин", "4"),
    ("петстотин", "5"),
    ("шестстотин", "6"),
    ("седемстотин", "7"),
    ("осемстотин", "8"),
    ("деветстотин", "9")
])

delete_space = pynini.closure(pynutil.delete(" "), 0, 1)
graph_and = pynutil.delete("и")

graph_digits = digits | pynutil.insert("0")
tens = tens | pynutil.insert("0") | tens + delete_space + graph_and + delete_space
graph_tens = tens + graph_digits
graph_teens_and_tens = graph_tens | teens

graph_all = graph_teens_and_tens | zero

hundreds = hundreds | pynutil.insert("00")
graph_hundreds_first_nine = hundreds + delete_space + graph_and + delete_space + graph_all
graph_other_hundreds = hundreds + delete_space + graph_all
graph_all_hundreds = graph_hundreds_first_nine | graph_other_hundreds


apply_fst("нула", graph_all_hundreds)
apply_fst("пет", graph_all_hundreds)
apply_fst("десет", graph_all_hundreds)
apply_fst("тринадесет", graph_all_hundreds)
apply_fst("двадесет", graph_all_hundreds)
apply_fst("петдесет и осем", graph_all_hundreds)
apply_fst("сто", graph_all_hundreds)
apply_fst("двеста тридесет и пет", graph_all_hundreds)
