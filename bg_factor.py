#!/usr/bin/env python3

""" Bulgarian cardinal number factorization grammar """

import string

import pynini
from pynini.lib import pynutil
from pynini.lib import rewrite


_digit = pynini.union(*string.digits)
# Powers of ten that have single-word representations in Bulgarian. E1*
# is a special symbol used in the teens below.
_powers = pynini.union("[E1]", "[E1*]", "[E2]", "[E3]", "[E6]", "[E9]", "[E12]")
_sigma_star = pynini.union(_digit, _powers).closure().optimize()

# Inserts factors in the appropriate place in the digit sequence.
_raw_factorizer = (
    _digit
    + pynutil.insert("[E6]")
    + _digit
    + pynutil.insert("[E3]")
    + _digit
    + pynutil.insert("[E2]")
    + _digit
    + pynutil.insert("[E1]")
    + _digit
    + pynutil.insert("[E6]")
    + _digit
    + pynutil.insert("[E2]")
    + _digit
    + pynutil.insert("[E1]")
    + _digit
    + pynutil.insert("[E3]")
    + _digit
    + pynutil.insert("[E2]")
    + _digit
    + pynutil.insert("[E1]")
    + _digit
)

# Deletes "0" and "0" followed by a factor, so as to clear out unverbalized
# material in cases like "2,000,324". This needs to be done with some care since
# we need to keep E3 if it has a multiplier, but not if there is nothing between
# the thousands and the millions place.
_del_zeros = (
    pynini.cdrewrite(pynutil.delete("0"), "", "[EOS]", _sigma_star)
    @ pynini.cdrewrite(pynutil.delete("0[E1]"), "", "", _sigma_star)
    @ pynini.cdrewrite(pynutil.delete("0[E2]"), "", "", _sigma_star)
    @ pynini.cdrewrite(pynutil.delete("0[E3]"), "[E6]", "", _sigma_star)
    @ pynini.cdrewrite(pynutil.delete("0[E6]"), "", "", _sigma_star)
    @ pynini.cdrewrite(pynutil.delete("0"), "", "", _sigma_star)
).optimize()
# Inserts an arbitrary number of zeros at the beginning of a string so that
# shorter strings can match the length expected by the raw factorizer.
_pad_zeros = pynutil.insert("0").closure().concat(pynini.closure(_digit))

# Changes E1 to E1* for 11-19.
_fix_teens = pynini.cdrewrite(pynini.cross("[E1]", "[E1*]"), "1", _digit, _sigma_star)

# The actual factorizer
_phi = (_pad_zeros @ _raw_factorizer @ _del_zeros @ _fix_teens).optimize()

_lambda = pynini.string_map(
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
        ("1[E1]", "десет"),
        ("1[E1*]1", "единадесет"),
        ("1[E1*]2", "дванадесет"),
        ("1[E1*]3", "тринадесет"),
        ("1[E1*]4", "четиринадесет"),
        ("1[E1*]5", "петнадесет"),
        ("1[E1*]6", "шестнадесет"),
        ("1[E1*]7", "седемнадесет"),
        ("1[E1*]8", "осемнадесет"),
        ("1[E1*]9", "деветнадесет"),
        ("2[E1]", "двадесет"),
        ("3[E1]", "тридесет"),
        ("4[E1]", "четиридесет"),
        ("5[E1]", "петдесет"),
        ("6[E1]", "шейсет"),
        ("7[E1]", "седемдесет"),
        ("8[E1]", "осемдесет"),
        ("9[E1]", "деветдесет"),
        ("1[E2]", "сто"),
        ("2[E2]", "двеста"),
        ("3[E2]", "триста"),
        ("4[E2]", "четиристотин"),
        ("5[E2]", "петстотин"),
        ("6[E2]", "шестстотин"),
        ("7[E2]", "седемстотин"),
        ("8[E2]", "осемстотин"),
        ("9[E2]", "деветстотин"),
        ("[E3]", "хиляди"),
        ("[E6]", "милиона"),
        ("[E9]", "милиарда"),
        ("[E12]", "трилиона")
    ]
).optimize()
_lambda_star = pynutil.join(_lambda, pynutil.insert(" ")).optimize()

def number(token: str) -> str:
    return rewrite.one_top_rewrite(token, _phi @ _lambda_star)
