#!/usr/bin/env python3

"""Bulgarian cardinal number rules."""

import string

import pynini

from pynini.lib import pynutil
from pynini.lib import rewrite


graph_zero = pynini.string_map([("0", "нула")])

graph_digit = pynini.string_map(
    [
        ("1", "едно"),
        ("2", "две"),
        ("3", "три"),
        ("4", "четири"),
        ("5", "пет"),
        ("6", "шест"),
        ("7", "седем"),
        ("8", "осем"),
        ("9", "девет"),
    ]
)

graph_teen = pynini.string_map(
    [
        ("10", "десет"),
        ("11", "единадесет"),
        ("12", "дванадесет"),
        ("13", "тринадесет"),
        ("14", "четиринадесет"),
        ("15", "петнадесет"),
        ("16", "шестнадесет"),
        ("17", "седемнадесет"),
        ("18", "осемнадесет"),
        ("19", "деветнадесет"),
    ]
)

graph_ties = pynini.string_map(
    [
        ("2", "двадесет"),
        ("3", "тридесет"),
        ("4", "четиридесет"),
        ("5", "петдесет"),
        ("6", "шейсет"),
        ("7", "седемдесет"),
        ("8", "осемдесет"),
        ("9", "деветдесет"),
    ]
)

graph_hundred = pynini.string_map(
    [
        ("1", "сто"),
        ("2", "двеста"),
        ("3", "триста"),
        ("4", "четиристотин"),
        ("5", "петстотин"),
        ("6", "шестстотин"),
        ("7", "седемстотин"),
        ("8", "осемстотин"),
        ("9", "деветстотин"),
    ]
)

_and = pynutil.insert(" и ")
insert_space = pynini.closure(pynutil.insert(" "), 0, 1)

# single digit strings
digits = graph_digit

# double digit strings
tens = graph_teen
tens = tens | graph_ties + (pynutil.delete("0") | _and + digits)
tens = tens.optimize()
new_tens = pynini.union(digits, tens, (pynini.cross("0", " ") + digits))

# three digit strings
hundreds = graph_hundred
hundreds = hundreds | hundreds + pynutil.delete("00")
hundreds_and_tens = (
    hundreds | hundreds + pynutil.insert(_and, weight=0.0001) + new_tens | new_tens
)
new_hundreds_and_tens = hundreds_and_tens.optimize()


def number(token: str) -> str:
    return rewrite.one_top_rewrite(token, new_hundreds_and_tens)
